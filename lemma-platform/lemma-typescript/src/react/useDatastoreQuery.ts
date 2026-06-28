import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { DatastoreQueryResponse } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseDatastoreQueryOptions {
  client: LemmaClient;
  podId?: string;
  query?: string | null;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseDatastoreQueryResult<TRow extends Record<string, unknown> = Record<string, unknown>> {
  response: DatastoreQueryResponse | null;
  items: TRow[];
  total: number;
  sql: string;
  isLoading: boolean;
  error: Error | null;
  refresh: (overrides?: { query?: string | null }) => Promise<TRow[]>;
  reset: () => void;
}

export function useDatastoreQuery<TRow extends Record<string, unknown> = Record<string, unknown>>({
  client,
  podId,
  query = null,
  enabled = true,
  autoLoad = true,
}: UseDatastoreQueryOptions): UseDatastoreQueryResult<TRow> {
  const [response, setResponse] = useState<DatastoreQueryResponse | null>(null);
  const [sql, setSql] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const trimmedQuery = typeof query === "string" ? query.trim() : "";
  const isEnabled = enabled && trimmedQuery.length > 0;

  const reset = useCallback(() => {
    setResponse(null);
    setSql("");
    setError(null);
    setIsLoading(false);
  }, []);

  const refresh = useCallback(async (
    overrides: { query?: string | null } = {},
    signal?: AbortSignal,
  ): Promise<TRow[]> => {
    const nextQuery = typeof overrides.query === "string"
      ? overrides.query.trim()
      : trimmedQuery;

    if (!enabled || nextQuery.length === 0) {
      reset();
      return [];
    }

    setIsLoading(true);
    setError(null);
    setSql(nextQuery);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextResponse = await scopedClient.datastore.query(nextQuery);
      if (signal?.aborted) return [];
      setResponse(nextResponse);
      return (nextResponse.items ?? []) as TRow[];
    } catch (queryError) {
      if (signal?.aborted) return [];
      setError(normalizeError(queryError, "Failed to execute datastore query."));
      setResponse(null);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled, podId, reset, trimmedQuery]);

  useEffect(() => {
    if (!isEnabled || !autoLoad) {
      if (!isEnabled) reset();
      return;
    }
    const controller = new AbortController();
    void refresh({}, controller.signal);
    return () => controller.abort();
  }, [autoLoad, isEnabled, refresh, reset]);

  return useMemo(() => ({
    response,
    items: (response?.items ?? []) as TRow[],
    total: response?.total ?? 0,
    sql,
    isLoading,
    error,
    refresh,
    reset,
  }), [error, isLoading, refresh, reset, response, sql]);
}
