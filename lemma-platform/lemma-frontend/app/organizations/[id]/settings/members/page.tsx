'use client';

import { useMemo, useState } from 'react';
import {
    useOrganizationMembers,
    useOrganizationInvitations,
    useInviteMember,
    useRevokeInvitation,
    useRemoveOrgMember,
    useUpdateOrgMemberRole,
    useUpdateOrganization,
    useOrganizationDetails
} from '@/lib/hooks/use-organizations';
import { OrganizationJoinPolicy, OrganizationRole, type Organization, type OrganizationInvitation, type OrganizationMember } from '@/lib/types';
import { OrgJoinPolicyField, orgJoinPolicyLabel } from '@/components/organizations/org-join-policy-field';
import { useProfile } from '@/lib/hooks/use-user';
import { normalizeEmailDomain, workDomainFromEmail } from '@/lib/utils/organization-slugs';
import { Button } from '@/components/ui/button';
import { DestructiveConfirmationDialog } from '@/components/shared/destructive-confirmation-dialog';
import { EmptyState } from '@/components/shared/empty-state';
import { DestructiveResourceActionItem, ResourceActionsMenu } from '@/components/shared/resource-actions-menu';
import { Input } from '@/components/ui/input';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/components/ui/dialog";
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Plus, Mail } from 'lucide-react';
import { toast } from 'sonner';
import { format } from 'date-fns';
import { ProtectedRoute } from '@/components/auth/protected-route';
import { StepLoader } from '@/components/brand/loader';
import { PlainPageShell } from '@/components/dashboard/plain-page-shell';
import { OrganizationSettingsNav } from '@/components/organizations/organization-settings-nav';
import { ProductIcon } from '@/components/pod/product-icon';
import { formatRoleLabel } from '@/lib/utils/role-labels';
import { buildOrganizationInviteRedirectUri } from '@/lib/utils/invite-redirects';

import { useParams } from 'next/navigation';

export default function OrgMembersPage() {
    return (
        <ProtectedRoute>
            <OrgMembersPageContent />
        </ProtectedRoute>
    );
}

function OrgMembersPageContent() {
    const params = useParams();
    const orgId = params.id as string;
    // console.log('OrgMembersPage params (useParams):', orgId);

    const { data: membersData, isLoading: loadingMembers } = useOrganizationMembers(orgId);
    const { data: organization } = useOrganizationDetails(orgId);
    const { data: profile } = useProfile();
    // console.log('Members Data:', membersData, 'Loading:', loadingMembers, 'Error:', membersError);

    const { data: invitationsData, isLoading: loadingInvitations } = useOrganizationInvitations(orgId);

    const members = membersData?.items || [];
    const invitations = invitationsData?.items || [];
    const currentMembership = members.find((member) => member.user_id === profile?.id);
    const canManageAccess = currentMembership?.role === OrganizationRole.ORG_OWNER;

    return (
        <PlainPageShell
            title="Members"
            icon={<ProductIcon tone="settings" size="sm" />}
            backHref="/"
            backLabel="Home"
            meta="Organization"
            tabs={<OrganizationSettingsNav organizationId={orgId} />}
            contentWidthClassName="max-w-6xl"
            contentClassName="pb-16 sm:pb-20"
        >
            <section className="settings-stack office-arrive">
                <div className="settings-identity-band">
                    <div className="min-w-0">
                        <p className="type-eyebrow text-[var(--text-tertiary)]">Workspace</p>
                        <h2 className="mt-1 truncate text-xl font-semibold leading-tight text-[var(--text-primary)]">
                            {organization?.name || 'Organization access'}
                        </h2>
                        <p className="mt-2 max-w-2xl text-sm leading-6 text-[var(--text-secondary)]">
                            Manage members, invitations, and workspace entry rules.
                        </p>
                    </div>
                    {organization ? (
                        <div className="settings-stat-strip">
                            <OrgAccessStat label="URL slug" value={organization.slug} />
                            <OrgAccessStat label="Email domain" value={organization.email_domain || '—'} />
                            <OrgAccessStat label="Join policy" value={orgJoinPolicyLabel(organization.join_policy)} />
                        </div>
                    ) : null}
                </div>
                {organization ? (
                    <OrgAccessSettings
                        orgId={orgId}
                        organization={organization}
                        canManage={canManageAccess}
                        suggestedWorkDomain={workDomainFromEmail(profile?.email)}
                    />
                ) : null}
                <Tabs defaultValue="members" className="w-full">
                    <TabsList>
                        <TabsTrigger value="members">Members ({members.length})</TabsTrigger>
                        <TabsTrigger value="invitations">Invitations ({invitations.length})</TabsTrigger>
                    </TabsList>
                    <TabsContent value="members" className="mt-6">
                        <MembersList orgId={orgId} members={members} isLoading={loadingMembers} />
                    </TabsContent>
                    <TabsContent value="invitations" className="mt-6">
                        <InvitationsList orgId={orgId} invitations={invitations} isLoading={loadingInvitations} />
                    </TabsContent>
                </Tabs>
            </section>
        </PlainPageShell>
    );
}

