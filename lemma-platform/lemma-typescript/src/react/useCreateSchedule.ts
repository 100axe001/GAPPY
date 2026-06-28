import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { CreateScheduleRequest, Schedule } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseCreateScheduleOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  onSuccess?: (schedule: Schedule) => void;
  onError?: (error: unknown) => void;
}

export interface UseCreateScheduleResult {
  schedule: Schedule | null;
  isSubmitting: boolean;
  error: Error | null;
  create: (payload: CreateScheduleRequest) => Promise<Schedule | null>;
  reset: () => void;
}

export function useCreateSchedule({
  client,
  podId,
  enabled = true,
  onSuccess,
  onError,
}: UseCreateScheduleOptions): UseCreateScheduleResult {
  const [schedule, setSchedule] = useState<Schedule | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const create = useCallback(async (payload: CreateScheduleRequest): Promise<Schedule | null> => {
    if (!enabled) return null;

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextSchedule = await scopedClient.schedules.create(payload);
      setSchedule(nextSchedule);
      onSuccessRef.current?.(nextSchedule);
      return nextSchedule;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, "Failed to create schedule.");
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, enabled, podId]);

  const reset = useCallback(() => {
    setSchedule(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    schedule,
    isSubmitting,
    error,
    create,
    reset,
  }), [create, error, isSubmitting, reset, schedule]);
}
