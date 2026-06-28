'use client';

import { use, useCallback, useEffect, useRef, useState } from 'react';
import Link from 'next/link';
import { usePathname, useRouter, useSearchParams } from 'next/navigation';
import { CalendarClock, Loader2, Save, Share2 } from 'lucide-react';
import { toast } from 'sonner';

import { AgentEditor } from '@/components/agents/agent-editor';
import { AgentTestPanel } from '@/components/agents/agent-test-panel';
import {
    ResourceDetailHeader,
    ResourceDetailShell,
    ResourceDetailViewport,
    ResourceTabPane,
} from '@/components/pod/resource-layout';
import { ResourceArrivalNotice } from '@/components/shared/resource-feedback';
import { ResourceShareButton, ResourceVisibilityBadge, type ResourceVisibilityValue } from '@/components/shared/resource-visibility';
import { Button } from '@/components/ui/button';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip';
import { resourceAllows } from '@/lib/authz/resource-actions';
import { useAgent, useUpdateAgent } from '@/lib/hooks/use-agents';
import { usePodAccess } from '@/lib/hooks/use-pod-access';
import { useSchedules } from '@/lib/hooks/use-schedules';
import { Agent, UpdateAgentData } from '@/lib/types';

type AgentDetailMode = 'runs' | 'edit';

