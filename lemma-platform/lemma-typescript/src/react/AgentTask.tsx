import type { ReactNode } from "react";
import {
  useAgentTask,
  type UseAgentTaskOptions,
  type UseAgentTaskResult,
} from "./useAgentTask.js";

// Headless inline-task primitive: renders exactly what its render-prop returns —
// no markup, no styling. The app owns the visuals; the task behavior (run,
// activity, schema'd output) is handled for you.
export interface AgentTaskProps<T = unknown> extends UseAgentTaskOptions {
  children: (task: UseAgentTaskResult<T>) => ReactNode;
}

export function AgentTask<T = unknown>({ children, ...options }: AgentTaskProps<T>): ReactNode {
  const task = useAgentTask<T>(options);
  return children(task);
}
