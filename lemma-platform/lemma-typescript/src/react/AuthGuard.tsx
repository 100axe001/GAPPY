import { useCallback, useEffect, useState } from "react";
import type { ReactNode } from "react";
import type { LemmaClient } from "../client.js";
import { ApiError } from "../http.js";
import type { PodJoinRequestCreateResponse } from "../openapi_client/models/PodJoinRequestCreateResponse.js";
import { useAuth } from "./useAuth.js";

export interface AuthGuardProps {
  client: LemmaClient;
  children: ReactNode;
  /** Optional custom loading element. Defaults to a blank screen. */
  loadingFallback?: ReactNode;
  /** Optional custom unauthenticated element. Defaults to a centered sign-in page. */
  unauthenticatedFallback?: ReactNode;
  /** Optional custom element shown when user is authenticated but lacks pod membership. */
  accessRequestFallback?: ReactNode;
}

function DefaultSignInPage({ onSignIn }: { onSignIn: () => void }) {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        minHeight: "100vh",
        fontFamily: "system-ui, -apple-system, sans-serif",
        backgroundColor: "#f9fafb",
        gap: "16px",
      }}
    >
      <div
        style={{
          backgroundColor: "#fff",
          borderRadius: "12px",
          boxShadow: "0 1px 4px rgba(0,0,0,0.1)",
          padding: "40px 48px",
          textAlign: "center",
          maxWidth: "360px",
          width: "100%",
        }}
      >
        <div
          style={{
            width: "40px",
            height: "40px",
            borderRadius: "8px",
            backgroundColor: "#111827",
            margin: "0 auto 20px",
          }}
        />
        <h1 style={{ margin: "0 0 8px", fontSize: "20px", fontWeight: 600, color: "#111827" }}>
          Sign in to continue
        </h1>
        <p style={{ margin: "0 0 24px", fontSize: "14px", color: "#6b7280" }}>
          You need to be signed in to access this app.
        </p>
        <button
          onClick={onSignIn}
          style={{
            width: "100%",
            padding: "10px 16px",
            backgroundColor: "#111827",
            color: "#fff",
            border: "none",
            borderRadius: "8px",
            fontSize: "14px",
            fontWeight: 500,
            cursor: "pointer",
          }}
        >
          Sign In
        </button>
      </div>
    </div>
  );
}

function DefaultRequestAccessPage({
  isPending,
  isSubmitting,
  error,
  onRequestAccess,
}: {
  isPending: boolean;
  isSubmitting: boolean;
  error: string | null;
  onRequestAccess: () => void;
}) {
  const message = isPending
    ? "Access request sent. An admin can approve it from the pod settings."
    : "You are signed in, but you are not a member of this pod yet.";

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        minHeight: "100vh",
        fontFamily: "system-ui, -apple-system, sans-serif",
        backgroundColor: "#f9fafb",
        gap: "16px",
      }}
    >
      <div
        style={{
          backgroundColor: "#fff",
          borderRadius: "12px",
          boxShadow: "0 1px 4px rgba(0,0,0,0.1)",
          padding: "40px 48px",
          textAlign: "center",
          maxWidth: "420px",
          width: "100%",
        }}
      >
        <h1 style={{ margin: "0 0 8px", fontSize: "20px", fontWeight: 600, color: "#111827" }}>
          Request pod access
        </h1>
        <p style={{ margin: "0 0 24px", fontSize: "14px", color: "#6b7280" }}>{message}</p>
        <button
          onClick={onRequestAccess}
          disabled={isSubmitting || isPending}
          style={{
            width: "100%",
            padding: "10px 16px",
            backgroundColor: isSubmitting || isPending ? "#9ca3af" : "#111827",
            color: "#fff",
            border: "none",
            borderRadius: "8px",
            fontSize: "14px",
            fontWeight: 500,
            cursor: isSubmitting || isPending ? "not-allowed" : "pointer",
          }}
        >
          {isSubmitting ? "Submitting..." : isPending ? "Request Sent" : "Request Access"}
        </button>
        {error ? (
          <p style={{ margin: "12px 0 0", fontSize: "13px", color: "#b91c1c" }}>{error}</p>
        ) : null}
      </div>
    </div>
  );
}

