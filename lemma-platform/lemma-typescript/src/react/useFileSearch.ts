import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { FileSearchResponse, FileSearchResultSchema, SearchMethod } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseFileSearchOptions {
  client: LemmaClient;
  podId?: string;
  query?: string;
  enabled?: boolean;
  autoLoad?: boolean;
  minQueryLength?: number;
  limit?: number;
  searchMethod?: SearchMethod;
  scopePath?: string;
  scopeMode?: "DIRECT" | "SUBTREE";
}

export interface UseFileSearchResult {
  response: FileSearchResponse | null;
  results: FileSearchResultSchema[];
  totalResults: number;
  isLoading: boolean;
  error: Error | null;
  search: (overrides?: { query?: string; limit?: number; searchMethod?: SearchMethod; scopePath?: string; scopeMode?: "DIRECT" | "SUBTREE" }) => Promise<FileSearchResponse | null>;
  reset: () => void;
}

export function useFileSearch({
  client,
  podId,
  query = "",
  enabled = true,
  autoLoad = true,
  minQueryLength = 1,
  limit = 10,
  searchMethod,
  scopePath,
  scopeMode,
}: UseFileSearchOptions): UseFileSearchResult {
  const [response, setResponse] = useState<FileSearchResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const trimmedQuery = query.trim();

  const reset = useCallback(() => {
    setResponse(null);
    setError(null);
    setIsLoading(false);
  }, []);

  const search = useCallback(async (
    overrides: { query?: string; limit?: number; searchMethod?: SearchMethod; scopePath?: string; scopeMode?: "DIRECT" | "SUBTREE" } = {},
    signal?: AbortSignal,
  ): Promise<FileSearchResponse | null> => {
    const nextQuery = (overrides.query ?? trimmedQuery).trim();
    if (!enabled || nextQuery.length < minQueryLength) {
      reset();
      return null;
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextResponse = await scopedClient.files.search(nextQuery, {
        limit: overrides.limit ?? limit,
        searchMethod: overrides.searchMethod ?? searchMethod,
        scopePath: overrides.scopePath ?? scopePath,
        scopeMode: overrides.scopeMode ?? scopeMode,
      });
      if (signal?.aborted) return null;
      setResponse(nextResponse);
      return nextResponse;
    } catch (searchError) {
      if (signal?.aborted) return null;
      setError(normalizeError(searchError, "Failed to search files."));
      setResponse(null);
      return null;
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled, limit, minQueryLength, podId, reset, scopeMode, scopePath, searchMethod, trimmedQuery]);

  useEffect(() => {
    if (!enabled || !autoLoad) return;
    if (trimmedQuery.length < minQueryLength) {
      reset();
      return;
    }

    const controller = new AbortController();
    void search({}, controller.signal);
    return () => controller.abort();
  }, [autoLoad, enabled, minQueryLength, reset, search, trimmedQuery]);

  return useMemo(() => ({
    response,
    results: response?.items ?? [],
    totalResults: response?.total ?? 0,
    isLoading,
    error,
    search,
    reset,
  }), [error, isLoading, reset, response, search]);
}
