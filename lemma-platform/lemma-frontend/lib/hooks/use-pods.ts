'use client';

import { ApiError } from 'lemma-sdk';
import { useMemo } from 'react';
import { useQuery, useMutation, useQueryClient, useQueries } from '@tanstack/react-query';
import { getLemmaClient } from '../sdk/lemma-client';
import { useOrganizations } from './use-organizations';
import type { CreatePodData, UpdatePodData, Pod, PaginatedResponse, Organization } from '../types';

export const usePods = (orgId?: string, options?: { enabled?: boolean }) => {
    const enabled = options?.enabled ?? true;

    return useQuery({
        queryKey: ['pods', orgId],
        queryFn: () =>
            getLemmaClient().pods.listByOrganization(orgId!) as Promise<PaginatedResponse<Pod>>,
        enabled: enabled && !!orgId,
    });
};

export type AccessiblePod = Pod & {
    organization?: Organization;
    organization_name?: string;
};

export type AccessiblePodGroup = {
    organization: Organization;
    pods: AccessiblePod[];
};

export const useAccessiblePods = (options?: { enabled?: boolean }) => {
    const enabled = options?.enabled ?? true;
    const organizationsQuery = useOrganizations({ enabled });
    const organizations = useMemo(() => organizationsQuery.data?.items || [], [organizationsQuery.data?.items]);

    const podQueries = useQueries({
        queries: organizations.map((organization) => ({
            queryKey: ['pods', organization.id],
            queryFn: () =>
                getLemmaClient().pods.listByOrganization(organization.id) as Promise<PaginatedResponse<Pod>>,
            enabled: enabled && !!organization.id,
        })),
    });

    const groups = useMemo<AccessiblePodGroup[]>(() => {
        return organizations.map((organization, index) => {
            const pods = (podQueries[index]?.data?.items || []).map((pod) => ({
                ...pod,
                organization,
                organization_name: organization.name,
            }));

            return { organization, pods };
        });
    }, [organizations, podQueries]);

    const pods = useMemo(() => groups.flatMap((group) => group.pods), [groups]);
    const isLoadingPods = organizations.length > 0 && podQueries.some((query) => query.isLoading);
    const podError = podQueries.find((query) => query.isError)?.error;

    return {
        data: {
            items: pods,
            groups,
            organizations,
            hasMultipleOrganizations: organizations.length > 1,
        },
        isLoading: organizationsQuery.isLoading || isLoadingPods,
        isError: organizationsQuery.isError || podQueries.some((query) => query.isError),
        error: organizationsQuery.error || podError,
    };
};

export const usePod = (id: string | undefined) => {
    return useQuery({
        queryKey: ['pods', id],
        queryFn: () => getLemmaClient().pods.get(id!) as Promise<Pod>,
        enabled: !!id && id !== 'undefined',
        retry: (failureCount, error) => {
            if (error instanceof ApiError) {
                if (
                    error.statusCode === 401 ||
                    error.statusCode === 403 ||
                    error.statusCode === 404 ||
                    error.code === 'INSUFFICIENT_ROLE'
                ) {
                    return false;
                }
            }

            return failureCount < 2;
        },
    });
};

export const useCreatePod = () => {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: (data: CreatePodData) => getLemmaClient().pods.create(data) as Promise<Pod>,
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: ['pods'] });
        },
    });
};

export const useUpdatePod = () => {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: ({ id, data }: { id: string; data: UpdatePodData }) =>
            getLemmaClient().pods.update(id, data) as Promise<Pod>,
        onSuccess: (_, variables) => {
            queryClient.invalidateQueries({ queryKey: ['pods'] });
            queryClient.invalidateQueries({ queryKey: ['pods', variables.id] });
        },
    });
};

export const useDeletePod = () => {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: async (id: string) => {
            await getLemmaClient().pods.delete(id);
        },
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: ['pods'] });
        },
    });
};
