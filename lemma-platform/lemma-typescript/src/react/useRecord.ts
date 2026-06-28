import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import { normalizeError, resolvePodClient } from "./utils.js";

/**
 * React hook for fetching a single record by ID. The record API returns the
 * plain record object directly, so `record` is that object as-is.
 *
 * Perfect for detail panels — pair with `useRecords` for the list.
 *
 * @example
 * ```tsx
 * const { record, isLoading } = useRecord({
 *   client,
 *   tableName: "issues",
 *   recordId: selectedId,
 * });
 * // record is the issue object directly (or null)
 * ```
 */
export interface UseRecordOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  recordId?: string | null;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseRecordResult<TRecord extends Record<string, unknown> = Record<string, unknown>> {
  record: TRecord | null;
  isLoading: boolean;
  error: Error | null;
  refresh: (overrides?: { recordId?: string | null }) => Promise<TRecord | null>;
}



export function useRecord<TRecord extends Record<string, unknown> = Record<string, unknown>>({
  client,
  podId,
  tableName,
  recordId = null,
  enabled = true,
  autoLoad = true,
}: UseRecordOptions): UseRecordResult<TRecord> {
  const [record, setRecord] = useState<TRecord | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const trimmedTableName = tableName.trim();
  const trimmedRecordId = typeof recordId === "string" ? recordId.trim() : "";
  const isEnabled = enabled && trimmedTableName.length > 0 && trimmedRecordId.length > 0;

  const refresh = useCallback(async (
    overrides: { recordId?: string | null } = {},
    signal?: AbortSignal,
  ): Promise<TRecord | null> => {
    const nextRecordId = typeof overrides.recordId === "string"
      ? overrides.recordId.trim()
      : trimmedRecordId;

    if (!enabled || trimmedTableName.length === 0 || nextRecordId.length === 0) {
      setRecord(null);
      setError(null);
      setIsLoading(false);
      return null;
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await scopedClient.records.get(trimmedTableName, nextRecordId);
      if (signal?.aborted) return null;
      const nextRecord = (response ?? null) as TRecord | null;
      setRecord(nextRecord);
      return nextRecord;
    } catch (refreshError) {
      if (signal?.aborted) return null;
      const normalized = normalizeError(refreshError, "Failed to load record.");
      setError(normalized);
      return null;
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, enabled, podId, trimmedRecordId, trimmedTableName]);

  useEffect(() => {
    if (!isEnabled) {
      setRecord(null);
      setError(null);
      setIsLoading(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    let cancelled = false;
    (async () => {
      try {
        await refresh({}, controller.signal);
      } catch {
        if (!cancelled) {
          setError(normalizeError(new Error("Failed to load record."), "Failed to load record."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, isEnabled, refresh]);

  return useMemo(() => ({
    record,
    isLoading,
    error,
    refresh,
  }), [error, isLoading, record, refresh]);
}
