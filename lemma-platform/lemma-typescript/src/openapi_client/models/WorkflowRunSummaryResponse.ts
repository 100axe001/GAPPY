/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { FlowRunStatus } from './FlowRunStatus.js';
export type WorkflowRunSummaryResponse = {
    completed_at?: (string | null);
    created_at?: (string | null);
    current_node_id?: (string | null);
    error?: (string | null);
    failed_node_id?: (string | null);
    flow_id: string;
    id: string;
    pod_id: string;
    schedule_event_id?: (string | null);
    start_type?: string;
    started_at?: (string | null);
    status?: FlowRunStatus;
    updated_at?: (string | null);
    user_id: string;
};

