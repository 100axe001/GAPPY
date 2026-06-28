import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import { parseForeignKeyReference, type ForeignKeyReference } from "../datastore-query.js";
import type { ColumnSchema, Table } from "../types.js";
import { normalizeError, resolvePodId } from "./utils.js";

/**
 * React hook that resolves a foreign-key column into dropdown options.
 * Reads the FK metadata from the table schema, fetches records from the
 * referenced table, and returns `{ value, label, record }` options ready
 * for `<Select>` components.
 *
 * Auto-detects the best label field (name > title > label > email > slug).
 *
 * @example
 * ```tsx
 * const { options, isLoading } = useForeignKeyOptions({
 *   client,
 *   tableName: "issues",
 *   columnName: "team_id",
 * });
 * // options = [{ value: "team_1", label: "Engineering", record: {...} }, ...]
 * ```
 */
export interface ForeignKeyOption {
  value: unknown;
  label: string;
  record: Record<string, unknown>;
}

export interface UseForeignKeyOptionsOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  columnName: string;
  labelField?: string;
  labelFields?: string[];
  search?: string;
  limit?: number;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseForeignKeyOptionsResult {
  table: Table | null;
  column: ColumnSchema | null;
  reference: ForeignKeyReference | null;
  labelField: string | null;
  options: ForeignKeyOption[];
  isLoading: boolean;
  error: Error | null;
  refresh: () => Promise<ForeignKeyOption[]>;
}

const EMPTY_LABEL_FIELDS: string[] = [];



function readRecordValue(record: Record<string, unknown>, field?: string | null): unknown {
  if (!field) return undefined;
  return record[field];
}

function pickResolvedLabelField(
  records: Record<string, unknown>[],
  referenceColumn: string,
  explicitLabelField?: string,
  explicitLabelFields?: string[],
): string | null {
  const candidates = [
    explicitLabelField,
    ...(explicitLabelFields ?? []),
    "name",
    "title",
    "label",
    "email",
    "slug",
    referenceColumn,
    "id",
  ].filter((value): value is string => typeof value === "string" && value.trim().length > 0);

  for (const candidate of candidates) {
    if (records.some((record) => {
      const value = record[candidate];
      return typeof value === "string"
        ? value.trim().length > 0
        : typeof value !== "undefined" && value !== null;
    })) {
      return candidate;
    }
  }

  return null;
}

function matchesSearch(record: Record<string, unknown>, search: string, fields: string[]): boolean {
  const normalized = search.trim().toLowerCase();
  if (!normalized) return true;

  return fields.some((field) => {
    const value = record[field];
    if (typeof value === "string") {
      return value.toLowerCase().includes(normalized);
    }
    if (typeof value === "number" || typeof value === "boolean") {
      return String(value).toLowerCase().includes(normalized);
    }
    return false;
  });
}

export function useForeignKeyOptions({
  client,
  podId,
  tableName,
  columnName,
  labelField,
  labelFields = EMPTY_LABEL_FIELDS,
  search,
  limit = 50,
  enabled = true,
  autoLoad = true,
}: UseForeignKeyOptionsOptions): UseForeignKeyOptionsResult {
  const [table, setTable] = useState<Table | null>(null);
  const [column, setColumn] = useState<ColumnSchema | null>(null);
  const [reference, setReference] = useState<ForeignKeyReference | null>(null);
  const [resolvedLabelField, setResolvedLabelField] = useState<string | null>(null);
  const [options, setOptions] = useState<ForeignKeyOption[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const labelFieldsKey = useMemo(() => JSON.stringify(labelFields), [labelFields]);
  const stableLabelFields = useMemo(() => labelFields, [labelFieldsKey]);

  const refresh = useCallback(async (signal?: AbortSignal): Promise<ForeignKeyOption[]> => {
    if (!enabled) return [];

    setIsLoading(true);
    setError(null);

    try {
      const resolvedPodId = resolvePodId(client, podId);
      const scopedClient = resolvedPodId === client.podId ? client : client.withPod(resolvedPodId);
      const nextTable = await scopedClient.tables.get(tableName);
      if (signal?.aborted) return [];
      const nextColumn = nextTable.columns.find((entry) => entry.name === columnName) ?? null;
      const nextReference = nextColumn?.foreign_key?.references
        ? parseForeignKeyReference(nextColumn.foreign_key.references)
        : null;

      setTable(nextTable);
      setColumn(nextColumn);
      setReference(nextReference);

      if (!nextColumn) {
        throw new Error(`Column "${columnName}" was not found on table "${tableName}".`);
      }

      if (!nextReference) {
        setResolvedLabelField(null);
        setOptions([]);
        return [];
      }

      const canFilterOnServer = !!labelField && !!search?.trim();
      const response = await scopedClient.records.list(nextReference.table, {
        limit: canFilterOnServer ? Math.max(limit, 100) : (search ? Math.max(limit * 5, 100) : limit),
        filters: canFilterOnServer
          ? [{ field: labelField, op: "ilike", value: `%${search?.trim()}%` }]
          : undefined,
      });

      if (signal?.aborted) return [];
      const records = response.items ?? [];
      const nextResolvedLabelField = pickResolvedLabelField(
        records,
        nextReference.column,
        labelField,
        stableLabelFields,
      );
      const searchableFields = Array.from(
        new Set(
          [nextResolvedLabelField, ...stableLabelFields, nextReference.column, "id"]
            .filter((value): value is string => typeof value === "string" && value.trim().length > 0),
        ),
      );

      const filteredRecords = canFilterOnServer || !search?.trim()
        ? records
        : records.filter((record) => matchesSearch(record, search, searchableFields));

      const nextOptions = filteredRecords
        .slice(0, limit)
        .map((record) => {
          const value = readRecordValue(record, nextReference.column);
          const labelValue = readRecordValue(record, nextResolvedLabelField);
          return {
            value,
            label: typeof labelValue === "string" && labelValue.trim().length > 0
              ? labelValue
              : String(value ?? ""),
            record,
          };
        })
        .filter((option) => typeof option.value !== "undefined" && option.value !== null);

      setResolvedLabelField(nextResolvedLabelField);
      setOptions(nextOptions);
      return nextOptions;
    } catch (refreshError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(refreshError, "Failed to load foreign key options.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, columnName, enabled, labelField, limit, podId, search, stableLabelFields, tableName]);

  useEffect(() => {
    if (!enabled || !autoLoad) return;
    const controller = new AbortController();
    let cancelled = false;
    (async () => {
      try {
        await refresh(controller.signal);
      } catch {
        if (!cancelled) {
          setError(normalizeError(new Error("Failed to load foreign key options."), "Failed to load foreign key options."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, enabled, refresh]);

  return useMemo(() => ({
    table,
    column,
    reference,
    labelField: resolvedLabelField,
    options,
    isLoading,
    error,
    refresh,
  }), [column, error, isLoading, options, reference, refresh, resolvedLabelField, table]);
}
