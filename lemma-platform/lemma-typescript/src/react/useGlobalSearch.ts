import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { FileSearchResultSchema, RecordFilter, SearchMethod } from "../types.js";
import { escapeSqlString, quoteIdentifierPath, renderIdentifierPath, renderRecordFilters } from "./sql-utils.js";
import { normalizeError, resolvePodClient, stringifyComparable } from "./utils.js";

export interface GlobalSearchTableSource {
  key?: string;
  tableName: string;
  label?: string;
  searchFields: string[];
  displayField?: string;
  subtitleField?: string;
  limit?: number;
  filters?: RecordFilter[];
}

export interface GlobalSearchFilesSource {
  enabled?: boolean;
  label?: string;
  limit?: number;
  searchMethod?: SearchMethod;
}

export interface GlobalSearchRecordResult {
  kind: "record";
  sourceKey: string;
  sourceLabel: string;
  tableName: string;
  id: string;
  title: string;
  subtitle: string | null;
  record: Record<string, unknown>;
}

export interface GlobalSearchFileResult {
  kind: "file";
  sourceKey: string;
  sourceLabel: string;
  path: string;
  title: string;
  subtitle: string | null;
  result: FileSearchResultSchema;
}

export type GlobalSearchResult = GlobalSearchRecordResult | GlobalSearchFileResult;

export interface UseGlobalSearchOptions {
  client: LemmaClient;
  podId?: string;
  query?: string;
  tables?: GlobalSearchTableSource[];
  files?: GlobalSearchFilesSource | false;
  enabled?: boolean;
  autoLoad?: boolean;
  minQueryLength?: number;
}

export interface UseGlobalSearchResult {
  results: GlobalSearchResult[];
  recordResults: GlobalSearchRecordResult[];
  fileResults: GlobalSearchFileResult[];
  totalResults: number;
  sourceErrors: Record<string, Error>;
  isLoading: boolean;
  error: Error | null;
  search: (overrides?: { query?: string }) => Promise<GlobalSearchResult[]>;
  reset: () => void;
}

function buildTableSearchQuery(source: GlobalSearchTableSource, query: string): string {
  const fields = Array.from(new Set([
    "id",
    ...source.searchFields,
    source.displayField ?? "id",
    source.subtitleField ?? "",
  ].filter((value) => value.trim().length > 0)));

  const searchClauses = source.searchFields.map((field) =>
    `${renderIdentifierPath(field)} ILIKE '%${escapeSqlString(query)}%'`,
  );
  const filterClause = renderRecordFilters(source.filters);

  return [
    `SELECT ${fields.map((field) => renderIdentifierPath(field)).join(", ")}`,
    `FROM ${quoteIdentifierPath(source.tableName)}`,
    `WHERE (${searchClauses.join(" OR ")})${filterClause ? ` AND ${filterClause}` : ""}`,
    `LIMIT ${source.limit ?? 8}`,
  ].join(" ");
}

function readString(value: unknown): string | null {
  if (typeof value === "string" && value.trim().length > 0) return value;
  if (typeof value === "number" || typeof value === "boolean") return String(value);
  return null;
}

