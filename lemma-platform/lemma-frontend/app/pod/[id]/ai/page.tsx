'use client';

import { use, useMemo, useState } from 'react';
import Link from 'next/link';
import {
    Bot,
    ChevronRight,
    Plus,
    Share2,
} from 'lucide-react';
import { toast } from 'sonner';

import { Button } from '@/components/ui/button';
import { DestructiveConfirmationDialog } from '@/components/shared/destructive-confirmation-dialog';
import { EmptyState } from '@/components/shared/empty-state';
import { ProductIcon } from '@/components/pod/product-icon';
import { ConceptHint } from '@/components/education/concept-hint';
import { SectionPrimer } from '@/components/education/section-primer';
import { ResourceIndexHeader, ResourceIndexShell, ResourceMetricButton, ResourceMetricStrip } from '@/components/pod/resource-layout';
import { ResourceIcon } from '@/components/shared/resource-icon';
import { DestructiveResourceActionItem, ResourceActionsMenu } from '@/components/shared/resource-actions-menu';
import { ResourceShareButton, ResourceVisibilityBadge, type ResourceVisibilityValue } from '@/components/shared/resource-visibility';
import { DropdownMenuItem } from '@/components/ui/dropdown-menu';
import { useAgents, useDeleteAgent, useUpdateAgent } from '@/lib/hooks/use-agents';
import { resourceAllows } from '@/lib/authz/resource-actions';
import { usePodAccess } from '@/lib/hooks/use-pod-access';
import { useFlows } from '@/lib/hooks/use-flows';
import { useSchedules } from '@/lib/hooks/use-schedules';
import type { Agent, UpdateAgentData, Workflow } from '@/lib/types';
import { NodeType } from '@/lib/types';
import { getAgentNodeName } from '@/lib/utils/flow-node-config';
import { cn } from '@/lib/utils';

type AgentFilter = 'all' | 'workflows' | 'scheduled';

function countConnections(agent: Agent): number {
    return (
        (agent.tool_sets?.length ?? agent.toolsets?.length ?? 0)
        + (agent.accessible_tables?.length ?? 0)
        + (agent.accessible_folders?.length ?? 0)
        + (agent.accessible_connectors?.length ?? 0)
    );
}

function agentSummary(agent: Agent): string | null {
    const description = agent.description?.trim();
    if (description) return description;
    return null;
}

