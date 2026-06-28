import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseDeleteRecordOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  recordId?: string | null;
  enabled?: boolean;
  onSuccess?: () => void;
  onError?: (error: unknown) => void;
}

export interface UseDeleteRecordResult {
  isSubmitting: boolean;
  error: Error | null;
  lastMessage: string | null;
  remove: (overrides?: { recordId?: string | null }) => Promise<boolean>;
  reset: () => void;
}

export function useDeleteRecord({
  client,
  podId,
  tableName,
  recordId = null,
  enabled = true,
  onSuccess,
  onError,
}: UseDeleteRecordOptions): UseDeleteRecordResult {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [lastMessage, setLastMessage] = useState<string | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedTableName = tableName.trim();
  const trimmedRecordId = typeof recordId === "string" ? recordId.trim() : "";
  const isEnabled = enabled && trimmedTableName.length > 0;

  const remove = useCallback(async (
    overrides: { recordId?: string | null } = {},
  ): Promise<boolean> => {
    const nextRecordId = typeof overrides.recordId === "string"
      ? overrides.recordId.trim()
      : trimmedRecordId;

    if (!isEnabled || nextRecordId.length === 0) {
      return false;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      await scopedClient.records.delete(trimmedTableName, nextRecordId);
      setLastMessage("Record deleted.");
      onSuccessRef.current?.();
      return true;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, "Failed to delete record.");
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return false;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, isEnabled, podId, trimmedRecordId, trimmedTableName]);

  const reset = useCallback(() => {
    setError(null);
    setIsSubmitting(false);
    setLastMessage(null);
  }, []);

  return useMemo(() => ({
    isSubmitting,
    error,
    lastMessage,
    remove,
    reset,
  }), [error, isSubmitting, lastMessage, remove, reset]);
}
