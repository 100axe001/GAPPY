/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { SurfaceBehaviorConfigInput } from './SurfaceBehaviorConfigInput.js';
import type { SurfaceCredentialMode } from './SurfaceCredentialMode.js';
/**
 * The single create-or-update body for `PUT /surfaces/{platform}`.
 *
 * A surface is uniquely identified by `pod_id + platform`, so this one
 * request handles both creation and partial update. Only the fields present
 * in the request are applied on update (merge semantics); `is_enabled`
 * defaults to True on create and is only changed on update when sent.
 */
export type SurfaceUpsertRequest = {
    account_id?: (string | null);
    config?: SurfaceBehaviorConfigInput;
    credential_mode?: SurfaceCredentialMode;
    default_agent_name?: (string | null);
    is_enabled?: boolean;
};