function OrgAccessStat({ label, value }: { label: string; value: string }) {
    return (
        <div className="settings-stat">
            <p className="type-eyebrow">{label}</p>
            <p className="mt-1 break-all text-sm font-medium text-[var(--text-primary)]">{value}</p>
        </div>
    );
}

function OrgAccessSettings({
    orgId,
    organization,
    canManage,
    suggestedWorkDomain,
}: {
    orgId: string;
    organization: Organization;
    canManage: boolean;
    suggestedWorkDomain: string | null;
}) {
    const { mutate: updateOrganization, isPending } = useUpdateOrganization(orgId);
    const [joinPolicy, setJoinPolicy] = useState<OrganizationJoinPolicy>(organization.join_policy);
    const [emailDomain, setEmailDomain] = useState(organization.email_domain || '');

    const isEmailDomain = joinPolicy === OrganizationJoinPolicy.EMAIL_DOMAIN;
    const normalizedDomain = normalizeEmailDomain(emailDomain);
    const missingDomain = isEmailDomain && !normalizedDomain;
    const dirty =
        joinPolicy !== organization.join_policy ||
        (isEmailDomain && normalizedDomain !== (organization.email_domain || ''));

    const handleSave = () => {
        updateOrganization(
            {
                join_policy: joinPolicy,
                email_domain: isEmailDomain ? normalizedDomain : null,
            },
            {
                onSuccess: () => toast.success('Workspace access updated'),
                onError: (err) => toast.error('Failed to update access: ' + err.message),
            }
        );
    };

    return (
        <section className="settings-open-section">
            <div className="settings-panel-header">
                <div>
                    <h2 className="settings-title">Workspace access</h2>
                    <p className="settings-description">Control who can join this organization.</p>
                </div>
            </div>
            <div className="mt-5 max-w-md space-y-4">
                <OrgJoinPolicyField
                    value={joinPolicy}
                    onChange={(next) => {
                        setJoinPolicy(next);
                        if (
                            next === OrganizationJoinPolicy.EMAIL_DOMAIN &&
                            !emailDomain &&
                            suggestedWorkDomain
                        ) {
                            setEmailDomain(suggestedWorkDomain);
                        }
                    }}
                    emailDomain={emailDomain}
                    onEmailDomainChange={setEmailDomain}
                    suggestedWorkDomain={suggestedWorkDomain}
                    disabled={!canManage}
                />
                {canManage ? (
                    <Button
                        onClick={handleSave}
                        disabled={!dirty || missingDomain}
                        loading={isPending}
                        loadingLabel="Saving"
                    >
                        Save access
                    </Button>
                ) : (
                    <p className="settings-help-text">Only the organization owner can change who can join.</p>
                )}
            </div>
        </section>
    );
}

