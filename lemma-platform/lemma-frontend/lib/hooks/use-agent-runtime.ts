import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { getLemmaClient } from '@/lib/sdk/lemma-client';

export const agentRuntimeQueryKey = (organizationId?: string | null) =>
    ['agent-runtime', 'runtimes', organizationId ?? null] as const;

export const availableAgentRuntimeHarnessesQueryKey = () =>
    ['agent-runtime', 'available-harnesses'] as const;

export const useAvailableAgentRuntimeHarnesses = () => {
    return useQuery({
        queryKey: availableAgentRuntimeHarnessesQueryKey(),
        queryFn: () => getLemmaClient().agentRuntime.listAvailableHarnesses(),
        staleTime: 30000,
        refetchOnWindowFocus: true,
    });
};

export const useAgentRuntimes = (organizationId?: string | null) => {
    return useQuery({
        queryKey: agentRuntimeQueryKey(organizationId),
        queryFn: () => getLemmaClient().agentRuntime.listRuntimes(organizationId!),
        enabled: Boolean(organizationId),
        staleTime: 30000,
        refetchOnWindowFocus: true,
    });
};

export const useAgentRuntimeCatalog = useAgentRuntimes;

export const useCreateAgentRuntime = () => {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: ({
            organizationId,
            request,
        }: {
            organizationId: string;
            request: Parameters<ReturnType<typeof getLemmaClient>['agentRuntime']['createRuntime']>[1];
        }) => getLemmaClient().agentRuntime.createRuntime(organizationId, request),
        onSuccess: (_, variables) => {
            queryClient.invalidateQueries({ queryKey: agentRuntimeQueryKey(variables.organizationId) });
        },
    });
};

export const useUpdatePodDefaultAgentRuntime = () => {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: ({ podId, agentRuntimeId }: { podId: string; agentRuntimeId: string | null }) =>
            getLemmaClient().pods.update(podId, {
                config: {
                    default_profile_id: agentRuntimeId,
                },
            }),
        onSuccess: (_, variables) => {
            queryClient.invalidateQueries({ queryKey: ['pods'] });
            queryClient.invalidateQueries({ queryKey: ['pods', variables.podId] });
        },
    });
};

export const useUpdatePodDefaultRuntimeProfile = useUpdatePodDefaultAgentRuntime;
