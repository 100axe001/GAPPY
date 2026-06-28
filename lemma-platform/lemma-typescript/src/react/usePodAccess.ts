import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import { ApiError } from "../http.js";
import type { PodJoinRequest, PodMember, User } from "../types.js";
import { normalizeError, resolvePodId } from "./utils.js";

export type PodAccessStatus = "idle" | "checking" | "member" | "missing" | "pending" | "error";

export interface UsePodAccessOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UsePodAccessResult {
  status: PodAccessStatus;
  hasAccess: boolean;
  user: User | null;
  member: PodMember | null;
  joinRequest: PodJoinRequest | null;
  isLoading: boolean;
  isRequestingAccess: boolean;
  error: Error | null;
  refresh: () => Promise<PodAccessStatus>;
  requestAccess: () => Promise<PodJoinRequest>;
}

function isMissingAccessError(error: unknown): boolean {
  return error instanceof ApiError && (error.statusCode === 403 || error.statusCode === 404);
}

export function usePodAccess({
  client,
  podId,
  enabled = true,
  autoLoad = true,
}: UsePodAccessOptions): UsePodAccessResult {
  const [status, setStatus] = useState<PodAccessStatus>("idle");
  const [user, setUser] = useState<User | null>(null);
  const [member, setMember] = useState<PodMember | null>(null);
  const [joinRequest, setJoinRequest] = useState<PodJoinRequest | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isRequestingAccess, setIsRequestingAccess] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const refresh = useCallback(async (): Promise<PodAccessStatus> => {
    if (!enabled) {
      setStatus("idle");
      setUser(null);
      setMember(null);
      setJoinRequest(null);
      setError(null);
      setIsLoading(false);
      return "idle";
    }

    setStatus("checking");
    setIsLoading(true);
    setError(null);

    try {
      const resolvedPodId = resolvePodId(client, podId);
      const currentUser = await client.users.current();
      setUser(currentUser);

      try {
        const nextMember = await client.podMembers.lookupByUserId(resolvedPodId, currentUser.id);
        setMember(nextMember);
        setJoinRequest(null);
        setStatus("member");
        return "member";
      } catch (membershipError) {
        if (!isMissingAccessError(membershipError)) {
          throw membershipError;
        }
      }

      setMember(null);

      try {
        const request = await client.podJoinRequests.me(resolvedPodId);
        setJoinRequest(request);
        const nextStatus = request?.status === "PENDING" ? "pending" : "missing";
        setStatus(nextStatus);
        return nextStatus;
      } catch (joinRequestError) {
        if (!isMissingAccessError(joinRequestError)) {
          throw joinRequestError;
        }
      }

      setJoinRequest(null);
      setStatus("missing");
      return "missing";
    } catch (refreshError) {
      const normalized = normalizeError(refreshError, "Failed to check pod access.");
      setError(normalized);
      setStatus("error");
      return "error";
    } finally {
      setIsLoading(false);
    }
  }, [client, enabled, podId]);

  const requestAccess = useCallback(async (): Promise<PodJoinRequest> => {
    setIsRequestingAccess(true);
    setError(null);

    try {
      const resolvedPodId = resolvePodId(client, podId);
      const request = await client.podJoinRequests.create(resolvedPodId);
      setJoinRequest(request);
      setMember(null);
      setStatus(request.status === "PENDING" ? "pending" : "missing");
      return request;
    } catch (requestError) {
      const normalized = normalizeError(requestError, "Failed to request pod access.");
      setError(normalized);
      setStatus("error");
      throw normalized;
    } finally {
      setIsRequestingAccess(false);
    }
  }, [client, podId]);

  useEffect(() => {
    if (!enabled) {
      setStatus("idle");
      setUser(null);
      setMember(null);
      setJoinRequest(null);
      setError(null);
      setIsLoading(false);
      return;
    }

    if (!autoLoad) return;
    void refresh();
  }, [autoLoad, enabled, refresh]);

  return useMemo(() => ({
    status,
    hasAccess: status === "member",
    user,
    member,
    joinRequest,
    isLoading,
    isRequestingAccess,
    error,
    refresh,
    requestAccess,
  }), [
    error,
    isLoading,
    isRequestingAccess,
    joinRequest,
    member,
    refresh,
    requestAccess,
    status,
    user,
  ]);
}
