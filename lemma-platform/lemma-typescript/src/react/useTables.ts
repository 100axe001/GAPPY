import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { TableSummary } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseTablesOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  autoLoad?: boolean;
  limit?: number;
  pageToken?: string;
}

export interface UseTablesResult {
  tables: TableSummary[];
  total: number;
  nextPageToken: string | null;
  isLoading: boolean;
  isLoadingMore: boolean;
  error: Error | null;
  refresh: (overrides?: { limit?: number; pageToken?: string }) => Promise<TableSummary[]>;
  loadMore: (overrides?: { limit?: number }) => Promise<TableSummary[]>;
}

export function useTables({
  client,
  podId,
  enabled = true,
  autoLoad = true,
  limit = 100,
  pageToken,
}: UseTablesOptions): UseTablesResult {
  const [tables, setTables] = useState<TableSummary[]>([]);
  const [total, setTotal] = useState(0);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const refresh = useCallback(async (overrides: { limit?: number; pageToken?: string } = {}, signal?: AbortSignal): Promise<TableSummary[]> => {
    if (!enabled) {
      setTables([]);
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
      const response = await scopedClient.tables.list({
        limit: overrides.limit ?? limit,
        pageToken: overrides.pageToken ?? pageToken,
      });

      if (signal?.aborted) return [];
      const nextTables = response.items ?? [];
      setTables(nextTables);
      setTotal((response as { total?: number }).total ?? nextTables.length);
      setNextPageToken(response.next_page_token ?? null);
      return nextTables;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load tables.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled, limit, pageToken, podId]);

  const loadMore = useCallback(async (overrides: { limit?: number } = {}): Promise<TableSummary[]> => {
    if (!enabled || !nextPageToken || isLoading || isLoadingMore) {
      return [];
    }

    setIsLoadingMore(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await scopedClient.tables.list({
        limit: overrides.limit ?? limit,
        pageToken: nextPageToken,
      });
      const moreTables = response.items ?? [];
      setTables((previous) => [...previous, ...moreTables]);
      setTotal((response as { total?: number }).total ?? tables.length + moreTables.length);
      setNextPageToken(response.next_page_token ?? null);
      return moreTables;
    } catch (loadError) {
      const normalized = normalizeError(loadError, "Failed to load more tables.");
      setError(normalized);
      return [];
    } finally {
      setIsLoadingMore(false);
    }
  }, [client, enabled, isLoading, isLoadingMore, limit, nextPageToken, podId, tables.length]);

  useEffect(() => {
    if (!enabled) {
      setTables([]);
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
          setError(normalizeError(new Error("Failed to load tables."), "Failed to load tables."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, enabled, refresh]);

  return useMemo(() => ({
    tables,
    total,
    nextPageToken,
    isLoading,
    isLoadingMore,
    error,
    refresh,
    loadMore,
  }), [error, isLoading, isLoadingMore, loadMore, nextPageToken, refresh, tables, total]);
}
