/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Row-visibility mode for record reads/writes on RLS-enabled tables.
 *
 * ``USER`` (the default when the ``mode`` param is omitted) scopes rows to the
 * caller's own ``user_id`` so app apps keep their per-user semantics — pod
 * admins included. ``ADMIN`` returns and operates on every member's rows and
 * requires the caller to administer the table (otherwise the request is
 * rejected). The mode is a no-op for non-RLS tables, whose rows are shared by
 * every member regardless.
 *
 * Endpoints expose this as an *optional* query param (default ``None`` ==
 * ``USER``) rather than one defaulting to ``RecordAccessMode.USER``: a named
 * enum query param carrying a literal default makes the TypeScript generator
 * emit ``mode: RecordAccessMode = 'USER'``, which fails strict typecheck (a raw
 * string is not assignable to the enum). An optional param generates the valid
 * ``mode?: RecordAccessMode`` while keeping one shared, CAPS-valued enum type.
 */
export enum RecordAccessMode {
    USER = 'USER',
    ADMIN = 'ADMIN',
}
