import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { FileResponse } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UpdateFileInput {
  file?: Blob;
  name?: string;
  description?: string;
  directoryPath?: string;
  parentId?: string;
  newPath?: string;
  searchEnabled?: boolean;
}

export interface UseUpdateFileOptions {
  client: LemmaClient;
  podId?: string;
  path?: string | null;
  enabled?: boolean;
  onSuccess?: (file: FileResponse) => void;
  onError?: (error: unknown) => void;
}

export interface UseUpdateFileResult<TFile extends FileResponse = FileResponse> {
  updatedFile: TFile | null;
  isSubmitting: boolean;
  error: Error | null;
  update: (input?: UpdateFileInput, overrides?: { path?: string | null }) => Promise<TFile | null>;
  reset: () => void;
}

export function useUpdateFile<TFile extends FileResponse = FileResponse>({
  client,
  podId,
  path = null,
  enabled = true,
  onSuccess,
  onError,
}: UseUpdateFileOptions): UseUpdateFileResult<TFile> {
  const [updatedFile, setUpdatedFile] = useState<TFile | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedPath = typeof path === "string" ? path.trim() : "";
  const isEnabled = enabled && trimmedPath.length > 0;

  const update = useCallback(async (
    input: UpdateFileInput = {},
    overrides: { path?: string | null } = {},
  ): Promise<TFile | null> => {
    const nextPath = typeof overrides.path === "string"
      ? overrides.path.trim()
      : trimmedPath;

    if (!isEnabled || nextPath.length === 0) {
      return null;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextFile = await scopedClient.files.update(nextPath, {
        ...input,
      }) as TFile;
      setUpdatedFile(nextFile);
      onSuccessRef.current?.(nextFile);
      return nextFile;
    } catch (updateError) {
      const normalized = normalizeError(updateError, "Failed to update file.");
      setError(normalized);
      onErrorRef.current?.(updateError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, isEnabled, podId, trimmedPath]);

  const reset = useCallback(() => {
    setUpdatedFile(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    updatedFile,
    isSubmitting,
    error,
    update,
    reset,
  }), [error, isSubmitting, reset, update, updatedFile]);
}
