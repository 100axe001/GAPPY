import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { User } from "../types.js";
import { normalizeError } from "./utils.js";

export interface UseCurrentUserOptions {
  client: LemmaClient;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseCurrentUserResult {
  user: User | null;
  isLoading: boolean;
  error: Error | null;
  refresh: () => Promise<User | null>;
}

export function useCurrentUser({
  client,
  enabled = true,
  autoLoad = true,
}: UseCurrentUserOptions): UseCurrentUserResult {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const refresh = useCallback(async (signal?: AbortSignal): Promise<User | null> => {
    if (!enabled) {
      setUser(null);
      setError(null);
      setIsLoading(false);
      return null;
    }

    setIsLoading(true);
    setError(null);

    try {
      const nextUser = await client.users.current();
      if (signal?.aborted) return null;
      setUser(nextUser);
      return nextUser;
    } catch (refreshError) {
      if (signal?.aborted) return null;
      const normalized = normalizeError(refreshError, "Failed to load current user.");
      setError(normalized);
      setUser(null);
      return null;
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled]);

  useEffect(() => {
    if (!enabled) {
      setUser(null);
      setError(null);
      setIsLoading(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    let cancelled = false;
    (async () => {
      try {
        await refresh(controller.signal);
      } catch {
        if (!cancelled) {
          setError(normalizeError(new Error("Failed to load current user."), "Failed to load current user."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, enabled, refresh]);

  return useMemo(() => ({
    user,
    isLoading,
    error,
    refresh,
  }), [error, isLoading, refresh, user]);
}
