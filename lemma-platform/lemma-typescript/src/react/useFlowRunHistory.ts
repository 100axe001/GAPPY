import { useCallback, useEffect, useMemo, useState } from "react";
import type { FlowRun, WorkflowRunSummary } from "../types.js";
import type { UseFlowSessionResult } from "./useFlowSession.js";
import { normalizeError } from "./utils.js";

export interface UseFlowRunHistoryOptions {
  session: Pick<UseFlowSessionResult, "run" | "runId" | "setRunId" | "listHistory">;
  flowName: string;
  limit?: number;
  autoRefresh?: boolean;
}

export interface UseFlowRunHistoryResult {
  runs: WorkflowRunSummary[];
  selectedRunId: string | null;
  effectiveSelectedRunId: string | null;
  selectedRun: WorkflowRunSummary | null;
  isLoading: boolean;
  error: Error | null;
  setSelectedRunId: (runId: string | null) => void;
  refresh: () => Promise<WorkflowRunSummary[]>;
}


export function useFlowRunHistory({
  session,
  flowName,
  limit = 100,
  autoRefresh = true,
}: UseFlowRunHistoryOptions): UseFlowRunHistoryResult {
  const { listHistory, run: liveRun, runId: liveRunId, setRunId } = session;
  const [runs, setRuns] = useState<WorkflowRunSummary[]>([]);
  const [selectedRunId, setSelectedRunId] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const effectiveSelectedRunId = selectedRunId ?? runs[0]?.id ?? null;

  const refresh = useCallback(async (): Promise<WorkflowRunSummary[]> => {
    setIsLoading(true);
    setError(null);

    try {
      const nextRuns = await listHistory({ flowName, limit });
      setRuns(nextRuns);
      setSelectedRunId((previous) => (
        previous && nextRuns.some((run) => run.id === previous) ? previous : null
      ));
      return nextRuns;
    } catch (refreshError) {
      const normalized = normalizeError(refreshError, "Failed to list flow runs.");
      setError(normalized);
      return [];
    } finally {
      setIsLoading(false);
    }
  }, [flowName, limit, listHistory]);

  useEffect(() => {
    if (!autoRefresh) return;
    void refresh();
  }, [autoRefresh, flowName, refresh]);

  useEffect(() => {
    if (!autoRefresh || !liveRunId) return;
    void refresh();
  }, [autoRefresh, liveRunId, refresh]);

  useEffect(() => {
    if (!effectiveSelectedRunId) return;
    setRunId(effectiveSelectedRunId);
  }, [effectiveSelectedRunId, setRunId]);

  useEffect(() => {
    if (!liveRun?.id) return;

    const liveRunSummary: WorkflowRunSummary = {
      ...liveRun,
      id: liveRun.id,
    };

    setRuns((previous) => {
      const index = previous.findIndex((run) => run.id === liveRun.id);
      if (index === -1) {
        return [liveRunSummary, ...previous];
      }

      const next = [...previous];
      next[index] = { ...next[index], ...liveRunSummary };
      return next;
    });
  }, [liveRun]);

  const selectedRun = useMemo(() => {
    if (!effectiveSelectedRunId) return null;
    if (liveRun?.id === effectiveSelectedRunId) {
      return { ...liveRun, id: liveRun.id };
    }
    return runs.find((run) => run.id === effectiveSelectedRunId) ?? null;
  }, [effectiveSelectedRunId, liveRun, runs]);

  return {
    runs,
    selectedRunId,
    effectiveSelectedRunId,
    selectedRun,
    isLoading,
    error,
    setSelectedRunId,
    refresh,
  };
}
