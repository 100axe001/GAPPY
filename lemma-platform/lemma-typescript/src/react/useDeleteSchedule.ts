import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseDeleteScheduleOptions {
  client: LemmaClient;
  podId?: string;
  scheduleId?: string | null;
  enabled?: boolean;
  onSuccess?: (scheduleId: string) => void;
  onError?: (error: unknown) => void;
}

export interface UseDeleteScheduleResult {
  deletedScheduleId: string | null;
  isSubmitting: boolean;
  error: Error | null;
  remove: (overrides?: { scheduleId?: string | null }) => Promise<boolean>;
  reset: () => void;
}

export function useDeleteSchedule({
  client,
  podId,
  scheduleId = null,
  enabled = true,
  onSuccess,
  onError,
}: UseDeleteScheduleOptions): UseDeleteScheduleResult {
  const [deletedScheduleId, setDeletedScheduleId] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedScheduleId = typeof scheduleId === "string" ? scheduleId.trim() : "";

  const remove = useCallback(async (
    overrides: { scheduleId?: string | null } = {},
  ): Promise<boolean> => {
    const nextScheduleId = typeof overrides.scheduleId === "string"
      ? overrides.scheduleId.trim()
      : trimmedScheduleId;

    if (!enabled || nextScheduleId.length === 0) return false;

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      await scopedClient.schedules.delete(nextScheduleId);
      setDeletedScheduleId(nextScheduleId);
      onSuccessRef.current?.(nextScheduleId);
      return true;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, "Failed to delete schedule.");
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return false;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, enabled, podId, trimmedScheduleId]);

  const reset = useCallback(() => {
    setDeletedScheduleId(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    deletedScheduleId,
    isSubmitting,
    error,
    remove,
    reset,
  }), [deletedScheduleId, error, isSubmitting, remove, reset]);
}
