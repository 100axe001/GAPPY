'use client';

import { useMemo } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { getLemmaClient } from '../sdk/lemma-client';
import type { AppConfig, AppPage, AppPageRef } from '../types/app';
import { createUniqueAppPageSlug, normalizeAppPageSlug } from '../utils/app-page-slugs';

export interface AppListItem {
    id: string;
    name: string;
    url: string;
    description?: string | null;
    public_slug?: string;
    status?: string;
    visibility?: string | null;
    allowed_actions?: string[] | null;
}

interface AppPageQueryOptions {
    mode?: 'editor' | 'view';
}

function toOptionalString(value: unknown): string | undefined {
    return typeof value === 'string' && value.trim().length > 0 ? value.trim() : undefined;
}

function normalizeAppUrl(value: string | undefined): string | undefined {
    if (!value) return undefined;
    if (/^https?:\/\//i.test(value)) return value;
    if (value.startsWith('//')) return `https:${value}`;
    return `https://${value}`;
}

function normalizeAllowedActions(value: unknown): string[] | null {
    if (!Array.isArray(value)) return null;
    return value.filter((action): action is string => typeof action === 'string' && action.trim().length > 0);
}

export async function listAppPageRefs(podId: string): Promise<AppPageRef[]> {
    const response = await getLemmaClient(podId).apps.list({ limit: 1000 }) as { items?: unknown[] };
    const items = Array.isArray(response?.items) ? response.items : [];
    const existingSlugs: string[] = [];

    return items
        .map((item, index) => {
            const parsed = (item || {}) as Record<string, unknown>;
            const pageName = toOptionalString(parsed.name);
            if (!pageName) return null;
            const slug = createUniqueAppPageSlug({
                title: pageName,
                preferredSlug: pageName,
                existingSlugs,
            });
            existingSlugs.push(slug);
            return {
                id: toOptionalString(parsed.id),
                slug,
                title: pageName,
                appName: pageName,
                url: normalizeAppUrl(toOptionalString(parsed.url)),
                order: index,
                path: `pages/${slug}.json`,
                visibility: typeof parsed.visibility === 'string' ? parsed.visibility : null,
                allowed_actions: normalizeAllowedActions(parsed.allowed_actions),
            } as AppPageRef;
        })
        .filter((item): item is AppPageRef => item !== null);
}

export async function listApps(podId: string): Promise<AppListItem[]> {
    const response = await getLemmaClient(podId).apps.list({ limit: 1000 }) as { items?: unknown[] };
    const items = Array.isArray(response?.items) ? response.items : [];
    const apps: AppListItem[] = [];

    for (const item of items) {
        const parsed = (item || {}) as Record<string, unknown>;
        const id = toOptionalString(parsed.id);
        const name = toOptionalString(parsed.name);
        const url = normalizeAppUrl(toOptionalString(parsed.url));

        if (!id || !name || !url) continue;

        apps.push({
            id,
            name,
            url,
            description: typeof parsed.description === 'string' ? parsed.description : null,
            public_slug: toOptionalString(parsed.public_slug),
            status: toOptionalString(parsed.status),
            visibility: typeof parsed.visibility === 'string' ? parsed.visibility : null,
            allowed_actions: normalizeAllowedActions(parsed.allowed_actions),
        });
    }

    return apps;
}

export function useAppConfig(podId: string) {
    return useQuery({
        queryKey: ['app-config', podId],
        queryFn: async (): Promise<AppConfig | null> => {
            const pages = await listAppPageRefs(podId);
            if (pages.length === 0) return null;
            const now = new Date().toISOString();
            return {
                id: `${Date.now()}-${Math.random().toString(36).slice(2, 9)}`,
                podId,
                name: 'Default App',
                pages,
                createdAt: now,
                updatedAt: now,
            };
        },
        enabled: !!podId,
        staleTime: 2 * 60 * 1000,
        gcTime: 30 * 60 * 1000,
    });
}

// Get list of app pages
export function useAppPages(podId: string) {
    const { data: config, isLoading, error, refetch } = useAppConfig(podId);

    const pages = useMemo(() => {
        if (!config?.pages) return [];
        return [...config.pages].sort((a: AppPageRef, b: AppPageRef) => a.order - b.order);
    }, [config]);

    return { pages, isLoading, error, revalidate: refetch };
}

export function useApps(podId: string) {
    return useQuery({
        queryKey: ['apps', podId],
        queryFn: () => listApps(podId),
        enabled: !!podId,
        staleTime: 2 * 60 * 1000,
        gcTime: 30 * 60 * 1000,
    });
}

export function useDeleteApp() {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: ({ podId, name }: { podId: string; name: string }) =>
            getLemmaClient(podId).apps.delete(name),
        onSuccess: (_, variables) => {
            queryClient.invalidateQueries({ queryKey: ['apps', variables.podId] });
            queryClient.invalidateQueries({ queryKey: ['app-config', variables.podId] });
            queryClient.invalidateQueries({ queryKey: ['app-page', variables.podId] });
        },
    });
}

// Get a single app page
export function useAppPage(
    podId: string,
    pageSlug: string | null,
    pageRef?: AppPageRef | null,
    options?: AppPageQueryOptions
) {
    const mode = options?.mode || 'view';

    return useQuery({
        queryKey: ['app-page', podId, pageRef?.slug || pageSlug, mode],
        queryFn: async (): Promise<AppPage> => {
            const refs = await listAppPageRefs(podId);
            const targetRef = pageRef
                ? refs.find((entry) => entry.slug === pageRef.slug) || pageRef
                : refs.find((entry) => entry.slug === normalizeAppPageSlug(pageSlug || ''));
            if (!targetRef) {
                throw new Error('Page not found');
            }

            const pageName = targetRef.title;
            const metadataRaw = await getLemmaClient(podId).apps.get(pageName).catch(() => null);
            const metadata = metadataRaw && typeof metadataRaw === 'object'
                ? metadataRaw as Record<string, unknown>
                : {};
            const url = normalizeAppUrl(toOptionalString(metadata.url) || targetRef.url);
            const createdAt = toOptionalString(metadata.created_at) || new Date().toISOString();
            const updatedAt = toOptionalString(metadata.updated_at) || new Date().toISOString();

            return {
                id: toOptionalString(metadata.id) || targetRef.id,
                slug: targetRef.slug,
                podId,
                title: toOptionalString(metadata.name) || targetRef.title,
                url,
                icon: undefined,
                order: targetRef.order,
                createdAt,
                updatedAt,
                visibility: typeof metadata.visibility === 'string' ? metadata.visibility : targetRef.visibility,
                allowed_actions: normalizeAllowedActions(metadata.allowed_actions) || targetRef.allowed_actions,
            };
        },
        enabled: !!podId && !!pageSlug,
        staleTime: mode === 'view' ? 5 * 60 * 1000 : 0,
        refetchOnWindowFocus: mode !== 'view',
        refetchOnReconnect: mode !== 'view',
        gcTime: mode === 'view' ? 30 * 60 * 1000 : undefined,
    });
}
