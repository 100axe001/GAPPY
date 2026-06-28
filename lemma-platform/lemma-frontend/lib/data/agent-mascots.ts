export interface AgentMascot {
    id: string;
    label: string;
    src: string;
}

export const AGENT_MASCOTS: AgentMascot[] = [
    { id: 'think', label: 'Thinker', src: '/agent-mascots/mascot-think.png' },
    { id: 'laptop', label: 'Operator', src: '/agent-mascots/mascot-laptop.png' },
    { id: 'checklist', label: 'Checklist', src: '/agent-mascots/mascot-checklist.png' },
    { id: 'target', label: 'Target', src: '/agent-mascots/mascot-target.png' },
    { id: 'point', label: 'Guide', src: '/agent-mascots/mascot-point.png' },
    { id: 'wave', label: 'Greeter', src: '/agent-mascots/mascot-wave.png' },
    { id: 'run', label: 'Runner', src: '/agent-mascots/mascot-run.png' },
    { id: 'walk', label: 'Walker', src: '/agent-mascots/mascot-walk.png' },
    { id: 'celebrate', label: 'Closer', src: '/agent-mascots/mascot-celebrate.png' },
];

export function getAgentMascotBySrc(src?: string | null) {
    return AGENT_MASCOTS.find((mascot) => mascot.src === src);
}
