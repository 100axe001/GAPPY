import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import { parseForeignKeyReference } from "../datastore-query.js";
import type { RecordSort, Table } from "../types.js";
import { normalizeError, resolvePodClient, stringifyComparable } from "./utils.js";

/**
 * React hook for finding records in *other* tables that reference a given
 * record. Starts from the parent table, discovers all tables with FK
 * columns pointing back to it, and fetches the referencing rows.
 *
 * For the simpler case where you already know the referencing table and
 * FK column, prefer `useReferencingRecords` — it has a more intuitive API.
 *
 * @example All comments and history entries for an issue
 * ```tsx
 * const { relations, records, isLoading } = useReverseRelatedRecords({
 *   client,
 *   tableName: "issues",
 *   recordId: "issue_123",
 *   relation: { tableName: "comments", foreignKey: "issue_id" },
 * });
 * ```
 *
 * @see useReferencingRecords — flipped-perspective alias for the common
 *   "show me all rows in table X where FK = Y" pattern.
 */
export interface ReverseRelationSelector {
  tableName: string;
  foreignKey: string;
}

export interface ReverseRelatedRelation {
  tableName: string;
  foreignKey: string;
  referencedColumn: string;
  label: string;
}

export interface ReverseRelatedRecordsColumn {
  key: string;
  field: string;
  label: string;
}

export interface UseReverseRelatedRecordsOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  recordId?: string | null;
  relation?: ReverseRelationSelector | null;
  fields?: string[];
  limit?: number;
  offset?: number;
  sort?: RecordSort[];
  tablesLimit?: number;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseReverseRelatedRecordsResult<TRow extends Record<string, unknown> = Record<string, unknown>> {
  parentTable: Table | null;
  relatedTable: Table | null;
  parentRecord: Record<string, unknown> | null;
  relations: ReverseRelatedRelation[];
  selectedRelation: ReverseRelatedRelation | null;
  columns: ReverseRelatedRecordsColumn[];
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

export function useReverseRelatedRecords<TRow extends Record<string, unknown> = Record<string, unknown>>({
  client,
  podId,
  tableName,
  recordId = null,
  relation = null,
  fields,
  limit = 20,
  offset,
  sort,
  tablesLimit = 100,
  enabled = true,
  autoLoad = true,
}: UseReverseRelatedRecordsOptions): UseReverseRelatedRecordsResult<TRow> {
  const [parentTable, setParentTable] = useState<Table | null>(null);
  const [relatedTable, setRelatedTable] = useState<Table | null>(null);
  const [parentRecord, setParentRecord] = useState<Record<string, unknown> | null>(null);
  const [relations, setRelations] = useState<ReverseRelatedRelation[]>([]);
  const [selectedRelation, setSelectedRelation] = useState<ReverseRelatedRelation | null>(null);
  const [columns, setColumns] = useState<ReverseRelatedRecordsColumn[]>([]);
  const [records, setRecords] = useState<TRow[]>([]);
  const [total, setTotal] = useState(0);
  const [nextPageToken, setNextPageToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const trimmedTableName = tableName.trim();
  const trimmedRecordId = typeof recordId === "string" ? recordId.trim() : "";
  const relationKey = stringifyComparable(relation);
  const fieldsKey = stringifyComparable(fields);
  const sortKey = stringifyComparable(sort);
  const stableRelation = useMemo(() => relation, [relationKey]);
  const stableFields = useMemo(() => fields, [fieldsKey]);
  const stableSort = useMemo(() => sort, [sortKey]);
  const isEnabled = enabled && trimmedTableName.length > 0 && trimmedRecordId.length > 0;

  const refresh = useCallback(async (signal?: AbortSignal): Promise<TRow[]> => {
    if (!isEnabled) {
      setParentTable(null);
      setRelatedTable(null);
      setParentRecord(null);
      setRelations([]);
      setSelectedRelation(null);
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
      const [tablesResponse, parentRecordResponse] = await Promise.all([
        scopedClient.tables.list({ limit: tablesLimit }),
        scopedClient.records.get(trimmedTableName, trimmedRecordId),
      ]);

      if (signal?.aborted) return [];

      // The tables list returns lean summaries (no columns); fetch each table's
      // full schema to discover foreign-key relations pointing at the parent.
      const listedTables = await Promise.all(
        (tablesResponse.items ?? []).map((entry) => scopedClient.tables.get(entry.name)),
      );

      if (signal?.aborted) return [];

      const nextParentTable = listedTables.find((tableEntry) => tableEntry.name === trimmedTableName)
        ?? await scopedClient.tables.get(trimmedTableName);
      const nextParentRecord = parentRecordResponse ?? null;

      if (signal?.aborted) return [];

      setParentTable(nextParentTable);
      setParentRecord(nextParentRecord);

      const nextRelations = listedTables.flatMap((candidateTable) => candidateTable.columns.flatMap((column) => {
        const reference = column.foreign_key?.references
          ? parseForeignKeyReference(column.foreign_key.references)
          : null;

        if (!reference || reference.table !== trimmedTableName) {
          return [];
        }

        return [{
          tableName: candidateTable.name,
          foreignKey: column.name,
          referencedColumn: reference.column,
          label: `${candidateTable.name}.${column.name} -> ${trimmedTableName}.${reference.column}`,
        }];
      }));

      setRelations(nextRelations);

      const nextSelectedRelation = stableRelation
        ? nextRelations.find((entry) => (
          entry.tableName === stableRelation.tableName
          && entry.foreignKey === stableRelation.foreignKey
        )) ?? null
        : (nextRelations[0] ?? null);

      setSelectedRelation(nextSelectedRelation);

      if (!nextSelectedRelation) {
        setRelatedTable(null);
        setColumns([]);
        setRecords([]);
        setTotal(0);
        setNextPageToken(null);
        return [];
      }

      const nextRelatedTable = listedTables.find((tableEntry) => tableEntry.name === nextSelectedRelation.tableName)
        ?? await scopedClient.tables.get(nextSelectedRelation.tableName);
      const referenceValue = nextParentRecord?.[nextSelectedRelation.referencedColumn]
        ?? (nextSelectedRelation.referencedColumn === "id" ? trimmedRecordId : undefined);

      if (signal?.aborted) return [];

      setRelatedTable(nextRelatedTable);

      if (typeof referenceValue === "undefined" || referenceValue === null) {
        setColumns([]);
        setRecords([]);
        setTotal(0);
        setNextPageToken(null);
        return [];
      }

      const resolvedFields = (stableFields?.length ? stableFields : pickDefaultFields(nextRelatedTable, nextSelectedRelation.foreignKey))
        .filter((field, index, allFields) => field.trim().length > 0 && allFields.indexOf(field) === index);

      const response = await scopedClient.records.list(nextSelectedRelation.tableName, {
        filters: [{
          field: nextSelectedRelation.foreignKey,
          op: "eq",
          value: referenceValue,
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
      const normalized = normalizeError(refreshError, "Failed to load reverse-related records.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [
    client,
    isEnabled,
    limit,
    offset,
    podId,
    stableFields,
    stableRelation,
    stableSort,
    tablesLimit,
    trimmedRecordId,
    trimmedTableName,
  ]);

  useEffect(() => {
    if (!isEnabled) {
      setParentTable(null);
      setRelatedTable(null);
      setParentRecord(null);
      setRelations([]);
      setSelectedRelation(null);
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
          setError(normalizeError(new Error("Failed to load reverse-related records."), "Failed to load reverse-related records."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, isEnabled, refresh]);

  return useMemo(() => ({
    parentTable,
    relatedTable,
    parentRecord,
    relations,
    selectedRelation,
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
    parentRecord,
    parentTable,
    records,
    refresh,
    relatedTable,
    relations,
    selectedRelation,
    total,
  ]);
}
