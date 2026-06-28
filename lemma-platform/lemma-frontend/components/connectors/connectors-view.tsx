'use client';

import {
    useAccounts,
    useConnectors,
    useAuthConfigs,
    useCreateConnectRequest,
    useCreateConnectorAccount,
    useDeleteAccount,
    useEnableConnector
} from '@/lib/hooks/use-connectors';
import { Button } from '@/components/ui/button';
import { EmptyState } from '@/components/shared/empty-state';
import { DestructiveConfirmationDialog } from '@/components/shared/destructive-confirmation-dialog';
import { DestructiveResourceActionItem, ResourceActionsMenu } from '@/components/shared/resource-actions-menu';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Label } from '@/components/ui/label';
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Checkbox } from '@/components/ui/checkbox';
import { Switch, SwitchThumb, SwitchTrack } from '@/components/ui/switch';
import { Plug, ExternalLink, CheckCircle2, Search, Loader2 } from 'lucide-react';
import Image from 'next/image';
import { useMemo, useState } from 'react';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { toast } from 'sonner';
import type { Connector } from '@/lib/types';
import { useOrganization } from '@/components/dashboard/org-context';
import {
    buildSchemaFormFields,
    buildSchemaFormPayload,
    buildSchemaFormValues,
    type JsonSchemaLike,
    type SchemaFormField
} from 'lemma-sdk';

type AuthConfigMode = 'MANAGED' | 'CUSTOM';
type ProviderCapability = NonNullable<Connector['provider_capabilities']>[number];
type SchemaValues = Record<string, unknown>;

const isRecord = (value: unknown): value is Record<string, unknown> =>
    Boolean(value && typeof value === 'object' && !Array.isArray(value));

const getAppLabel = (app: Connector | null | undefined) => app?.title || app?.name || app?.id || 'this app';

const getProviderCapabilities = (app: Connector | null | undefined): ProviderCapability[] => {
    return (app?.provider_capabilities || []) as ProviderCapability[];
};

const getSupportedProviders = (app: Connector): string[] => {
    const providers = getProviderCapabilities(app)
        .map((capability) => capability.provider)
        .filter((provider): provider is string => typeof provider === 'string');
    return providers.length > 0 ? providers : ['LEMMA'];
};

const getPreferredProvider = (app: Connector): string => {
    const providers = getSupportedProviders(app);
    return providers[0] || 'LEMMA';
};

const getProviderCapability = (app: Connector | null | undefined, provider: string): ProviderCapability | null => {
    return getProviderCapabilities(app).find((capability) => capability.provider === provider) ?? null;
};

const getAuthConfigSchema = (capability: ProviderCapability | null): JsonSchemaLike | null => {
    const schema = capability?.auth_config_schema;
    return isRecord(schema) ? schema as JsonSchemaLike : null;
};

const getCredentialSchema = (capability: ProviderCapability | null): JsonSchemaLike | null => {
    if (!capability || !('credential_schema' in capability)) return null;
    const schema = capability.credential_schema;
    return isRecord(schema) ? schema as JsonSchemaLike : null;
};

const schemaHasFields = (schema: JsonSchemaLike | null): boolean =>
    buildSchemaFormFields(schema).length > 0;

const hasSystemDefault = (capability: ProviderCapability | null): boolean =>
    Boolean(capability?.system_default_available);

const supportsCustomConfig = (capability: ProviderCapability | null): boolean => {
    if (!capability) return false;
    const hasConfigFields = schemaHasFields(getAuthConfigSchema(capability));
    if ('supports_org_custom_oauth' in capability) return Boolean(capability.supports_org_custom_oauth && hasConfigFields);
    if ('supports_org_custom_auth_config' in capability) return Boolean(capability.supports_org_custom_auth_config && hasConfigFields);
    return hasConfigFields;
};

const usesDirectCredentials = (capability: ProviderCapability | null): boolean =>
    Boolean(getCredentialSchema(capability) || capability?.auth_scheme === 'API_KEY');

const formatProviderName = (provider: string): string => {
    if (provider === 'LEMMA') return 'OAuth';
    if (provider === 'COMPOSIO') return 'Composio';
    return provider
        .toLowerCase()
        .split('_')
        .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
        .join(' ');
};

const getProviderLabel = (provider: string, capability: ProviderCapability | null): string => {
    if (provider === 'LEMMA' && usesDirectCredentials(capability)) return 'Credentials';
    if (provider === 'LEMMA') return 'OAuth';
    return formatProviderName(provider);
};

