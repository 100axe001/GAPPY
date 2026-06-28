import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import { buildJoinedRecordsQuery, parseForeignKeyReference } from "../datastore-query.js";
import type { Table } from "../types.js";
import { normalizeError, resolvePodClient, stringifyComparable } from "./utils.js";

/**
 * React hook for fetching base-table rows with their FK-related data
 * joined in a single query. You specify which FK columns to include and
 * the hook auto-resolves the referenced table and join columns.
 *
 * The result has nested objects: `{ id, name, team: { id, name } }`.
 *
 * @example Issues with their team
 * ```tsx
 * const { records, isLoading } = useRelatedRecords({
 *   client,
 *   tableName: "issues",
 *   include: [{ foreignKey: "team_id" }],
 * });
 * // records[0] = { id: "1", title: "Bug", team: { id: "t1", name: "Eng" } }
 * ```
 */
export interface RelatedRecordsInclude {
  foreignKey: string;
  as?: string;
  fields?: string[];
}

export interface RelatedRecordsResolvedInclude {
  foreignKey: string;
  relationKey: string;
  relatedTable: string;
  relatedColumn: string;
  fields: string[];
}

export interface RelatedRecordsColumn {
  key: string;
  field: string;
  label: string;
  source: "base" | "related";
  relationKey?: string;
}

