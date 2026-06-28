import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import { normalizeError, resolvePodId } from "./utils.js";

export interface UseRemovePodMemberOptions {
  client: LemmaClient;
  podId?: string;
  memberId?: string | null;
  enabled?: boolean;
  onSuccess?: (memberId: string) => void;
  onError?: (error: unknown) => void;
}

export interface UseRemovePodMemberResult {
  removedMemberId: string | null;
  isSubmitting: boolean;
  error: Error | null;
  remove: (overrides?: { memberId?: string | null }) => Promise<boolean>;
  reset: () => void;
}

export function useRemovePodMember({
  client,
  podId,
  memberId = null,
  enabled = true,
  onSuccess,
  onError,
}: UseRemovePodMemberOptions): UseRemovePodMemberResult {
  const [removedMemberId, setRemovedMemberId] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedMemberId = typeof memberId === "string" ? memberId.trim() : "";

  const remove = useCallback(async (
    overrides: { memberId?: string | null } = {},
  ): Promise<boolean> => {
    const nextMemberId = typeof overrides.memberId === "string"
      ? overrides.memberId.trim()
      : trimmedMemberId;

    if (!enabled || nextMemberId.length === 0) {
      return false;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const resolvedPodId = resolvePodId(client, podId);
      await client.podMembers.remove(resolvedPodId, nextMemberId);
      setRemovedMemberId(nextMemberId);
      onSuccessRef.current?.(nextMemberId);
      return true;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, "Failed to remove pod member.");
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return false;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, enabled, podId, trimmedMemberId]);

  const reset = useCallback(() => {
    setRemovedMemberId(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    removedMemberId,
    isSubmitting,
    error,
    remove,
    reset,
  }), [error, isSubmitting, remove, removedMemberId, reset]);
}
