'use client';

import type { Dispatch, ReactNode, SetStateAction } from 'react';
import { createContext, useContext } from 'react';

export type PodTopbarState = {
    title?: ReactNode;
    icon?: ReactNode;
    backHref?: string;
    backLabel?: string;
    eyebrow?: ReactNode;
    meta?: ReactNode;
    switcher?: ReactNode;
    tabs?: ReactNode;
    actions?: ReactNode;
    fullscreen?: boolean;
};

type PodTopbarContextValue = {
    setTopbar: Dispatch<SetStateAction<PodTopbarState>>;
};

const PodTopbarContext = createContext<PodTopbarContextValue | null>(null);

export function PodTopbarProvider({
    value,
    children,
}: {
    value: PodTopbarContextValue;
    children: ReactNode;
}) {
    return (
        <PodTopbarContext.Provider value={value}>
            {children}
        </PodTopbarContext.Provider>
    );
}

export function usePodTopbar() {
    return useContext(PodTopbarContext);
}