export function useGlobalSearch({
  client,
  podId,
  query = "",
  tables = [],
  files,
  enabled = true,
  autoLoad = true,
  minQueryLength = 1,
}: UseGlobalSearchOptions): UseGlobalSearchResult {
  const [results, setResults] = useState<GlobalSearchResult[]>([]);
  const [sourceErrors, setSourceErrors] = useState<Record<string, Error>>({});
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const trimmedQuery = query.trim();
  const tablesKey = stringifyComparable(tables);
  const filesKey = stringifyComparable(files);
  const stableTables = useMemo(() => tables, [tablesKey]);
  const stableFiles = useMemo(() => files, [filesKey]);

  const reset = useCallback(() => {
    setResults([]);
    setSourceErrors({});
    setError(null);
    setIsLoading(false);
  }, []);

  const search = useCallback(async (
    overrides: { query?: string } = {},
    signal?: AbortSignal,
  ): Promise<GlobalSearchResult[]> => {
    const nextQuery = (overrides.query ?? trimmedQuery).trim();
    if (!enabled || nextQuery.length < minQueryLength) {
      reset();
      return [];
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const searchTasks: Array<Promise<{ key: string; results: GlobalSearchResult[]; error?: Error }>> = [];

      stableTables.forEach((source, index) => {
        const sourceKey = source.key?.trim() || source.tableName;
        searchTasks.push((async () => {
          try {
            const sql = buildTableSearchQuery(source, nextQuery);
            const response = await scopedClient.datastore.query(sql);
            const rows = response.items ?? [];
            const mapped: GlobalSearchRecordResult[] = rows.map((record) => {
              const displayField = source.displayField ?? source.searchFields[0] ?? "id";
              const subtitleField = source.subtitleField;
              const id = readString(record.id) ?? `${source.tableName}-${index}`;
              return {
                kind: "record",
                sourceKey,
                sourceLabel: source.label ?? source.tableName,
                tableName: source.tableName,
                id,
                title: readString(record[displayField]) ?? id,
                subtitle: subtitleField ? readString(record[subtitleField]) : null,
                record,
              };
            });
            return { key: sourceKey, results: mapped };
          } catch (tableError) {
            return {
              key: sourceKey,
              results: [],
              error: normalizeError(tableError, `Failed to search ${source.tableName}.`),
            };
          }
        })());
      });

      if (stableFiles !== false && stableFiles?.enabled !== false) {
        searchTasks.push((async () => {
          const sourceKey = "files";
          try {
            const response = await scopedClient.files.search(nextQuery, {
              limit: stableFiles?.limit ?? 8,
              searchMethod: stableFiles?.searchMethod,
            });
            const mapped: GlobalSearchFileResult[] = (response.items ?? []).map((result: FileSearchResultSchema) => ({
              kind: "file",
              sourceKey,
              sourceLabel: stableFiles?.label ?? "Files",
              path: result.path,
              title: result.path.split("/").filter(Boolean).pop() || result.path,
              subtitle: typeof result.content === "string" && result.content.trim().length > 0
                ? result.content.slice(0, 160)
                : null,
              result,
            }));
            return { key: sourceKey, results: mapped };
          } catch (fileError) {
            return {
              key: sourceKey,
              results: [],
              error: normalizeError(fileError, "Failed to search files."),
            };
          }
        })());
      }

      const settled = await Promise.all(searchTasks);
      if (signal?.aborted) return [];

      const nextErrors: Record<string, Error> = {};
      const nextResults = settled.flatMap((entry) => {
        if (entry.error) {
          nextErrors[entry.key] = entry.error;
        }
        return entry.results;
      });

      setSourceErrors(nextErrors);
      setResults(nextResults);
      return nextResults;
    } catch (searchError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(searchError, "Failed to run global search.");
      setError(normalized);
      setResults([]);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled, minQueryLength, podId, reset, stableFiles, stableTables, trimmedQuery]);

  useEffect(() => {
    if (!enabled || !autoLoad) return;
    if (trimmedQuery.length < minQueryLength) {
      reset();
      return;
    }

    const controller = new AbortController();
    void search({}, controller.signal);
    return () => controller.abort();
  }, [autoLoad, enabled, minQueryLength, reset, search, trimmedQuery]);

  return useMemo(() => {
    const recordResults = results.filter((entry): entry is GlobalSearchRecordResult => entry.kind === "record");
    const fileResults = results.filter((entry): entry is GlobalSearchFileResult => entry.kind === "file");
    return {
      results,
      recordResults,
      fileResults,
      totalResults: results.length,
      sourceErrors,
      isLoading,
      error,
      search,
      reset,
    };
  }, [error, isLoading, reset, results, search, sourceErrors]);
}
