'use client';

import { useQuery } from '@tanstack/react-query';

import { getLemmaClient } from '@/lib/sdk/lemma-client';
import type { RecentUsage, UsageLimits, UsageStats, UsageSummary } from '@/lib/types';

export interface UsageFilters {
    start?: string | null;
    end?: string | null;
    modelName?: string | null;
    podId?: string | null;
    userId?: string | null;
    agentId?: string | null;
    usageKind?: string | null;
    status?: string | null;
    days?: number;
    limit?: number;
}

export interface UsageStatsFilters extends UsageFilters {
    granularity?: 'hour' | 'day' | 'week' | 'month' | string;
    groupBy?: string | null;
}

function compactParams(params: Record<string, string | number | boolean | null | undefined>) {
    return Object.fromEntries(
        Object.entries(params).filter(([, value]) => value !== undefined && value !== null && value !== '')
    );
}

function usageParams(filters: UsageFilters = {}) {
    return compactParams({
        start: filters.start,
        end: filters.end,
        model_name: filters.modelName,
        pod_id: filters.podId,
        user_id: filters.userId,
        agent_id: filters.agentId,
        usage_kind: filters.usageKind,
        status: filters.status,
        days: filters.days,
        limit: filters.limit,
    });
}

function encodePath(value: string) {
    return encodeURIComponent(value);
}

export function useUsageSummary(
    organizationId: string | undefined,
    filters: UsageFilters = {},
    options?: { enabled?: boolean }
) {
    return useQuery({
        queryKey: ['usage', 'summary', organizationId, filters],
        queryFn: () => {
            if (!organizationId) {
                throw new Error('Organization is required to load usage.');
            }

            return getLemmaClient().request<UsageSummary>(
                'GET',
                `/usage/organizations/${encodePath(organizationId)}/summary`,
                { params: usageParams(filters) }
            );
        },
        enabled: Boolean(organizationId) && (options?.enabled ?? true),
    });
}

export function useUsageStats(
    organizationId: string | undefined,
    filters: UsageStatsFilters = {},
    options?: { enabled?: boolean }
) {
    return useQuery({
        queryKey: ['usage', 'stats', organizationId, filters],
        queryFn: () => {
            if (!organizationId) {
                throw new Error('Organization is required to load usage stats.');
            }

            return getLemmaClient().request<UsageStats>(
                'GET',
                `/usage/organizations/${encodePath(organizationId)}/stats`,
                {
                    params: {
                        ...usageParams(filters),
                        granularity: filters.granularity ?? 'day',
                        group_by: filters.groupBy,
                    },
                }
            );
        },
        enabled: Boolean(organizationId) && (options?.enabled ?? true),
    });
}

export function useRecentUsage(
    organizationId: string | undefined,
    filters: UsageFilters = {},
    options?: { enabled?: boolean }
) {
    return useQuery({
        queryKey: ['usage', 'recent', organizationId, filters],
        queryFn: () => {
            if (!organizationId) {
                throw new Error('Organization is required to load recent usage.');
            }

            return getLemmaClient().request<RecentUsage>(
                'GET',
                `/usage/organizations/${encodePath(organizationId)}/events`,
                { params: usageParams(filters) }
            );
        },
        enabled: Boolean(organizationId) && (options?.enabled ?? true),
    });
}

export function useUsageLimits(organizationId: string | undefined, options?: { enabled?: boolean }) {
    return useQuery({
        queryKey: ['usage', 'limits', organizationId],
        queryFn: () => {
            if (!organizationId) {
                throw new Error('Organization is required to load usage limits.');
            }

            return getLemmaClient().request<UsageLimits>(
                'GET',
                `/usage/organizations/${encodePath(organizationId)}/limits`
            );
        },
        enabled: Boolean(organizationId) && (options?.enabled ?? true),
    });
}