type MembershipState = "idle" | "checking" | "member" | "missing";

/**
 * AuthGuard wraps your connector and handles auth state:
 * - Loading: shows loadingFallback (blank by default)
 * - Unauthenticated: shows sign-in page (or custom unauthenticatedFallback)
 * - Authenticated and member: renders children
 * - Authenticated but not pod member: shows request-access page
 *
 * Usage:
 *   <AuthGuard client={getClient()}>
 *     <App />
 *   </AuthGuard>
 */
export function AuthGuard({
  client,
  children,
  loadingFallback = null,
  unauthenticatedFallback,
  accessRequestFallback,
}: AuthGuardProps) {
  const { isLoading, isAuthenticated, redirectToAuth } = useAuth(client);
  const [membershipState, setMembershipState] = useState<MembershipState>("idle");
  const [membershipError, setMembershipError] = useState<string | null>(null);
  const [isSubmittingJoinRequest, setIsSubmittingJoinRequest] = useState(false);
  const [joinRequest, setJoinRequest] = useState<PodJoinRequestCreateResponse | null>(null);

  const checkMembership = useCallback(async () => {
    if (!isAuthenticated || !client.podId) {
      setMembershipState("member");
      return;
    }

    setMembershipState("checking");
    setMembershipError(null);

    try {
      const currentUser = await client.users.current();
      await client.podMembers.lookupByUserId(client.podId, currentUser.id);
      setMembershipState("member");
      setJoinRequest(null);
      return;
    } catch (error) {
      const apiError = error instanceof ApiError ? error : null;
      const isMissingMembership = apiError?.statusCode === 404 || apiError?.statusCode === 403;
      if (!isMissingMembership) {
        throw error;
      }
    }

    try {
      const existingRequest = await client.podJoinRequests.me(client.podId);
      setJoinRequest(existingRequest);
    } catch {
      // non-fatal: request could still be created by the user manually
    }

    setMembershipState("missing");
  }, [client, isAuthenticated]);

  useEffect(() => {
    let cancelled = false;

    const run = async () => {
      if (!isAuthenticated) {
        setMembershipState("idle");
        setJoinRequest(null);
        setMembershipError(null);
        return;
      }

      try {
        await checkMembership();
      } catch (error) {
        if (cancelled) return;
        const message =
          error instanceof Error
            ? error.message
            : "Failed to verify pod membership. Please try again.";
        setMembershipError(message);
        setMembershipState("missing");
      }
    };

    void run();
    return () => {
      cancelled = true;
    };
  }, [checkMembership, isAuthenticated]);

  const handleRequestAccess = useCallback(async () => {
    if (!client.podId || isSubmittingJoinRequest || joinRequest?.status === "PENDING") {
      return;
    }

    setIsSubmittingJoinRequest(true);
    setMembershipError(null);
    try {
      const request = await client.podJoinRequests.create(client.podId);
      setJoinRequest(request);
    } catch (error) {
      const message =
        error instanceof Error
          ? error.message
          : "Failed to create access request. Please try again.";
      setMembershipError(message);
    } finally {
      setIsSubmittingJoinRequest(false);
    }
  }, [client, isSubmittingJoinRequest, joinRequest]);

  if (isLoading || (isAuthenticated && membershipState === "checking")) {
    return <>{loadingFallback}</>;
  }

  if (!isAuthenticated) {
    if (unauthenticatedFallback !== undefined) {
      return <>{unauthenticatedFallback}</>;
    }
    return <DefaultSignInPage onSignIn={redirectToAuth} />;
  }

  if (membershipState === "missing") {
    if (accessRequestFallback !== undefined) {
      return <>{accessRequestFallback}</>;
    }

    return (
      <DefaultRequestAccessPage
        isPending={joinRequest?.status === "PENDING"}
        isSubmitting={isSubmittingJoinRequest}
        error={membershipError}
        onRequestAccess={handleRequestAccess}
      />
    );
  }

  return <>{children}</>;
}
