import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { RecordFilter } from "../types.js";
import { encodeSqlValue, quoteIdentifierPath, renderIdentifierPath, renderRecordFilters } from "./sql-utils.js";
import { normalizeError, resolvePodClient, stringifyComparable } from "./utils.js";

export interface RecordAggregateMetric {
  key: string;
  op: "count" | "sum" | "avg" | "min" | "max";
  field?: string;
  distinct?: boolean;
}

export interface RecordAggregateOrderBy {
  field: string;
  direction?: "asc" | "desc";
}

export interface UseRecordAggregatesOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  metrics: RecordAggregateMetric[];
  groupBy?: string | string[];
  filters?: RecordFilter[];
  limit?: number;
  offset?: number;
  orderBy?: RecordAggregateOrderBy[];
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseRecordAggregatesResult<TRow extends Record<string, unknown> = Record<string, unknown>> {
  rows: TRow[];
  row: TRow | null;
  total: number;
  sql: string;
  isLoading: boolean;
  error: Error | null;
  refresh: () => Promise<TRow[]>;
}

function buildMetricExpression(metric: RecordAggregateMetric): string {
  const fn = metric.op.toUpperCase();
  if (metric.op === "count" && !metric.field) {
    return `${fn}(*) AS ${quoteIdentifierPath(metric.key)}`;
  }
  if (!metric.field) {
    throw new Error(`Aggregate metric "${metric.key}" requires a field.`);
  }
  const renderedField = renderIdentifierPath(metric.field);
  const distinct = metric.distinct ? "DISTINCT " : "";
  return `${fn}(${distinct}${renderedField}) AS ${quoteIdentifierPath(metric.key)}`;
}

function buildRecordAggregatesQuery({
  tableName,
  metrics,
  groupBy,
  filters,
  limit,
  offset,
  orderBy,
}: {
  tableName: string;
  metrics: RecordAggregateMetric[];
  groupBy?: string | string[];
  filters?: RecordFilter[];
  limit?: number;
  offset?: number;
  orderBy?: RecordAggregateOrderBy[];
}): string {
  const groups = (Array.isArray(groupBy) ? groupBy : groupBy ? [groupBy] : [])
    .map((field) => field.trim())
    .filter((field) => field.length > 0);

  const selectParts = [
    ...groups.map((field) => `${renderIdentifierPath(field)} AS ${quoteIdentifierPath(field)}`),
    ...metrics.map((metric) => buildMetricExpression(metric)),
  ];

  const whereClause = renderRecordFilters(filters);
  const orderClause = orderBy?.length
    ? ` ORDER BY ${orderBy.map((entry) => `${renderIdentifierPath(entry.field)} ${(entry.direction ?? "desc").toUpperCase()}`).join(", ")}`
    : "";
  const groupClause = groups.length
    ? ` GROUP BY ${groups.map((field) => renderIdentifierPath(field)).join(", ")}`
    : "";
  const limitClause = typeof limit === "number" ? ` LIMIT ${encodeSqlValue(limit)}` : "";
  const offsetClause = typeof offset === "number" ? ` OFFSET ${encodeSqlValue(offset)}` : "";

  return [
    `SELECT ${selectParts.join(", ")}`,
    `FROM ${quoteIdentifierPath(tableName)}`,
    whereClause ? `WHERE ${whereClause}` : "",
    groupClause,
    orderClause,
    limitClause,
    offsetClause,
  ].filter(Boolean).join(" ");
}

export function useRecordAggregates<TRow extends Record<string, unknown> = Record<string, unknown>>({
  client,
  podId,
  tableName,
  metrics,
  groupBy,
  filters = [],
  limit,
  offset,
  orderBy,
  enabled = true,
  autoLoad = true,
}: UseRecordAggregatesOptions): UseRecordAggregatesResult<TRow> {
  const [rows, setRows] = useState<TRow[]>([]);
  const [total, setTotal] = useState(0);
  const [sql, setSql] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const metricsKey = stringifyComparable(metrics);
  const filtersKey = stringifyComparable(filters);
  const groupByKey = stringifyComparable(groupBy);
  const orderByKey = stringifyComparable(orderBy);
  const stableMetrics = useMemo(() => metrics, [metricsKey]);
  const stableFilters = useMemo(() => filters, [filtersKey]);
  const stableGroupBy = useMemo(() => groupBy, [groupByKey]);
  const stableOrderBy = useMemo(() => orderBy, [orderByKey]);
  const trimmedTableName = tableName.trim();
  const isEnabled = enabled && trimmedTableName.length > 0 && stableMetrics.length > 0;

  const refresh = useCallback(async (signal?: AbortSignal): Promise<TRow[]> => {
    if (!isEnabled) {
      setRows([]);
      setTotal(0);
      setSql("");
      setError(null);
      setIsLoading(false);
      return [];
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextSql = buildRecordAggregatesQuery({
        tableName: trimmedTableName,
        metrics: stableMetrics,
        groupBy: stableGroupBy,
        filters: stableFilters,
        limit,
        offset,
        orderBy: stableOrderBy,
      });
      setSql(nextSql);
      const response = await scopedClient.datastore.query(nextSql);
      if (signal?.aborted) return [];
      const nextRows = (response.items ?? []) as TRow[];
      setRows(nextRows);
      setTotal(response.total ?? nextRows.length);
      return nextRows;
    } catch (aggregateError) {
      if (signal?.aborted) return [];
      const normalized = normalizeError(aggregateError, "Failed to load record aggregates.");
      setError(normalized);
      return [];
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, isEnabled, limit, offset, podId, stableFilters, stableGroupBy, stableMetrics, stableOrderBy, trimmedTableName]);

  useEffect(() => {
    if (!isEnabled) {
      setRows([]);
      setTotal(0);
      setSql("");
      setError(null);
      setIsLoading(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    void refresh(controller.signal);
    return () => controller.abort();
  }, [autoLoad, isEnabled, refresh]);

  return useMemo(() => ({
    rows,
    row: rows[0] ?? null,
    total,
    sql,
    isLoading,
    error,
    refresh,
  }), [error, isLoading, refresh, rows, sql, total]);
}
