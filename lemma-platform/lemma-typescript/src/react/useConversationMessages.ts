import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { SseRawEvent } from "../streams.js";
import type { Conversation, ConversationMessage } from "../types.js";
import {
  conversationMessageText,
  getLatestAssistantMessage,
  isConversationRunningStatus,
  normalizeConversationStatus,
  sortConversationMessagesByCreatedAt,
} from "./assistant-output.js";
import {
  useAssistantSession,
  type CreateConversationInput,
  type ResumeAssistantOptions,
  type SendAssistantMessageOptions,
} from "./useAssistantSession.js";

export interface UseConversationMessagesOptions {
  client: LemmaClient;
  podId?: string;
  agentName?: string;
  /**
   * @deprecated Use agentName instead.
   */
  assistantName?: string;
  /**
   * @deprecated Use agentName instead.
   */
  assistantId?: string;
  organizationId?: string;
  instructions?: string | null;
  conversationId?: string | null;
  enabled?: boolean;
  autoLoad?: boolean;
  autoResume?: boolean;
  limit?: number;
  syncOnTurnEnd?: boolean;
  onEvent?: (event: SseRawEvent, payload: unknown | null) => void;
  onStatus?: (status: string) => void;
  onMessage?: (message: ConversationMessage) => void;
  onError?: (error: unknown) => void;
}

export interface UseConversationMessagesResult {
  conversationId: string | null;
  conversation: Conversation | null;
  messages: ConversationMessage[];
  status?: string;
  isRunning: boolean;
  isStreaming: boolean;
  isLoading: boolean;
  isLoadingOlder: boolean;
  hasOlderMessages: boolean;
  nextPageToken: string | null;
  streamingText: string;
  latestAssistantMessage: ConversationMessage | null;
  output: ConversationMessage | null;
  outputText: string;
  finalOutput: ConversationMessage | null;
  finalOutputText: string;
  error: Error | null;
  refresh: (options?: {
    conversationId?: string | null;
    limit?: number;
    pageToken?: string;
  }) => Promise<ConversationMessage[]>;
  loadOlder: (options?: { limit?: number }) => Promise<ConversationMessage[]>;
  sendMessage: (content: string, options?: SendAssistantMessageOptions) => Promise<Conversation>;
  resume: (conversationId?: string | null | ResumeAssistantOptions) => Promise<void>;
  resumeIfRunning: (conversationId?: string | null) => Promise<boolean>;
  stop: (conversationId?: string | null) => Promise<void>;
  cancel: () => void;
  clearMessages: () => void;
  createConversation: (input?: CreateConversationInput) => Promise<Conversation>;
}

function resolveConversationId(
  preferred?: string | null,
  fallback?: string | null,
): string | null {
  return preferred ?? fallback ?? null;
}

function isSettledStatus(status: unknown, isStreaming: boolean): boolean {
  if (isStreaming) return false;
  const normalized = normalizeConversationStatus(status);
  if (!normalized) return true;
  return !isConversationRunningStatus(normalized);
}

