/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VerifyTokenResponse } from '../models/VerifyTokenResponse.js';
import type { CancelablePromise } from '../core/CancelablePromise.js';
import { OpenAPI } from '../core/OpenAPI.js';
import { request as __request } from '../core/request.js';
export class AuthService {
    /**
     * Verify access token
     * Validate the current bearer token and return the resolved user context.
     * @returns VerifyTokenResponse Successful Response
     * @throws ApiError
     */
    public static authVerifyToken(): CancelablePromise<VerifyTokenResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/auth/verify-token',
        });
    }
}
