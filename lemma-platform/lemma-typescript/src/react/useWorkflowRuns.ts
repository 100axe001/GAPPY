import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { WorkflowRunSummary } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseWorkflowRunsOptions {
  client: LemmaClient;
  podId?: string;
  workflowName: string;
  enabled?: boolean;
  autoLoad?: boolean;
  limit?: number;
  pageToken?: string;
  initialRunId?: string | null;
}

export interface UseWorkflowRunsResult {
  runs: WorkflowRunSummary[];
  total: number;
  nextPageToken: string | null;
  selectedRunId: string | null;
  effectiveSelectedRunId: string | null;
  selectedRun: WorkflowRunSummary | null;
  isLoading: boolean;
  isLoadingMore: boolean;
  error: Error | null;
  selectRun: (runId: string | null) => void;
  clearSelection: () => void;
  refresh: (overrides?: { limit?: number; pageToken?: string }) => Promise<WorkflowRunSummary[]>;
  loadMore: (overrides?: { limit?: number }) => Promise<WorkflowRunSummary[]>;
}

export function useWorkflowRuns({
  client,
  podId,
  workflowName,
  enabled = true,
  autoLoad = true,
  limit = 100,
  pageToken,
  initialRunId = null,
}: UseWorkflowRunsOptions): UseWorkflowRunsResult {
  const [runs, setRuns] = useState<WorkflowRunSummary[]>([]);
  const [total, setTotal] = useState(0);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [selectedRunId, setSelectedRunId] = useState<string | null>(initialRunId);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const trimmedWorkflowName = workflowName.trim();
  const isEnabled = enabled && trimmedWorkflowName.length > 0;

  const refresh = useCallback(async (overrides: { limit?: number; pageToken?: string } = {}, signal?: AbortSignal): Promise<WorkflowRunSummary[]> => {
    if (!isEnabled) {
      setRuns([]);
      setTotal(0);
      setNextPageToken(null);
      setError(null);
      setIsLoading(false);
      return [];
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await scopedClient.workflows.runs.list(trimmedWorkflowName, {
        limit: overrides.limit ?? limit,
        pageToken: overrides.pageToken ?? pageToken,
      });
      if (signal?.aborted) return [];
      const nextRuns = response.items ?? [];
      setRuns(nextRuns);
      setTotal((response as { total?: number }).total ?? nextRuns.length);
      setNextPageToken(response.next_page_token ?? null);
      setSelectedRunId((current) => (
        current && nextRuns.some((run) => run.id === current) ? current : initialRunId
      ));
      return nextRuns;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load workflow runs.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, initialRunId, isEnabled, limit, pageToken, podId, trimmedWorkflowName]);

  const loadMore = useCallback(async (overrides: { limit?: number } = {}): Promise<WorkflowRunSummary[]> => {
    if (!isEnabled || !nextPageToken || isLoading || isLoadingMore) {
      return [];
    }

    setIsLoadingMore(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await scopedClient.workflows.runs.list(trimmedWorkflowName, {
        limit: overrides.limit ?? limit,
        pageToken: nextPageToken,
      });
      const moreRuns = response.items ?? [];
      setRuns((previous) => [...previous, ...moreRuns]);
      setTotal((response as { total?: number }).total ?? runs.length + moreRuns.length);
      setNextPageToken(response.next_page_token ?? null);
      return moreRuns;
    } catch (loadError) {
      const normalized = normalizeError(loadError, "Failed to load more workflow runs.");
      setError(normalized);
      return [];
    } finally {
      setIsLoadingMore(false);
    }
  }, [client, isEnabled, isLoading, isLoadingMore, limit, nextPageToken, podId, trimmedWorkflowName]);

  useEffect(() => {
    setSelectedRunId(initialRunId);
  }, [initialRunId]);

  useEffect(() => {
    if (!isEnabled) {
      setRuns([]);
      setTotal(0);
      setNextPageToken(null);
      setError(null);
      setIsLoading(false);
      setIsLoadingMore(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    let cancelled = false;
    (async () => {
      try {
        await refresh({}, controller.signal);
      } catch {
        if (!cancelled) {
          setError(normalizeError(new Error("Failed to load workflow runs."), "Failed to load workflow runs."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, isEnabled, refresh]);

  const selectRun = useCallback((runId: string | null) => {
    setSelectedRunId(runId);
  }, []);

  const clearSelection = useCallback(() => {
    setSelectedRunId(null);
  }, []);

  return useMemo(() => {
    const effectiveSelectedRunId = selectedRunId ?? runs[0]?.id ?? null;
    const selectedRun = effectiveSelectedRunId
      ? runs.find((run) => run.id === effectiveSelectedRunId) ?? null
      : null;

    return {
      runs,
      total,
      nextPageToken,
      selectedRunId,
      effectiveSelectedRunId,
      selectedRun,
      isLoading,
      isLoadingMore,
      error,
      selectRun,
      clearSelection,
      refresh,
      loadMore,
    };
  }, [
    clearSelection,
    error,
    isLoading,
    isLoadingMore,
    loadMore,
    nextPageToken,
    refresh,
    runs,
    selectRun,
    selectedRunId,
    total,
  ]);
}
