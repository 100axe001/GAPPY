import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { DatastoreCountResponse } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseBulkRecordsOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  enabled?: boolean;
  onSuccess?: (response: DatastoreCountResponse) => void;
  onError?: (error: unknown) => void;
}

export interface UseBulkRecordsResult {
  isSubmitting: boolean;
  error: Error | null;
  lastMessage: string | null;
  createMany: (records: Record<string, unknown>[]) => Promise<DatastoreCountResponse | null>;
  updateMany: (records: Record<string, unknown>[]) => Promise<DatastoreCountResponse | null>;
  deleteMany: (recordIds: Array<string | number>) => Promise<DatastoreCountResponse | null>;
  reset: () => void;
}

export function useBulkRecords({
  client,
  podId,
  tableName,
  enabled = true,
  onSuccess,
  onError,
}: UseBulkRecordsOptions): UseBulkRecordsResult {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [lastMessage, setLastMessage] = useState<string | null>(null);

  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);

  useEffect(() => { onSuccessRef.current = onSuccess; }, [onSuccess]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const trimmedTableName = tableName.trim();
  const isEnabled = enabled && trimmedTableName.length > 0;

  const runBulkOperation = useCallback(async (
    action: (scopedClient: LemmaClient) => Promise<DatastoreCountResponse>,
    fallbackError: string,
    describe: (count: number) => string,
  ): Promise<DatastoreCountResponse | null> => {
    if (!isEnabled) {
      return null;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const response = await action(scopedClient);
      setLastMessage(describe(response.count));
      onSuccessRef.current?.(response);
      return response;
    } catch (mutationError) {
      const normalized = normalizeError(mutationError, fallbackError);
      setError(normalized);
      onErrorRef.current?.(mutationError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [client, isEnabled, podId]);

  const createMany = useCallback(async (
    records: Record<string, unknown>[],
  ): Promise<DatastoreCountResponse | null> => {
    if (records.length === 0) return null;
    return runBulkOperation(
      (scopedClient) => scopedClient.records.bulk.create(trimmedTableName, records),
      "Failed to bulk create records.",
      (count) => `${count} record${count === 1 ? "" : "s"} created.`,
    );
  }, [runBulkOperation, trimmedTableName]);

  const updateMany = useCallback(async (
    records: Record<string, unknown>[],
  ): Promise<DatastoreCountResponse | null> => {
    if (records.length === 0) return null;
    return runBulkOperation(
      (scopedClient) => scopedClient.records.bulk.update(trimmedTableName, records),
      "Failed to bulk update records.",
      (count) => `${count} record${count === 1 ? "" : "s"} updated.`,
    );
  }, [runBulkOperation, trimmedTableName]);

  const deleteMany = useCallback(async (
    recordIds: Array<string | number>,
  ): Promise<DatastoreCountResponse | null> => {
    if (recordIds.length === 0) return null;
    return runBulkOperation(
      (scopedClient) => scopedClient.records.bulk.delete(trimmedTableName, recordIds),
      "Failed to bulk delete records.",
      (count) => `${count} record${count === 1 ? "" : "s"} deleted.`,
    );
  }, [runBulkOperation, trimmedTableName]);

  const reset = useCallback(() => {
    setError(null);
    setIsSubmitting(false);
    setLastMessage(null);
  }, []);

  return useMemo(() => ({
    isSubmitting,
    error,
    lastMessage,
    createMany,
    updateMany,
    deleteMany,
    reset,
  }), [createMany, deleteMany, error, isSubmitting, lastMessage, reset, updateMany]);
}
