/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ResourceAccessGrantRequest } from '../models/ResourceAccessGrantRequest.js';
import type { ResourceAccessResponse } from '../models/ResourceAccessResponse.js';
import type { ResourceType } from '../models/ResourceType.js';
import type { CancelablePromise } from '../core/CancelablePromise.js';
import { OpenAPI } from '../core/OpenAPI.js';
import { request as __request } from '../core/request.js';
export class PodResourceAccessService {
    /**
     * Get Resource Access
     * @param podId
     * @param resourceType
     * @param resourceName
     * @returns ResourceAccessResponse Successful Response
     * @throws ApiError
     */
    public static podResourceAccessGet(
        podId: string,
        resourceType: ResourceType,
        resourceName: string,
    ): CancelablePromise<ResourceAccessResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/pods/{pod_id}/resources/{resource_type}/{resource_name}/access',
            path: {
                'pod_id': podId,
                'resource_type': resourceType,
                'resource_name': resourceName,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Resource Access Grant
     * @param podId
     * @param resourceType
     * @param resourceName
     * @param granteeType
     * @param granteeId
     * @returns ResourceAccessResponse Successful Response
     * @throws ApiError
     */
    public static podResourceAccessGrantDelete(
        podId: string,
        resourceType: ResourceType,
        resourceName: string,
        granteeType: string,
        granteeId: string,
    ): CancelablePromise<ResourceAccessResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/pods/{pod_id}/resources/{resource_type}/{resource_name}/access/grantees/{grantee_type}/{grantee_id}',
            path: {
                'pod_id': podId,
                'resource_type': resourceType,
                'resource_name': resourceName,
                'grantee_type': granteeType,
                'grantee_id': granteeId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Replace Resource Access Grant
     * @param podId
     * @param resourceType
     * @param resourceName
     * @param granteeType
     * @param granteeId
     * @param requestBody
     * @returns ResourceAccessResponse Successful Response
     * @throws ApiError
     */
    public static podResourceAccessGrantReplace(
        podId: string,
        resourceType: ResourceType,
        resourceName: string,
        granteeType: string,
        granteeId: string,
        requestBody: ResourceAccessGrantRequest,
    ): CancelablePromise<ResourceAccessResponse> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/pods/{pod_id}/resources/{resource_type}/{resource_name}/access/grantees/{grantee_type}/{grantee_id}',
            path: {
                'pod_id': podId,
                'resource_type': resourceType,
                'resource_name': resourceName,
                'grantee_type': granteeType,
                'grantee_id': granteeId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
