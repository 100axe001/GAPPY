import { parseForeignKeyReference, type ForeignKeyReference } from "./datastore-query.js";
import { DatastoreDataType, type ColumnSchema, type Table } from "./types.js";

export type RecordSchemaFieldKind =
  | "text"
  | "textarea"
  | "number"
  | "boolean"
  | "json"
  | "date"
  | "datetime"
  | "select"
  | "foreign-key"
  | "uuid";

export interface RecordSchemaField {
  name: string;
  label: string;
  kind: RecordSchemaFieldKind;
  column: ColumnSchema;
  required: boolean;
  readOnly: boolean;
  system: boolean;
  computed: boolean;
  auto: boolean;
  options: string[];
  foreignKey: ForeignKeyReference | null;
}

export interface BuildRecordPayloadOptions {
  mode?: "create" | "update";
}

export interface BuildRecordPayloadResult {
  data: Record<string, unknown>;
  errors: Record<string, string>;
  isValid: boolean;
}

export const DEFAULT_RECORD_FORM_HIDDEN_FIELDS = [
  "id",
  "created_at",
  "updated_at",
  "creator_user_id",
  "sort_order",
] as const;

function sentenceCase(value: string): string {
  return value
    .replace(/_/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/\b\w/g, (match) => match.toUpperCase());
}

function isBlank(value: unknown): boolean {
  return value === null || typeof value === "undefined" || (typeof value === "string" && value.trim() === "");
}

function isIntegerLike(value: number): boolean {
  return Number.isInteger(value);
}

function getRawColumnDefault(column: ColumnSchema): unknown {
  return (column as ColumnSchema & { default?: unknown }).default;
}

function shouldUseTextarea(column: ColumnSchema): boolean {
  if (typeof column.max_length === "number" && column.max_length >= 240) {
    return true;
  }

  return /(description|content|body|note|instruction|summary|message)/i.test(column.name);
}

function toDateInputValue(value: unknown): string {
  if (typeof value === "string") {
    return value.includes("T") ? value.slice(0, 10) : value;
  }

  if (value instanceof Date && !Number.isNaN(value.getTime())) {
    return value.toISOString().slice(0, 10);
  }

  return String(value);
}

function toDateTimeLocalInputValue(value: unknown): string {
  if (typeof value === "string") {
    const timestamp = new Date(value);
    if (!Number.isNaN(timestamp.getTime())) {
      const pad = (part: number) => String(part).padStart(2, "0");
      return [
        timestamp.getFullYear(),
        pad(timestamp.getMonth() + 1),
        pad(timestamp.getDate()),
      ].join("-") + `T${pad(timestamp.getHours())}:${pad(timestamp.getMinutes())}`;
    }

    return value;
  }

  if (value instanceof Date && !Number.isNaN(value.getTime())) {
    const pad = (part: number) => String(part).padStart(2, "0");
    return [
      value.getFullYear(),
      pad(value.getMonth() + 1),
      pad(value.getDate()),
    ].join("-") + `T${pad(value.getHours())}:${pad(value.getMinutes())}`;
  }

  return String(value);
}

export function getRecordFieldKind(column: ColumnSchema): RecordSchemaFieldKind {
  if (column.foreign_key?.references) return "foreign-key";
  if (column.type === DatastoreDataType.ENUM) return "select";
  if (column.type === DatastoreDataType.BOOLEAN) return "boolean";
  if (column.type === DatastoreDataType.JSON || column.type === DatastoreDataType.VECTOR) return "json";
  if (
    column.type === DatastoreDataType.INTEGER
    || column.type === DatastoreDataType.FLOAT
    || column.type === DatastoreDataType.SERIAL
  ) {
    return "number";
  }
  if (column.type === DatastoreDataType.DATE) return "date";
  if (column.type === DatastoreDataType.DATETIME) return "datetime";
  if (column.type === DatastoreDataType.UUID) return "uuid";
  if (column.type === DatastoreDataType.TEXT && shouldUseTextarea(column)) return "textarea";
  return "text";
}

