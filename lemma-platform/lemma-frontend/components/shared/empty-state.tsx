import type { ReactNode } from 'react';

import { getConcept, type ConceptId } from '@/lib/education/concepts';
import { cn } from '@/lib/utils';

interface EmptyStateProps {
    title: string;
    description?: string;
    /** Teaching fallback: when no description is passed, explain the concept instead. */
    concept?: ConceptId;
    icon?: ReactNode;
    action?: ReactNode;
    variant?: 'compact' | 'panel' | 'full';
    className?: string;
}

export function EmptyState({ title, description, concept, icon, action, variant = 'panel', className }: EmptyStateProps) {
    const isCompact = variant === 'compact';
    const isPanel = variant === 'panel';
    const resolvedDescription = description ?? (concept ? getConcept(concept).oneLiner : '');

    return (
        <div
            className={cn(
                'flex flex-col items-center justify-center text-center',
                isCompact
                    ? 'rounded-lg bg-[var(--bg-subtle)] px-4 py-5'
                    : isPanel
                        ? 'rounded-lg border border-dashed border-[color:color-mix(in_srgb,var(--border-subtle)_60%,transparent)] bg-[var(--surface-1)] px-5 py-10'
                        : 'surface-panel-dashed px-6 py-24',
                className
            )}
        >
            {icon && (
                <div
                    className={cn(
                        'flex items-center justify-center rounded-full bg-[var(--surface-1)] border border-[var(--border-subtle)] text-[var(--text-tertiary)]',
                        isCompact ? 'mb-3 h-8 w-8' : isPanel ? 'mb-3 h-10 w-10' : 'mb-6 h-20 w-20 rounded-2xl'
                    )}
                >
                    {icon}
                </div>
            )}
            <h3
                className={cn(
                    'font-semibold tracking-normal text-[var(--text-primary)]',
                    isCompact ? 'mb-1 text-sm' : isPanel ? 'mb-1 text-sm' : 'font-display mb-3 text-2xl tracking-tight'
                )}
            >
                {title}
            </h3>
            <p
                className={cn(
                    'max-w-sm text-[var(--text-secondary)]',
                    isCompact ? 'text-xs leading-5' : isPanel ? 'text-xs leading-5' : 'mb-8 text-base leading-relaxed'
                )}
            >
                {resolvedDescription}
            </p>
            {action && (
                <div className={cn(isCompact ? 'mt-2' : isPanel ? 'mt-3' : 'mt-2')}>
                    {action}
                </div>
            )}
        </div>
    );
}

export function InlineEmptyState({
    icon,
    title,
    description,
    concept,
    action,
    className,
}: {
    icon?: ReactNode;
    title: string;
    description?: string;
    concept?: ConceptId;
    action?: ReactNode;
    className?: string;
}) {
    const resolvedDescription = description ?? (concept ? getConcept(concept).oneLiner : undefined);
    return (
        <div className={cn('flex items-start gap-3 rounded-md px-2 py-3 text-left', className)}>
            {icon ? (
                <span className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full border border-[var(--border-subtle)] text-[var(--text-tertiary)]">
                    {icon}
                </span>
            ) : null}
            <div className="min-w-0 flex-1">
                <p className="text-sm font-medium text-[var(--text-primary)]">{title}</p>
                {resolvedDescription ? <p className="mt-0.5 text-xs leading-5 text-[var(--text-secondary)]">{resolvedDescription}</p> : null}
            </div>
            {action ? <div className="shrink-0">{action}</div> : null}
        </div>
    );
}

export function QuietEmptyState({
    icon,
    children,
    className,
}: {
    icon?: ReactNode;
    children: ReactNode;
    className?: string;
}) {
    return (
        <div className={cn('flex items-center gap-2 px-1 py-3 text-sm text-[var(--text-tertiary)]', className)}>
            {icon}
            <span>{children}</span>
        </div>
    );
}

export function SidebarEmptyState({ children, className }: { children: ReactNode; className?: string }) {
    return (
        <div className={cn('lemma-sidebar-empty', className)}>
            {children}
        </div>
    );
}

export function RecoveryState({
    title,
    description,
    icon,
    action,
    className,
}: {
    title: string;
    description: string;
    icon?: ReactNode;
    action?: ReactNode;
    className?: string;
}) {
    return (
        <EmptyState
            variant="panel"
            icon={icon}
            title={title}
            description={description}
            action={action}
            className={className}
        />
    );
}
