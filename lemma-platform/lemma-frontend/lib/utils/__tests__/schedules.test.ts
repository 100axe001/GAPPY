import { describe, expect, it } from 'vitest';

import {
    describeCron,
    describeScheduleConfig,
    getScheduleConfigDetails,
    getScheduleTargetKind,
    getScheduleTargetName,
} from '../schedules';

describe('schedule formatting helpers', () => {
    it('describes common cron expressions', () => {
        expect(describeCron('0 * * * *')).toBe('Every hour');
        expect(describeCron('0 */6 * * *')).toBe('Every 6 hours');
        expect(describeCron('30 9 * * 1-5')).toBe('Weekdays at 09:30');
        expect(describeCron('15 8 1 * *')).toBe('1st of each month at 08:15');
    });

    it('extracts target kind and name from workflow and agent schedules', () => {
        expect(getScheduleTargetKind({ workflow_name: 'daily-review' } as never)).toBe('workflow');
        expect(getScheduleTargetName({ workflow_name: 'daily-review' } as never)).toBe('daily-review');

        expect(getScheduleTargetKind({ agent_name: 'triage-agent' } as never)).toBe('agent');
        expect(getScheduleTargetName({ agent_name: 'triage-agent' } as never)).toBe('triage-agent');
    });

    it('flattens nested schedule config details', () => {
        const schedule = {
            schedule_type: 'TIME',
            config: JSON.stringify({
                schedule: {
                    cron_expression: '0 10 * * *',
                    timezone: 'Asia/Kolkata',
                },
            }),
        } as never;

        expect(describeScheduleConfig(schedule)).toBe('Daily at 10:00 · Asia/Kolkata');
        expect(getScheduleConfigDetails(schedule)).toEqual([
            { label: 'Cron', value: '0 10 * * *' },
            { label: 'TZ', value: 'Asia/Kolkata' },
        ]);
    });
});
