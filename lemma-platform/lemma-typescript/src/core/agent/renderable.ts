// Renderable agent-message types. A "renderable message" is the richer,
// parts-based view of a conversation message (text / reasoning / tool parts)
// that the display pipeline operates on. These are pure data types — they live
// in the core so the pipeline (and the React hooks that produce them) share one
// definition. Re-exported from lemma-sdk/react for back-compat.
import type { MessageKind } from "../../types.js";

export interface AssistantToolInvocation {
  toolCallId: string;
  toolName: string;
  args: Record<string, unknown>;
  state: "call" | "result";
  result?: Record<string, unknown>;
}

export type AssistantMessagePart =
  | {
      id: string;
      type: "text";
      text: string;
    }
  | {
      id: string;
      type: "reasoning";
      text: string;
      state?: "streaming" | "done";
      durationMs?: number;
      startedAtMs?: number;
      /** Set when a turn's intermediate text was folded into a collapsible trace. */
      traceNote?: boolean;
    }
  | {
      id: string;
      type: "tool";
      toolInvocation: AssistantToolInvocation;
    };

export interface AssistantRenderableMessage {
  id: string;
  role: "user" | "assistant" | "system";
  content: string;
  toolInvocations?: AssistantToolInvocation[];
  parts?: AssistantMessagePart[];
  createdAt?: Date;
  conversation_id?: string;
  sequence?: number;
  agent_run_id?: string | null;
  metadata?: Record<string, unknown> | null;
  message_metadata?: Record<string, unknown> | null;
  /** Flat message fields, passed through so consumers can inspect the raw kind. */
  kind?: MessageKind;
  tool_call_id?: string | null;
  tool_name?: string | null;
  tool_args?: unknown;
  tool_result?: unknown;
}
