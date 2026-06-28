import { useCallback, useEffect, useRef, useState } from "react";
import type { ConversationMessage } from "../types.js";

type RuntimeConversationMessage = ConversationMessage & { conversation_id?: string };

export interface UseAssistantRuntimeOptions {
  conversationId?: string | null;
  sessionConversationId?: string | null;
  sessionMessages?: ConversationMessage[];
}

export interface UseAssistantRuntimeResult {
  runtimeMessages: ConversationMessage[];
  appendOptimisticUserMessage: (
    content: string,
    options?: { conversationId?: string | null },
  ) => ConversationMessage;
  replaceLoadedMessages: (messages: ConversationMessage[]) => void;
  mergeMessages: (messages: ConversationMessage[]) => void;
  clear: () => void;
}

function messageText(message: Pick<ConversationMessage, "text">): string {
  return typeof message.text === "string" ? message.text.trim() : "";
}

function messageTime(message: RuntimeConversationMessage): number {
  const timestamp = new Date(message.created_at).getTime();
  return Number.isFinite(timestamp) ? timestamp : 0;
}

function isOptimisticId(messageId: string): boolean {
  return messageId.startsWith("optimistic-user-");
}

const OPTIMISTIC_MATCH_WINDOW_MS = 2 * 60 * 1000;

function upsertRuntimeMessage(
  previous: RuntimeConversationMessage[],
  incoming: RuntimeConversationMessage,
): RuntimeConversationMessage[] {
  const next = [...previous];
  const directIndex = next.findIndex((message) => message.id === incoming.id);

  if (directIndex >= 0) {
    next[directIndex] = incoming;
    return next;
  }

  if (incoming.role === "user") {
    const incomingText = messageText(incoming);
    if (incomingText) {
      const incomingTimestamp = messageTime(incoming);
      let optimisticIndex = -1;
      let bestDistance = Number.POSITIVE_INFINITY;

      next.forEach((message, index) => {
        if (
          message.role !== "user"
          || !isOptimisticId(message.id)
          || messageText(message) !== incomingText
        ) {
          return;
        }

        const distance = Math.abs(messageTime(message) - incomingTimestamp);
        if (distance > OPTIMISTIC_MATCH_WINDOW_MS || distance >= bestDistance) {
          return;
        }

        optimisticIndex = index;
        bestDistance = distance;
      });

      if (optimisticIndex >= 0) {
        next[optimisticIndex] = incoming;
        return next;
      }
    }
  }

  next.push(incoming);
  return next;
}

function toRuntimeMessage(
  message: ConversationMessage,
  fallbackConversationId?: string | null,
): RuntimeConversationMessage {
  const runtimeMessage = message as RuntimeConversationMessage;
  if (runtimeMessage.conversation_id || !fallbackConversationId) {
    return runtimeMessage;
  }

  return {
    ...runtimeMessage,
    conversation_id: fallbackConversationId,
  };
}

function buildOptimisticId(): string {
  if (typeof globalThis.crypto !== "undefined" && typeof globalThis.crypto.randomUUID === "function") {
    return `optimistic-user-${globalThis.crypto.randomUUID()}`;
  }

  return `optimistic-user-${Date.now()}-${Math.random().toString(36).slice(2)}`;
}

export function useAssistantRuntime({
  conversationId = null,
  sessionConversationId = null,
  sessionMessages = [],
}: UseAssistantRuntimeOptions): UseAssistantRuntimeResult {
  const [runtimeMessages, setRuntimeMessages] = useState<RuntimeConversationMessage[]>([]);

  const mergeMessages = useCallback((messages: ConversationMessage[]) => {
    setRuntimeMessages((previous) => {
      const merged = messages.reduce(
        (accumulator, message) => upsertRuntimeMessage(accumulator, toRuntimeMessage(message, conversationId)),
        previous,
      );

      return [...merged].sort((a, b) => messageTime(a) - messageTime(b));
    });
  }, [conversationId]);

  const replaceLoadedMessages = useCallback((messages: ConversationMessage[]) => {
    const normalized = messages
      .map((message) => toRuntimeMessage(message, conversationId))
      .filter((message) => !conversationId || message.conversation_id === conversationId);

    setRuntimeMessages((previous) => {
      const scopedPrevious = previous.filter((message) => !conversationId || message.conversation_id === conversationId);

      // Loads can complete after optimistic appends or stream events. Merge the
      // loaded snapshot into the current runtime state so newer local messages
      // are not temporarily dropped while the server catches up.
      const merged = normalized.reduce(
        (accumulator, message) => upsertRuntimeMessage(accumulator, message),
        scopedPrevious,
      );

      return [...merged].sort((a, b) => messageTime(a) - messageTime(b));
    });
  }, [conversationId]);

  const appendOptimisticUserMessage = useCallback((
    content: string,
    options?: { conversationId?: string | null },
  ): ConversationMessage => {
    const trimmed = content.trim();
    const optimisticConversationId = options?.conversationId ?? conversationId ?? undefined;
    const optimistic: RuntimeConversationMessage = {
      id: buildOptimisticId(),
      role: "user",
      kind: "TEXT",
      text: trimmed,
      created_at: new Date().toISOString(),
      metadata: null,
      ...(optimisticConversationId ? { conversation_id: optimisticConversationId } : {}),
    };

    setRuntimeMessages((previous) => {
      const next = upsertRuntimeMessage(previous, optimistic);
      return [...next].sort((a, b) => messageTime(a) - messageTime(b));
    });

    return optimistic;
  }, [conversationId]);

  const clear = useCallback(() => {
    setRuntimeMessages([]);
  }, []);

  useEffect(() => {
    lastSessionMessageIdRef.current = null;
    setRuntimeMessages((previous) => {
      if (!conversationId) {
        return [];
      }

      return previous.filter((message) => message.conversation_id === conversationId);
    });
  }, [conversationId]);

  const lastSessionMessageIdRef = useRef<string | null>(null);

  useEffect(() => {
    if (sessionMessages.length === 0) return;

    const lastSessionMessage = sessionMessages[sessionMessages.length - 1];
    const lastSessionId = lastSessionMessage?.id ?? null;
    if (lastSessionId && lastSessionId === lastSessionMessageIdRef.current) return;
    lastSessionMessageIdRef.current = lastSessionId;

    const fallbackConversationId = sessionConversationId ?? conversationId;

    const normalized = sessionMessages
      .map((message) => toRuntimeMessage(message, fallbackConversationId))
      .filter((message) => !conversationId || message.conversation_id === conversationId);

    if (normalized.length === 0) return;
    mergeMessages(normalized);
  }, [conversationId, mergeMessages, sessionConversationId, sessionMessages]);

  return {
    runtimeMessages,
    appendOptimisticUserMessage,
    replaceLoadedMessages,
    mergeMessages,
    clear,
  };
}
