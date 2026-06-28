import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { FileResponse } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface CreateFolderInput {
  directoryPath?: string;
  parentId?: string;
  description?: string;
}

export interface UseCreateFolderOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  onSuccess?: (folder: FileResponse) => void;
  onError?: (error: unknown) => void;
}

export interface UseCreateFolderResult<TFile extends FileResponse = FileResponse> {
  createdFolder: TFile | null;
  isSubmitting: boolean;
  error: Error | null;
  createFolder: (name: string, options?: CreateFolderInput) => Promise<TFile | null>;
  reset: () => void;
}

export function useCreateFolder<TFile extends FileResponse = FileResponse>({
  client,
  podId,
  enabled = true,
  onSuccess,
  onError,
}: UseCreateFolderOptions): UseCreateFolderResult<TFile> {
  const [createdFolder, setCreatedFolder] = useState<TFile | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const createFolder = useCallback(async (
    name: string,
    options: CreateFolderInput = {},
  ): Promise<TFile | null> => {
    const trimmedName = name.trim();
    if (!enabled || trimmedName.length === 0) {
      return null;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextFolder = await scopedClient.files.folder.create(trimmedName, {
        ...options,
      }) as TFile;
      setCreatedFolder(nextFolder);
      onSuccessRef.current?.(nextFolder);
      return nextFolder;
    } catch (createError) {
      const normalized = normalizeError(createError, "Failed to create folder.");
      setError(normalized);
      onErrorRef.current?.(createError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, enabled, podId]);

  const reset = useCallback(() => {
    setCreatedFolder(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    createdFolder,
    isSubmitting,
    error,
    createFolder,
    reset,
  }), [createFolder, createdFolder, error, isSubmitting, reset]);
}
