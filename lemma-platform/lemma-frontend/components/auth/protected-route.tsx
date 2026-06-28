"use client";

import { useMemo, type ReactNode } from "react";
import { AuthGuard } from "lemma-sdk/react";
import { PageLoader } from "@/components/brand/loader";
import { getLemmaClient } from "@/lib/sdk/lemma-client";

export function ProtectedRoute({ children }: { children: ReactNode }) {
    const client = useMemo(() => getLemmaClient(), []);

    return (
        <AuthGuard client={client} loadingFallback={<PageLoader />}>
            {children}
        </AuthGuard>
    );
}
