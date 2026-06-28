import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { ListRecordsOptions } from "../types.js";
import { normalizeError, resolvePodClient, stringifyComparable } from "./utils.js";

export interface UseRecordsOptions extends ListRecordsOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseRecordsResult<TRecord extends Record<string, unknown> = Record<string, unknown>> {
  records: TRecord[];
  total: number;
  nextPageToken: string | null;
  isLoading: boolean;
  isLoadingMore: boolean;
  error: Error | null;
  refresh: (overrides?: Partial<ListRecordsOptions>) => Promise<TRecord[]>;
  loadMore: (overrides?: Partial<ListRecordsOptions>) => Promise<TRecord[]>;
}




export function useRecords<TRecord extends Record<string, unknown> = Record<string, unknown>>({
  client,
  podId,
  tableName,
  filters,
  sort,
  limit = 20,
  pageToken,
  offset,
  enabled = true,
  autoLoad = true,
}: UseRecordsOptions): UseRecordsResult<TRecord> {
  const [records, setRecords] = useState<TRecord[]>([]);
  const [total, setTotal] = useState(0);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const trimmedTableName = tableName.trim();
  const isEnabled = enabled && trimmedTableName.length > 0;
  const filtersKey = stringifyComparable(filters);
  const sortKey = stringifyComparable(sort);
  const stableFilters = useMemo(() => filters, [filtersKey]);
  const stableSort = useMemo(() => sort, [sortKey]);

  const refresh = useCallback(async (overrides: Partial<ListRecordsOptions> = {}, signal?: AbortSignal): Promise<TRecord[]> => {
    if (!isEnabled) {
      setRecords([]);
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
      const response = await scopedClient.records.list(trimmedTableName, {
        filters: overrides.filters ?? stableFilters,
        sort: overrides.sort ?? stableSort,
        limit: overrides.limit ?? limit,
        pageToken: overrides.pageToken ?? pageToken,
        offset: overrides.offset ?? offset,
      });

      if (signal?.aborted) return [];
      const nextRecords = (response.items ?? []) as TRecord[];
      setRecords(nextRecords);
      setTotal(response.total ?? nextRecords.length);
      setNextPageToken(response.next_page_token ?? null);
      return nextRecords;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load records.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [
    client,
    isEnabled,
    limit,
    offset,
    pageToken,
    podId,
    stableFilters,
    stableSort,
    trimmedTableName,
  ]);

  const loadMore = useCallback(async (overrides: Partial<ListRecordsOptions> = {}): Promise<TRecord[]> => {
    const loadedCount = records.length;
    const canLoadWithCursor = Boolean(nextPageToken);
    const canLoadWithOffset = loadedCount < total;

    if (!isEnabled || isLoading || isLoadingMore || (!canLoadWithCursor && !canLoadWithOffset)) {
      return [];
    }

    setIsLoadingMore(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await scopedClient.records.list(trimmedTableName, {
        filters: stableFilters,
        sort: stableSort,
        limit: overrides.limit ?? limit,
        pageToken: overrides.pageToken ?? nextPageToken ?? undefined,
        offset: overrides.offset ?? (nextPageToken ? undefined : (offset ?? 0) + loadedCount),
      });
      const moreRecords = (response.items ?? []) as TRecord[];
      setRecords((previous) => [...previous, ...moreRecords]);
      setTotal((response as { total?: number }).total ?? loadedCount + moreRecords.length);
      setNextPageToken(response.next_page_token ?? null);
      return moreRecords;
    } catch (loadError) {
      const normalized = normalizeError(loadError, "Failed to load more records.");
      setError(normalized);
      return [];
    } finally {
      setIsLoadingMore(false);
    }
  }, [client, isEnabled, isLoading, isLoadingMore, limit, nextPageToken, offset, podId, records.length, stableFilters, stableSort, total, trimmedTableName]);

  useEffect(() => {
    if (!isEnabled) {
      setRecords([]);
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
          setError(normalizeError(new Error("Failed to load records."), "Failed to load records."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, isEnabled, refresh]);

  return useMemo(() => ({
    records,
    total,
    nextPageToken,
    isLoading,
    isLoadingMore,
    error,
    refresh,
    loadMore,
  }), [error, isLoading, isLoadingMore, loadMore, nextPageToken, records, refresh, total]);
}
