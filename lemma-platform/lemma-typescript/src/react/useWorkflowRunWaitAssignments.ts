import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { WorkflowRunWait } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseWorkflowRunWaitAssignmentsOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  autoLoad?: boolean;
  limit?: number;
  pageToken?: string | null;
}

export interface UseWorkflowRunWaitAssignmentsResult {
  assignments: WorkflowRunWait[];
  total: number;
  nextPageToken: string | null;
  isLoading: boolean;
  isLoadingMore: boolean;
  error: Error | null;
  refresh: (overrides?: { limit?: number; pageToken?: string | null }) => Promise<WorkflowRunWait[]>;
  loadMore: (overrides?: { limit?: number }) => Promise<WorkflowRunWait[]>;
}

export function useWorkflowRunWaitAssignments({
  client,
  podId,
  enabled = true,
  autoLoad = true,
  limit = 100,
  pageToken = null,
}: UseWorkflowRunWaitAssignmentsOptions): UseWorkflowRunWaitAssignmentsResult {
  const [assignments, setAssignments] = useState<WorkflowRunWait[]>([]);
  const [total, setTotal] = useState(0);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const refresh = useCallback(async (
    overrides: { limit?: number; pageToken?: string | null } = {},
    signal?: AbortSignal,
  ): Promise<WorkflowRunWait[]> => {
    if (!enabled) {
      setAssignments([]);
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
      const response = await scopedClient.workflows.runs.waitingAssignedToMe({
        limit: overrides.limit ?? limit,
        pageToken: overrides.pageToken ?? pageToken ?? undefined,
      });
      if (signal?.aborted) return [];
      const nextAssignments = response.items ?? [];
      setAssignments(nextAssignments);
      setTotal((response as { total?: number }).total ?? nextAssignments.length);
      setNextPageToken(response.next_page_token ?? null);
      return nextAssignments;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load waiting workflow runs.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled, limit, pageToken, podId]);

  const loadMore = useCallback(async (overrides: { limit?: number } = {}): Promise<WorkflowRunWait[]> => {
    if (!enabled || !nextPageToken || isLoading || isLoadingMore) {
      return [];
    }

    setIsLoadingMore(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await scopedClient.workflows.runs.waitingAssignedToMe({
        limit: overrides.limit ?? limit,
        pageToken: nextPageToken,
      });
      const moreAssignments = response.items ?? [];
      setAssignments((previous) => [...previous, ...moreAssignments]);
      setTotal((response as { total?: number }).total ?? assignments.length + moreAssignments.length);
      setNextPageToken(response.next_page_token ?? null);
      return moreAssignments;
    } catch (loadError) {
      const normalized = normalizeError(loadError, "Failed to load more waiting workflow runs.");
      setError(normalized);
      return [];
    } finally {
      setIsLoadingMore(false);
    }
  }, [assignments.length, client, enabled, isLoading, isLoadingMore, limit, nextPageToken, podId]);

  useEffect(() => {
    if (!enabled) {
      setAssignments([]);
      setTotal(0);
      setNextPageToken(null);
      setError(null);
      setIsLoading(false);
      setIsLoadingMore(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    void refresh({}, controller.signal);
    return () => {
      controller.abort();
    };
  }, [autoLoad, enabled, refresh]);

  return useMemo(() => ({
    assignments,
    total,
    nextPageToken,
    isLoading,
    isLoadingMore,
    error,
    refresh,
    loadMore,
  }), [assignments, error, isLoading, isLoadingMore, loadMore, nextPageToken, refresh, total]);
}
