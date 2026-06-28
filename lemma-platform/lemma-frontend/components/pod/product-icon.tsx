'use client';

import {
    Chat,
    ChatCircle,
    Clock,
    Code,
    Database,
    File,
    FileText,
    FolderOpen,
    Gear,
    GitMerge,
    Plugs,
    Rss,
    ShieldCheck,
    Sparkle,
    SquaresFour,
    Table,
} from '@phosphor-icons/react';

export type ProductIconTone =
    | 'pods'
    | 'connectors'
    | 'apps'
    | 'agents'
    | 'workflows'
    | 'schedules'
    | 'data'
    | 'tables'
    | 'docs'
    | 'files'
    | 'folders'
    | 'functions'
    | 'surfaces'
    | 'channels'
    | 'settings'
    | 'auth-rbac'
    | 'conversation';

const iconByTone: Record<ProductIconTone, typeof FolderOpen> = {
    pods: FolderOpen,
    connectors: Plugs,
    apps: SquaresFour,
    agents: Sparkle,
    workflows: GitMerge,
    schedules: Clock,
    data: Database,
    tables: Table,
    docs: FileText,
    files: File,
    folders: FolderOpen,
    functions: Code,
    surfaces: ChatCircle,
    channels: Rss,
    settings: Gear,
    'auth-rbac': ShieldCheck,
    conversation: Chat,
};

export function ProductIcon({
    tone,
    size = 'md',
}: {
    tone: ProductIconTone;
    size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
}) {
    const Icon = iconByTone[tone] || FolderOpen;

    return (
        <span className="lemma-product-icon" data-size={size} data-tone={tone}>
            <Icon weight="regular" className="h-full w-full" />
        </span>
    );
}
