import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { DirectoryTreeNode, DirectoryTreeResponse } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseFileTreeOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  autoLoad?: boolean;
  rootPath?: string;
  filesPerDirectory?: number;
}

export interface UseFileTreeResult {
  tree: DirectoryTreeNode | null;
  response: DirectoryTreeResponse | null;
  isLoading: boolean;
  error: Error | null;
  refresh: (overrides?: {
    rootPath?: string;
    filesPerDirectory?: number;
  }) => Promise<DirectoryTreeResponse | null>;
}

export function useFileTree({
  client,
  podId,
  enabled = true,
  autoLoad = true,
  rootPath = "/",
  filesPerDirectory = 3,
}: UseFileTreeOptions): UseFileTreeResult {
  const [response, setResponse] = useState<DirectoryTreeResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const refresh = useCallback(async (
    overrides: {
      rootPath?: string;
      filesPerDirectory?: number;
    } = {},
    signal?: AbortSignal,
  ): Promise<DirectoryTreeResponse | null> => {
    if (!enabled) {
      setResponse(null);
      setError(null);
      setIsLoading(false);
      return null;
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextResponse = await scopedClient.files.tree({
        rootPath: overrides.rootPath ?? rootPath,
        filesPerDirectory: overrides.filesPerDirectory ?? filesPerDirectory,
      });
      if (signal?.aborted) return null;
      setResponse(nextResponse);
      return nextResponse;
    } catch (refreshError) {
      if (signal?.aborted) return null;
      setError(normalizeError(refreshError, "Failed to load file tree."));
      setResponse(null);
      return null;
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled, filesPerDirectory, podId, rootPath]);

  useEffect(() => {
    if (!enabled) {
      setResponse(null);
      setError(null);
      setIsLoading(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    void refresh({}, controller.signal);
    return () => controller.abort();
  }, [autoLoad, enabled, refresh]);

  return useMemo(() => ({
    tree: response?.tree ?? null,
    response,
    isLoading,
    error,
    refresh,
  }), [error, isLoading, refresh, response]);
}
