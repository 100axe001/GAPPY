import { useCallback, useMemo } from "react";
import type { LemmaClient } from "../client.js";
import {
  buildRecordFormValues,
  buildRecordSchemaFields,
  getEditableRecordFields,
  type RecordSchemaField,
} from "../record-form.js";
import type { Table } from "../types.js";
import { useTableGet } from "./generated/tables.js";

export interface UseRecordSchemaOptions {
  client: LemmaClient;
  podId?: string;
  tableName: string;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseRecordSchemaResult {
  table: Table | null;
  fields: RecordSchemaField[];
  editableFields: RecordSchemaField[];
  defaults: Record<string, unknown>;
  isLoading: boolean;
  error: Error | null;
  refresh: () => Promise<Table | null>;
}

// Bespoke hook composing the generated `useTableGet` primitive: it owns the table fetch
// (cache + invalidation come from the generated layer) and derives the record-form schema
// on top. `enabled`/`autoLoad` map to the query's `enabled` flag.
export function useRecordSchema({
  client,
  podId,
  tableName,
  enabled = true,
  autoLoad = true,
}: UseRecordSchemaOptions): UseRecordSchemaResult {
  const query = useTableGet(client, podId, tableName, {
    enabled: enabled && autoLoad && tableName.trim().length > 0,
  });

  const table = (query.data ?? null) as Table | null;
  const fields = useMemo(() => (table ? buildRecordSchemaFields(table) : []), [table]);
  const editableFields = useMemo(() => (table ? getEditableRecordFields(table) : []), [table]);
  const defaults = useMemo(() => (table ? buildRecordFormValues(table) : {}), [table]);

  const refresh = useCallback(async (): Promise<Table | null> => {
    const result = await query.refetch();
    return (result.data ?? null) as Table | null;
  }, [query]);

  return useMemo(
    () => ({
      table,
      fields,
      editableFields,
      defaults,
      isLoading: query.isLoading,
      error: query.error,
      refresh,
    }),
    [defaults, editableFields, fields, query.error, query.isLoading, refresh, table],
  );
}
