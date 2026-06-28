import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { PodMember, PodRole } from "../types.js";
import { normalizeError, resolvePodId } from "./utils.js";

export interface UseUpdatePodMemberRoleOptions {
  client: LemmaClient;
  podId?: string;
  memberId?: string | null;
  enabled?: boolean;
  onSuccess?: (member: PodMember) => void;
  onError?: (error: unknown) => void;
}

export interface UseUpdatePodMemberRoleResult {
  updatedMember: PodMember | null;
  isSubmitting: boolean;
  error: Error | null;
  updateRole: (
    role: PodRole,
    overrides?: { memberId?: string | null },
  ) => Promise<PodMember | null>;
  reset: () => void;
}

export function useUpdatePodMemberRole({
  client,
  podId,
  memberId = null,
  enabled = true,
  onSuccess,
  onError,
}: UseUpdatePodMemberRoleOptions): UseUpdatePodMemberRoleResult {
  const [updatedMember, setUpdatedMember] = useState<PodMember | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedMemberId = typeof memberId === "string" ? memberId.trim() : "";

  const updateRole = useCallback(async (
    role: PodRole,
    overrides: { memberId?: string | null } = {},
  ): Promise<PodMember | null> => {
    const nextMemberId = typeof overrides.memberId === "string"
      ? overrides.memberId.trim()
      : trimmedMemberId;

    if (!enabled || nextMemberId.length === 0) {
      return null;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const resolvedPodId = resolvePodId(client, podId);
      const nextMember = await client.podMembers.updateRole(resolvedPodId, nextMemberId, role);
      setUpdatedMember(nextMember);
      onSuccessRef.current?.(nextMember);
      return nextMember;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, "Failed to update pod member role.");
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, enabled, podId, trimmedMemberId]);

  const reset = useCallback(() => {
    setUpdatedMember(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    updatedMember,
    isSubmitting,
    error,
    updateRole,
    reset,
  }), [error, isSubmitting, reset, updateRole, updatedMember]);
}
