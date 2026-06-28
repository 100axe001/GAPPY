/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Discriminates the flat message body.
 *
 * A message carries exactly one kind. Textual kinds use ``text``; tool kinds
 * use ``tool_name``/``tool_call_id`` plus ``tool_args`` (call) or
 * ``tool_result`` (return). There is no nested ``content`` object.
 */
export enum MessageKind {
    TEXT = 'TEXT',
    NOTIFICATION = 'NOTIFICATION',
    THINKING = 'THINKING',
    TOOL_CALL = 'TOOL_CALL',
    TOOL_RETURN = 'TOOL_RETURN',
}