export interface UseRelatedRecordsOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  baseFields?: string[];
  include: RelatedRecordsInclude[];
  limit?: number;
  offset?: number;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseRelatedRecordsResult<TRow extends Record<string, unknown> = Record<string, unknown>> {
  records: TRow[];
  columns: RelatedRecordsColumn[];
  sql: string;
  includes: RelatedRecordsResolvedInclude[];
  baseTable: Table | null;
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

function inferRelationKey(foreignKey: string, relatedTable: string): string {
  const stripped = foreignKey
    .replace(/_id$/i, "")
    .replace(/_uuid$/i, "")
    .replace(/_fk$/i, "")
    .trim();

  return stripped.length > 0 ? stripped : relatedTable;
}

function pickDefaultBaseFields(table: Table): string[] {
  const names = table.columns
    .map((column) => column.name)
    .filter((name) => name !== "created_at" && name !== "updated_at");

  const prioritized = ["id", "name", "title", "label", "status", "type"];
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

  return next.slice(0, 5);
}

function pickDefaultRelatedFields(table: Table, relatedColumn: string): string[] {
  const names = table.columns.map((column) => column.name);
  const prioritized = ["id", "name", "title", "label", "email", "slug", relatedColumn];
  const next: string[] = [];

  prioritized.forEach((name) => {
    if (names.includes(name) && !next.includes(name)) {
      next.push(name);
    }
  });

  if (next.length === 0 && names.length > 0) {
    next.push(names[0]);
  }

  return next.slice(0, 3);
}

function readAliasedValue(record: Record<string, unknown>, prefix: string, field: string): unknown {
  return record[`${prefix}${field}`];
}

export function useRelatedRecords<TRow extends Record<string, unknown> = Record<string, unknown>>({
  client,
  podId,
  tableName,
  baseFields,
  include,
  limit = 20,
  offset,
  enabled = true,
  autoLoad = true,
}: UseRelatedRecordsOptions): UseRelatedRecordsResult<TRow> {
  const [records, setRecords] = useState<TRow[]>([]);
  const [columns, setColumns] = useState<RelatedRecordsColumn[]>([]);
  const [sql, setSql] = useState("");
  const [includes, setIncludes] = useState<RelatedRecordsResolvedInclude[]>([]);
  const [baseTable, setBaseTable] = useState<Table | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const trimmedTableName = tableName.trim();
  const includeKey = stringifyComparable(include);
  const baseFieldsKey = stringifyComparable(baseFields);
  const stableInclude = useMemo(() => include, [includeKey]);
  const stableBaseFields = useMemo(() => baseFields, [baseFieldsKey]);
  const isEnabled = enabled && trimmedTableName.length > 0 && stableInclude.length > 0;

  const refresh = useCallback(async (signal?: AbortSignal): Promise<TRow[]> => {
    if (!isEnabled) {
      setRecords([]);
      setColumns([]);
      setSql("");
      setIncludes([]);
      setBaseTable(null);
      setError(null);
      setIsLoading(false);
      return [];
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextBaseTable = await scopedClient.tables.get(trimmedTableName);
      if (signal?.aborted) return [];

      if (nextBaseTable.enable_rls) {
        throw new Error(
          `Related record queries are not supported for RLS-enabled table "${trimmedTableName}". Use table-scoped record APIs instead.`,
        );
      }

      setBaseTable(nextBaseTable);

      const resolvedBaseFields = (stableBaseFields?.length ? stableBaseFields : pickDefaultBaseFields(nextBaseTable))
        .filter((field, index, allFields) => field.trim().length > 0 && allFields.indexOf(field) === index);

      const resolvedIncludes = await Promise.all(stableInclude.map(async (entry, index) => {
        if (signal?.aborted) throw new Error("Aborted");
        const baseColumn = nextBaseTable.columns.find((column) => column.name === entry.foreignKey) ?? null;
        const reference = baseColumn?.foreign_key?.references
          ? parseForeignKeyReference(baseColumn.foreign_key.references)
          : null;

        if (!baseColumn) {
          throw new Error(`Column "${entry.foreignKey}" was not found on table "${trimmedTableName}".`);
        }

        if (!reference) {
          throw new Error(`Column "${entry.foreignKey}" on "${trimmedTableName}" is not a foreign key.`);
        }

        const relatedTable = await scopedClient.tables.get(reference.table);
        if (relatedTable.enable_rls) {
          throw new Error(
            `Related record queries cannot join into RLS-enabled table "${reference.table}". Use table-scoped record APIs instead.`,
          );
        }
        const relationKey = entry.as?.trim() || inferRelationKey(entry.foreignKey, reference.table);
        const relatedFields = (entry.fields?.length ? entry.fields : pickDefaultRelatedFields(relatedTable, reference.column))
          .filter((field, fieldIndex, allFields) => field.trim().length > 0 && allFields.indexOf(field) === fieldIndex);

        if (relatedFields.length === 0) {
          throw new Error(`No display fields were resolved for relation "${entry.foreignKey}".`);
        }

        return {
          foreignKey: entry.foreignKey,
          relationKey,
          relatedTable: reference.table,
          relatedColumn: reference.column,
          fields: relatedFields,
          alias: `rel_${index}_${relationKey}`,
        };
      }));

      const nextSql = buildJoinedRecordsQuery({
        from: { table: trimmedTableName, alias: "base" },
        select: [
          ...resolvedBaseFields.map((field) => ({
            table: "base",
            column: field,
            as: `base__${field}`,
          })),
          ...resolvedIncludes.flatMap((entry) => entry.fields.map((field) => ({
            table: entry.alias,
            column: field,
            as: `${entry.relationKey}__${field}`,
          }))),
        ],
        joins: resolvedIncludes.map((entry) => ({
          table: entry.relatedTable,
          alias: entry.alias,
          type: "left",
          on: {
            left: { table: "base", column: entry.foreignKey },
            right: { table: entry.alias, column: entry.relatedColumn },
          },
        })),
        limit,
        offset,
      });

      setSql(nextSql);
      setIncludes(resolvedIncludes.map(({ alias: _alias, ...rest }) => rest));

      const response = await scopedClient.datastore.query(nextSql);
      if (signal?.aborted) return [];
      const nextColumns: RelatedRecordsColumn[] = [
        ...resolvedBaseFields.map((field) => ({
          key: field,
          field,
          label: sentenceCase(field),
          source: "base" as const,
        })),
        ...resolvedIncludes.flatMap((entry) => entry.fields.map((field) => ({
          key: `${entry.relationKey}.${field}`,
          field,
          label: `${sentenceCase(entry.relationKey)} ${sentenceCase(field)}`,
          source: "related" as const,
          relationKey: entry.relationKey,
        }))),
      ];

      const nextRecords = ((response.items ?? []) as Record<string, unknown>[]).map((record) => {
        const nextRecord: Record<string, unknown> = {};

        resolvedBaseFields.forEach((field) => {
          nextRecord[field] = readAliasedValue(record, "base__", field);
        });

        resolvedIncludes.forEach((entry) => {
          nextRecord[entry.relationKey] = entry.fields.reduce<Record<string, unknown>>((accumulator, field) => {
            accumulator[field] = readAliasedValue(record, `${entry.relationKey}__`, field);
            return accumulator;
          }, {});
        });

        return nextRecord as TRow;
      });

      setColumns(nextColumns);
      setRecords(nextRecords);
      return nextRecords;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load related records.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, isEnabled, limit, offset, podId, stableBaseFields, stableInclude, trimmedTableName]);

  useEffect(() => {
    if (!isEnabled) {
      setRecords([]);
      setColumns([]);
      setSql("");
      setIncludes([]);
      setBaseTable(null);
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
          setError(normalizeError(new Error("Failed to load related records."), "Failed to load related records."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, isEnabled, refresh]);

  return useMemo(() => ({
    records,
    columns,
    sql,
    includes,
    baseTable,
    isLoading,
    error,
    refresh,
  }), [baseTable, columns, error, includes, isLoading, records, refresh, sql]);
}
