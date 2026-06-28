import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { DatastoreFileSummary } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseFilesOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  autoLoad?: boolean;
  limit?: number;
  pageToken?: string;
  directoryPath?: string;
  parentId?: string;
}

export interface UseFilesResult {
  files: DatastoreFileSummary[];
  nextPageToken: string | null;
  isLoading: boolean;
  isLoadingMore: boolean;
  error: Error | null;
  refresh: (overrides?: {
    limit?: number;
    pageToken?: string;
    directoryPath?: string;
    parentId?: string;
  }) => Promise<DatastoreFileSummary[]>;
  loadMore: (overrides?: { limit?: number }) => Promise<DatastoreFileSummary[]>;
}

export function useFiles({
  client,
  podId,
  enabled = true,
  autoLoad = true,
  limit = 100,
  pageToken,
  directoryPath = "/",
  parentId,
}: UseFilesOptions): UseFilesResult {
  const [files, setFiles] = useState<DatastoreFileSummary[]>([]);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const refresh = useCallback(async (
    overrides: {
      limit?: number;
      pageToken?: string;
      directoryPath?: string;
      parentId?: string;
    } = {},
    signal?: AbortSignal,
  ): Promise<DatastoreFileSummary[]> => {
    if (!enabled) return [];

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await scopedClient.files.list({
        limit: overrides.limit ?? limit,
        pageToken: overrides.pageToken ?? pageToken,
        directoryPath: overrides.directoryPath ?? directoryPath,
        parentId: overrides.parentId ?? parentId,
      });

      if (signal?.aborted) return [];
      const nextFiles = response.items ?? [];
      setFiles(nextFiles);
      setNextPageToken(response.next_page_token ?? null);
      return nextFiles;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      setError(normalizeError(refreshError, "Failed to load files."));
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, directoryPath, enabled, limit, pageToken, parentId, podId]);

  const loadMore = useCallback(async (overrides: { limit?: number } = {}): Promise<DatastoreFileSummary[]> => {
    if (!enabled || !nextPageToken || isLoading || isLoadingMore) return [];

    setIsLoadingMore(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await scopedClient.files.list({
        limit: overrides.limit ?? limit,
        pageToken: nextPageToken,
        directoryPath,
        parentId,
      });
      const moreFiles = response.items ?? [];
      setFiles((previous) => [...previous, ...moreFiles]);
      setNextPageToken(response.next_page_token ?? null);
      return moreFiles;
    } catch (loadError) {
      setError(normalizeError(loadError, "Failed to load more files."));
      return [];
    } finally {
      setIsLoadingMore(false);
    }
  }, [client, directoryPath, enabled, isLoading, isLoadingMore, limit, nextPageToken, parentId, podId]);

  useEffect(() => {
    if (!enabled) {
      setFiles([]);
      setNextPageToken(null);
      setError(null);
      setIsLoading(false);
      setIsLoadingMore(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    void refresh({}, controller.signal);
    return () => controller.abort();
  }, [autoLoad, enabled, refresh]);

  return useMemo(() => ({
    files,
    nextPageToken,
    isLoading,
    isLoadingMore,
    error,
    refresh,
    loadMore,
  }), [error, files, isLoading, isLoadingMore, loadMore, nextPageToken, refresh]);
}
