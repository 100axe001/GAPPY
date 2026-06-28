import { useCallback, useEffect, useMemo, useRef, useSyncExternalStore } from "react";
import type { LemmaClient } from "../client.js";
import type { ConversationMessage } from "../types.js";
import {
  AgentController,
  selectAgentTask,
  type AgentControllerOptions,
  type AgentTaskStatus,
  type CreateConversationInput,
} from "../core/agent/index.js";

// The inline agent-task preset: fire a one-shot run, watch the activity, render
// the (optionally schema-parsed) output. A thin React adapter over AgentController
// + the pure `selectAgentTask` projection — not a full chat thread.
export interface UseAgentTaskOptions {
  client: LemmaClient;
  agentName?: string;
  podId?: string;
  instructions?: string | null;
  title?: string | null;
  metadata?: Record<string, unknown> | null;
  /** Parse the final answer as JSON structured output. Default true. */
  parseOutput?: boolean;
  onError?: (error: unknown) => void;
}

export interface UseAgentTaskResult<T = unknown> {
  status: AgentTaskStatus;
  isRunning: boolean;
  isDone: boolean;
  activity: string;
  streamingText: string;
  outputText: string;
  output: T | null;
  finalMessage: ConversationMessage | null;
  error: Error | null;
  /** Start a fresh run with the given input (string, or JSON-serializable object). */
  run: (input: string | Record<string, unknown>) => Promise<void>;
  /** Stop the active run (aborts the local stream and asks the server to stop). */
  stop: () => void;
  /** Clear the task back to idle. */
  reset: () => void;
}

function toControllerOptions(options: UseAgentTaskOptions): AgentControllerOptions {
  return {
    client: options.client,
    scope: { podId: options.podId ?? null, agentName: options.agentName ?? null },
    instructions: options.instructions ?? null,
    onError: options.onError,
  };
}

export function useAgentTask<T = unknown>(options: UseAgentTaskOptions): UseAgentTaskResult<T> {
  const { parseOutput = true, title, instructions, metadata } = options;

  const controllerRef = useRef<AgentController | null>(null);
  if (controllerRef.current === null) {
    controllerRef.current = new AgentController(toControllerOptions(options));
  }
  const controller = controllerRef.current;

  useEffect(() => {
    controller.setOptions(toControllerOptions(options));
  });

  const state = useSyncExternalStore(
    controller.subscribe,
    controller.getState,
    controller.getState,
  );

  useEffect(() => () => controller.destroy(), [controller]);

  const run = useCallback(async (input: string | Record<string, unknown>): Promise<void> => {
    const createInput: CreateConversationInput = {
      title: title ?? null,
      instructions: instructions ?? undefined,
      metadata: metadata ?? null,
      setActive: true,
    };
    await controller.createConversation(createInput);
    const content = typeof input === "string" ? input : JSON.stringify(input);
    await controller.sendMessage(content);
  }, [controller, title, instructions, metadata]);

  const stop = useCallback(() => {
    controller.cancel();
    if (controller.getState().conversationId) {
      void controller.stop().catch(() => {
        // Best-effort server stop; the local stream is already aborted.
      });
    }
  }, [controller]);

  const reset = useCallback(() => {
    controller.setConversationId(null);
  }, [controller]);

  const task = useMemo(() => selectAgentTask<T>(state, { parseOutput }), [state, parseOutput]);

  return { ...task, run, stop, reset };
}
