export function normalizeConversationStatus(status: unknown): string {
    return typeof status === 'string'
        ? status.trim().toLowerCase().replace(/[-_\s]+/g, '_')
        : '';
}

export type ConversationStatusState = 'running' | 'stopping' | 'waiting' | 'completed' | 'failed' | 'stopped' | 'unknown';
export type ConversationStatusTone = 'live' | 'warning' | 'neutral' | 'danger' | 'muted';

export interface ConversationStatusView {
    state: ConversationStatusState;
    label: string;
    dotLabel: string;
    tone: ConversationStatusTone;
    isActive: boolean;
    isAwaiting: boolean;
    isTerminal: boolean;
}

export function isConversationRunningStatus(status: unknown): boolean {
    return getConversationStatusView(status).state === 'running';
}

export function formatConversationStatus(status: unknown): string {
    return getConversationStatusView(status).label;
}

export function getConversationStatusView(status: unknown): ConversationStatusView {
    const normalized = normalizeConversationStatus(status);

    if (normalized === 'running' || normalized === 'in_progress' || normalized === 'processing') {
        return {
            state: 'running',
            label: 'Working',
            dotLabel: 'Live',
            tone: 'live',
            isActive: true,
            isAwaiting: false,
            isTerminal: false,
        };
    }

    if (normalized === 'stop_requested' || normalized === 'stopping') {
        return {
            state: 'stopping',
            label: 'Stopping',
            dotLabel: 'Stopping',
            tone: 'warning',
            isActive: true,
            isAwaiting: false,
            isTerminal: false,
        };
    }

    if (normalized === 'waiting' || normalized === 'awaiting' || normalized === 'waiting_for_input') {
        return {
            state: 'waiting',
            label: 'Awaiting input',
            dotLabel: 'Awaiting',
            tone: 'warning',
            isActive: false,
            isAwaiting: true,
            isTerminal: false,
        };
    }

    if (normalized === 'failed' || normalized === 'error') {
        return {
            state: 'failed',
            label: 'Failed',
            dotLabel: 'Failed',
            tone: 'danger',
            isActive: false,
            isAwaiting: false,
            isTerminal: true,
        };
    }

    if (normalized === 'stopped' || normalized === 'cancelled' || normalized === 'canceled') {
        return {
            state: 'stopped',
            label: 'Stopped',
            dotLabel: 'Stopped',
            tone: 'muted',
            isActive: false,
            isAwaiting: false,
            isTerminal: true,
        };
    }

    if (normalized === 'completed' || normalized === 'complete' || normalized === 'done') {
        return {
            state: 'completed',
            label: 'Done',
            dotLabel: 'Done',
            tone: 'neutral',
            isActive: false,
            isAwaiting: false,
            isTerminal: true,
        };
    }

    return {
        state: 'unknown',
        label: 'Ready',
        dotLabel: 'Ready',
        tone: 'muted',
        isActive: false,
        isAwaiting: false,
        isTerminal: false,
    };
}
