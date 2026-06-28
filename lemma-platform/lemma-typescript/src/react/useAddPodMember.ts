import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import { PodRole, type PodMember } from "../types.js";
import { normalizeError, resolvePodId } from "./utils.js";

export interface AddPodMemberInput {
  organizationMemberId: string;
  role?: PodRole;
}

export interface UseAddPodMemberOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  defaultRole?: PodRole;
  onSuccess?: (member: PodMember) => void;
  onError?: (error: unknown) => void;
}

export interface UseAddPodMemberResult {
  addedMember: PodMember | null;
  isSubmitting: boolean;
  error: Error | null;
  add: (input: AddPodMemberInput) => Promise<PodMember | null>;
  reset: () => void;
}

export function useAddPodMember({
  client,
  podId,
  enabled = true,
  defaultRole = PodRole.POD_USER,
  onSuccess,
  onError,
}: UseAddPodMemberOptions): UseAddPodMemberResult {
  const [addedMember, setAddedMember] = useState<PodMember | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const add = useCallback(async (input: AddPodMemberInput): Promise<PodMember | null> => {
    const organizationMemberId = input.organizationMemberId.trim();

    if (!enabled || organizationMemberId.length === 0) {
      return null;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const resolvedPodId = resolvePodId(client, podId);
      const nextMember = await client.podMembers.add(resolvedPodId, {
        organization_member_id: organizationMemberId,
        roles: [input.role ?? defaultRole],
      });
      setAddedMember(nextMember);
      onSuccessRef.current?.(nextMember);
      return nextMember;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, "Failed to add pod member.");
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, defaultRole, enabled, podId]);

  const reset = useCallback(() => {
    setAddedMember(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    addedMember,
    isSubmitting,
    error,
    add,
    reset,
  }), [add, addedMember, error, isSubmitting, reset]);
}
