'use client';

import { createContext, useContext, useMemo, ReactNode } from 'react';
import { useAppConfig } from '@/lib/hooks/use-app';
import type { AppPageRef } from '@/lib/types/app';

interface AppContextType {
    pages: AppPageRef[];
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export function AppProvider({ children, podId }: { children: ReactNode; podId: string }) {
    const { data: config } = useAppConfig(podId);

    const pages = useMemo(() => {
        const items = config?.pages || [];
        return [...items].sort((a, b) => a.order - b.order);
    }, [config?.pages]);

    return (
        <AppContext.Provider value={{
            pages,
        }}>
            {children}
        </AppContext.Provider>
    );
}

export function useApp() {
    const context = useContext(AppContext);
    if (context === undefined) {
        throw new Error('useApp must be used within a AppProvider');
    }
    return context;
}
