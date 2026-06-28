import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { FunctionRun } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

/**
 * React hook for creating a single record. Manages loading/error state and
 * exposes a `create` function you can call from event handlers.
 *
 * Supports two modes:
 * - `"direct"` (default): calls `records.create` directly.
 * - `"function"`: calls `functions.runs.create`, routing the create through
 *   a pod function that may enforce business logic.
 *
 * @example Direct create
 * ```tsx
 * const { create, isSubmitting } = useCreateRecord({ client, tableName: "comments" });
 * await create({ body: "Hello", issue_id: "123" });
 * ```
 *
 * @example Function-backed create
 * ```tsx
 * const { create, isSubmitting } = useCreateRecord({
 *   client,
 *   tableName: "issues",
 *   createVia: "function",
 *   createFunctionName: "create-issue",
 * });
 * await create({ title: "Bug", team_id: "team_1" });
 * ```
 */
export interface UseCreateRecordOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  enabled?: boolean;
  /** How the record is created. `"direct"` calls `records.create`. `"function"` calls `functions.runs.create`. */
  createVia?: "direct" | "function";
  /** Function name to run when `createVia` is `"function"`. Falls back to `tableName` if omitted. */
  createFunctionName?: string;
  onSuccess?: (record: Record<string, unknown>, response: Record<string, unknown> | FunctionRun) => void;
  onError?: (error: unknown) => void;
}

export interface UseCreateRecordResult<TRecord extends Record<string, unknown> = Record<string, unknown>> {
  createdRecord: TRecord | null;
  isSubmitting: boolean;
  error: Error | null;
  create: (data: Record<string, unknown>) => Promise<TRecord | null>;
  reset: () => void;
}

export function useCreateRecord<TRecord extends Record<string, unknown> = Record<string, unknown>>({
  client,
  podId,
  tableName,
  enabled = true,
  createVia = "direct",
  createFunctionName,
  onSuccess,
  onError,
}: UseCreateRecordOptions): UseCreateRecordResult<TRecord> {
  const [createdRecord, setCreatedRecord] = useState<TRecord | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedTableName = tableName.trim();
  const isEnabled = enabled && trimmedTableName.length > 0;

  const create = useCallback(async (data: Record<string, unknown>): Promise<TRecord | null> => {
    if (!isEnabled) {
      return null;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);

      if (createVia === "function") {
        const functionName = createFunctionName ?? trimmedTableName;
        const run = await scopedClient.functions.runs.create(functionName, { input: data });
        const nextRecord = ((run.output_data as Record<string, unknown> | undefined) ?? { id: run.id, ...data }) as TRecord | null;
        setCreatedRecord(nextRecord);
        if (nextRecord) {
          onSuccessRef.current?.(nextRecord, run);
        }
        return nextRecord;
      }

      const response = await scopedClient.records.create(trimmedTableName, data);
      const nextRecord = (response ?? null) as TRecord | null;
      setCreatedRecord(nextRecord);
      if (nextRecord) {
        onSuccessRef.current?.(nextRecord, response);
      }
      return nextRecord;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, "Failed to create record.");
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, createFunctionName, createVia, isEnabled, podId, trimmedTableName]);

  const reset = useCallback(() => {
    setCreatedRecord(null);
    setError(null);
    setIsSubmitting(false);
  }, []);

  return useMemo(() => ({
    createdRecord,
    isSubmitting,
    error,
    create,
    reset,
  }), [create, createdRecord, error, isSubmitting, reset]);
}
