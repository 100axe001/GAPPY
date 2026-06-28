'use client';

import { use } from 'react';
import { useSearchParams } from 'next/navigation';
import { PanelsTopLeft } from 'lucide-react';
import { useAppPage } from '@/lib/hooks/use-app';
import { resourceAllows } from '@/lib/authz/resource-actions';
import { usePodAccess } from '@/lib/hooks/use-pod-access';
import { RecoveryState } from '@/components/shared/empty-state';
import { AppFrame } from '@/components/app/app-launch';
import { ProtectedRoute } from '@/components/auth/protected-route';
import { StepLoader } from '@/components/brand/loader';

export default function AppViewPage({ params }: { params: Promise<{ id: string }> }) {
    const { id: podId } = use(params);
    const searchParams = useSearchParams();
    const requestedPageSlug = searchParams.get('page');
    const podAccess = usePodAccess(podId);

    const { data: page, isLoading } = useAppPage(podId, requestedPageSlug, null, { mode: 'view' });

    if (!requestedPageSlug) {
        return (
            <ProtectedRoute>
                <div className="h-full flex items-center justify-center">
                    <RecoveryState
                        icon={<PanelsTopLeft className="h-5 w-5" />}
                        title="Missing app page"
                        description="Open an app from the Apps list so Lemma knows which workspace to show."
                    />
                </div>
            </ProtectedRoute>
        );
    }

    if (isLoading) {
        return (
            <div className="h-full flex items-center justify-center">
                <StepLoader size="sm" />
            </div>
        );
    }

    if (!page) {
        return (
            <div className="h-full flex items-center justify-center">
                <RecoveryState
                    icon={<PanelsTopLeft className="h-5 w-5" />}
                    title="App unavailable"
                    description="The selected app could not be loaded. Try opening it again from the Apps list."
                />
            </div>
        );
    }

    return (
        <ProtectedRoute>
            <div className="h-full w-full overflow-hidden">
                {page.url ? (
                    <AppFrame
                        podId={podId}
                        appId={page.id}
                        appName={page.title}
                        title={page.title}
                        url={page.url}
                        visibility={page.visibility}
                        canShare={resourceAllows(page, 'app.update', podAccess.can('app.update'))}
                    />
                ) : (
                    <div className="state-surface-warning h-full p-4">
                        <p className="mb-2 text-sm font-semibold text-[var(--state-warning)]">App link not available</p>
                        <p className="text-xs text-[var(--text-secondary)]">
                            This app app did not return a web app URL from the server.
                        </p>
                    </div>
                )}
            </div>
        </ProtectedRoute>
    );
}
