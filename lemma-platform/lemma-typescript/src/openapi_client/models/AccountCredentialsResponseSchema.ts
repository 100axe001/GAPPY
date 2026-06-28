/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ApiKeyCredentialsResponseSchema } from './ApiKeyCredentialsResponseSchema.js';
import type { CredentialTypes } from './CredentialTypes.js';
import type { OauthCredentialsResponseSchema } from './OauthCredentialsResponseSchema.js';
/**
 * Schema for account credentials response.
 */
export type AccountCredentialsResponseSchema = {
    data: (OauthCredentialsResponseSchema | ApiKeyCredentialsResponseSchema);
    type?: CredentialTypes;
    user_data?: (Record<string, any> | null);
};

