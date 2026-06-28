import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { OrganizationMember } from "../types.js";
import { normalizeError } from "./utils.js";

export interface UseOrganizationMembersOptions {
  client: LemmaClient;
  organizationId: string;
  enabled?: boolean;
  autoLoad?: boolean;
  limit?: number;
  pageToken?: string;
}

export interface UseOrganizationMembersResult {
  members: OrganizationMember[];
  total: number;
  nextPageToken: string | null;
  isLoading: boolean;
  isLoadingMore: boolean;
  error: Error | null;
  refresh: (overrides?: { limit?: number; pageToken?: string }) => Promise<OrganizationMember[]>;
  loadMore: (overrides?: { limit?: number }) => Promise<OrganizationMember[]>;
}

export function useOrganizationMembers({
  client,
  organizationId,
  enabled = true,
  autoLoad = true,
  limit = 100,
  pageToken,
}: UseOrganizationMembersOptions): UseOrganizationMembersResult {
  const [members, setMembers] = useState<OrganizationMember[]>([]);
  const [total, setTotal] = useState(0);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const trimmedOrganizationId = organizationId.trim();
  const isEnabled = enabled && trimmedOrganizationId.length > 0;

  const refresh = useCallback(async (overrides: { limit?: number; pageToken?: string } = {}, signal?: AbortSignal): Promise<OrganizationMember[]> => {
    if (!isEnabled) {
      setMembers([]);
      setTotal(0);
      setNextPageToken(null);
      setError(null);
      setIsLoading(false);
      return [];
    }

    setIsLoading(true);
    setError(null);

    try {
      const response = await client.organizations.members.list(trimmedOrganizationId, {
        limit: overrides.limit ?? limit,
        pageToken: overrides.pageToken ?? pageToken,
      });
      if (signal?.aborted) return [];
      const nextMembers = response.items ?? [];
      setMembers(nextMembers);
      setTotal((response as { total?: number }).total ?? nextMembers.length);
      setNextPageToken(response.next_page_token ?? null);
      return nextMembers;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load organization members.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, isEnabled, limit, pageToken, trimmedOrganizationId]);

  const loadMore = useCallback(async (overrides: { limit?: number } = {}): Promise<OrganizationMember[]> => {
    if (!isEnabled || !nextPageToken || isLoading || isLoadingMore) {
      return [];
    }

    setIsLoadingMore(true);
    setError(null);

    try {
      const response = await client.organizations.members.list(trimmedOrganizationId, {
        limit: overrides.limit ?? limit,
        pageToken: nextPageToken,
      });
      const moreMembers = response.items ?? [];
      setMembers((previous) => [...previous, ...moreMembers]);
      setTotal((response as { total?: number }).total ?? members.length + moreMembers.length);
      setNextPageToken(response.next_page_token ?? null);
      return moreMembers;
    } catch (loadError) {
      const normalized = normalizeError(loadError, "Failed to load more organization members.");
      setError(normalized);
      return [];
    } finally {
      setIsLoadingMore(false);
    }
  }, [client, isEnabled, isLoading, isLoadingMore, limit, members.length, nextPageToken, trimmedOrganizationId]);

  useEffect(() => {
    if (!isEnabled) {
      setMembers([]);
      setTotal(0);
      setNextPageToken(null);
      setError(null);
      setIsLoading(false);
      setIsLoadingMore(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    let cancelled = false;
    (async () => {
      try {
        await refresh({}, controller.signal);
      } catch {
        if (!cancelled) {
          setError(normalizeError(new Error("Failed to load organization members."), "Failed to load organization members."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, isEnabled, refresh]);

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