function MembersList({ orgId, members, isLoading }: { orgId: string, members: OrganizationMember[], isLoading: boolean }) {
    const { mutate: removeMember, isPending: isRemoving } = useRemoveOrgMember(orgId);
    const { mutate: updateRole, isPending: isUpdating } = useUpdateOrgMemberRole(orgId);
    const [inviteOpen, setInviteOpen] = useState(false);
    const [memberPendingRemove, setMemberPendingRemove] = useState<{ id: string; label: string } | null>(null);

    if (isLoading) {
        return <div className="flex justify-center p-8"><StepLoader size="sm" /></div>;
    }

    const handleRemove = () => {
        if (!memberPendingRemove) return;
        removeMember(memberPendingRemove.id, {
            onSuccess: () => {
                toast.success('Member removed');
                setMemberPendingRemove(null);
            },
            onError: (err) => toast.error('Failed to remove member: ' + err.message)
        });
    };

    const handleRoleChange = (memberId: string, newRole: OrganizationRole) => {
        updateRole({ memberId, role: newRole }, {
            onSuccess: () => toast.success('Role updated'),
            onError: (err) => toast.error('Failed to update role: ' + err.message)
        });
    };

    return (
        <section className="settings-open-section">
            <div className="settings-panel-header">
                <div>
                    <h2 className="settings-title">Members</h2>
                    <p className="settings-description">People with access to this organization.</p>
                </div>
                <InviteMemberDialog orgId={orgId} open={inviteOpen} onOpenChange={setInviteOpen} />
            </div>
            <div className="settings-list mt-5">
                {members.map((member) => {
                    const displayName = member.user?.first_name
                        ? `${member.user.first_name} ${member.user.last_name || ''}`.trim()
                        : (member.user?.email || 'Unknown User');

                    return (
                        <div key={member.id} className="settings-list-row">
                            <div className="flex items-center gap-4">
                                <Avatar>
                                    <AvatarImage src={member.user?.avatar_url} />
                                    <AvatarFallback>
                                        {(member.user?.first_name?.[0] || member.user?.email?.[0] || 'U').toUpperCase()}
                                    </AvatarFallback>
                                </Avatar>
                                <div>
                                    <p className="text-sm font-medium text-[var(--text-primary)]">
                                        {displayName}
                                    </p>
                                    <p className="text-xs text-[var(--text-tertiary)]">{member.user?.email}</p>
                                </div>
                            </div>
                            <div className="flex items-center gap-4">
                                <Select
                                    defaultValue={member.role}
                                    onValueChange={(val) => handleRoleChange(member.id, val as OrganizationRole)}
                                    disabled={isUpdating}
                                >
                                    <SelectTrigger className="w-[110px]">
                                        <SelectValue />
                                    </SelectTrigger>
                                    <SelectContent>
                                        <SelectItem value={OrganizationRole.ORG_OWNER}>Owner</SelectItem>
                                        <SelectItem value={OrganizationRole.ORG_EDITOR}>Editor</SelectItem>
                                        <SelectItem value={OrganizationRole.ORG_MEMBER}>Member</SelectItem>
                                    </SelectContent>
                                </Select>
                                <ResourceActionsMenu ariaLabel={`Open actions for ${displayName}`} triggerClassName="h-8 w-8">
                                    <DestructiveResourceActionItem
                                        disabled={isRemoving}
                                        onSelect={() => setMemberPendingRemove({ id: member.id, label: displayName })}
                                    >
                                        Remove from organization
                                    </DestructiveResourceActionItem>
                                </ResourceActionsMenu>
                            </div>
                        </div>
                    );
                })}
                {members.length === 0 ? (
                    <EmptyState
                        variant="compact"
                        title="No members yet"
                        description="Invite the people who should help own this organization."
                        className="surface-panel-muted py-8"
                    />
                ) : null}
            </div>
            <DestructiveConfirmationDialog
                open={Boolean(memberPendingRemove)}
                onOpenChange={(open) => {
                    if (!open) setMemberPendingRemove(null);
                }}
                title="Remove organization member"
                description={`Remove ${memberPendingRemove?.label ?? 'this member'} from this organization?`}
                resourceName={memberPendingRemove?.label ?? 'member'}
                confirmationText=""
                consequences={[
                    'They will lose organization access and any pod access that depends on it.',
                    'This does not delete their user account.',
                ]}
                confirmLabel="Remove member"
                pendingLabel="Removing member..."
                isPending={isRemoving}
                onConfirm={handleRemove}
            />
        </section>
    );
}

