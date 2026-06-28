import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { RecordSort, Table } from "../types.js";
import { normalizeError, resolvePodClient, stringifyComparable } from "./utils.js";

/**
 * React hook for fetching records from a referencing table that point back
 * to a specific record via a foreign key.
 *
 * Unlike `useReverseRelatedRecords` which starts from a parent table and
 * discovers what references it, this hook starts from the child table and
 * says "give me all rows in this table where this FK column equals this ID."
 *
 * @example Fetch all comments for an issue
 * ```tsx
 * const { records, isLoading } = useReferencingRecords({
 *   client,
 *   table: "comments",
 *   foreignKey: "issue_id",
 *   recordId: "issue_123",
 * });
 * ```
 *
 * @example Fetch history entries
 * ```tsx
 * const { records, columns, isLoading } = useReferencingRecords({
 *   client,
 *   table: "issue_history",
 *   foreignKey: "issue_id",
 *   recordId: selectedIssueId,
 *   sort: [{ field: "created_at", direction: "desc" }],
 * });
 * ```
 */

export interface ReferencingRecordsColumn {
  key: string;
  field: string;
  label: string;
}

export interface UseReferencingRecordsOptions {
  client: LemmaClient;
  podId?: string;
  /** The referencing (child) table, e.g. "comments". */
  table: string;
  /** The foreign-key column in the referencing table, e.g. "issue_id". */
  foreignKey: string;
  /** The record ID value to match against the foreign-key column. */
  recordId?: string | null;
  /** Fields to select. Auto-resolved from the table schema if omitted. */
  fields?: string[];
  limit?: number;
  offset?: number;
  sort?: RecordSort[];
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseReferencingRecordsResult<TRow extends Record<string, unknown> = Record<string, unknown>> {
  referencedTable: Table | null;
  columns: ReferencingRecordsColumn[];
  records: TRow[];
  total: number;
  nextPageToken: string | null;
  isLoading: boolean;
  error: Error | null;
  refresh: () => Promise<TRow[]>;
}

function sentenceCase(value: string): string {
  return value
    .replace(/[_\.]/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/\b\w/g, (match) => match.toUpperCase());
}

function pickDefaultFields(table: Table, foreignKey: string): string[] {
  const names = table.columns
    .map((column) => column.name)
    .filter((name) => name !== "created_at" && name !== "updated_at");

  const prioritized = ["id", "name", "title", "label", "status", foreignKey];
  const next: string[] = [];

  prioritized.forEach((name) => {
    if (names.includes(name) && !next.includes(name)) {
      next.push(name);
    }
  });

  names.forEach((name) => {
    if (!next.includes(name)) {
      next.push(name);
    }
  });

  return next.slice(0, 6);
}

export function useReferencingRecords<TRow extends Record<string, unknown> = Record<string, unknown>>({
  client,
  podId,
  table,
  foreignKey,
  recordId = null,
  fields,
  limit = 20,
  offset,
  sort,
  enabled = true,
  autoLoad = true,
}: UseReferencingRecordsOptions): UseReferencingRecordsResult<TRow> {
  const [referencedTable, setReferencedTable] = useState<Table | null>(null);
  const [columns, setColumns] = useState<ReferencingRecordsColumn[]>([]);
  const [records, setRecords] = useState<TRow[]>([]);
  const [total, setTotal] = useState(0);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const trimmedTable = table.trim();
  const trimmedRecordId = typeof recordId === "string" ? recordId.trim() : "";
  const fieldsKey = stringifyComparable(fields);
  const sortKey = stringifyComparable(sort);
  const stableFields = useMemo(() => fields, [fieldsKey]);
  const stableSort = useMemo(() => sort, [sortKey]);
  const isEnabled = enabled && trimmedTable.length > 0 && trimmedRecordId.length > 0;

  const refresh = useCallback(async (signal?: AbortSignal): Promise<TRow[]> => {
    if (!isEnabled) {
      setReferencedTable(null);
      setColumns([]);
      setRecords([]);
      setTotal(0);
      setNextPageToken(null);
      setError(null);
      setIsLoading(false);
      return [];
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);

      const tableResponse = await scopedClient.tables.get(trimmedTable);
      if (signal?.aborted) return [];

      setReferencedTable(tableResponse);

      const resolvedFields = (stableFields?.length ? stableFields : pickDefaultFields(tableResponse, foreignKey))
        .filter((field, index, allFields) => field.trim().length > 0 && allFields.indexOf(field) === index);

      const response = await scopedClient.records.list(trimmedTable, {
        filters: [{
          field: foreignKey,
          op: "eq",
          value: trimmedRecordId,
        }],
        limit,
        offset,
        sort: stableSort,
      });

      if (signal?.aborted) return [];

      const nextRecords = (response.items ?? []) as TRow[];
      setColumns(resolvedFields.map((field) => ({
        key: field,
        field,
        label: sentenceCase(field),
      })));
      setRecords(nextRecords);
      setTotal(response.total ?? nextRecords.length);
      setNextPageToken(response.next_page_token ?? null);
      return nextRecords;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load referencing records.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [
    client,
    foreignKey,
    isEnabled,
    limit,
    offset,
    podId,
    stableFields,
    stableSort,
    trimmedRecordId,
    trimmedTable,
  ]);

  useEffect(() => {
    if (!isEnabled) {
      setReferencedTable(null);
      setColumns([]);
      setRecords([]);
      setTotal(0);
      setNextPageToken(null);
      setError(null);
      setIsLoading(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    let cancelled = false;
    (async () => {
      try {
        await refresh(controller.signal);
      } catch {
        if (!cancelled) {
          setError(normalizeError(new Error("Failed to load referencing records."), "Failed to load referencing records."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, isEnabled, refresh]);

  return useMemo(() => ({
    referencedTable,
    columns,
    records,
    total,
    nextPageToken,
    isLoading,
    error,
    refresh,
  }), [
    columns,
    error,
    isLoading,
    nextPageToken,
    records,
    refresh,
    referencedTable,
    total,
  ]);
}
