import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { Schedule, UpdateScheduleRequest } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseUpdateScheduleOptions {
  client: LemmaClient;
  podId?: string;
  scheduleId?: string | null;
  enabled?: boolean;
  onSuccess?: (schedule: Schedule) => void;
  onError?: (error: unknown) => void;
}

export interface UseUpdateScheduleResult {
  schedule: Schedule | null;
  isSubmitting: boolean;
  error: Error | null;
  update: (
    payload: UpdateScheduleRequest,
    overrides?: { scheduleId?: string | null },
  ) => Promise<Schedule | null>;
  reset: () => void;
}

export function useUpdateSchedule({
  client,
  podId,
  scheduleId = null,
  enabled = true,
  onSuccess,
  onError,
}: UseUpdateScheduleOptions): UseUpdateScheduleResult {
  const [schedule, setSchedule] = useState<Schedule | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedScheduleId = typeof scheduleId === "string" ? scheduleId.trim() : "";

  const update = useCallback(async (
    payload: UpdateScheduleRequest,
    overrides: { scheduleId?: string | null } = {},
  ): Promise<Schedule | null> => {
    const nextScheduleId = typeof overrides.scheduleId === "string"
      ? overrides.scheduleId.trim()
      : trimmedScheduleId;

    if (!enabled || nextScheduleId.length === 0) return null;

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextSchedule = await scopedClient.schedules.update(nextScheduleId, payload);
      setSchedule(nextSchedule);
      onSuccessRef.current?.(nextSchedule);
      return nextSchedule;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, "Failed to update schedule.");
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, enabled, podId, trimmedScheduleId]);

  const reset = useCallback(() => {
    setSchedule(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    schedule,
    isSubmitting,
    error,
    update,
    reset,
  }), [error, isSubmitting, reset, schedule, update]);
}
