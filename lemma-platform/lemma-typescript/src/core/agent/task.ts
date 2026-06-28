// The inline "agent task" preset: a one-shot run that goes working → output,
// rather than a full chat thread. This is pure derivation over an AgentController
// snapshot (no React), so the React hook (`useAgentTask`), a web component, and
// the product all shape the same task view identically.
import type { ConversationMessage } from "../../types.js";
import { isConversationRunningStatus } from "./messages.js";
import { selectAgentOutputs, type AgentSessionState } from "./agent-controller.js";
import { extractAgentFinalOutput, type MessageLike } from "./output.js";

export type AgentTaskStatus = "idle" | "running" | "done" | "error";

export interface AgentTaskView<T = unknown> {
  status: AgentTaskStatus;
  isRunning: boolean;
  isDone: boolean;
  /** Human label for the current activity ("Working…", "Using <tool>"). */
  activity: string;
  streamingText: string;
  /** Final answer as text. */
  outputText: string;
  /** Final answer parsed as structured output (null if not JSON / not parsed). */
  output: T | null;
  finalMessage: ConversationMessage | null;
  error: Error | null;
}

export interface SelectAgentTaskOptions {
  /** Extract structured output from the final answer. Default true. */
  parseOutput?: boolean;
}

/** A short label for what the agent is doing right now (empty when settled). */
export function agentActivityLabel(state: AgentSessionState): string {
  const running = state.isStreaming || isConversationRunningStatus(state.status);
  if (!running) return "";
  if (state.streamingTool?.toolName) return `Using ${state.streamingTool.toolName}`;
  return "Working…";
}

/**
 * Project a session snapshot into the inline task shape: a coarse status, the
 * current activity label, and the (optionally parsed) final output. Structured
 * output uses the shared `extractAgentFinalOutput` pipeline (metadata, final
 * tool calls, fenced JSON) once the run settles.
 */
export function selectAgentTask<T = unknown>(
  state: AgentSessionState,
  options: SelectAgentTaskOptions = {},
): AgentTaskView<T> {
  const outputs = selectAgentOutputs(state);
  const running = state.isStreaming || isConversationRunningStatus(state.status);

  let status: AgentTaskStatus;
  if (state.error) status = "error";
  else if (running) status = "running";
  else if (outputs.finalOutput) status = "done";
  else status = "idle";

  return {
    status,
    isRunning: running,
    isDone: status === "done",
    activity: agentActivityLabel(state),
    streamingText: state.streamingText,
    outputText: outputs.finalOutputText,
    output: options.parseOutput === false || running
      ? null
      : (extractAgentFinalOutput(state.messages as MessageLike[], {
          parseTextFallback: true,
        }) as T | null),
    finalMessage: outputs.finalOutput,
    error: state.error,
  };
}