function InvitationsList({ orgId, invitations, isLoading }: { orgId: string, invitations: OrganizationInvitation[], isLoading: boolean }) {
    const { mutate: revoke, isPending } = useRevokeInvitation(orgId);
    const [invitationPendingRevoke, setInvitationPendingRevoke] = useState<{ id: string; email: string } | null>(null);

    if (isLoading) {
        return <div className="flex justify-center p-8"><StepLoader size="sm" /></div>;
    }

    const handleRevoke = () => {
        if (!invitationPendingRevoke) return;
        revoke(invitationPendingRevoke.id, {
            onSuccess: () => {
                toast.success('Invitation revoked');
                setInvitationPendingRevoke(null);
            },
            onError: (err) => toast.error('Failed to revoke invitation: ' + err.message)
        });
    };

    return (
        <section className="settings-open-section">
            <div className="settings-panel-header">
                <div>
                    <h2 className="settings-title">Pending invitations</h2>
                    <p className="settings-description">Users invited to join the organization.</p>
                </div>
            </div>
            <div className="settings-list mt-5">
                {invitations.map((invite) => (
                    <div key={invite.id} className="settings-list-row">
                        <div className="flex items-center gap-4">
                            <div className="settings-panel-icon h-10 w-10">
                                <Mail className="h-4 w-4 text-[var(--text-tertiary)]" />
                            </div>
                            <div>
                                <p className="text-sm font-medium text-[var(--text-primary)]">{invite.email}</p>
                                <p className="text-xs text-[var(--text-tertiary)]">
                                    Role: {formatRoleLabel(invite.pod_role || invite.role)} • Expires: {invite.expires_at ? format(new Date(invite.expires_at), 'PPP') : 'Never'}
                                </p>
                                {invite.pod_name ? (
                                    <p className="mt-1 text-xs text-[var(--text-secondary)]">
                                        Pod: {invite.pod_name}
                                    </p>
                                ) : null}
                                {invite.pod_description ? (
                                    <p className="mt-1 line-clamp-2 text-xs text-[var(--text-tertiary)]">
                                        {invite.pod_description}
                                    </p>
                                ) : null}
                                {invite.redirect_uri ? (
                                    <p className="mt-1 break-all text-xs text-[var(--text-tertiary)]">
                                        Redirect: {invite.redirect_uri}
                                    </p>
                                ) : null}
                            </div>
                        </div>
                        <ResourceActionsMenu ariaLabel={`Open actions for invite ${invite.email}`} triggerClassName="h-8 w-8">
                            <DestructiveResourceActionItem
                                disabled={isPending}
                                onSelect={() => setInvitationPendingRevoke({ id: invite.id, email: invite.email })}
                            >
                                Revoke invite
                            </DestructiveResourceActionItem>
                        </ResourceActionsMenu>
                    </div>
                ))}
                {invitations.length === 0 ? (
                    <div className="surface-panel-muted py-8 text-center">
                        <p className="settings-help-text">No pending invitations.</p>
                    </div>
                ) : null}
            </div>
            <DestructiveConfirmationDialog
                open={Boolean(invitationPendingRevoke)}
                onOpenChange={(open) => {
                    if (!open) setInvitationPendingRevoke(null);
                }}
                title="Revoke invite"
                description={`Revoke the pending invite for ${invitationPendingRevoke?.email ?? 'this person'}?`}
                resourceName={invitationPendingRevoke?.email ?? 'invite'}
                confirmationText=""
                consequences={[
                    'The invite link will stop working.',
                    'You can send a new invite later if needed.',
                ]}
                confirmLabel="Revoke invite"
                pendingLabel="Revoking invite..."
                isPending={isPending}
                onConfirm={handleRevoke}
            />
        </section>
    );
}

function InviteMemberDialog({ orgId, open, onOpenChange }: { orgId: string, open: boolean, onOpenChange: (open: boolean) => void }) {
    const { mutate: invite, isPending } = useInviteMember(orgId);
    const [email, setEmail] = useState('');
    const [role, setRole] = useState<OrganizationRole>(OrganizationRole.ORG_MEMBER);
    const defaultRedirectUri = useMemo(
        () => buildOrganizationInviteRedirectUri({ orgId, role }),
        [orgId, role]
    );

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        invite({ email, role, redirect_uri: defaultRedirectUri }, {
            onSuccess: () => {
                toast.success('Invitation sent');
                onOpenChange(false);
                setEmail('');
                setRole(OrganizationRole.ORG_MEMBER);
            },
            onError: (err) => toast.error('Failed to send invitation: ' + err.message)
        });
    };

    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogTrigger asChild>
                <Button>
                    <Plus className="w-4 h-4 mr-2" />
                    Invite Member
                </Button>
            </DialogTrigger>
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>Invite New Member</DialogTitle>
                    <DialogDescription>
                        Send an invitation to join your organization.
                    </DialogDescription>
                </DialogHeader>
                <form onSubmit={handleSubmit} className="space-y-4">
                    <div className="space-y-2">
                        <label className="text-sm font-medium">Email Address</label>
                        <Input
                            type="email"
                            placeholder="colleague@example.com"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>
                    <div className="space-y-2">
                        <label className="text-sm font-medium">Role</label>
                        <Select value={role} onValueChange={(val) => setRole(val as OrganizationRole)}>
                            <SelectTrigger>
                                <SelectValue />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem value={OrganizationRole.ORG_OWNER}>Owner</SelectItem>
                                <SelectItem value={OrganizationRole.ORG_EDITOR}>Editor</SelectItem>
                                <SelectItem value={OrganizationRole.ORG_MEMBER}>Member</SelectItem>
                            </SelectContent>
                        </Select>
                    </div>
                    <div className="space-y-2">
                        <p className="text-sm font-medium">Redirect after accept</p>
                        <p className="break-all text-xs text-[var(--text-tertiary)]">
                            {defaultRedirectUri}
                        </p>
                    </div>
                    <DialogFooter>
                        <Button type="button" variant="ghost" onClick={() => onOpenChange(false)}>Cancel</Button>
                        <Button type="submit" disabled={isPending}>
                            {isPending ? 'Sending...' : 'Send Invitation'}
                        </Button>
                    </DialogFooter>
                </form>
            </DialogContent>
        </Dialog>
    );
}
