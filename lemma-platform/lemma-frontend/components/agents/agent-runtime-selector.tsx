'use client';

import { useMemo, useState } from 'react';
import { RuntimeProfileScope } from 'lemma-sdk';
import type {
    AgentHarnessListResponse,
    AgentHarnessInfo,
    AgentRuntimeConfig,
    AgentRuntimeProfileListResponse,
    AgentRuntimeProfileResponse,
} from 'lemma-sdk';
import { ChevronDown, Loader2, Search, Zap } from 'lucide-react';
import { toast } from 'sonner';

import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
} from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { useCreateAgentRuntime } from '@/lib/hooks/use-agent-runtime';
import { cn } from '@/lib/utils';
import {
    availableHarnessKey,
    availableHarnessStatusLabel,
    CUSTOM_PROVIDER_OPTIONS,
    DEFAULT_VALUE,
    defaultAgentRuntimeFromProfile,
    findProfileByRuntime,
    firstHarnessModelName,
    firstRuntime,
    formatAgentRuntime,
    harnessLogo,
    harnessModelOptions,
    isHarnessAvailable,
    LOCAL_RUNTIME_SETUP_OPTIONS,
    resolveDefaultAgentRuntime,
    runtimeAvailabilityLabel,
    runtimeKey,
    runtimeModels,
    runtimeProfileDaemonKey,
    shortModelName,
    splitModelNames,
    type AgentRuntimeSelectionMode,
    type AvailableHarnessOption,
    type CustomProviderKind,
    type LocalRuntimeSetupOption,
} from './agent-runtime-helpers';
import {
    CustomProviderForm,
    HarnessChoiceRow,
    LocalRuntimeUnavailableDetail,
    RuntimeMark,
} from './agent-runtime-rows';
import {
    AvailableHarnessDetail,
    HarnessModelList,
    RuntimeListView,
} from './agent-runtime-views';

export { defaultAgentRuntimeFromProfile, resolveDefaultAgentRuntime, formatAgentRuntime };

