/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { PodRoleCreateRequest } from '../models/PodRoleCreateRequest.js';
import type { PodRoleListResponse } from '../models/PodRoleListResponse.js';
import type { PodRolePermissionsReplaceRequest } from '../models/PodRolePermissionsReplaceRequest.js';
import type { PodRolePermissionsResponse } from '../models/PodRolePermissionsResponse.js';
import type { PodRoleResponse } from '../models/PodRoleResponse.js';
import type { CancelablePromise } from '../core/CancelablePromise.js';
import { OpenAPI } from '../core/OpenAPI.js';
import { request as __request } from '../core/request.js';
export class PodRolesService {
    /**
     * List Pod Roles
     * @param podId
     * @returns PodRoleListResponse Successful Response
     * @throws ApiError
     */
    public static podRolesList(
        podId: string,
    ): CancelablePromise<PodRoleListResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/pods/{pod_id}/roles',
            path: {
                'pod_id': podId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Pod Role
     * @param podId
     * @param requestBody
     * @returns PodRoleResponse Successful Response
     * @throws ApiError
     */
    public static podRolesCreate(
        podId: string,
        requestBody: PodRoleCreateRequest,
    ): CancelablePromise<PodRoleResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/pods/{pod_id}/roles',
            path: {
                'pod_id': podId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Pod Role
     * @param podId
     * @param roleName
     * @returns void
     * @throws ApiError
     */
    public static podRolesDelete(
        podId: string,
        roleName: string,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/pods/{pod_id}/roles/{role_name}',
            path: {
                'pod_id': podId,
                'role_name': roleName,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Pod Role
     * @param podId
     * @param roleName
     * @param requestBody
     * @returns PodRoleResponse Successful Response
     * @throws ApiError
     */
    public static podRolesUpdate(
        podId: string,
        roleName: string,
        requestBody: PodRoleCreateRequest,
    ): CancelablePromise<PodRoleResponse> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/pods/{pod_id}/roles/{role_name}',
            path: {
                'pod_id': podId,
                'role_name': roleName,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Pod Role Permissions
     * @param podId
     * @param roleName
     * @returns PodRolePermissionsResponse Successful Response
     * @throws ApiError
     */
    public static podRolePermissionsGet(
        podId: string,
        roleName: string,
    ): CancelablePromise<PodRolePermissionsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/pods/{pod_id}/roles/{role_name}/permissions',
            path: {
                'pod_id': podId,
                'role_name': roleName,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Replace Pod Role Permissions
     * @param podId
     * @param roleName
     * @param requestBody
     * @returns PodRolePermissionsResponse Successful Response
     * @throws ApiError
     */
    public static podRolePermissionsReplace(
        podId: string,
        roleName: string,
        requestBody: PodRolePermissionsReplaceRequest,
    ): CancelablePromise<PodRolePermissionsResponse> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/pods/{pod_id}/roles/{role_name}/permissions',
            path: {
                'pod_id': podId,
                'role_name': roleName,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