const getProviderDescription = (provider: string, capability: ProviderCapability | null): string => {
    if (usesDirectCredentials(capability)) return 'Connect with credentials from this app, such as an API key or bot token.';
    if (provider === 'COMPOSIO') return 'Use Composio-managed auth for trigger-backed workflows.';
    if (provider === 'LEMMA') return 'Use OAuth with Lemma-managed or organization-managed credentials.';
    return 'Use this provider for the connector connection.';
};

const getManagedConfigCopy = (provider: string, capability: ProviderCapability | null): string => {
    if (usesDirectCredentials(capability)) return 'Use the default credential setup for this app. Account credentials are added after enabling it.';
    if (provider === 'COMPOSIO') return 'Composio uses the system default configuration and supports triggers.';
    if (provider === 'LEMMA') return 'Use the system default OAuth configuration for this app.';
    return `Use the default ${formatProviderName(provider)} auth configuration for this app.`;
};

interface ConnectorsViewProps {
    organizationId?: string;
    organizationName?: string;
    embedded?: boolean;
    showHeader?: boolean;
}

export function ConnectorsView({ organizationId, organizationName, embedded = false, showHeader = true }: ConnectorsViewProps) {
    const { currentOrg, organizations } = useOrganization();
    const effectiveOrganizationId = organizationId || currentOrg?.id;
    const effectiveOrganizationName =
        organizationName ||
        organizations.find((org) => org.id === effectiveOrganizationId)?.name ||
        currentOrg?.name;
    const { data: accounts, isLoading: isLoadingAccounts } = useAccounts({ organizationId: effectiveOrganizationId, limit: 200 });
    const { data: authConfigs, isLoading: isLoadingAuthConfigs } = useAuthConfigs({ organizationId: effectiveOrganizationId, limit: 200 });
    const { data: connectors, isLoading: isLoadingApps } = useConnectors({ limit: 200 });
    const deleteAccount = useDeleteAccount(effectiveOrganizationId);
    const enableConnector = useEnableConnector(effectiveOrganizationId);
    const createConnectRequest = useCreateConnectRequest(effectiveOrganizationId);
    const createConnectorAccount = useCreateConnectorAccount(effectiveOrganizationId);
    const [searchTerm, setSearchTerm] = useState('');
    const [connectingAppId, setConnectingAppId] = useState<string | null>(null);
    const [enablingAppId, setEnablingAppId] = useState<string | null>(null);
    const [deletingAccountId, setDeletingAccountId] = useState<string | null>(null);
    const [authConfigApp, setAuthConfigApp] = useState<Connector | null>(null);
    const [authConfigMode, setAuthConfigMode] = useState<AuthConfigMode>('MANAGED');
    const [authConfigProvider, setAuthConfigProvider] = useState('LEMMA');
    const [showCustomConfigForm, setShowCustomConfigForm] = useState(false);
    const [authConfigValues, setAuthConfigValues] = useState<SchemaValues>({});
    const [customConfigName, setCustomConfigName] = useState('');
    const [credentialApp, setCredentialApp] = useState<Connector | null>(null);
    const [credentialValues, setCredentialValues] = useState<SchemaValues>({});
    const [accountPendingDisconnect, setAccountPendingDisconnect] = useState<{
        id: string;
        appName: string;
        accountLabel: string;
    } | null>(null);

    const enabledConfigByAppId = useMemo(() => {
        return new Map((authConfigs || [])
            .filter((config) => config.status === 'ACTIVE')
            .map((config) => [config.connector_id, config]));
    }, [authConfigs]);

    const handleConnect = async (app: Connector) => {
        const appId = app.id;
        const authConfig = enabledConfigByAppId.get(appId);
        if (!authConfig) {
            toast.error('Enable this app before connecting an account');
            return;
        }

        const capability = getProviderCapability(app, authConfig.provider);
        const credentialSchema = getCredentialSchema(capability);
        if (usesDirectCredentials(capability) && credentialSchema) {
            setCredentialApp(app);
            setCredentialValues(buildSchemaFormValues(credentialSchema));
            return;
        }

        try {
            setConnectingAppId(appId);
            const response = await createConnectRequest.mutateAsync({
                connectorId: appId,
                authConfigId: authConfig.id,
            });
            if (response.authorization_url) {
                window.open(response.authorization_url, '_blank', 'noopener,noreferrer');
            }
        } catch (error) {
            console.error('Failed to connect:', error);
            toast.error('Failed to initiate connection');
        } finally {
            setConnectingAppId(null);
        }
    };

    const openEnableDialog = (app: Connector) => {
        const provider = getPreferredProvider(app);
        const capability = getProviderCapability(app, provider);
        setAuthConfigApp(app);
        setAuthConfigProvider(provider);
        setAuthConfigMode(hasSystemDefault(capability) ? 'MANAGED' : 'CUSTOM');
        setShowCustomConfigForm(!hasSystemDefault(capability) && supportsCustomConfig(capability));
        setAuthConfigValues(buildSchemaFormValues(getAuthConfigSchema(capability)));
        setCustomConfigName('');
    };

    const handleAuthConfigProviderChange = (provider: string) => {
        const capability = getProviderCapability(authConfigApp, provider);
        const hasDefault = hasSystemDefault(capability);
        const canUseCustom = supportsCustomConfig(capability);

        setAuthConfigProvider(provider);
        setAuthConfigMode(hasDefault ? 'MANAGED' : 'CUSTOM');
        setShowCustomConfigForm(!hasDefault && canUseCustom);
        setAuthConfigValues(buildSchemaFormValues(getAuthConfigSchema(capability)));
        setCustomConfigName('');
    };

    const handleEnableFromDialog = async () => {
        if (!authConfigApp) return;
        const capability = getProviderCapability(authConfigApp, authConfigProvider);

        try {
            setEnablingAppId(authConfigApp.id);

            if (authConfigMode === 'MANAGED') {
                if (!hasSystemDefault(capability)) {
                    toast.error(`${formatProviderName(authConfigProvider)} does not expose managed credentials for this app`);
                    return;
                }
                await enableConnector.mutateAsync({
                    connectorId: authConfigApp.id,
                    provider: authConfigProvider,
                    configSource: 'SYSTEM_DEFAULT',
                });
                toast.success('Connector enabled');
                setAuthConfigApp(null);
                return;
            }

            const schema = getAuthConfigSchema(capability);
            const payload = buildSchemaFormPayload(schema, authConfigValues);
            if (!payload.isValid) {
                toast.error(Object.values(payload.errors)[0] || 'Custom config is incomplete');
                return;
            }

            await enableConnector.mutateAsync({
                connectorId: authConfigApp.id,
                provider: authConfigProvider,
                configSource: 'ORG_CUSTOM',
                credentialConfig: payload.data,
                name: customConfigName.trim() || null,
            });
            toast.success('Connector enabled');
            setAuthConfigApp(null);
        } catch (error) {
            console.error('Failed to enable connector:', error);
            toast.error('Failed to enable connector');
        } finally {
            setEnablingAppId(null);
        }
    };

    const handleCreateCredentialAccount = async () => {
        if (!credentialApp) return;
        const authConfig = enabledConfigByAppId.get(credentialApp.id);
        if (!authConfig) {
            toast.error('Enable this app before adding credentials');
            return;
        }

        const capability = getProviderCapability(credentialApp, authConfig.provider);
        const schema = getCredentialSchema(capability);
        const payload = buildSchemaFormPayload(schema, credentialValues);
        if (!payload.isValid) {
            toast.error(Object.values(payload.errors)[0] || 'Credentials are incomplete');
            return;
        }

        try {
            setConnectingAppId(credentialApp.id);
            await createConnectorAccount.mutateAsync({
                authConfigId: authConfig.id,
                credentials: payload.data,
            });
            toast.success(`${getAppLabel(credentialApp)} connected`);
            setCredentialApp(null);
            setCredentialValues({});
        } catch (error) {
            console.error('Failed to connect credential account:', error);
            toast.error('Failed to save credentials');
        } finally {
            setConnectingAppId(null);
        }
    };

    const handleDisconnect = async () => {
        if (!accountPendingDisconnect) return;
        try {
            setDeletingAccountId(accountPendingDisconnect.id);
            await deleteAccount.mutateAsync(accountPendingDisconnect.id);
            toast.success(`${accountPendingDisconnect.appName} disconnected`);
            setAccountPendingDisconnect(null);
        } catch (error) {
            console.error('Failed to disconnect account:', error);
            toast.error('Failed to disconnect account');
        } finally {
            setDeletingAccountId(null);
        }
    };

    const connectedAppIds = useMemo(() => new Set((accounts || []).map((acc) => acc.connector_id)), [accounts]);

    const filteredApps = (connectors || []).filter(app =>
        (app.title && app.title.toLowerCase().includes(searchTerm.toLowerCase())) ||
        (app.name && app.name.toLowerCase().includes(searchTerm.toLowerCase())) ||
        (app.description && app.description.toLowerCase().includes(searchTerm.toLowerCase()))
    );
    const enabledConnectors = filteredApps.filter((app) => enabledConfigByAppId.has(app.id));
    const availableConnectors = filteredApps.filter((app) => !enabledConfigByAppId.has(app.id));
    const authConfigCapability = getProviderCapability(authConfigApp, authConfigProvider);
    const authConfigProviderLabel = getProviderLabel(authConfigProvider, authConfigCapability);
    const authConfigSchema = getAuthConfigSchema(authConfigCapability);
    const authConfigHasSystemDefault = hasSystemDefault(authConfigCapability);
    const authConfigSupportsCustom = supportsCustomConfig(authConfigCapability);
    const canEnableAuthConfig = Boolean(
        authConfigApp &&
        (
            (authConfigMode === 'MANAGED' && authConfigHasSystemDefault) ||
            (authConfigMode === 'CUSTOM' && authConfigSupportsCustom)
        )
    );
    const credentialCapability = credentialApp
        ? getProviderCapability(credentialApp, enabledConfigByAppId.get(credentialApp.id)?.provider || getPreferredProvider(credentialApp))
        : null;
    const credentialSchema = getCredentialSchema(credentialCapability);

    const renderConnectorCard = (app: Connector) => {
        const authConfig = enabledConfigByAppId.get(app.id);
        const isEnabled = Boolean(authConfig);
        const isConnected = connectedAppIds.has(app.id);
        const isBusy = enablingAppId === app.id || connectingAppId === app.id;
        const activeCapability = authConfig ? getProviderCapability(app, authConfig.provider) : null;
        const connectsWithCredentials = usesDirectCredentials(activeCapability);

        return (
            <div
                key={app.id}
                className="resource-index-card group p-4"
            >
                <div className="mb-3 flex items-start justify-between gap-3">
                    <div className="flex items-center gap-3">
                        {app.icon ? (
                            <div className="relative h-10 w-10 rounded-lg bg-transparent p-1.5">
                                <Image
                                    src={app.icon}
                                    alt={app.title || app.name || 'App'}
                                    fill
                                    className="object-contain p-1"
                                />
                            </div>
                        ) : (
                            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-[color:color-mix(in_srgb,var(--surface-2)_46%,transparent)]">
                                <Plug className="h-5 w-5 text-[var(--text-tertiary)]" />
                            </div>
                        )}
                        <div>
                            <p className="text-sm font-normal text-[var(--text-primary)]">{app.title || app.name}</p>
                        </div>
                    </div>
                    {isEnabled ? (
                        <span className="inline-flex shrink-0 items-center gap-1.5 rounded-full bg-transparent py-1 text-xs font-medium text-[var(--state-success)]">
                            <CheckCircle2 className="h-3.5 w-3.5" />
                            Enabled
                        </span>
                    ) : (
                        <Switch
                            checked={false}
                            aria-label={`Enable ${app.title || app.name || app.id}`}
                            className="flex shrink-0 items-center gap-2 rounded-full bg-transparent px-0 py-1 text-xs font-medium text-[var(--text-secondary)] transition-colors hover:text-[var(--text-primary)] disabled:cursor-default disabled:opacity-80"
                            onClick={() => openEnableDialog(app)}
                            disabled={isBusy}
                        >
                            {isBusy && !isConnected ? (
                                <Loader2 className="h-3.5 w-3.5 animate-spin" />
                            ) : (
                                <SwitchTrack>
                                    <SwitchThumb />
                                </SwitchTrack>
                            )}
                            <span>Enable</span>
                        </Switch>
                    )}
                </div>

                <p className="mb-4 min-h-[44px] line-clamp-2 text-sm leading-6 text-[var(--text-secondary)]">
                    {app.description || `Connect ${app.title || app.name} to your workflows.`}
                </p>

                {isEnabled ? (
                    <Button
                        className="w-full justify-center"
                        variant={isConnected ? 'outline' : 'primary'}
                        onClick={() => handleConnect(app)}
                        disabled={isBusy || isConnected}
                    >
                        {isBusy ? (
                            <>
                                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                                Connecting...
                            </>
                        ) : isConnected ? (
                            'Connected'
                        ) : (
                            <>
                                Connect account
                                {connectsWithCredentials ? null : <ExternalLink className="ml-2 h-4 w-4" />}
                            </>
                        )}
                    </Button>
                ) : null}
            </div>
        );
    };

    if (!effectiveOrganizationId) {
        return (
            <EmptyState
                variant="panel"
                icon={<Plug className="h-5 w-5" />}
                title="Select an organization"
                description="Connectors are enabled and connected inside an organization."
            />
        );
    }

    if (isLoadingAccounts || isLoadingApps || isLoadingAuthConfigs) {
        return (
            <div className={embedded ? "flex min-h-[30vh] items-center justify-center bg-transparent" : "context-shell flex min-h-full items-center justify-center bg-transparent pb-8"}>
                <Loader2 className="h-8 w-8 animate-spin text-[var(--text-tertiary)]" />
            </div>
        );
    }

    return (
        <div className={embedded ? "min-h-full bg-transparent" : "context-shell min-h-full bg-transparent pb-8"}>
            {showHeader ? (
                <>
                    <div className="context-header">
                        <div>
                            <p className="section-label">Connectors</p>
                            <h1 className="font-display text-4xl font-normal text-[var(--text-primary)]">Connectors</h1>
                            <p className="mt-2 max-w-2xl text-sm text-[var(--text-secondary)]">
                                Enabled connectors and connected accounts are available to you across every pod in {effectiveOrganizationName || 'this organization'}.
                            </p>
                        </div>

                        <div className="relative w-full max-w-sm">
                            <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[var(--text-tertiary)]" />
                            <Input
                                placeholder="Search apps"
                                className="pl-9"
                                value={searchTerm}
                                onChange={(e) => setSearchTerm(e.target.value)}
                            />
                        </div>
                    </div>

                    <p className="context-inline-note">
                        Enable an connector once for the organization. Each user still connects their own account per organization.
                    </p>
                </>
            ) : (
                <div className="mb-8 flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
                    <p className="max-w-2xl text-sm leading-6 text-[var(--text-secondary)]">
                        Connectors you enable, and accounts you connect, are available to you across every pod in {effectiveOrganizationName || 'this organization'}.
                    </p>
                    <div className="relative w-full max-w-sm">
                        <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[var(--text-tertiary)]" />
                        <Input
                            placeholder="Search apps"
                            className="pl-9"
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                        />
                    </div>
                </div>
            )}

            {accounts && accounts.length > 0 && (
                <section className="context-section">
                    <div className="mb-3 flex items-center gap-2">
                        <CheckCircle2 className="h-4 w-4 text-[var(--state-success)]" />
                        <h2 className="text-base font-normal text-[var(--text-primary)]">Connected accounts</h2>
                        <span className="text-xs text-[var(--text-tertiary)]">{accounts.length}</span>
                    </div>
                    <div className="resource-index-grid resource-index-grid-md-2 resource-index-grid-xl-3 grid-cols-1 md:grid-cols-2 xl:grid-cols-3">
                        {(accounts || []).map((account) => (
                            <div
                                key={account.id}
                                className="resource-index-card group p-4"
                            >
                                <div className="flex items-center justify-between">
                                    <div className="flex items-center gap-3">
                                        {account.connector?.icon ? (
                                            <div className="relative h-10 w-10 rounded-lg bg-transparent p-1.5">
                                                <Image
                                                    src={account.connector.icon}
                                                    alt={account.connector.title || account.connector.name || 'App'}
                                                    fill
                                                    className="object-contain p-1"
                                                />
                                            </div>
                                        ) : (
                                            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-[color:color-mix(in_srgb,var(--surface-2)_46%,transparent)]">
                                                <Plug className="h-5 w-5 text-[var(--text-tertiary)]" />
                                            </div>
                                        )}
                                        <div className="min-w-0">
                                            <p className="truncate text-sm font-normal text-[var(--text-primary)]">
                                                {account.connector?.title || account.connector?.name || 'Unknown App'}
                                            </p>
                                            <p className="truncate text-xs text-[var(--text-tertiary)]">
                                                {account.email || 'Connected'}
                                            </p>
                                        </div>
                                    </div>
                                    <ResourceActionsMenu
                                        ariaLabel={`Open actions for ${account.connector?.title || account.connector?.name || 'connected account'}`}
                                        triggerClassName="h-8 w-8 opacity-0 transition-opacity group-hover:opacity-100 group-focus-within:opacity-100"
                                    >
                                        <DestructiveResourceActionItem
                                            disabled={deletingAccountId === account.id}
                                            onSelect={() => setAccountPendingDisconnect({
                                                id: account.id,
                                                appName: account.connector?.title || account.connector?.name || 'this app',
                                                accountLabel: account.email || account.connector?.title || account.connector?.name || 'Connected account',
                                            })}
                                        >
                                            Disconnect
                                        </DestructiveResourceActionItem>
                                    </ResourceActionsMenu>
                                </div>
                            </div>
                        ))}
                    </div>
                </section>
            )}

            <DestructiveConfirmationDialog
                open={Boolean(accountPendingDisconnect)}
                onOpenChange={(open) => {
                    if (!open) setAccountPendingDisconnect(null);
                }}
                title="Disconnect connector"
                description={`Disconnect ${accountPendingDisconnect?.appName ?? 'this connector'}? This revokes the account connection.`}
                resourceName={accountPendingDisconnect?.accountLabel ?? 'connected account'}
                confirmationText="disconnect"
                consequences={[
                    'Agents and workflows using this account will lose access.',
                    'You can reconnect the app later, but existing runs may fail until access is restored.',
                ]}
                confirmLabel="Disconnect"
                pendingLabel="Disconnecting..."
                isPending={Boolean(deletingAccountId)}
                onConfirm={() => void handleDisconnect()}
            />

            {enabledConnectors.length > 0 ? (
                <section className="context-section">
                    <div className="mb-3 flex items-center gap-2">
                        <CheckCircle2 className="h-4 w-4 text-[var(--state-success)]" />
                        <h2 className="text-base font-normal text-[var(--text-primary)]">Enabled connectors</h2>
                        <span className="text-xs text-[var(--text-tertiary)]">{enabledConnectors.length}</span>
                    </div>
                    <div className="resource-index-grid resource-index-grid-md-2 resource-index-grid-xl-3 grid-cols-1 md:grid-cols-2 xl:grid-cols-3">
                        {enabledConnectors.map(renderConnectorCard)}
                    </div>
                </section>
            ) : null}

            <section>
                <div className="mb-3 flex items-center gap-2">
                    <Plug className="h-4 w-4 text-[var(--text-tertiary)]" />
                    <h2 className="text-base font-normal text-[var(--text-primary)]">All connectors</h2>
                    <span className="text-xs text-[var(--text-tertiary)]">{availableConnectors.length}</span>
                </div>

                <div className="resource-index-grid resource-index-grid-md-2 resource-index-grid-xl-3 grid-cols-1 md:grid-cols-2 xl:grid-cols-3">
                    {availableConnectors.map(renderConnectorCard)}

                    {filteredApps.length === 0 && (
                        <EmptyState
                            variant="panel"
                            icon={<Plug className="h-4 w-4" />}
                            title="No connectors match this search"
                            description={`Try a different app name${searchTerm ? ` than "${searchTerm}"` : ''}.`}
                            className="col-span-full"
                        />
                    )}
                </div>
            </section>

            <Dialog open={Boolean(authConfigApp)} onOpenChange={(open) => {
                if (!open) {
                    setAuthConfigApp(null);
                    setAuthConfigMode('MANAGED');
                    setAuthConfigProvider('LEMMA');
                    setShowCustomConfigForm(false);
                    setAuthConfigValues({});
                    setCustomConfigName('');
                }
            }}>
                <DialogContent>
                    <DialogHeader>
                        <DialogTitle>Enable connector</DialogTitle>
                        <DialogDescription>
                            {usesDirectCredentials(authConfigCapability)
                                ? `Enable ${getAppLabel(authConfigApp)} for this organization. Account credentials are connected after enabling it.`
                                : `Choose how ${getAppLabel(authConfigApp)} should be authorized for this organization.`}
                        </DialogDescription>
                    </DialogHeader>
                    <div className="space-y-4 py-2">
                        {authConfigApp && getSupportedProviders(authConfigApp).length > 1 ? (
                            <div className="space-y-2">
                                <Label>Provider</Label>
                                <RadioGroup
                                    value={authConfigProvider}
                                    onValueChange={handleAuthConfigProviderChange}
                                    className="grid gap-2 sm:grid-cols-2"
                                >
                                    {getSupportedProviders(authConfigApp).map((provider) => (
                                        <Label
                                            key={provider}
                                            className="flex cursor-pointer items-start gap-3 rounded-lg border border-[var(--border-subtle)] bg-[var(--surface-1)] p-3 text-[var(--text-primary)]"
                                            data-selected={authConfigProvider === provider}
                                        >
                                            <RadioGroupItem value={provider} className="mt-0.5" />
                                            <span className="grid gap-1">
                                                <span className="text-sm font-medium text-[var(--text-primary)]">
                                                    {getProviderLabel(provider, getProviderCapability(authConfigApp, provider))}
                                                </span>
                                                <span className="text-xs leading-5 text-[var(--text-secondary)]">
                                                    {getProviderDescription(provider, getProviderCapability(authConfigApp, provider))}
                                                </span>
                                            </span>
                                        </Label>
                                    ))}
                                </RadioGroup>
                            </div>
                        ) : authConfigApp ? (
                            <div className="surface-panel-muted px-3 py-2 text-sm text-[var(--text-secondary)]">
                                {authConfigProviderLabel}
                            </div>
                        ) : null}

                        {authConfigHasSystemDefault ? (
                            <div className="flex items-start justify-between gap-3 rounded-lg border border-[var(--border-subtle)] bg-[var(--surface-1)] p-3">
                                <span className="grid gap-1">
                                    <span className="text-sm font-medium text-[var(--text-primary)]">System default</span>
                                    <span className="text-xs leading-5 text-[var(--text-secondary)]">
                                        {getManagedConfigCopy(authConfigProvider, authConfigCapability)}
                                    </span>
                                </span>
                                {authConfigSupportsCustom ? (
                                    <Button
                                        type="button"
                                        size="sm"
                                        variant="ghost"
                                        className="h-7 shrink-0 px-2 text-xs"
                                        onClick={() => {
                                            setAuthConfigMode('CUSTOM');
                                            setShowCustomConfigForm(true);
                                        }}
                                    >
                                        Add custom config
                                    </Button>
                                ) : null}
                            </div>
                        ) : authConfigSupportsCustom ? (
                            <div className="surface-panel-muted px-3 py-2 text-sm text-[var(--text-secondary)]">
                                Add an organization OAuth configuration to enable this app.
                            </div>
                        ) : (
                            <div className="state-surface-error rounded-lg px-3 py-3 text-sm text-[var(--text-secondary)]">
                                This provider does not have an available auth configuration yet.
                            </div>
                        )}

                        {authConfigMode === 'CUSTOM' && showCustomConfigForm ? (
                            <div className="space-y-3">
                                <div className="flex items-center justify-between gap-3">
                                    <Label>Custom configuration</Label>
                                    {authConfigHasSystemDefault ? (
                                        <Button
                                            type="button"
                                            size="sm"
                                            variant="ghost"
                                            className="h-7 px-2 text-xs"
                                            onClick={() => {
                                                setAuthConfigMode('MANAGED');
                                                setShowCustomConfigForm(false);
                                            }}
                                        >
                                            Use default
                                        </Button>
                                    ) : null}
                                </div>
                                <Input
                                    placeholder="Config name"
                                    value={customConfigName}
                                    onChange={(event) => setCustomConfigName(event.target.value)}
                                />
                                <SchemaFields
                                    schema={authConfigSchema}
                                    values={authConfigValues}
                                    onChange={setAuthConfigValues}
                                    emptyMessage="No custom configuration fields are available for this provider."
                                />
                            </div>
                        ) : null}
                    </div>
                    <DialogFooter>
                        <Button variant="outline" onClick={() => setAuthConfigApp(null)}>
                            Cancel
                        </Button>
                        <Button
                            onClick={() => void handleEnableFromDialog()}
                            disabled={!canEnableAuthConfig || Boolean(authConfigApp && enablingAppId === authConfigApp.id)}
                        >
                            {authConfigApp && enablingAppId === authConfigApp.id ? (
                                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                            ) : null}
                            Enable
                        </Button>
                    </DialogFooter>
                </DialogContent>
            </Dialog>

            <Dialog open={Boolean(credentialApp)} onOpenChange={(open) => {
                if (!open) {
                    setCredentialApp(null);
                    setCredentialValues({});
                }
            }}>
                <DialogContent>
                    <DialogHeader>
                        <DialogTitle>Connect account</DialogTitle>
                        <DialogDescription>
                            Enter the credentials for {getAppLabel(credentialApp)}. Fields come from the connector credential schema.
                        </DialogDescription>
                    </DialogHeader>
                    <div className="py-2">
                        <SchemaFields
                            schema={credentialSchema}
                            values={credentialValues}
                            onChange={setCredentialValues}
                            emptyMessage="No credential fields are required for this app."
                        />
                    </div>
                    <DialogFooter>
                        <Button variant="outline" onClick={() => setCredentialApp(null)}>
                            Cancel
                        </Button>
                        <Button onClick={() => void handleCreateCredentialAccount()} disabled={Boolean(credentialApp && connectingAppId === credentialApp.id)}>
                            {credentialApp && connectingAppId === credentialApp.id ? (
                                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                            ) : null}
                            Connect
                        </Button>
                    </DialogFooter>
                </DialogContent>
            </Dialog>
        </div>
    );
}

