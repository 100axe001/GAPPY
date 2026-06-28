import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { FunctionRun } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

/**
 * React hook for updating a single record. Manages loading/error state and
 * exposes an `update` function you can call from event handlers.
 *
 * Supports two modes:
 * - `"direct"` (default): calls `records.update` directly.
 * - `"function"`: calls `functions.runs.create`, routing the update through
 *   a pod function (e.g. for status transitions that log history).
 *
 * @example Direct update
 * ```tsx
 * const { update, isSubmitting } = useUpdateRecord({ client, tableName: "issues", recordId: "123" });
 * await update({ status: "closed" });
 * ```
 *
 * @example Function-backed update
 * ```tsx
 * const { update, isSubmitting } = useUpdateRecord({
 *   client,
 *   tableName: "issues",
 *   recordId: "123",
 *   updateVia: "function",
 *   updateFunctionName: "update-issue-status",
 * });
 * await update({ status: "in_progress" });
 * ```
 */
export interface UseUpdateRecordOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  recordId?: string | null;
  enabled?: boolean;
  /** How the record is updated. `"direct"` calls `records.update`. `"function"` calls `functions.runs.create`. */
  updateVia?: "direct" | "function";
  /** Function name to run when `updateVia` is `"function"`. Falls back to `tableName` if omitted. */
  updateFunctionName?: string;
  onSuccess?: (record: Record<string, unknown>, response: Record<string, unknown> | FunctionRun) => void;
  onError?: (error: unknown) => void;
}

export interface UseUpdateRecordResult<TRecord extends Record<string, unknown> = Record<string, unknown>> {
  updatedRecord: TRecord | null;
  isSubmitting: boolean;
  error: Error | null;
  update: (
    data: Record<string, unknown>,
    overrides?: { recordId?: string | null },
  ) => Promise<TRecord | null>;
  reset: () => void;
}

export function useUpdateRecord<TRecord extends Record<string, unknown> = Record<string, unknown>>({
  client,
  podId,
  tableName,
  recordId = null,
  enabled = true,
  updateVia = "direct",
  updateFunctionName,
  onSuccess,
  onError,
}: UseUpdateRecordOptions): UseUpdateRecordResult<TRecord> {
  const [updatedRecord, setUpdatedRecord] = useState<TRecord | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedTableName = tableName.trim();
  const trimmedRecordId = typeof recordId === "string" ? recordId.trim() : "";
  const isEnabled = enabled && trimmedTableName.length > 0;

  const update = useCallback(async (
    data: Record<string, unknown>,
    overrides: { recordId?: string | null } = {},
  ): Promise<TRecord | null> => {
    const nextRecordId = typeof overrides.recordId === "string"
      ? overrides.recordId.trim()
      : trimmedRecordId;

    if (!isEnabled || nextRecordId.length === 0) {
      return null;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);

      if (updateVia === "function") {
        const functionName = updateFunctionName ?? trimmedTableName;
        const input = { ...data, id: nextRecordId, record_id: nextRecordId };
        const run = await scopedClient.functions.runs.create(functionName, { input });
        const nextRecord = ((run.output_data as Record<string, unknown> | undefined) ?? { id: nextRecordId, ...data }) as TRecord | null;
        setUpdatedRecord(nextRecord);
        if (nextRecord) {
          onSuccessRef.current?.(nextRecord, run);
        }
        return nextRecord;
      }

      const response = await scopedClient.records.update(trimmedTableName, nextRecordId, data);
      const nextRecord = (response ?? null) as TRecord | null;
      setUpdatedRecord(nextRecord);
      if (nextRecord) {
        onSuccessRef.current?.(nextRecord, response);
      }
      return nextRecord;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, "Failed to update record.");
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, isEnabled, podId, trimmedRecordId, trimmedTableName, updateFunctionName, updateVia]);

  const reset = useCallback(() => {
    setUpdatedRecord(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    updatedRecord,
    isSubmitting,
    error,
    update,
    reset,
  }), [error, isSubmitting, reset, update, updatedRecord]);
}
