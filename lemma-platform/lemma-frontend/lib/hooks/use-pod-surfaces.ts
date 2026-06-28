'use client';

import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { getLemmaClient } from '@/lib/sdk/lemma-client';
import type { AssistantSurface } from '@/lib/types';
import type {
    AvailableSurfaceChannelsResponse,
    SurfacePlatform,
    SurfaceSetupResponse,
    SurfaceUpsertRequest,
} from 'lemma-sdk';

export type SurfacePlatformValue = `${SurfacePlatform}`;

export interface UpsertPodSurfaceInput {
    podId: string;
    platform: SurfacePlatformValue;
    data: SurfaceUpsertRequest;
}

const surfacesKey = (podId: string) => ['pod-surfaces', podId];
const setupKey = (podId: string, platform: string) => ['pod-surface-setup', podId, platform];

export const usePodSurfaces = (podId: string | undefined) => {
    return useQuery({
        queryKey: ['pod-surfaces', podId],
        queryFn: async () => {
            const response = await getLemmaClient().podSurfaces.list(podId!);
            return (response.items || []) as AssistantSurface[];
        },
        enabled: !!podId,
    });
};

/**
 * Unified setup read: live status + webhook info + admin-consent + the platform
 * checklist, in one call. Works before a surface exists (guide only) and after.
 */
export const useSurfaceSetup = (
    podId: string,
    platform: SurfacePlatformValue | null | undefined,
    enabled = true
) => {
    return useQuery({
        queryKey: setupKey(podId, String(platform)),
        queryFn: () =>
            getLemmaClient().podSurfaces.setup(podId, platform as string) as Promise<SurfaceSetupResponse>,
        enabled: Boolean(podId && platform && enabled),
    });
};

/** Live channels/groups this surface can be routed to (Slack/Teams). */
export const useSurfaceChannels = (
    podId: string,
    platform: SurfacePlatformValue | null | undefined,
    enabled = true
) => {
    return useQuery({
        queryKey: ['pod-surface-channels', podId, platform],
        queryFn: () =>
            getLemmaClient().podSurfaces.channels(podId, platform as string) as Promise<AvailableSurfaceChannelsResponse>,
        enabled: Boolean(podId && platform && enabled),
        staleTime: 60 * 1000,
    });
};

/**
 * The single create-or-update write. Covers config, agent, account, credential
 * mode, channel routes (via config.channels), and enable/disable (is_enabled).
 */
export const useUpsertPodSurface = () => {
    const queryClient = useQueryClient();
    return useMutation({
        mutationFn: ({ podId, platform, data }: UpsertPodSurfaceInput) =>
            getLemmaClient().podSurfaces.upsert(podId, platform, data),
        onSuccess: (_data, vars) => {
            queryClient.invalidateQueries({ queryKey: surfacesKey(vars.podId) });
            queryClient.invalidateQueries({ queryKey: setupKey(vars.podId, vars.platform) });
        },
    });
};

/** Enable/disable convenience: a thin upsert that only flips is_enabled. */
export const useTogglePodSurface = () => {
    const queryClient = useQueryClient();
    return useMutation({
        mutationFn: ({ podId, platform, isActive }: { podId: string; platform: SurfacePlatformValue; isActive: boolean }) =>
            getLemmaClient().podSurfaces.upsert(podId, platform, { is_enabled: isActive }),
        onSuccess: (_data, vars) => {
            queryClient.invalidateQueries({ queryKey: surfacesKey(vars.podId) });
            queryClient.invalidateQueries({ queryKey: setupKey(vars.podId, vars.platform) });
        },
    });
};

/** Delete removes the surface entirely, freeing its account for another pod. */
export const useDeletePodSurface = () => {
    const queryClient = useQueryClient();
    return useMutation({
        mutationFn: ({ podId, platform }: { podId: string; platform: SurfacePlatformValue }) =>
            getLemmaClient().podSurfaces.delete(podId, platform),
        onSuccess: (_data, vars) => {
            queryClient.invalidateQueries({ queryKey: surfacesKey(vars.podId) });
            queryClient.invalidateQueries({ queryKey: setupKey(vars.podId, vars.platform) });
        },
    });
};
