import type { ColumnSchema } from "./types.js";

export interface RecordDetailFieldGroupDefinition {
  label: string;
  fields: string[];
}

export function detectRecordTitleColumn(columns: ColumnSchema[]): ColumnSchema | undefined {
  return columns.find((column) =>
    !column.system && !column.auto && !column.computed && /title|name|subject|label/i.test(column.name),
  );
}

export function detectRecordDescriptionColumn(columns: ColumnSchema[]): ColumnSchema | undefined {
  return columns.find((column) =>
    !column.system
    && !column.auto
    && !column.computed
    && column.type === "TEXT"
    && /description|summary|body|content|notes|reason/i.test(column.name),
  );
}

export function detectRecordStatusColumn(columns: ColumnSchema[]): ColumnSchema | undefined {
  return columns.find((column) => /status|state|stage/i.test(column.name));
}

export function isDefaultRecordDetailHiddenField(name: string): boolean {
  return name === "id" || name === "created_at" || name === "updated_at";
}

export function buildDefaultRecordDetailFieldGroups(
  columns: ColumnSchema[],
  options: {
    hiddenFields?: string[];
    titleField?: string;
    descriptionField?: string;
    statusField?: string;
    identifierField?: string;
  } = {},
): RecordDetailFieldGroupDefinition[] {
  const excluded = new Set(
    [
      ...(options.hiddenFields ?? []),
      options.titleField,
      options.descriptionField,
      options.statusField,
      options.identifierField,
    ].filter((value): value is string => Boolean(value)),
  );

  const displayable = columns.filter((column) =>
    !column.system
    && !column.auto
    && !column.computed
    && !isDefaultRecordDetailHiddenField(column.name)
    && !excluded.has(column.name),
  );

  if (displayable.length === 0) return [];

  return [
    {
      label: "Details",
      fields: displayable.map((column) => column.name),
    },
  ];
}

export function humanizeRecordFieldName(value: string): string {
  return value
    .replace(/[_\.]/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/\b\w/g, (match) => match.toUpperCase());
}

export function formatRecordPlainValue(value: unknown): string {
  if (value == null || value === "") return "";
  if (value instanceof Date) return formatRecordDateDisplayValue(value);
  if (typeof value === "boolean") return value ? "Yes" : "No";
  if (typeof value === "number") return value.toLocaleString();
  if (Array.isArray(value)) return value.map(formatRecordPlainValue).filter(Boolean).join(", ");
  if (typeof value === "object") return JSON.stringify(value);
  return String(value);
}

export function formatRecordDisplayValue(value: unknown): string {
  return formatRecordPlainValue(value) || "Not set";
}

export function formatRecordDateDisplayValue(
  value: unknown,
  options?: Intl.DateTimeFormatOptions,
): string {
  if (value == null || value === "") return "Not set";

  const date = value instanceof Date ? value : new Date(String(value));
  if (Number.isNaN(date.getTime())) return String(value);

  return new Intl.DateTimeFormat(undefined, {
    month: "short",
    day: "numeric",
    year: "numeric",
    hour: "numeric",
    minute: "2-digit",
    ...options,
  }).format(date);
}