export default function AgentsPage({
    params,
}: {
    params: Promise<{ id: string }>;
}) {
    const { id: podId } = use(params);
    const podAccess = usePodAccess(podId);
    const canCreateAgent = podAccess.can('agent.create');
    const canUpdateAgent = podAccess.can('agent.update');
    const canDeleteAgent = podAccess.can('agent.delete');
    const canReadSchedules = podAccess.can('schedule.read');
    const canReadWorkflows = podAccess.can('workflow.read');
    const { data: agentsData, isLoading } = useAgents(podId);
    const { data: schedulesData } = useSchedules(canReadSchedules ? podId : undefined, { limit: 100 });
    const { data: flowsData } = useFlows(canReadWorkflows ? podId : undefined);
    const { mutate: deleteAgent, isPending: isDeletingAgent } = useDeleteAgent();
    const updateAgent = useUpdateAgent();
    const [agentFilter, setAgentFilter] = useState<AgentFilter>('all');
    const [agentPendingDelete, setAgentPendingDelete] = useState<Agent | null>(null);

    const agents = useMemo(() => agentsData?.items ?? [], [agentsData?.items]);
    const flows = useMemo(() => flowsData || [], [flowsData]);
    const schedules = useMemo(() => schedulesData?.items || [], [schedulesData?.items]);
    const activeAgentScheduleCount = schedules.filter((schedule) => schedule.agent_name && schedule.is_active !== false).length;
    const scheduledAgentNames = useMemo(() => new Set(
        schedules
            .filter((schedule) => schedule.agent_name && schedule.is_active !== false)
            .map((schedule) => schedule.agent_name as string)
    ), [schedules]);
    const agentUsage = useMemo(() => buildAgentUsage(flows), [flows]);
    const filteredAgents = useMemo(() => {
        return agents.filter((agent) => {
            const isScheduled = scheduledAgentNames.has(agent.name);
            const isInWorkflow = (agentUsage.get(agent.name)?.size || 0) > 0;
            const matchesFilter =
                agentFilter === 'all'
                || (agentFilter === 'scheduled' && isScheduled)
                || (agentFilter === 'workflows' && isInWorkflow);
            return matchesFilter;
        });
    }, [agentFilter, agentUsage, agents, scheduledAgentNames]);
    const agentsInWorkflows = agents.filter((agent) => (agentUsage.get(agent.name)?.size || 0) > 0).length;
    const agentPendingDeleteScheduleCount = agentPendingDelete
        ? schedules.filter((schedule) => schedule.agent_name === agentPendingDelete.name && schedule.is_active !== false).length
        : 0;
    const agentPendingDeleteWorkflowCount = agentPendingDelete
        ? agentUsage.get(agentPendingDelete.name)?.size || 0
        : 0;

    const handleDeleteAgent = () => {
        if (!agentPendingDelete) return;
        if (!resourceAllows(agentPendingDelete, 'agent.delete', canDeleteAgent)) return;
        deleteAgent(
            { podId, agentName: agentPendingDelete.name },
            {
                onSuccess: () => {
                    toast.success('Agent deleted');
                    setAgentPendingDelete(null);
                },
                onError: () => toast.error('Failed to delete agent'),
            }
        );
    };

    return (
        <ResourceIndexShell>
            <ResourceIndexHeader
                title="Agents"
                productIconTone="agents"
                meta={<ConceptHint concept="agent" />}
                actions={(
                    canCreateAgent ? <Link href={`/pod/${podId}/agents/new`}>
                        <Button className="gap-2" size="sm">
                            <Plus className="h-4 w-4" />
                            New agent
                        </Button>
                    </Link> : null
                )}
            />

            <SectionPrimer concept="agent" className="mb-4" />

            {isLoading ? (
                <div className="space-y-4">
                    <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
                        {[1, 2, 3, 4].map((item) => (
                            <div key={`agent-metric-skeleton-${item}`} className="h-28 animate-pulse rounded-lg bg-[var(--surface-2)]" />
                        ))}
                    </div>
                    <div className="h-80 animate-pulse rounded-lg bg-[var(--surface-2)]" />
                </div>
            ) : agents.length === 0 ? (
                <EmptyState
                    variant="panel"
                    icon={<Bot className="h-5 w-5" />}
                    title="No agents yet"
                    description={canCreateAgent
                        ? "Add the first agent this pod can run. Start with a role, instructions, and the context it can access."
                        : "No agents are available to you yet."}
                    action={canCreateAgent ? (
                        <Link href={`/pod/${podId}/agents/new`}>
                            <Button size="sm" className="gap-2">
                                <Plus className="h-4 w-4" />
                                New agent
                            </Button>
                        </Link>
                    ) : undefined}
                />
            ) : (
                <div>
                    <ResourceMetricStrip>
                        <ResourceMetricButton active={agentFilter === 'all'} label="Agents" count={agents.length} onClick={() => setAgentFilter('all')} />
                        <ResourceMetricButton active={agentFilter === 'workflows'} label="In workflows" count={agentsInWorkflows} onClick={() => setAgentFilter('workflows')} />
                        <ResourceMetricButton active={agentFilter === 'scheduled'} label="Scheduled" count={activeAgentScheduleCount} onClick={() => setAgentFilter('scheduled')} />
                    </ResourceMetricStrip>

                    <section className="resource-index-grid resource-index-grid-md-2 resource-index-grid-xl-3 sm:grid-cols-2 xl:grid-cols-3">
                        {filteredAgents.map((agent) => (
                            <AgentProfileCard
                                key={agent.id}
                                agent={agent}
                                podId={podId}
                                activeScheduleCount={schedules.filter((schedule) => schedule.agent_name === agent.name && schedule.is_active !== false).length}
                                workflowCount={agentUsage.get(agent.name)?.size || 0}
                                onDelete={setAgentPendingDelete}
                                canUpdate={resourceAllows(agent, 'agent.update', canUpdateAgent)}
                                canDelete={resourceAllows(agent, 'agent.delete', canDeleteAgent)}
                                onShareVisibilityChange={async (visibility) => {
                                    await updateAgent.mutateAsync({
                                        podId,
                                        agentName: agent.name,
                                        data: { visibility: visibility as UpdateAgentData['visibility'] },
                                    });
                                }}
                            />
                        ))}
                        {filteredAgents.length === 0 ? (
                            <EmptyState
                                variant="compact"
                                icon={<Bot className="h-4 w-4" />}
                                title="No agents match this search"
                                description="Try a different agent name or description."
                            />
                        ) : null}
                    </section>
                </div>
            )}
            <DestructiveConfirmationDialog
                open={Boolean(agentPendingDelete)}
                onOpenChange={(open) => {
                    if (!open) setAgentPendingDelete(null);
                }}
                title="Delete agent"
                description={`Delete "${agentPendingDelete?.name ?? ''}"? This removes the agent from this pod.`}
                resourceName={agentPendingDelete?.name ?? ''}
                consequences={[
                    agentPendingDeleteWorkflowCount > 0
                        ? `${agentPendingDeleteWorkflowCount} workflow${agentPendingDeleteWorkflowCount === 1 ? '' : 's'} reference this agent and may fail until updated.`
                        : 'No workflows currently reference this agent.',
                    agentPendingDeleteScheduleCount > 0
                        ? `${agentPendingDeleteScheduleCount} active schedule${agentPendingDeleteScheduleCount === 1 ? '' : 's'} target this agent.`
                        : 'No active schedules currently target this agent.',
                    'This action cannot be undone.',
                ]}
                confirmLabel="Delete agent"
                pendingLabel="Deleting agent..."
                isPending={isDeletingAgent}
                onConfirm={handleDeleteAgent}
            />
        </ResourceIndexShell>
    );
}

