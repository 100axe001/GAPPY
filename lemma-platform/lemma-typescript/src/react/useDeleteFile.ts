import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseDeleteFileOptions {
  client: LemmaClient;
  podId?: string;
  path?: string | null;
  enabled?: boolean;
  onSuccess?: (path: string) => void;
  onError?: (error: unknown) => void;
}

export interface UseDeleteFileResult {
  deletedPath: string | null;
  isSubmitting: boolean;
  error: Error | null;
  remove: (overrides?: { path?: string | null }) => Promise<boolean>;
  reset: () => void;
}

export function useDeleteFile({
  client,
  podId,
  path = null,
  enabled = true,
  onSuccess,
  onError,
}: UseDeleteFileOptions): UseDeleteFileResult {
  const [deletedPath, setDeletedPath] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedPath = typeof path === "string" ? path.trim() : "";
  const isEnabled = enabled && trimmedPath.length > 0;

  const remove = useCallback(async (
    overrides: { path?: string | null } = {},
  ): Promise<boolean> => {
    const nextPath = typeof overrides.path === "string"
      ? overrides.path.trim()
      : trimmedPath;

    if (!isEnabled || nextPath.length === 0) {
      return false;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      await scopedClient.files.delete(nextPath);
      setDeletedPath(nextPath);
      onSuccessRef.current?.(nextPath);
      return true;
    } catch (removeError) {
      const normalized = normalizeError(removeError, "Failed to delete file.");
      setError(normalized);
      onErrorRef.current?.(removeError);
      return false;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, isEnabled, podId, trimmedPath]);

  const reset = useCallback(() => {
    setDeletedPath(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    deletedPath,
    isSubmitting,
    error,
    remove,
    reset,
  }), [deletedPath, error, isSubmitting, remove, reset]);
}
