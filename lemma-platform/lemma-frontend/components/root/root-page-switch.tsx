'use client';

import { useEffect, useSyncExternalStore } from 'react';
import { useRouter } from 'next/navigation';
import { PageLoader } from '@/components/brand/loader';
import DashboardHomePage from '@/components/home/dashboard-home-page';
import LandingPage from '@/components/landing/landing-page';
import { AccountOnboarding } from '@/components/onboarding/account-onboarding';
import { useLemmaAuth } from '@/lib/hooks/use-lemma-auth';
import { useAccessiblePods } from '@/lib/hooks/use-pods';
import {
    readLastOpenedPodId,
    subscribeToLastOpenedPodId,
} from '@/lib/pods/last-opened-pod';

type RootPageMode = 'redirect' | 'home';

export function RootPageSwitch({ mode = 'redirect' }: { mode?: RootPageMode }) {
    const { isAuthenticated, isLoading } = useLemmaAuth();

    if (isLoading) {
        return <PageLoader />;
    }

    return isAuthenticated ? (
        <AccountOnboarding preflightFallback={<PageLoader />}>
            {mode === 'home' ? <DashboardHomePage /> : <AuthenticatedRootRedirect />}
        </AccountOnboarding>
    ) : (
        <LandingPage />
    );
}

function AuthenticatedRootRedirect() {
    const router = useRouter();
    const storedPodId = useSyncExternalStore(
        subscribeToLastOpenedPodId,
        readLastOpenedPodId,
        () => null,
    );
    const shouldFetchPods = !storedPodId;
    const { data: podsData, isLoading } = useAccessiblePods({ enabled: shouldFetchPods });

    useEffect(() => {
        if (storedPodId) {
            router.replace(`/pod/${storedPodId}?fromRoot=1`);
        }
    }, [router, storedPodId]);

    useEffect(() => {
        if (!shouldFetchPods || isLoading) return;

        const firstPod = podsData?.items?.[0];
        if (firstPod) {
            router.replace(`/pod/${firstPod.id}`);
        }
    }, [isLoading, podsData?.items, router, shouldFetchPods]);

    return <PageLoader />;
}