function AgentProfileCard({
    agent,
    podId,
    activeScheduleCount,
    workflowCount,
    onDelete,
    canUpdate,
    canDelete,
    onShareVisibilityChange,
}: {
    agent: Agent;
    podId: string;
    activeScheduleCount: number;
    workflowCount: number;
    onDelete: (agent: Agent) => void;
    canUpdate: boolean;
    canDelete: boolean;
    onShareVisibilityChange: (visibility: ResourceVisibilityValue) => Promise<void>;
}) {
    const connectionCount = countConnections(agent);
    const summary = agentSummary(agent);
    const statusLabel = activeScheduleCount > 0
        ? 'Scheduled'
        : workflowCount > 0
            ? 'In workflow'
            : connectionCount > 0
                ? `Access ${connectionCount}`
                : 'Draft';
    const hasMenuActions = canUpdate || canDelete;
    const agentShareUrl = typeof window === 'undefined'
        ? undefined
        : `${window.location.origin}/pod/${podId}/agents/${encodeURIComponent(agent.name)}`;

    return (
        <div className="resource-index-card group min-h-40 p-4">
            <div className="flex items-start justify-between gap-3">
                <Link href={`/pod/${podId}/agents/${encodeURIComponent(agent.name)}`} className="min-w-0 flex-1">
                    <ResourceIcon
                        iconUrl={agent.icon_url}
                        alt={`${agent.name} profile picture`}
                        label={agent.name}
                        imageClassName="object-contain p-1"
                        className="h-11 w-11 shrink-0 rounded-lg bg-transparent"
                        fallback={<ProductIcon tone="agents" size="lg" />}
                    />
                </Link>
                <div className="flex shrink-0 items-center gap-1">
                    <span className={cn('chip chip-sm', getAgentStatusClass(activeScheduleCount, workflowCount, connectionCount))}>
                        {statusLabel}
                    </span>
                </div>
            </div>

            <Link href={`/pod/${podId}/agents/${encodeURIComponent(agent.name)}`} className="block">
                <div className="mt-3 min-w-0">
                    <h2 className="truncate text-base font-semibold tracking-normal text-[var(--text-primary)]">{agent.name}</h2>
                    <p className="mt-1 line-clamp-2 min-h-10 text-sm leading-6 text-[var(--text-secondary)]">
                        {summary || 'Ready for instructions, tools, and pod context.'}
                    </p>
                </div>

                <div className="mt-4 flex flex-wrap gap-1.5">
                    <ResourceVisibilityBadge visibility={agent.visibility} resourceLabel="agents" />
                    <AgentCardPill label={`Access ${connectionCount}`} muted={connectionCount === 0} />
                    <AgentCardPill label={`${workflowCount} workflow${workflowCount === 1 ? '' : 's'}`} muted={workflowCount === 0} />
                    <AgentCardPill label={activeScheduleCount ? `${activeScheduleCount} schedule${activeScheduleCount === 1 ? '' : 's'}` : 'No schedules'} muted={activeScheduleCount === 0} />
                </div>
            </Link>

            <div className="mt-3 flex items-center justify-between text-xs text-[var(--text-tertiary)]">
                {hasMenuActions ? (
                    <ResourceActionsMenu
                        ariaLabel={`Open actions for ${agent.name}`}
                        align="start"
                        triggerClassName="h-7 w-7 opacity-0 transition-opacity group-hover:opacity-100 group-focus-within:opacity-100"
                    >
                        {canUpdate ? (
                            <ResourceShareButton
                                value={agent.visibility}
                                podId={podId}
                                resourceType="agent"
                                resourceId={agent.id}
                                resourceLabel="agents"
                                resourceName={agent.name}
                                shareUrl={agentShareUrl}
                                onChange={onShareVisibilityChange}
                                className="contents"
                                trigger={({ openShare, disabled }) => (
                                    <DropdownMenuItem
                                        disabled={disabled}
                                        onSelect={(event) => {
                                            event.preventDefault();
                                            openShare();
                                        }}
                                    >
                                        <Share2 className="mr-2 h-4 w-4" />
                                        Share
                                    </DropdownMenuItem>
                                )}
                            />
                        ) : null}
                        {canDelete ? (
                            <DestructiveResourceActionItem onSelect={() => onDelete(agent)}>
                            Delete agent
                            </DestructiveResourceActionItem>
                        ) : null}
                    </ResourceActionsMenu>
                ) : <span />}
                <Link
                    href={`/pod/${podId}/agents/${encodeURIComponent(agent.name)}`}
                    className="inline-flex items-center gap-1 font-medium text-[var(--text-secondary)] opacity-0 transition-gentle group-hover:translate-x-0.5 group-hover:opacity-100"
                >
                    Open
                    <ChevronRight className="h-3.5 w-3.5" />
                </Link>
            </div>
        </div>
    );
}

function AgentCardPill({ label, muted }: { label: string; muted?: boolean }) {
    return (
        <span className={cn(
            'chip chip-sm',
            muted ? 'chip-muted text-[var(--text-tertiary)]' : 'state-badge-brand'
        )}>
            {label}
        </span>
    );
}

function getAgentStatusClass(activeScheduleCount: number, workflowCount: number, connectionCount: number): string {
    if (activeScheduleCount > 0) return 'state-badge-brand';
    if (workflowCount > 0) return 'state-badge-brand';
    if (connectionCount > 0) return 'state-badge-brand';
    return 'chip-muted text-[var(--text-tertiary)]';
}

function buildAgentUsage(flows: Workflow[]) {
    const usage = new Map<string, Set<string>>();
    flows.forEach((flow) => {
        (flow.nodes || []).forEach((node) => {
            if (node.type !== NodeType.AGENT) return;
            const agentName = getAgentNodeName(node.config);
            if (!agentName) return;
            const set = usage.get(agentName) || new Set<string>();
            set.add(flow.name);
            usage.set(agentName, set);
        });
    });
    return usage;
}
