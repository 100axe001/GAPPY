'use client';

import type { ReactNode } from 'react';

import { PodHeaderMetrics, PodPageHeader } from '@/components/pod/pod-page-header';
import { PodSettingsNav } from '@/components/pod/pod-settings-nav';
import { ResourcePanel, ResourcePanelHeader } from '@/components/pod/resource-layout';
import { cn } from '@/lib/utils';

interface PodSettingsStat {
    label: string;
    value: string;
    detail?: string;
}

interface PodSettingsShellProps {
    podId: string;
    title: string;
    description: string;
    action?: ReactNode;
    stats?: PodSettingsStat[];
    children: ReactNode;
}

export function PodSettingsShell({
    podId,
    title,
    description,
    action,
    stats = [],
    children,
}: PodSettingsShellProps) {
    return (
        <div className="context-shell min-h-full bg-transparent">
            <section>
                <PodPageHeader
                    podId={podId}
                    showBack={false}
                    title={title}
                    description={description}
                    productIconTone="settings"
                    meta={stats.length > 0 ? <PodHeaderMetrics items={stats.map((stat) => ({ label: stat.label, value: stat.value }))} /> : undefined}
                    actions={action}
                    switcher={<PodSettingsNav podId={podId} />}
                />

            </section>

            {children}
        </div>
    );
}

interface PodSettingsPanelProps {
    title: string;
    description?: string;
    action?: ReactNode;
    children: ReactNode;
    className?: string;
}

export function PodSettingsPanel({
    title,
    description,
    action,
    children,
    className,
}: PodSettingsPanelProps) {
    return (
        <ResourcePanel className={cn('overflow-hidden', className)}>
            <ResourcePanelHeader title={title} description={description} action={action} />
            <div className="px-4 py-4">{children}</div>
        </ResourcePanel>
    );
}
