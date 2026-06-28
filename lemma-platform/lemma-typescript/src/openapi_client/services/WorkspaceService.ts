/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { WorkspaceMeResponse } from '../models/WorkspaceMeResponse.js';
import type { CancelablePromise } from '../core/CancelablePromise.js';
import { OpenAPI } from '../core/OpenAPI.js';
import { request as __request } from '../core/request.js';
export class WorkspaceService {
    /**
     * Get current workspace state
     * @returns WorkspaceMeResponse Successful Response
     * @throws ApiError
     */
    public static workspaceMe(): CancelablePromise<WorkspaceMeResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/workspace/me',
        });
    }
}
