/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { PodEffectivePermissionsResponse } from '../models/PodEffectivePermissionsResponse.js';
import type { PodPermissionCatalogResponse } from '../models/PodPermissionCatalogResponse.js';
import type { CancelablePromise } from '../core/CancelablePromise.js';
import { OpenAPI } from '../core/OpenAPI.js';
import { request as __request } from '../core/request.js';
export class PodPermissionsService {
    /**
     * Get Pod Permission Catalog
     * @param podId
     * @returns PodPermissionCatalogResponse Successful Response
     * @throws ApiError
     */
    public static podPermissionsCatalog(
        podId: string,
    ): CancelablePromise<PodPermissionCatalogResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/pods/{pod_id}/permissions/catalog',
            path: {
                'pod_id': podId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get My Pod Permissions
     * @param podId
     * @returns PodEffectivePermissionsResponse Successful Response
     * @throws ApiError
     */
    public static podPermissionsMe(
        podId: string,
    ): CancelablePromise<PodEffectivePermissionsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/pods/{pod_id}/permissions/me',
            path: {
                'pod_id': podId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
