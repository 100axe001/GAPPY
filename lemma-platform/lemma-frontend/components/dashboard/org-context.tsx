'use client';

import { createContext, useContext, useEffect, useMemo, useState } from 'react';
import { useOrganizations } from '@/lib/hooks/use-organizations';
import { useLemmaAuth } from '@/lib/hooks/use-lemma-auth';
import type { Organization } from '@/lib/types';

interface OrganizationContextType {
    currentOrg: Organization | null;
    setCurrentOrg: (org: Organization) => void;
    organizations: Organization[];
    isLoading: boolean;
    hasSession: boolean;
}

const OrganizationContext = createContext<OrganizationContextType | undefined>(undefined);
const ORG_STORAGE_KEY = 'lemma:selected-org-id';

function getStoredOrgId() {
    if (typeof window === 'undefined') {
        return null;
    }

    return window.localStorage.getItem(ORG_STORAGE_KEY);
}

export function OrganizationProvider({ children }: { children: React.ReactNode }) {
    const { isAuthenticated, isLoading } = useLemmaAuth();
    const hasSession = isAuthenticated;
    const { data: orgsData, isLoading: isLoadingOrganizations } = useOrganizations({ enabled: hasSession });
    const organizations = useMemo(() => orgsData?.items || [], [orgsData?.items]);
    const [currentOrgId, setCurrentOrgId] = useState<string | null>(() => getStoredOrgId());

    useEffect(() => {
        if (typeof window === 'undefined') {
            return;
        }

        if (!hasSession) {
            window.localStorage.removeItem(ORG_STORAGE_KEY);
            return;
        }

        if (organizations.length === 0) {
            window.localStorage.removeItem(ORG_STORAGE_KEY);
            return;
        }

        if (!currentOrgId) {
            return;
        }

        const orgStillExists = organizations.some((org) => org.id === currentOrgId);
        if (orgStillExists) {
            window.localStorage.setItem(ORG_STORAGE_KEY, currentOrgId);
            return;
        }

        window.localStorage.removeItem(ORG_STORAGE_KEY);
    }, [currentOrgId, hasSession, organizations]);

    const currentOrg = useMemo(() => {
        if (!hasSession) return null;
        if (organizations.length === 0) return null;
        if (!currentOrgId) return organizations[0];

        return organizations.find((org) => org.id === currentOrgId) || organizations[0];
    }, [hasSession, organizations, currentOrgId]);

    const setCurrentOrg = (org: Organization) => {
        if (typeof window !== 'undefined') {
            window.localStorage.setItem(ORG_STORAGE_KEY, org.id);
        }
        setCurrentOrgId(org.id);
    };

    const isContextLoading = isLoading || (hasSession && isLoadingOrganizations);

    return (
        <OrganizationContext.Provider value={{ currentOrg, setCurrentOrg, organizations, isLoading: isContextLoading, hasSession }}>
            {children}
        </OrganizationContext.Provider>
    );
}

export function useOrganization() {
    const context = useContext(OrganizationContext);
    if (context === undefined) {
        throw new Error('useOrganization must be used within an OrganizationProvider');
    }
    return context;
}
