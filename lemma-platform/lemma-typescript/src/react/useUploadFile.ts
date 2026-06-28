import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { FileResponse } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UploadFileInput {
  name?: string;
  directoryPath?: string;
  parentId?: string;
  searchEnabled?: boolean;
  description?: string;
}

export interface UseUploadFileOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  onSuccess?: (file: FileResponse) => void;
  onError?: (error: unknown) => void;
}

export interface UseUploadFileResult<TFile extends FileResponse = FileResponse> {
  uploadedFile: TFile | null;
  isSubmitting: boolean;
  error: Error | null;
  upload: (file: Blob, options?: UploadFileInput) => Promise<TFile | null>;
  reset: () => void;
}

export function useUploadFile<TFile extends FileResponse = FileResponse>({
  client,
  podId,
  enabled = true,
  onSuccess,
  onError,
}: UseUploadFileOptions): UseUploadFileResult<TFile> {
  const [uploadedFile, setUploadedFile] = useState<TFile | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const upload = useCallback(async (
    file: Blob,
    options: UploadFileInput = {},
  ): Promise<TFile | null> => {
    if (!enabled) {
      return null;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextFile = await scopedClient.files.upload(file, {
        ...options,
      }) as TFile;
      setUploadedFile(nextFile);
      onSuccessRef.current?.(nextFile);
      return nextFile;
    } catch (uploadError) {
      const normalized = normalizeError(uploadError, "Failed to upload file.");
      setError(normalized);
      onErrorRef.current?.(uploadError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, enabled, podId]);

  const reset = useCallback(() => {
    setUploadedFile(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    uploadedFile,
    isSubmitting,
    error,
    upload,
    reset,
  }), [error, isSubmitting, reset, uploadedFile, upload]);
}
