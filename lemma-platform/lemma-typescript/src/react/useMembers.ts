import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { PodMember } from "../types.js";
import { normalizeError, resolvePodId } from "./utils.js";

export interface UseMembersOptions {
  client: LemmaClient;
  podId?: string;
  enabled?: boolean;
  autoLoad?: boolean;
  limit?: number;
  pageToken?: string;
}

export interface UseMembersResult {
  members: PodMember[];
  total: number;
  nextPageToken: string | null;
  isLoading: boolean;
  isLoadingMore: boolean;
  error: Error | null;
  refresh: (overrides?: { limit?: number; pageToken?: string }) => Promise<PodMember[]>;
  loadMore: (overrides?: { limit?: number }) => Promise<PodMember[]>;
}

export function useMembers({
  client,
  podId,
  enabled = true,
  autoLoad = true,
  limit = 100,
  pageToken,
}: UseMembersOptions): UseMembersResult {
  const [members, setMembers] = useState<PodMember[]>([]);
  const [total, setTotal] = useState(0);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const refresh = useCallback(async (overrides: { limit?: number; pageToken?: string } = {}, signal?: AbortSignal): Promise<PodMember[]> => {
    if (!enabled) return [];

    setIsLoading(true);
    setError(null);

    try {
      const resolvedPodId = resolvePodId(client, podId);
      const response = await client.podMembers.list(resolvedPodId, {
        limit: overrides.limit ?? limit,
        pageToken: overrides.pageToken ?? pageToken,
      });

      if (signal?.aborted) return [];
      const nextMembers = response.items ?? [];
      setMembers(nextMembers);
      setTotal(response.total ?? nextMembers.length);
      setNextPageToken(response.next_page_token ?? null);
      return nextMembers;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load pod members.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled, limit, pageToken, podId]);

  const loadMore = useCallback(async (overrides: { limit?: number } = {}): Promise<PodMember[]> => {
    if (!enabled || !nextPageToken || isLoading || isLoadingMore) {
      return [];
    }

    setIsLoadingMore(true);
    setError(null);

    try {
      const resolvedPodId = resolvePodId(client, podId);
      const response = await client.podMembers.list(resolvedPodId, {
        limit: overrides.limit ?? limit,
        pageToken: nextPageToken,
      });
      const moreMembers = response.items ?? [];
      setMembers((previous) => [...previous, ...moreMembers]);
      setTotal(response.total ?? members.length + moreMembers.length);
      setNextPageToken(response.next_page_token ?? null);
      return moreMembers;
    } catch (loadError) {
      const normalized = normalizeError(loadError, "Failed to load more pod members.");
      setError(normalized);
      return [];
    } finally {
      setIsLoadingMore(false);
    }
  }, [client, enabled, isLoading, isLoadingMore, limit, members.length, nextPageToken, podId]);

  useEffect(() => {
    if (!enabled || !autoLoad) return;
    const controller = new AbortController();
    let cancelled = false;
    (async () => {
      try {
        await refresh({}, controller.signal);
      } catch {
        if (!cancelled) {
          setError(normalizeError(new Error("Failed to load pod members."), "Failed to load pod members."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, enabled, refresh]);

  return useMemo(() => ({
    members,
    total,
    nextPageToken,
    isLoading,
    isLoadingMore,
    error,
    refresh,
    loadMore,
  }), [error, isLoading, isLoadingMore, loadMore, members, nextPageToken, refresh, total]);
}