function SchemaFields({
    schema,
    values,
    onChange,
    emptyMessage = 'No configurable fields are required for this provider.',
}: {
    schema: JsonSchemaLike | null;
    values: SchemaValues;
    onChange: (values: SchemaValues) => void;
    emptyMessage?: string;
}) {
    const fields = buildSchemaFormFields(schema);

    if (fields.length === 0) {
        return (
            <div className="surface-panel-muted p-3 text-sm text-[var(--text-secondary)]">
                {emptyMessage}
            </div>
        );
    }

    const updateField = (name: string, value: unknown) => {
        onChange({ ...values, [name]: value });
    };

    return (
        <div className="space-y-3">
            {fields.map((field) => (
                <SchemaField
                    key={field.name}
                    field={field}
                    value={values[field.name]}
                    onChange={(value) => updateField(field.name, value)}
                />
            ))}
        </div>
    );
}

function SchemaField({
    field,
    value,
    onChange,
}: {
    field: SchemaFormField;
    value: unknown;
    onChange: (value: unknown) => void;
}) {
    const fieldId = `connector-schema-${field.name}`;
    const label = `${field.label}${field.required ? ' *' : ''}`;
    const stringValue = typeof value === 'string' ? value : value == null ? '' : String(value);

    if (field.kind === 'boolean') {
        return (
            <Label htmlFor={fieldId} className="flex cursor-pointer items-start gap-3 rounded-lg border border-[var(--border-subtle)] bg-[var(--surface-1)] p-3">
                <Checkbox
                    id={fieldId}
                    checked={Boolean(value)}
                    onCheckedChange={(checked) => onChange(Boolean(checked))}
                    className="mt-0.5"
                />
                <span className="grid gap-1">
                    <span className="text-sm font-medium text-[var(--text-primary)]">{label}</span>
                    {field.description ? (
                        <span className="text-xs leading-5 text-[var(--text-secondary)]">{field.description}</span>
                    ) : null}
                </span>
            </Label>
        );
    }

    return (
        <div className="space-y-1.5">
            <Label htmlFor={fieldId}>{label}</Label>
            {field.kind === 'select' ? (
                <Select value={stringValue} onValueChange={onChange}>
                    <SelectTrigger id={fieldId}>
                        <SelectValue placeholder={`Select ${field.label}`} />
                    </SelectTrigger>
                    <SelectContent>
                        {field.options.map((option) => (
                            <SelectItem key={option.value} value={option.value}>
                                {option.label}
                            </SelectItem>
                        ))}
                    </SelectContent>
                </Select>
            ) : field.kind === 'textarea' || field.kind === 'json' ? (
                <Textarea
                    id={fieldId}
                    className="form-field-control-flat min-h-28 p-3"
                    value={stringValue}
                    onChange={(event) => onChange(event.target.value)}
                    spellCheck={field.kind !== 'json'}
                />
            ) : (
                <Input
                    id={fieldId}
                    type={field.kind === 'number' ? 'number' : field.kind === 'email' ? 'email' : field.format === 'password' ? 'password' : 'text'}
                    value={stringValue}
                    onChange={(event) => onChange(event.target.value)}
                />
            )}
            {field.description ? (
                <p className="text-xs leading-5 text-[var(--text-tertiary)]">{field.description}</p>
            ) : null}
        </div>
    );
}
