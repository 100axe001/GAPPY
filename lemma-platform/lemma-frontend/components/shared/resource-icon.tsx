'use client';

import { ReactNode, useMemo, useState } from 'react';
import { cn } from '@/lib/utils';

interface ResourceIconProps {
    iconUrl?: string | null;
    alt: string;
    label?: string;
    fallback?: ReactNode;
    className?: string;
    imageClassName?: string;
}

function getInitials(label?: string): string {
    const trimmed = label?.trim();
    if (!trimmed) return '?';
    const words = trimmed.split(/\s+/).slice(0, 2);
    return words.map((word) => word.charAt(0).toUpperCase()).join('');
}

export function ResourceIcon({ iconUrl, alt, label, fallback, className, imageClassName }: ResourceIconProps) {
    const [imageFailed, setImageFailed] = useState(false);
    const initials = useMemo(() => getInitials(label), [label]);
    const shouldShowImage = Boolean(iconUrl) && !imageFailed;

    return (
        <div
            className={cn(
                'relative flex items-center justify-center overflow-hidden rounded-lg border border-transparent text-[var(--text-secondary)]',
                shouldShowImage ? 'bg-transparent' : 'bg-[color:color-mix(in_srgb,var(--surface-2)_52%,transparent)]',
                className
            )}
        >
            {shouldShowImage ? (
                // eslint-disable-next-line @next/next/no-img-element
                <img
                    src={iconUrl || ''}
                    alt={alt}
                    className={cn('h-full w-full object-cover', imageClassName)}
                    onError={() => setImageFailed(true)}
                />
            ) : fallback ? (
                fallback
            ) : (
                <span className="text-sm font-normal">{initials}</span>
            )}
        </div>
    );
}