export default function AgentDetailPage({
    params,
}: {
    params: Promise<{ id: string; agentId: string }>;
}) {
    const { id: podId, agentId: agentNameParam } = use(params);
    const agentName = agentNameParam;
    const pathname = usePathname();
    const router = useRouter();
    const searchParams = useSearchParams();
    const podAccess = usePodAccess(podId);
    const canUpdateAgent = podAccess.can('agent.update');
    const canExecuteAgent = podAccess.can('agent.execute');
    const canUseSchedules = podAccess.canAny(['schedule.read', 'schedule.create']);

    const { data: agentData, isLoading } = useAgent(podId, agentName);
    const { data: schedulesData } = useSchedules(canUseSchedules ? podId : undefined, {
        agentName,
        limit: 20,
    });
    const updateAgent = useUpdateAgent();
    const { mutateAsync: updateAgentAsync } = updateAgent;

    const [localAgent, setLocalAgent] = useState<Agent | null>(null);
    const [hasUnsavedChanges, setHasUnsavedChanges] = useState(false);
    const [isRunFullView, setIsRunFullView] = useState(false);
    const lastSavedHashRef = useRef('');

    const buildUpdatePayload = useCallback((agent: Agent) => ({
        description: agent.description,
        icon_url: agent.icon_url,
        agent_runtime: agent.agent_runtime ?? null,
        instruction: agent.instruction,
        input_schema: agent.input_schema,
        output_schema: agent.output_schema,
        tool_sets: agent.tool_sets,
        accessible_tables: agent.accessible_tables,
        accessible_folders: agent.accessible_folders,
        accessible_connectors: agent.accessible_connectors,
        accessible_functions: agent.function_names ?? undefined,
        accessible_agents: agent.agent_names ?? undefined,
        visibility: agent.visibility as UpdateAgentData['visibility'],
    }), []);

    useEffect(() => {
        if (agentData && !hasUnsavedChanges) {
            // eslint-disable-next-line react-hooks/set-state-in-effect
            setLocalAgent(agentData);
            lastSavedHashRef.current = JSON.stringify(buildUpdatePayload(agentData));
        }
    }, [agentData, buildUpdatePayload, hasUnsavedChanges]);

    const isEqualValue = (currentValue: unknown, nextValue: unknown): boolean => {
        if (Object.is(currentValue, nextValue)) return true;
        if (typeof currentValue === 'object' && currentValue !== null && typeof nextValue === 'object' && nextValue !== null) {
            try {
                return JSON.stringify(currentValue) === JSON.stringify(nextValue);
            } catch {
                return false;
            }
        }
        return false;
    };

    const handleUpdate = useCallback((updates: Partial<Agent>) => {
        setLocalAgent((prev) => {
            if (!prev) return prev;
            if (!resourceAllows(prev, 'agent.update', canUpdateAgent)) return prev;

            const changed = Object.entries(updates).some(([key, value]) => {
                const currentValue = prev[key as keyof Agent];
                return !isEqualValue(currentValue, value);
            });

            if (!changed) return prev;
            setHasUnsavedChanges(true);
            return { ...prev, ...updates };
        });
    }, [canUpdateAgent]);

    const handleSave = useCallback(async () => {
        const currentAgent = localAgent;
        if (!currentAgent) return;
        if (!resourceAllows(currentAgent, 'agent.update', canUpdateAgent)) return;

        const payload = buildUpdatePayload(currentAgent);
        const payloadHash = JSON.stringify(payload);

        if (payloadHash === lastSavedHashRef.current) {
            setHasUnsavedChanges(false);
            return;
        }

        try {
            await updateAgentAsync({
                podId,
                agentName,
                data: payload,
            });
            lastSavedHashRef.current = payloadHash;
            setHasUnsavedChanges(false);
        } catch (error) {
            console.error('Failed to save agent:', error);
            toast.error(error instanceof Error ? error.message : 'Failed to save agent. Please try again.');
        }
    }, [agentName, buildUpdatePayload, canUpdateAgent, localAgent, podId, updateAgentAsync]);

    const handleShareVisibilityChange = useCallback(async (visibility: ResourceVisibilityValue) => {
        const currentAgent = localAgent;
        if (!currentAgent) return;
        if (!resourceAllows(currentAgent, 'agent.update', canUpdateAgent)) return;

        try {
            await updateAgentAsync({
                podId,
                agentName,
                data: { visibility: visibility as UpdateAgentData['visibility'] },
            });
        } catch (error) {
            console.error('Failed to update agent visibility:', error);
            toast.error(error instanceof Error ? error.message : 'Failed to update visibility. Please try again.');
            return;
        }

        const nextAgent = { ...currentAgent, visibility };
        setLocalAgent((prev) => prev ? { ...prev, visibility } : prev);

        if (!hasUnsavedChanges) {
            lastSavedHashRef.current = JSON.stringify(buildUpdatePayload(nextAgent));
        }
    }, [agentName, buildUpdatePayload, canUpdateAgent, hasUnsavedChanges, localAgent, podId, updateAgentAsync]);

    const canUpdateCurrentAgent = resourceAllows(localAgent, 'agent.update', canUpdateAgent);
    const canExecuteCurrentAgent = resourceAllows(localAgent, 'agent.execute', canExecuteAgent);
    const activeScheduleCount = (schedulesData?.items || []).filter((schedule) => schedule.is_active !== false).length;
    const activeMode: AgentDetailMode = canUpdateCurrentAgent && searchParams.get('mode') === 'edit' ? 'edit' : 'runs';

    const setActiveMode = useCallback((nextMode: AgentDetailMode) => {
        if (nextMode === 'edit' && !canUpdateCurrentAgent) return;
        const nextParams = new URLSearchParams(searchParams.toString());
        if (nextMode === 'edit') {
            nextParams.set('mode', 'edit');
            setIsRunFullView(false);
        } else {
            nextParams.delete('mode');
        }
        const nextQuery = nextParams.toString();
        router.replace(nextQuery ? `${pathname}?${nextQuery}` : pathname, { scroll: false });
    }, [canUpdateCurrentAgent, pathname, router, searchParams, setIsRunFullView]);

    if (isLoading) {
        return (
            <div className="flex h-full overflow-hidden bg-transparent">
                <div className="flex min-w-0 flex-1 flex-col">
                    <div className="sticky top-0 z-10 flex items-center justify-between bg-[color:color-mix(in_srgb,var(--card-bg)_88%,transparent)] px-4 py-2 shadow-[var(--shadow-xs)]">
                        <div className="flex items-center gap-2">
                            <div className="h-5 w-5 animate-pulse rounded bg-[var(--bg-subtle)]" />
                            <div className="h-5 w-32 animate-pulse rounded bg-[var(--bg-subtle)]" />
                        </div>
                        <div className="flex gap-2">
                            <div className="h-7 w-16 animate-pulse rounded bg-[var(--bg-subtle)]" />
                            <div className="h-7 w-8 animate-pulse rounded bg-[var(--bg-subtle)]" />
                        </div>
                    </div>

                    <div className="flex-1 space-y-8 p-12">
                        <div className="h-16 w-16 animate-pulse rounded-xl bg-[var(--bg-subtle)]" />
                        <div className="h-10 max-w-md animate-pulse rounded bg-[var(--bg-subtle)]" />
                        <div className="space-y-4">
                            <div className="h-8 w-full animate-pulse rounded bg-[var(--bg-subtle)]" />
                            <div className="h-24 w-full animate-pulse rounded bg-[var(--bg-subtle)]" />
                        </div>
                    </div>
                </div>

                <div className="hidden w-[500px] bg-[var(--card-bg)] shadow-[var(--shadow-sm)] lg:block">
                    <div className="p-4">
                        <div className="h-8 w-32 animate-pulse rounded bg-[var(--bg-subtle)]" />
                    </div>
                    <div className="space-y-4 p-4">
                        <div className="h-32 animate-pulse rounded bg-[var(--bg-subtle)]" />
                        <div className="h-10 animate-pulse rounded bg-[var(--bg-subtle)]" />
                    </div>
                </div>
            </div>
        );
    }

    if (!localAgent) {
        return (
            <div className="flex h-full items-center justify-center bg-transparent">
                <div className="text-center">
                    <h2 className="font-display text-2xl font-semibold text-[var(--text-primary)]">Agent not found</h2>
                </div>
            </div>
        );
    }

    const agentShareUrl = typeof window === 'undefined'
        ? undefined
        : `${window.location.origin}/pod/${podId}/agents/${encodeURIComponent(localAgent.name || agentName)}`;

    return (
        <ResourceDetailShell>
            <ResourceDetailHeader
                title={localAgent.name}
                productIconTone="agents"
                backHref={`/pod/${podId}/ai`}
                backLabel="Agents"
                meta={(
                    <div className="flex flex-wrap items-center gap-2">
                        <ResourceVisibilityBadge visibility={localAgent.visibility} resourceLabel="agents" />
                        <span className="chip chip-sm chip-muted">
                            {activeScheduleCount ? `${activeScheduleCount} active schedule${activeScheduleCount === 1 ? '' : 's'}` : 'No schedules'}
                        </span>
                    </div>
                )}
                fullscreen={activeMode === 'runs' && isRunFullView}
                tabs={(
                    <AgentModeSwitch
                        value={activeMode}
                        onChange={setActiveMode}
                        canEdit={canUpdateCurrentAgent}
                    />
                )}
                actions={(
                    <TooltipProvider>
                    <>
                        {canUpdateCurrentAgent && (hasUnsavedChanges || updateAgent.isPending) ? (
                            <Button
                                type="button"
                                size="sm"
                                className="h-8 gap-1.5 px-3 text-xs font-medium"
                                onClick={() => void handleSave()}
                                disabled={updateAgent.isPending || !hasUnsavedChanges}
                            >
                                {updateAgent.isPending ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <Save className="h-3.5 w-3.5" />}
                                {updateAgent.isPending ? 'Saving...' : 'Save changes'}
                            </Button>
                        ) : null}
                        {canUseSchedules ? (
                            <Tooltip>
                                <TooltipTrigger asChild>
                                    <Button asChild variant="ghost" size="icon" className="h-8 w-8 rounded" aria-label={activeScheduleCount ? 'Schedules' : 'Schedule'}>
                                        <Link href={`/pod/${podId}/schedules?agent=${encodeURIComponent(localAgent.name || agentName)}`}>
                                            <CalendarClock className="h-4 w-4" />
                                        </Link>
                                    </Button>
                                </TooltipTrigger>
                                <TooltipContent>{activeScheduleCount ? 'Schedules' : 'Schedule'}</TooltipContent>
                            </Tooltip>
                        ) : null}
                        {canUpdateCurrentAgent ? (
                            <ResourceShareButton
                                value={localAgent.visibility}
                                podId={podId}
                                resourceType="agent"
                                resourceId={localAgent.id}
                                resourceLabel="agents"
                                resourceName={localAgent.name}
                                shareUrl={agentShareUrl}
                                onChange={handleShareVisibilityChange}
                                trigger={({ openShare, disabled }) => (
                                    <Tooltip>
                                        <TooltipTrigger asChild>
                                            <Button
                                                type="button"
                                                variant="ghost"
                                                size="icon"
                                                className="h-8 w-8 rounded"
                                                onClick={openShare}
                                                disabled={disabled}
                                                aria-label="Share"
                                            >
                                                <Share2 className="h-4 w-4" />
                                            </Button>
                                        </TooltipTrigger>
                                        <TooltipContent>Share</TooltipContent>
                                    </Tooltip>
                                )}
                            />
                        ) : null}
                    </>
                    </TooltipProvider>
                )}
            />
            <ResourceArrivalNotice
                resource="agent"
                title="Agent created"
                description="Ready for a first run. Try it here, then tune setup or add a schedule."
                celebrate
                actions={[
                    ...(canUpdateCurrentAgent ? [{ label: 'Edit setup', onClick: () => setActiveMode('edit'), variant: 'primary' as const }] : []),
                    ...(canUseSchedules ? [{ label: 'Schedule', href: `/pod/${podId}/schedules?agent=${encodeURIComponent(localAgent.name || agentName)}` }] : []),
                ]}
                className="mx-4 mt-3"
            />

            <ResourceDetailViewport>
                <ResourceTabPane active={activeMode === 'edit'}>
                    {activeMode === 'edit' ? (
                        <AgentEditor
                            podId={podId}
                            agent={localAgent}
                            onUpdate={handleUpdate}
                            isNameEditable={false}
                            shareUrl={agentShareUrl}
                            onShareVisibilityChange={handleShareVisibilityChange}
                        />
                    ) : null}
                </ResourceTabPane>

                <ResourceTabPane active={activeMode === 'runs'}>
                    {activeMode === 'runs' && canExecuteCurrentAgent ? (
                        <div className="h-full min-h-0 bg-[var(--card-bg)]">
                            <AgentTestPanel
                                podId={podId}
                                agentName={localAgent.name || agentName}
                                agentOverride={localAgent}
                                isFullView={isRunFullView}
                                onToggleFullView={() => setIsRunFullView((prev) => !prev)}
                            />
                        </div>
                    ) : activeMode === 'runs' ? (
                        <div className="flex h-full items-center justify-center bg-[var(--card-bg)] px-6 text-center text-sm text-[var(--text-secondary)]">
                            You can view this agent, but running it is outside your current permissions.
                        </div>
                    ) : null}
                </ResourceTabPane>
            </ResourceDetailViewport>
        </ResourceDetailShell>
    );
}

function AgentModeSwitch({
    value,
    onChange,
    canEdit,
}: {
    value: AgentDetailMode;
    onChange: (value: AgentDetailMode) => void;
    canEdit: boolean;
}) {
    const items: AgentDetailMode[] = canEdit ? ['runs', 'edit'] : ['runs'];
    return (
        <div className="segmented-control">
            {items.map((item) => (
                <button
                    key={item}
                    type="button"
                    onClick={() => onChange(item)}
                    className="segmented-control-item custom-focus-ring"
                    data-active={value === item}
                    aria-pressed={value === item}
                >
                    {item === 'runs' ? 'Runs' : 'Edit'}
                </button>
            ))}
        </div>
    );
}
