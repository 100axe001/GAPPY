/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AgentSurfaceListResponse } from '../models/AgentSurfaceListResponse.js';
import type { AvailableSurfaceChannelsResponse } from '../models/AvailableSurfaceChannelsResponse.js';
import type { SurfaceSetupResponse } from '../models/SurfaceSetupResponse.js';
import type { SurfaceUpsertRequest } from '../models/SurfaceUpsertRequest.js';
import type { CancelablePromise } from '../core/CancelablePromise.js';
import { OpenAPI } from '../core/OpenAPI.js';
import { request as __request } from '../core/request.js';
export class AgentSurfacesService {
    /**
     * List Surfaces
     * @param podId
     * @param limit
     * @param pageToken
     * @returns AgentSurfaceListResponse Successful Response
     * @throws ApiError
     */
    public static agentSurfaceList(
        podId: string,
        limit: number = 100,
        pageToken?: (string | null),
    ): CancelablePromise<AgentSurfaceListResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/pods/{pod_id}/surfaces',
            path: {
                'pod_id': podId,
            },
            query: {
                'limit': limit,
                'page_token': pageToken,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Surface
     * @param podId
     * @param platform
     * @returns void
     * @throws ApiError
     */
    public static agentSurfaceDelete(
        podId: string,
        platform: string,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/pods/{pod_id}/surfaces/{platform}',
            path: {
                'pod_id': podId,
                'platform': platform,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Surface
     * @param podId
     * @param platform
     * @returns any Successful Response
     * @throws ApiError
     */
    public static agentSurfaceGet(
        podId: string,
        platform: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/pods/{pod_id}/surfaces/{platform}',
            path: {
                'pod_id': podId,
                'platform': platform,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Upsert Surface
     * Create the surface for a platform, or merge updates into the existing one.
     *
     * A surface is unique per ``pod_id + platform``, so this single idempotent
     * write covers create, config edits, channel routing, account/credential
     * changes, and enable/disable. Only fields present in the request are applied
     * on update.
     * @param podId
     * @param platform
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static agentSurfaceUpsert(
        podId: string,
        platform: string,
        requestBody: SurfaceUpsertRequest,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/pods/{pod_id}/surfaces/{platform}',
            path: {
                'pod_id': podId,
                'platform': platform,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * List Surface Channels
     * List the channels/groups this surface bot can be configured to respond in.
     *
     * Returns an empty list for platforms without an enumerable channel concept
     * (Telegram groups, WhatsApp, email).
     * @param podId
     * @param platform
     * @returns AvailableSurfaceChannelsResponse Successful Response
     * @throws ApiError
     */
    public static agentSurfaceChannels(
        podId: string,
        platform: string,
    ): CancelablePromise<AvailableSurfaceChannelsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/pods/{pod_id}/surfaces/{platform}/channels',
            path: {
                'pod_id': podId,
                'platform': platform,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Surface Setup
     * Everything needed to finish setting up this platform's surface.
     *
     * Merges the static platform checklist with live webhook + admin-consent
     * state. Works before the surface exists (guide only) and after (live state).
     * @param podId
     * @param platform
     * @returns SurfaceSetupResponse Successful Response
     * @throws ApiError
     */
    public static agentSurfaceSetup(
        podId: string,
        platform: string,
    ): CancelablePromise<SurfaceSetupResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/pods/{pod_id}/surfaces/{platform}/setup',
            path: {
                'pod_id': podId,
                'platform': platform,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