export function buildRecordSchemaFields(table: Table): RecordSchemaField[] {
  return table.columns.map((column) => {
    const foreignKey = column.foreign_key?.references
      ? parseForeignKeyReference(column.foreign_key.references)
      : null;

    return {
      name: column.name,
      label: sentenceCase(column.name),
      kind: getRecordFieldKind(column),
      column,
      required: column.required === true,
      readOnly: column.system === true || column.computed === true || column.auto === true,
      system: column.system === true,
      computed: column.computed === true,
      auto: column.auto === true,
      options: column.options ?? [],
      foreignKey,
    };
  });
}

export function getEditableRecordFields(table: Table): RecordSchemaField[] {
  return buildRecordSchemaFields(table).filter((field) => !field.readOnly);
}

export function orderRecordSchemaFields<T extends { name: string }>(
  fields: T[],
  fieldOrder?: string[],
): T[] {
  if (!fieldOrder?.length) return fields;

  const ordered = fieldOrder
    .map((name) => fields.find((field) => field.name === name))
    .filter((field): field is T => field !== undefined);
  const remaining = fields.filter((field) => !fieldOrder.includes(field.name));

  return [...ordered, ...remaining];
}

export function formatRecordValueForForm(column: ColumnSchema, value: unknown): unknown {
  const kind = getRecordFieldKind(column);

  if (value === null || typeof value === "undefined") {
    if (kind === "boolean") return false;
    return "";
  }

  if (kind === "boolean") {
    return Boolean(value);
  }

  if (kind === "json") {
    if (typeof value === "string") return value;
    try {
      return JSON.stringify(value, null, 2);
    } catch {
      return String(value);
    }
  }

  if (kind === "date") {
    return toDateInputValue(value);
  }

  if (kind === "datetime") {
    return toDateTimeLocalInputValue(value);
  }

  if (kind === "number") {
    return String(value);
  }

  return String(value);
}

export function buildRecordFormValues(
  table: Table,
  values: Record<string, unknown> = {},
): Record<string, unknown> {
  const next: Record<string, unknown> = {};

  buildRecordSchemaFields(table).forEach((field) => {
    const provided = values[field.name];
    const rawDefault = getRawColumnDefault(field.column);
    const source = typeof provided !== "undefined" ? provided : rawDefault;
    next[field.name] = formatRecordValueForForm(field.column, source);
  });

  return next;
}

function coerceEmptyValue(
  mode: "create" | "update",
  name: string,
  target: Record<string, unknown>,
): void {
  if (mode === "update") {
    target[name] = null;
  }
}

export function buildRecordPayload(
  table: Table,
  values: Record<string, unknown>,
  options: BuildRecordPayloadOptions = {},
): BuildRecordPayloadResult {
  const mode = options.mode ?? "create";
  const data: Record<string, unknown> = {};
  const errors: Record<string, string> = {};

  getEditableRecordFields(table).forEach((field) => {
    const rawValue = values[field.name];
    const value = typeof rawValue === "string" ? rawValue : rawValue;

    if (field.kind === "boolean") {
      data[field.name] = Boolean(rawValue);
      return;
    }

    if (isBlank(value)) {
      if (field.required) {
        errors[field.name] = `${field.label} is required.`;
        return;
      }

      coerceEmptyValue(mode, field.name, data);
      return;
    }

    if (field.kind === "number") {
      const parsed = Number(value);
      if (!Number.isFinite(parsed)) {
        errors[field.name] = `${field.label} must be a valid number.`;
        return;
      }

      if (
        (field.column.type === DatastoreDataType.INTEGER || field.column.type === DatastoreDataType.SERIAL)
        && !isIntegerLike(parsed)
      ) {
        errors[field.name] = `${field.label} must be a whole number.`;
        return;
      }

      data[field.name] = parsed;
      return;
    }

    if (field.kind === "json") {
      try {
        data[field.name] = typeof value === "string" ? JSON.parse(value) : value;
      } catch {
        errors[field.name] = `${field.label} must be valid JSON.`;
      }
      return;
    }

    data[field.name] = typeof value === "string" ? value : String(value);
  });

  return {
    data,
    errors,
    isValid: Object.keys(errors).length === 0,
  };
}
