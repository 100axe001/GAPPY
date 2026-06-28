import { useCallback, useMemo } from "react";
import { isTerminalFunctionStatus, normalizeRunStatus } from "../run-utils.js";
import type { FunctionRun, FunctionRunSummary } from "../types.js";
import {
  useFunctionSession,
  type UseFunctionSessionOptions,
  type UseFunctionSessionResult,
} from "./useFunctionSession.js";

/**
 * React hook for running a pod function and tracking its output.
 * Wraps `useFunctionSession` with a simpler API — call `start(input)`
 * from an event handler, read `output` / `finalOutput`.
 *
 * @example Run a function on button click
 * ```tsx
 * const { start, output, isFinished, isPolling } = useFunctionRun({
 *   client,
 *   functionName: "update-issue-status",
 * });
 *
 * <button onClick={() => start({ issue_id: "123", status: "closed" })}>
 *   Close issue
 * </button>
 * ```
 */
export interface UseFunctionRunOptions
  extends UseFunctionSessionOptions {}

export interface UseFunctionRunResult
  extends Omit<UseFunctionSessionResult, "start" | "listHistory"> {
  output: FunctionRun["output_data"];
  finalOutput: FunctionRun["output_data"];
  isFinished: boolean;
  start: (
    input?: Record<string, unknown>,
    options?: { functionName?: string; connect?: boolean },
  ) => Promise<FunctionRun>;
  listRuns: (options?: {
    functionName?: string;
    limit?: number;
    pageToken?: string;
  }) => Promise<FunctionRunSummary[]>;
}

export function useFunctionRun(options: UseFunctionRunOptions): UseFunctionRunResult {
  const session = useFunctionSession(options);

  const start = useCallback(async (
    input?: Record<string, unknown>,
    startOptions: { functionName?: string; connect?: boolean } = {},
  ): Promise<FunctionRun> => {
    return session.start({
      functionName: startOptions.functionName,
      input,
      connect: startOptions.connect,
    });
  }, [session]);

  const listRuns = useCallback(async (listOptions: {
    functionName?: string;
    limit?: number;
    pageToken?: string;
  } = {}): Promise<FunctionRunSummary[]> => {
    return session.listHistory(listOptions);
  }, [session]);

  return useMemo(() => {
    const normalizedStatus = normalizeRunStatus(session.status);
    const isFinished = isTerminalFunctionStatus(normalizedStatus);
    const output = session.run?.output_data ?? null;
    const finalOutput = isFinished ? output : null;

    return {
      ...session,
      output,
      finalOutput,
      isFinished,
      start,
      listRuns,
    };
  }, [listRuns, session, start]);
}