export function AgentRuntimeSelector({
    catalog,
    availableHarnesses,
    organizationId,
    defaultRuntime,
    value,
    onChange,
    onCommit,
    onRefresh,
    commitLabel = 'Set model',
    commitLoading = false,
    isRefreshing = false,
    isLoading = false,
    disabled = false,
    allowDefault = false,
    label,
    description,
    variant = 'field',
    selectionMode = 'model',
}: {
    catalog?: AgentRuntimeProfileListResponse;
    availableHarnesses?: AgentHarnessListResponse;
    organizationId?: string | null;
    defaultRuntime?: AgentRuntimeConfig | null;
    value?: AgentRuntimeConfig | null;
    onChange: (runtime: AgentRuntimeConfig | null) => void;
    onCommit?: (runtime: AgentRuntimeConfig | null) => void;
    onRefresh?: () => void | Promise<void>;
    commitLabel?: string;
    commitLoading?: boolean;
    isRefreshing?: boolean;
    isLoading?: boolean;
    disabled?: boolean;
    allowDefault?: boolean;
    label?: string;
    description?: string;
    variant?: 'field' | 'compact' | 'list';
    selectionMode?: AgentRuntimeSelectionMode;
}) {
    const [isOpen, setIsOpen] = useState(false);
    const [query, setQuery] = useState('');
    const [activeProfileId, setActiveProfileId] = useState<string | null>(null);
    const [activeAvailableHarnessKey, setActiveAvailableHarnessKey] = useState<string | null>(null);
    const [activeLocalRuntimeSetupKey, setActiveLocalRuntimeSetupKey] = useState<string | null>(null);
    const [activeCustomProviderKind, setActiveCustomProviderKind] = useState<CustomProviderKind | null>(null);
    const [pendingRuntime, setPendingRuntime] = useState<AgentRuntimeConfig | null>(null);
    const [creatingHarnessKey, setCreatingHarnessKey] = useState<string | null>(null);
    const [localRuntimeScope, setLocalRuntimeScope] = useState<RuntimeProfileScope>(RuntimeProfileScope.ORGANIZATION);
    const [availableHarnessModelSelections, setAvailableHarnessModelSelections] = useState<Record<string, string>>({});
    const [isCreatingCustomProvider, setIsCreatingCustomProvider] = useState(false);
    const [customRuntimeName, setCustomRuntimeName] = useState('');
    const [customBaseUrl, setCustomBaseUrl] = useState('');
    const [customApiKey, setCustomApiKey] = useState('');
    const [customModelNames, setCustomModelNames] = useState('');
    const [customDefaultModelName, setCustomDefaultModelName] = useState('');
    const [createdProfiles, setCreatedProfiles] = useState<AgentRuntimeProfileResponse[]>([]);
    const createAgentRuntime = useCreateAgentRuntime();
    const isAddOnlyMode = variant === 'list';
    const runtimeCatalog = useMemo<AgentRuntimeProfileListResponse | undefined>(() => {
        if (createdProfiles.length === 0) return catalog;
        const existingIds = new Set((catalog?.items ?? []).map((profile) => profile.id));
        const newProfiles = createdProfiles.filter((profile) => !existingIds.has(profile.id));
        if (newProfiles.length === 0) return catalog;
        return {
            default_runtime: catalog?.default_runtime ?? {
                profile_id: newProfiles[0].id,
                model_name: newProfiles[0].default_model_name ?? null,
            },
            items: [...(catalog?.items ?? []), ...newProfiles],
        };
    }, [catalog, createdProfiles]);
    const fallbackRuntime = defaultRuntime ?? firstRuntime(runtimeCatalog);
    const selectedRuntime = value ?? fallbackRuntime;
    const selectedProfile = findProfileByRuntime(runtimeCatalog, selectedRuntime);
    const selectedLogo = harnessLogo(selectedProfile?.derived_harness_kind);
    const knownModels = runtimeModels(selectedProfile, availableHarnesses);
    const configuredDaemonHarnessKeys = new Set(
        (runtimeCatalog?.items ?? []).map(runtimeProfileDaemonKey).filter(Boolean)
    );
    const configuredHarnessKinds = new Set(
        (runtimeCatalog?.items ?? [])
            .filter((profile) => runtimeProfileDaemonKey(profile) === null)
            .map((profile) => profile.derived_harness_kind)
    );
    const discoveredLocalHarnesses = (availableHarnesses?.items ?? []).filter((harness) =>
        harness.harness_kind !== 'LEMMA'
    );
    const availableLocalHarnesses = discoveredLocalHarnesses.filter((harness) =>
        isHarnessAvailable(harness)
        && !configuredDaemonHarnessKeys.has(availableHarnessKey(harness))
        && !configuredHarnessKinds.has(harness.harness_kind)
    );
    const unavailableLocalRuntimes = LOCAL_RUNTIME_SETUP_OPTIONS.map((option): LocalRuntimeSetupOption | null => {
        const savedProfile = (runtimeCatalog?.items ?? []).find((profile) =>
            profile.derived_harness_kind === option.harnessKind
            && profile.daemon_id
        );
        const discoveredHarness = discoveredLocalHarnesses.find((harness) =>
            harness.harness_kind === option.harnessKind
        );
        const hasUnsavedAvailableHarness = availableLocalHarnesses.some((harness) =>
            harness.harness_kind === option.harnessKind
        );
        if (
            hasUnsavedAvailableHarness
            || savedProfile?.availability_status === 'READY'
            || (!savedProfile && discoveredHarness && isHarnessAvailable(discoveredHarness))
        ) {
            return null;
        }
        if (savedProfile) {
            return {
                harnessKind: option.harnessKind,
                title: option.title,
                statusLabel: runtimeAvailabilityLabel(savedProfile) === 'Offline'
                    ? 'Offline'
                    : 'Not configured',
                daemonDisplayName: savedProfile.daemon_display_name,
            };
        }
        if (discoveredHarness && !isHarnessAvailable(discoveredHarness)) {
            return {
                harnessKind: option.harnessKind,
                title: option.title,
                statusLabel: availableHarnessStatusLabel(discoveredHarness) === 'Offline'
                    ? 'Offline'
                    : 'Not configured',
                daemonDisplayName: discoveredHarness.daemon_display_name,
            };
        }
        return {
            harnessKind: option.harnessKind,
            title: option.title,
            statusLabel: 'Offline',
        };
    }).filter((option): option is LocalRuntimeSetupOption => Boolean(option));
    const filteredUnavailableLocalRuntimes = unavailableLocalRuntimes.filter((option) =>
        [
            option.title,
            option.harnessKind,
            option.statusLabel,
            option.daemonDisplayName,
        ].filter(Boolean).join(' ').toLowerCase().includes(query.trim().toLowerCase())
    );
    const canEdit = !disabled && !isLoading;
    const chooseModels = selectionMode === 'model';
    const fieldLabel = label ?? (chooseModels ? 'Model' : 'Agent Runtime');
    const showFreeformModel = chooseModels && selectedRuntime && selectedProfile && knownModels.length === 0;
    const displayRuntime = allowDefault && !value && fallbackRuntime
        ? `Default · ${formatAgentRuntime(fallbackRuntime, runtimeCatalog, { includeModel: chooseModels })}`
        : selectedRuntime
            ? formatAgentRuntime(selectedRuntime, runtimeCatalog, { includeModel: chooseModels })
            : chooseModels ? 'Choose model' : 'Choose Agent Runtime';
    const pendingKey = allowDefault && !pendingRuntime
        ? DEFAULT_VALUE
        : pendingRuntime
            ? runtimeKey(pendingRuntime)
            : '';
    const filteredHarnesses = useMemo(() => {
        const normalizedQuery = query.trim().toLowerCase();
        return (runtimeCatalog?.items ?? []).map((profile) => {
            const models = runtimeModels(profile, availableHarnesses);
            const profileMatches = [
                profile.name,
                profile.id,
                profile.description,
                profile.derived_harness_kind,
                profile.protocol,
            ].filter(Boolean).join(' ').toLowerCase().includes(normalizedQuery);
            const matchingModels = normalizedQuery && !profileMatches
                ? models.filter((modelName) =>
                    [
                        profile.name,
                        profile.id,
                        profile.derived_harness_kind,
                        modelName.name,
                        modelName.display_name,
                        modelName.provider_model_name,
                        shortModelName(modelName.name),
                    ].filter(Boolean).join(' ')
                        .toLowerCase()
                        .includes(normalizedQuery)
                )
                : models;
            return {
                ...profile,
                models: matchingModels,
            };
        }).filter((profile) => profile.models.length > 0 || [
            profile.name,
            profile.id,
            profile.derived_harness_kind,
            profile.protocol,
        ].filter(Boolean).join(' ').toLowerCase().includes(normalizedQuery));
    }, [availableHarnesses, runtimeCatalog?.items, query]);
    const filteredAvailableHarnesses = useMemo(() => {
        const normalizedQuery = query.trim().toLowerCase();
        return availableLocalHarnesses.map((harness) => {
            const models = harnessModelOptions(harness);
            const harnessMatches = [
                harness.display_name,
                harness.harness_kind,
            ].filter(Boolean).join(' ').toLowerCase().includes(normalizedQuery);
            const matchingModels = normalizedQuery && !harnessMatches
                ? models.filter((model) =>
                    [
                        harness.display_name,
                        harness.harness_kind,
                        model.name,
                        shortModelName(model.name),
                    ].filter(Boolean).join(' ').toLowerCase().includes(normalizedQuery)
                )
                : models;
            return {
                ...harness,
                models: matchingModels,
            };
        }).filter((harness) => harness.models.length > 0 || [
            harness.display_name,
            harness.harness_kind,
        ].filter(Boolean).join(' ').toLowerCase().includes(normalizedQuery));
    }, [availableLocalHarnesses, query]);
    const activeLocalRuntimeSetup = filteredUnavailableLocalRuntimes.find((option) =>
        option.harnessKind === activeLocalRuntimeSetupKey
    ) ?? (
        !activeProfileId
        && !activeAvailableHarnessKey
        && !activeCustomProviderKind
        && (!isAddOnlyMode || filteredAvailableHarnesses.length === 0)
            ? filteredUnavailableLocalRuntimes[0]
            : undefined
    );
    const activeHarness = activeLocalRuntimeSetup
        ? undefined
        : isAddOnlyMode
            ? undefined
            : filteredHarnesses.find((profile) => profile.id === activeProfileId)
            ?? filteredHarnesses.find((profile) => profile.id === pendingRuntime?.profile_id)
            ?? filteredHarnesses[0];
    const activeAvailableHarness = activeProfileId || activeLocalRuntimeSetup
        ? undefined
        : filteredAvailableHarnesses.find((harness) => availableHarnessKey(harness) === activeAvailableHarnessKey)
            ?? (!activeHarness ? filteredAvailableHarnesses[0] : undefined);
    const activeAvailableHarnessKeyValue = activeAvailableHarness
        ? availableHarnessKey(activeAvailableHarness)
        : null;
    const activeAvailableHarnessModelName = activeAvailableHarness && activeAvailableHarnessKeyValue
        ? availableHarnessModelSelections[activeAvailableHarnessKeyValue] ?? firstHarnessModelName(activeAvailableHarness) ?? null
        : null;
    const activeHarnessAvailabilityLabel = activeHarness ? runtimeAvailabilityLabel(activeHarness) : null;
    const activeHarnessUnavailableOption = activeHarness && activeHarnessAvailabilityLabel
        ? {
            harnessKind: activeHarness.derived_harness_kind,
            title: LOCAL_RUNTIME_SETUP_OPTIONS.find((option) =>
                option.harnessKind === activeHarness.derived_harness_kind
            )?.title ?? activeHarness.name,
            statusLabel: activeHarnessAvailabilityLabel === 'Offline' ? 'Offline' : 'Not configured',
            daemonDisplayName: activeHarness.daemon_display_name,
        }
        : undefined;
    const activeCustomProvider = activeCustomProviderKind
        ? CUSTOM_PROVIDER_OPTIONS.find((option) => option.kind === activeCustomProviderKind)
        : undefined;
    const showDetailPane = chooseModels
        || Boolean(activeCustomProvider)
        || Boolean(activeAvailableHarness)
        || Boolean(activeLocalRuntimeSetup)
        || Boolean(activeHarnessUnavailableOption);

    const openPicker = () => {
        const runtimeForDraft = allowDefault && !value ? null : selectedRuntime;
        setPendingRuntime(runtimeForDraft);
        setActiveProfileId(isAddOnlyMode ? null : runtimeForDraft?.profile_id ?? runtimeCatalog?.items?.[0]?.id ?? null);
        setActiveAvailableHarnessKey(null);
        setActiveLocalRuntimeSetupKey(null);
        setActiveCustomProviderKind(null);
        setQuery('');
        setIsOpen(true);
    };

    const selectRuntime = (nextRuntime: AgentRuntimeConfig | null) => {
        if (variant === 'compact') {
            onChange(nextRuntime);
            onCommit?.(nextRuntime);
            closePicker();
            return;
        }
        setPendingRuntime(nextRuntime);
        void nextRuntime;
    };

    const selectAgentRuntime = (profile: AgentRuntimeProfileResponse) => {
        const nextRuntime = chooseModels
            ? defaultAgentRuntimeFromProfile(profile, availableHarnesses)
            : { profile_id: profile.id, model_name: null };
        selectRuntime(nextRuntime);
    };

    const createAndSelectAvailableHarness = async (
        harness: AgentHarnessInfo | AvailableHarnessOption,
        modelName?: string | null,
    ) => {
        if (!organizationId) {
            toast.error('Choose an organization before adding an Agent Runtime');
            return;
        }
        if (!harness.daemon_id) {
            toast.error('Start the Lemma daemon before adding this Agent Runtime');
            return;
        }
        setCreatingHarnessKey(availableHarnessKey(harness));
        try {
            const runtimeProfile = await createAgentRuntime.mutateAsync({
                organizationId,
                request: {
                    source: 'USER_DAEMON',
                    daemon_id: harness.daemon_id,
                    harness_kind: harness.harness_kind,
                    scope: localRuntimeScope,
                    name: `${harness.display_name} daemon`,
                    default_model_name: modelName || firstHarnessModelName(harness) || undefined,
                },
            });
            const nextRuntime = {
                profile_id: runtimeProfile.id,
                model_name: chooseModels ? modelName ?? runtimeProfile.default_model_name ?? null : null,
            };
            toast.success(`${harness.display_name} Agent Runtime added`);
            setCreatedProfiles((current) => [...current.filter((profile) => profile.id !== runtimeProfile.id), runtimeProfile]);
            if (isAddOnlyMode) {
                await onRefresh?.();
                closePicker();
                return;
            }
            setActiveProfileId(runtimeProfile.id);
            setActiveAvailableHarnessKey(null);
            setActiveLocalRuntimeSetupKey(null);
            setActiveCustomProviderKind(null);
            selectRuntime(nextRuntime);
        } catch (error) {
            toast.error(`Failed to add ${harness.display_name}: ${error instanceof Error ? error.message : 'Unknown error'}`);
        } finally {
            setCreatingHarnessKey(null);
        }
    };

    const selectCustomProvider = (kind: CustomProviderKind) => {
        const provider = CUSTOM_PROVIDER_OPTIONS.find((option) => option.kind === kind);
        setActiveProfileId(null);
        setActiveAvailableHarnessKey(null);
        setActiveLocalRuntimeSetupKey(null);
        setActiveCustomProviderKind(kind);
        setCustomRuntimeName((current) => current || provider?.title || '');
        setCustomBaseUrl((current) => current || provider?.defaultBaseUrl || '');
    };

    const createAndSelectCustomProvider = async () => {
        if (!organizationId) {
            toast.error('Choose an organization before adding an Agent Runtime');
            return;
        }
        if (!activeCustomProviderKind) return;
        const name = customRuntimeName.trim();
        const baseUrl = customBaseUrl.trim();
        const apiKey = customApiKey.trim();
        const modelNames = splitModelNames(customModelNames);
        const defaultModelName = customDefaultModelName.trim() || modelNames[0] || undefined;
        if (!name) {
            toast.error('Name this Agent Runtime');
            return;
        }
        if (activeCustomProviderKind === 'openai' && !baseUrl) {
            toast.error('Enter the provider base URL');
            return;
        }
        if (activeCustomProviderKind === 'anthropic' && !apiKey) {
            toast.error('Enter the API key');
            return;
        }
        setIsCreatingCustomProvider(true);
        try {
            const runtimeProfile = await createAgentRuntime.mutateAsync({
                organizationId,
                request: activeCustomProviderKind === 'openai'
                    ? {
                        source: 'OPENAI_COMPATIBLE',
                        name,
                        base_url: baseUrl,
                        api_key: apiKey || null,
                        default_model_name: defaultModelName,
                        model_names: modelNames,
                    }
                    : {
                        source: 'ANTHROPIC_COMPATIBLE',
                        name,
                        base_url: baseUrl || null,
                        api_key: apiKey,
                        default_model_name: defaultModelName,
                        model_names: modelNames,
                    },
            });
            toast.success(`${runtimeProfile.name} saved`);
            setCreatedProfiles((current) => [...current.filter((profile) => profile.id !== runtimeProfile.id), runtimeProfile]);
            if (isAddOnlyMode) {
                await onRefresh?.();
                closePicker();
                return;
            }
            setActiveProfileId(runtimeProfile.id);
            setActiveAvailableHarnessKey(null);
            setActiveLocalRuntimeSetupKey(null);
            setActiveCustomProviderKind(null);
        } catch (error) {
            toast.error(`Failed to create Agent Runtime: ${error instanceof Error ? error.message : 'Unknown error'}`);
        } finally {
            setIsCreatingCustomProvider(false);
        }
    };

    const closePicker = () => {
        setIsOpen(false);
        setQuery('');
        setActiveProfileId(null);
        setActiveAvailableHarnessKey(null);
        setActiveLocalRuntimeSetupKey(null);
        setActiveCustomProviderKind(null);
        setPendingRuntime(null);
    };

    const commitRuntime = () => {
        if (!allowDefault && !pendingRuntime) return;
        onChange(pendingRuntime);
        onCommit?.(pendingRuntime);
        closePicker();
    };

    const handleModelChange = (modelName: string) => {
        if (!selectedRuntime) return;
        onChange({
            profile_id: selectedRuntime.profile_id,
            model_name: modelName,
        });
    };

    const compactModelLabel = selectedRuntime?.model_name
        ? shortModelName(selectedRuntime.model_name)
        : fallbackRuntime?.model_name
            ? shortModelName(fallbackRuntime.model_name)
            : 'Auto';
    const compactProfileLabel = selectedProfile?.name
        ?? findProfileByRuntime(runtimeCatalog, fallbackRuntime)?.name
        ?? null;

    return (
        <div className={variant === 'compact' ? "min-w-0" : "settings-field-stack gap-3"}>
            {variant === 'compact' ? (
                <button
                    type="button"
                    onClick={openPicker}
                    disabled={!canEdit}
                    className="agent-runtime-trigger-button custom-focus-ring inline-flex h-9 max-w-[16rem] items-center gap-1.5 rounded-md px-2.5 text-sm font-medium text-[var(--text-secondary)] transition-colors hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] disabled:cursor-not-allowed disabled:opacity-50"
                    title={compactProfileLabel ? `${compactProfileLabel} · ${compactModelLabel}` : compactModelLabel}
                >
                    <Zap className="h-4 w-4 shrink-0 text-[var(--text-tertiary)]" />
                    <span className="truncate text-[var(--text-primary)]">{compactModelLabel}</span>
                    <ChevronDown className="h-3.5 w-3.5 shrink-0 text-[var(--text-tertiary)]" />
                </button>
            ) : variant === 'list' ? (
                <RuntimeListView
                    canEdit={canEdit}
                    isLoading={isLoading}
                    runtimeCatalog={runtimeCatalog}
                    availableHarnesses={availableHarnesses}
                    availableLocalHarnesses={availableLocalHarnesses}
                    onAdd={openPicker}
                    onSelectAvailableHarness={(harnessKey) => {
                        setActiveProfileId(null);
                        setActiveAvailableHarnessKey(harnessKey);
                        setActiveLocalRuntimeSetupKey(null);
                        setActiveCustomProviderKind(null);
                        setPendingRuntime(null);
                        setIsOpen(true);
                    }}
                />
            ) : (
                <>
            <div className="settings-field">
                <button
                    type="button"
                    onClick={openPicker}
                    disabled={!canEdit}
                    className="agent-runtime-trigger-button group flex min-h-16 w-full items-center justify-between gap-4 rounded-lg bg-[color:color-mix(in_srgb,var(--surface-2)_40%,transparent)] px-3.5 py-3 text-left text-sm transition-gentle hover:bg-[color:color-mix(in_srgb,var(--surface-2)_62%,transparent)] disabled:cursor-not-allowed disabled:opacity-50"
                >
                    <RuntimeMark selected={Boolean(selectedRuntime)} logo={selectedLogo} />
                    <span className="min-w-0 flex-1">
                        <span className="block text-xs font-medium uppercase tracking-wider text-[var(--text-tertiary)]">{fieldLabel}</span>
                        <span className="mt-1 block truncate text-sm font-semibold text-[var(--text-primary)]">
                            {isLoading ? (chooseModels ? 'Loading models' : 'Loading Agent Runtimes') : displayRuntime}
                        </span>
                        {selectedRuntime?.model_name && shortModelName(selectedRuntime.model_name) !== selectedRuntime.model_name ? (
                            <span className="mt-0.5 block truncate font-mono text-xs text-[var(--text-tertiary)]">
                                {selectedRuntime.model_name}
                            </span>
                        ) : null}
                    </span>
                    <span className="shrink-0 rounded-md px-2.5 py-1.5 text-xs font-medium text-[var(--text-secondary)] transition-gentle group-hover:bg-[color:color-mix(in_srgb,var(--surface-1)_64%,transparent)] group-hover:text-[var(--text-primary)]">
                        Change
                    </span>
                </button>
                {description ? (
                    <p className="settings-help-text">{description}</p>
                ) : null}
            </div>

            {showFreeformModel ? (
                <div className="settings-field">
                    <Label className="text-[var(--text-secondary)]">Model name</Label>
                    <Input
                        value={selectedRuntime.model_name ?? ''}
                        onChange={(event) => handleModelChange(event.target.value)}
                        disabled={disabled || isLoading}
                        placeholder="Model identifier"
                    />
                </div>
            ) : null}

            {isLoading ? (
                <div className="flex items-center gap-2 text-sm text-[var(--text-tertiary)]">
                    <Loader2 className="h-3.5 w-3.5 animate-spin" />
                    {chooseModels ? 'Loading model options' : 'Loading Agent Runtimes'}
                </div>
            ) : null}

            {!isLoading && !runtimeCatalog?.items?.length ? (
                <div className="state-surface-warning rounded-md px-3 py-2 text-sm text-[var(--text-secondary)]">
                    No Agent Runtimes are saved yet. Run the local daemon to use Codex, Claude Code, or OpenCode here.
                </div>
            ) : null}

            {fallbackRuntime && allowDefault && !value ? (
                <div className="chip chip-md chip-muted w-fit">
                    Uses {formatAgentRuntime(fallbackRuntime, runtimeCatalog, { includeModel: chooseModels })}
                </div>
            ) : null}
                </>
            )}

            <Dialog
                open={isOpen}
                onOpenChange={(nextOpen) => {
                    if (nextOpen) openPicker();
                    else closePicker();
                }}
            >
                <DialogContent className="flex h-[min(600px,calc(100vh-40px))] max-h-[calc(100vh-40px)] w-[min(760px,calc(100vw-32px))] max-w-none grid-rows-none flex-col gap-0 overflow-hidden p-0">
                    <DialogHeader className="shrink-0 border-b border-[var(--border-subtle)] px-5 py-4 pr-12">
                        <div className="min-w-0">
                            <DialogTitle>{isAddOnlyMode ? 'Add Agent Runtime' : chooseModels ? 'Choose model' : 'Choose Agent Runtime'}</DialogTitle>
                            <DialogDescription>
                                {isAddOnlyMode
                                    ? 'Save a detected local harness or add a custom provider route.'
                                    : chooseModels
                                    ? 'Pick an Agent Runtime, then choose the model.'
                                    : 'Add or change a saved harness for this workspace.'}
                            </DialogDescription>
                        </div>
                    </DialogHeader>

                    <div className="shrink-0 border-b border-[var(--border-subtle)] px-5 py-3">
                        <div className="flex h-9 items-center gap-2 rounded-md border border-[var(--field-border)] bg-[var(--field-bg)] px-3 focus-within:border-[var(--field-border-focus)]">
                            <Search className="h-4 w-4 shrink-0 text-[var(--text-tertiary)]" />
                            <input
                                value={query}
                                onChange={(event) => setQuery(event.target.value)}
                                placeholder={isAddOnlyMode ? 'Search detected harnesses or providers' : chooseModels ? 'Search Agent Runtime or model' : 'Search Agent Runtime'}
                                className="inline-edit-field h-full min-w-0 flex-1 bg-transparent text-sm text-[var(--text-primary)] outline-none placeholder:text-[var(--text-tertiary)]"
                            />
                        </div>
                    </div>

                    <div className={cn(
                        'grid min-h-0 flex-1 grid-cols-1 overflow-hidden',
                        showDetailPane && 'sm:grid-cols-[220px_minmax(0,1fr)]'
                    )}>
                        <div className={cn(
                            'min-h-0 overflow-y-auto bg-[var(--surface-2)] p-2',
                            showDetailPane && 'border-b border-[var(--border-subtle)] sm:border-b-0 sm:border-r'
                        )}>
                            <div className="space-y-1">
                                {allowDefault && fallbackRuntime ? (
                                    <HarnessChoiceRow
                                        title="Use default"
                                        subtitle={formatAgentRuntime(fallbackRuntime, runtimeCatalog, { includeModel: chooseModels })}
                                        selected={pendingKey === DEFAULT_VALUE}
                                        active={pendingKey === DEFAULT_VALUE}
                                        onClick={() => {
                                            setActiveLocalRuntimeSetupKey(null);
                                            selectRuntime(null);
                                        }}
                                    />
                                ) : null}

                                {!isAddOnlyMode && filteredHarnesses.map((profile) => {
                                    const profileIsSelected = pendingRuntime?.profile_id === profile.id;
                                    const availabilityLabel = runtimeAvailabilityLabel(profile);
                                    return (
                                        <HarnessChoiceRow
                                            key={profile.id}
                                            title={profile.name}
                                            subtitle={profileIsSelected && pendingRuntime?.model_name
                                                ? shortModelName(pendingRuntime.model_name ?? '')
                                                : `${profile.models?.length ?? 0} model${profile.models?.length === 1 ? '' : 's'}`}
                                            selected={profileIsSelected}
                                            active={activeHarness?.id === profile.id}
                                            logo={harnessLogo(profile.derived_harness_kind)}
                                            trailing={availabilityLabel ? (
                                                <span className="chip chip-sm chip-pill state-badge-warning">{availabilityLabel}</span>
                                            ) : null}
                                            onClick={() => {
                                                setActiveProfileId(profile.id);
                                                setActiveAvailableHarnessKey(null);
                                                setActiveLocalRuntimeSetupKey(null);
                                                setActiveCustomProviderKind(null);
                                                if (!chooseModels) selectAgentRuntime(profile);
                                            }}
                                        />
                                    );
                                })}

                                {filteredAvailableHarnesses.map((harness) => {
                                    const harnessKey = availableHarnessKey(harness);
                                    const active = activeAvailableHarness ? availableHarnessKey(activeAvailableHarness) === harnessKey : false;
                                    const isCreating = creatingHarnessKey === harnessKey;
                                    return (
                                        <HarnessChoiceRow
                                            key={`available-${harnessKey}`}
                                            title={harness.display_name}
                                            subtitle={`${harness.models?.length ?? 0} model${harness.models?.length === 1 ? '' : 's'} from ${harness.daemon_display_name ?? 'local daemon'}`}
                                            selected={false}
                                            active={active}
                                            logo={harnessLogo(harness.harness_kind)}
                                            trailing={isCreating
                                                ? <Loader2 className="h-3.5 w-3.5 animate-spin text-[var(--text-tertiary)]" />
                                                : <span className="chip chip-sm chip-pill chip-muted">Detected</span>}
                                            onClick={() => {
                                                setActiveProfileId(null);
                                                setActiveAvailableHarnessKey(harnessKey);
                                                setActiveLocalRuntimeSetupKey(null);
                                                setActiveCustomProviderKind(null);
                                            }}
                                        />
                                    );
                                })}

                                {filteredUnavailableLocalRuntimes.map((option) => (
                                    <HarnessChoiceRow
                                        key={`local-runtime-setup-${option.harnessKind}`}
                                        title={option.title}
                                        subtitle={option.daemonDisplayName ?? 'Local runtime'}
                                        selected={false}
                                        active={activeLocalRuntimeSetup?.harnessKind === option.harnessKind}
                                        logo={harnessLogo(option.harnessKind)}
                                        trailing={<span className="chip chip-sm chip-pill state-badge-warning">{option.statusLabel}</span>}
                                        onClick={() => {
                                            setActiveProfileId(null);
                                            setActiveAvailableHarnessKey(null);
                                            setActiveLocalRuntimeSetupKey(option.harnessKind);
                                            setActiveCustomProviderKind(null);
                                        }}
                                    />
                                ))}

                                {CUSTOM_PROVIDER_OPTIONS.map((provider) => {
                                    const providerMatches = [
                                        provider.title,
                                        provider.subtitle,
                                    ].join(' ').toLowerCase().includes(query.trim().toLowerCase());
                                    if (query.trim() && !providerMatches) return null;
                                    return (
                                        <HarnessChoiceRow
                                            key={`custom-${provider.kind}`}
                                            title={provider.title}
                                            subtitle={provider.subtitle}
                                            selected={false}
                                            active={activeCustomProviderKind === provider.kind}
                                            onClick={() => selectCustomProvider(provider.kind)}
                                        />
                                    );
                                })}
                            </div>
                        </div>

                        {showDetailPane ? (
                        <div className="min-h-0 overflow-y-auto p-3">
                            {activeCustomProvider ? (
                                <CustomProviderForm
                                    providerTitle={activeCustomProvider.title}
                                    providerKind={activeCustomProvider.kind}
                                    name={customRuntimeName}
                                    baseUrl={customBaseUrl}
                                    apiKey={customApiKey}
                                    modelNames={customModelNames}
                                    defaultModelName={customDefaultModelName}
                                    isSaving={isCreatingCustomProvider}
                                    onNameChange={setCustomRuntimeName}
                                    onBaseUrlChange={setCustomBaseUrl}
                                    onApiKeyChange={setCustomApiKey}
                                    onModelNamesChange={setCustomModelNames}
                                    onDefaultModelNameChange={setCustomDefaultModelName}
                                    onSubmit={createAndSelectCustomProvider}
                                />
                            ) : (activeLocalRuntimeSetup || activeHarnessUnavailableOption) ? (
                                <LocalRuntimeUnavailableDetail
                                    option={(activeLocalRuntimeSetup ?? activeHarnessUnavailableOption)!}
                                    isRefreshing={isRefreshing}
                                    onRefresh={onRefresh}
                                />
                            ) : activeAvailableHarness ? (
                                <AvailableHarnessDetail
                                    harness={activeAvailableHarness}
                                    localRuntimeScope={localRuntimeScope}
                                    activeModelName={activeAvailableHarnessModelName}
                                    isSettingUp={creatingHarnessKey === availableHarnessKey(activeAvailableHarness)}
                                    isPending={createAgentRuntime.isPending}
                                    onScopeChange={setLocalRuntimeScope}
                                    onSelectModel={(modelName) => {
                                        if (!activeAvailableHarnessKeyValue) return;
                                        setAvailableHarnessModelSelections((current) => ({
                                            ...current,
                                            [activeAvailableHarnessKeyValue]: modelName,
                                        }));
                                    }}
                                    onSave={() => {
                                        void createAndSelectAvailableHarness(activeAvailableHarness, activeAvailableHarnessModelName);
                                    }}
                                />
                            ) : chooseModels && activeHarness ? (
                                <HarnessModelList
                                    harness={activeHarness}
                                    pendingRuntime={pendingRuntime}
                                    pendingKey={pendingKey}
                                    onSelectRuntime={selectRuntime}
                                />
                            ) : chooseModels ? (
                                <div className="state-surface-warning rounded-md px-3 py-3 text-sm text-[var(--text-secondary)]">
                                    No models match that search.
                                </div>
                            ) : null}
                        </div>
                        ) : null}
                    </div>

                    {variant === 'compact' || isAddOnlyMode ? null : (
                        <DialogFooter className="shrink-0 border-t border-[var(--border-subtle)] bg-[var(--surface-1)] px-5 py-3">
                            <Button type="button" variant="ghost" size="sm" onClick={closePicker}>
                                Cancel
                            </Button>
                            <Button
                                type="button"
                                size="sm"
                                onClick={commitRuntime}
                                disabled={commitLoading || (!allowDefault && !pendingRuntime)}
                                loading={commitLoading}
                            >
                                {commitLabel}
                            </Button>
                        </DialogFooter>
                    )}
                </DialogContent>
            </Dialog>
        </div>
    );
}
