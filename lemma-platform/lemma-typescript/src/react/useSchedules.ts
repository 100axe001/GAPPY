import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { Schedule, ScheduleType } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseSchedulesOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  autoLoad?: boolean;
  scheduleType?: ScheduleType | null;
  isActive?: boolean | null;
  agentName?: string | null;
  workflowName?: string | null;
  limit?: number;
  pageToken?: string | null;
}

export interface UseSchedulesResult {
  schedules: Schedule[];
  total: number;
  nextPageToken: string | null;
  isLoading: boolean;
  isLoadingMore: boolean;
  error: Error | null;
  refresh: (overrides?: { limit?: number; pageToken?: string | null }) => Promise<Schedule[]>;
  loadMore: (overrides?: { limit?: number }) => Promise<Schedule[]>;
}

export function useSchedules({
  client,
  podId,
  enabled = true,
  autoLoad = true,
  scheduleType = null,
  isActive = null,
  agentName = null,
  workflowName = null,
  limit = 100,
  pageToken = null,
}: UseSchedulesOptions): UseSchedulesResult {
  const [schedules, setSchedules] = useState<Schedule[]>([]);
  const [total, setTotal] = useState(0);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const refresh = useCallback(async (
    overrides: { limit?: number; pageToken?: string | null } = {},
    signal?: AbortSignal,
  ): Promise<Schedule[]> => {
    if (!enabled) {
      setSchedules([]);
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
      const response = await scopedClient.schedules.list({
        scheduleType,
        isActive,
        agentName,
        workflowName,
        limit: overrides.limit ?? limit,
        pageToken: overrides.pageToken ?? pageToken,
      });
      if (signal?.aborted) return [];
      const nextSchedules = response.items ?? [];
      setSchedules(nextSchedules);
      setTotal((response as { total?: number }).total ?? nextSchedules.length);
      setNextPageToken(response.next_page_token ?? null);
      return nextSchedules;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load schedules.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [agentName, client, enabled, isActive, limit, pageToken, podId, scheduleType, workflowName]);

  const loadMore = useCallback(async (overrides: { limit?: number } = {}): Promise<Schedule[]> => {
    if (!enabled || !nextPageToken || isLoading || isLoadingMore) {
      return [];
    }

    setIsLoadingMore(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await scopedClient.schedules.list({
        scheduleType,
        isActive,
        agentName,
        workflowName,
        limit: overrides.limit ?? limit,
        pageToken: nextPageToken,
      });
      const moreSchedules = response.items ?? [];
      setSchedules((previous) => [...previous, ...moreSchedules]);
      setTotal((response as { total?: number }).total ?? schedules.length + moreSchedules.length);
      setNextPageToken(response.next_page_token ?? null);
      return moreSchedules;
    } catch (loadError) {
      const normalized = normalizeError(loadError, "Failed to load more schedules.");
      setError(normalized);
      return [];
    } finally {
      setIsLoadingMore(false);
    }
  }, [
    agentName,
    client,
    enabled,
    isActive,
    isLoading,
    isLoadingMore,
    limit,
    nextPageToken,
    podId,
    scheduleType,
    schedules.length,
    workflowName,
  ]);

  useEffect(() => {
    if (!enabled) {
      setSchedules([]);
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
    schedules,
    total,
    nextPageToken,
    isLoading,
    isLoadingMore,
    error,
    refresh,
    loadMore,
  }), [error, isLoading, isLoadingMore, loadMore, nextPageToken, refresh, schedules, total]);
}
