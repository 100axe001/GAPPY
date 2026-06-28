import { useCallback, useMemo } from "react";
import { selectWorkflowOutputs } from "../core/workflow/index.js";
import type { FlowRun, WorkflowRunInputs, WorkflowRunSummary } from "../types.js";
import {
  useFlowSession,
  type UseFlowSessionOptions,
  type UseFlowSessionResult,
} from "./useFlowSession.js";

export interface UseWorkflowRunOptions
  extends Omit<UseFlowSessionOptions, "flowName"> {
  workflowName?: string;
}

export interface UseWorkflowRunResult
  extends Omit<UseFlowSessionResult, "start" | "listHistory"> {
  output: FlowRun["execution_context"] | null;
  finalOutput: FlowRun["execution_context"] | null;
  isWaitingForInput: boolean;
  isFinished: boolean;
  start: (
    inputs?: WorkflowRunInputs,
    options?: { workflowName?: string; connect?: boolean },
  ) => Promise<FlowRun>;
  listRuns: (options?: {
    workflowName?: string;
    limit?: number;
    pageToken?: string;
  }) => Promise<WorkflowRunSummary[]>;
}

function resolveWorkflowName(base?: string, override?: string): string {
  const resolved = override ?? base;
  if (!resolved) {
    throw new Error("workflowName is required.");
  }
  return resolved;
}

export function useWorkflowRun({
  workflowName,
  ...options
}: UseWorkflowRunOptions): UseWorkflowRunResult {
  const session = useFlowSession({
    ...options,
    flowName: workflowName,
  });

  const start = useCallback(async (
    inputs?: WorkflowRunInputs,
    startOptions: { workflowName?: string; connect?: boolean } = {},
  ): Promise<FlowRun> => {
    return session.start({
      flowName: resolveWorkflowName(workflowName, startOptions.workflowName),
      inputs,
      connect: startOptions.connect,
    });
  }, [session, workflowName]);

  const listRuns = useCallback(async (listOptions: {
    workflowName?: string;
    limit?: number;
    pageToken?: string;
  } = {}): Promise<WorkflowRunSummary[]> => {
    return session.listHistory({
      flowName: resolveWorkflowName(workflowName, listOptions.workflowName),
      limit: listOptions.limit,
      pageToken: listOptions.pageToken,
    });
  }, [session, workflowName]);

  return useMemo(() => {
    const { isFinished, isWaitingForInput, output, finalOutput } = selectWorkflowOutputs(session.run);
    return {
      ...session,
      output,
      finalOutput,
      isWaitingForInput,
      isFinished,
      start,
      listRuns,
    };
  }, [listRuns, session, start]);
}
