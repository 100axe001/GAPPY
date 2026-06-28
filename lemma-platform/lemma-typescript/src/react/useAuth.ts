import { useState, useEffect } from "react"; // peer dependency
import type { LemmaClient } from "../client.js";
import type { AuthState, BuildAuthUrlOptions } from "../auth.js";

type RedirectToAuthOptions = Omit<BuildAuthUrlOptions, "redirectUri"> & { redirectUri?: string };

export interface UseAuthResult {
  status: AuthState["status"];
  user: AuthState["user"];
  isLoading: boolean;
  isAuthenticated: boolean;
  redirectToAuth: (options?: RedirectToAuthOptions) => void;
}

/**
 * React hook for subscribing to Lemma auth state.
 *
 * Usage:
 *   const { isAuthenticated, isLoading, redirectToAuth } = useAuth(client);
 */
export function useAuth(client: LemmaClient): UseAuthResult {
  const [state, setState] = useState<AuthState>(client.auth.getState());

  useEffect(() => {
    // Subscribe to future state changes
    const unsubscribe = client.auth.subscribe((next) => setState(next));

    // If still in loading state, trigger the auth check
    if (state.status === "loading") {
      client.auth.checkAuth().catch(() => {
        // checkAuth already handles errors internally
      });
    }

    return unsubscribe;
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [client]);

  return {
    status: state.status,
    user: state.user,
    isLoading: state.status === "loading",
    isAuthenticated: state.status === "authenticated",
    redirectToAuth: (options?: RedirectToAuthOptions) => client.auth.redirectToAuth(options),
  };
}
