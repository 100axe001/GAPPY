/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { WidgetEmbedUrlResponse } from '../models/WidgetEmbedUrlResponse.js';
import type { CancelablePromise } from '../core/CancelablePromise.js';
import { OpenAPI } from '../core/OpenAPI.js';
import { request as __request } from '../core/request.js';
export class WidgetsService {
    /**
     * Mint Widget Embed URL
     * Mint a short-lived, signed embed URL for a widget the caller may view.
     *
     * Per-view (not baked into the persisted tool result) so the token stays
     * ephemeral and membership is re-checked each time the widget is opened.
     * @param podId
     * @param conversationId
     * @param toolCallId
     * @returns WidgetEmbedUrlResponse Successful Response
     * @throws ApiError
     */
    public static widgetEmbedToken(
        podId: string,
        conversationId: string,
        toolCallId: string,
    ): CancelablePromise<WidgetEmbedUrlResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/pods/{pod_id}/widgets/{conversation_id}/{tool_call_id}/embed-token',
            path: {
                'pod_id': podId,
                'conversation_id': conversationId,
                'tool_call_id': toolCallId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