export function useConversationMessages({
  client,
  podId,
  agentName,
  assistantName,
  assistantId,
  organizationId,
  instructions,
  conversationId = null,
  enabled = true,
  autoLoad = true,
  autoResume = false,
  limit = 100,
  syncOnTurnEnd = false,
  onEvent,
  onStatus,
  onMessage,
  onError,
}: UseConversationMessagesOptions): UseConversationMessagesResult {
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingOlder, setIsLoadingOlder] = useState(false);
  const autoLoadInFlightKeyRef = useRef<string | null>(null);
  const lastAutoLoadedKeyRef = useRef<string | null>(null);

  const {
    conversation: sessionConversation,
    conversationId: sessionConversationId,
    messages: sessionMessages,
    status,
    streamingText,
    isStreaming,
    error,
    refreshConversation,
    loadMessages,
    sendMessage,
    resume,
    resumeIfRunning,
    stop,
    cancel,
    clearMessages: clearSessionMessages,
    createConversation,
  } = useAssistantSession({
    client,
    podId,
    agentName: agentName ?? assistantName ?? assistantId,
    assistantName,
    assistantId,
    organizationId,
    instructions,
    conversationId: conversationId ?? undefined,
    autoLoad: false,
    autoResume: false,
    syncOnTurnEnd,
    onEvent,
    onStatus,
    onMessage,
    onError,
  });

  const refresh = useCallback(async (options: {
    conversationId?: string | null;
    limit?: number;
    pageToken?: string;
  } = {}): Promise<ConversationMessage[]> => {
    const targetConversationId = resolveConversationId(options.conversationId, sessionConversationId);
    if (!enabled || !targetConversationId) {
      setNextPageToken(null);
      setIsLoading(false);
      return [];
    }

    setIsLoading(true);
    try {
      await refreshConversation(targetConversationId);
      const response = await loadMessages({
        conversationId: targetConversationId,
        limit: options.limit ?? limit,
        pageToken: options.pageToken,
      });
      setNextPageToken(response.next_page_token ?? null);
      return sortConversationMessagesByCreatedAt(response.items ?? []);
    } finally {
      setIsLoading(false);
    }
  }, [enabled, limit, loadMessages, refreshConversation, sessionConversationId]);

  const loadOlder = useCallback(async (options: { limit?: number } = {}): Promise<ConversationMessage[]> => {
    const targetConversationId = sessionConversationId;
    if (!enabled || !targetConversationId || !nextPageToken || isLoading || isLoadingOlder) {
      return [];
    }

    setIsLoadingOlder(true);
    try {
      const response = await loadMessages({
        conversationId: targetConversationId,
        limit: options.limit ?? limit,
        pageToken: nextPageToken,
      });
      setNextPageToken(response.next_page_token ?? null);
      return sortConversationMessagesByCreatedAt(response.items ?? []);
    } finally {
      setIsLoadingOlder(false);
    }
  }, [enabled, isLoading, isLoadingOlder, limit, loadMessages, nextPageToken, sessionConversationId]);

  useEffect(() => {
    if (!enabled || !conversationId) {
      autoLoadInFlightKeyRef.current = null;
      lastAutoLoadedKeyRef.current = null;
      setNextPageToken(null);
      setIsLoading(false);
      setIsLoadingOlder(false);
      cancel();
      clearSessionMessages();
      return;
    }

    setNextPageToken(null);
    if (!autoLoad) return;

    const bootstrapKey = `${conversationId}:${limit}:${autoResume ? "resume" : "load"}`;
    if (
      autoLoadInFlightKeyRef.current === bootstrapKey
      || lastAutoLoadedKeyRef.current === bootstrapKey
    ) {
      return;
    }

    autoLoadInFlightKeyRef.current = bootstrapKey;
    let cancelled = false;
    const bootstrap = async () => {
      await refresh({ conversationId, limit });
      if (cancelled || !autoResume) return;
      await resumeIfRunning(conversationId);
    };

    void bootstrap()
      .catch(() => undefined)
      .finally(() => {
        if (autoLoadInFlightKeyRef.current === bootstrapKey) {
          autoLoadInFlightKeyRef.current = null;
        }
        lastAutoLoadedKeyRef.current = bootstrapKey;
      });
    return () => {
      cancelled = true;
    };
  }, [autoLoad, autoResume, cancel, clearSessionMessages, conversationId, enabled, limit, refresh, resumeIfRunning]);

  const messages = useMemo(
    () => sortConversationMessagesByCreatedAt(sessionMessages),
    [sessionMessages],
  );
  const latestAssistantMessage = useMemo(
    () => getLatestAssistantMessage(messages),
    [messages],
  );

  const output = latestAssistantMessage ?? null;
  const latestAssistantText = conversationMessageText(latestAssistantMessage);
  const outputText = streamingText.trim() || latestAssistantText;
  const finalOutput = isSettledStatus(status, isStreaming) ? output : null;
  const finalOutputText = isSettledStatus(status, isStreaming) ? latestAssistantText : "";
  const isRunning = isConversationRunningStatus(status) || isStreaming;

  const clearMessages = useCallback(() => {
    clearSessionMessages();
    setNextPageToken(null);
  }, [clearSessionMessages]);

  return useMemo(() => ({
    conversationId: sessionConversationId,
    conversation: sessionConversation,
    messages,
    status,
    isRunning,
    isStreaming,
    isLoading,
    isLoadingOlder,
    hasOlderMessages: !!nextPageToken,
    nextPageToken,
    streamingText,
    latestAssistantMessage,
    output,
    outputText,
    finalOutput,
    finalOutputText,
    error,
    refresh,
    loadOlder,
    sendMessage,
    resume,
    resumeIfRunning,
    stop,
    cancel,
    clearMessages,
    createConversation,
  }), [
    cancel,
    clearMessages,
    createConversation,
    error,
    finalOutput,
    finalOutputText,
    isLoading,
    isLoadingOlder,
    isRunning,
    isStreaming,
    latestAssistantMessage,
    loadOlder,
    messages,
    nextPageToken,
    output,
    outputText,
    refresh,
    resume,
    resumeIfRunning,
    sendMessage,
    sessionConversation,
    sessionConversationId,
    status,
    stop,
    streamingText,
  ]);
}
