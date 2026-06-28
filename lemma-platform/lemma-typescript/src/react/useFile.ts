import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { FileResponse } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseFileOptions {
  client: LemmaClient;
  podId?: string;
  path?: string | null;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseFileResult {
  file: FileResponse | null;
  isLoading: boolean;
  error: Error | null;
  refresh: (overrides?: { path?: string | null }) => Promise<FileResponse | null>;
}

export function useFile({
  client,
  podId,
  path = null,
  enabled = true,
  autoLoad = true,
}: UseFileOptions): UseFileResult {
  const [file, setFile] = useState<FileResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const trimmedPath = typeof path === "string" ? path.trim() : "";
  const isEnabled = enabled && trimmedPath.length > 0;

  const refresh = useCallback(async (
    overrides: { path?: string | null } = {},
    signal?: AbortSignal,
  ): Promise<FileResponse | null> => {
    const nextPath = typeof overrides.path === "string" ? overrides.path.trim() : trimmedPath;
    if (!enabled || nextPath.length === 0) {
      setFile(null);
      setError(null);
      setIsLoading(false);
      return null;
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextFile = await scopedClient.files.get(nextPath);
      if (signal?.aborted) return null;
      setFile(nextFile);
      return nextFile;
    } catch (refreshError) {
      if (signal?.aborted) return null;
      setError(normalizeError(refreshError, "Failed to load file."));
      setFile(null);
      return null;
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled, podId, trimmedPath]);

  useEffect(() => {
    if (!isEnabled) {
      setFile(null);
      setError(null);
      setIsLoading(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    void refresh({}, controller.signal);
    return () => controller.abort();
  }, [autoLoad, isEnabled, refresh]);

  return useMemo(() => ({
    file,
    isLoading,
    error,
    refresh,
  }), [error, file, isLoading, refresh]);
}
