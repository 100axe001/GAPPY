export type JsonSchemaPrimitiveType =
  | "string"
  | "number"
  | "integer"
  | "boolean"
  | "object"
  | "array"
  | "null";

export interface JsonSchemaLike {
  type?: JsonSchemaPrimitiveType | JsonSchemaPrimitiveType[];
  title?: string;
  description?: string;
  format?: string;
  default?: unknown;
  enum?: unknown[];
  properties?: Record<string, JsonSchemaLike>;
  required?: string[];
  items?: JsonSchemaLike;
  anyOf?: JsonSchemaLike[];
  oneOf?: JsonSchemaLike[];
  allOf?: JsonSchemaLike[];
  [key: string]: unknown;
}

export type SchemaFormFieldKind =
  | "text"
  | "textarea"
  | "number"
  | "boolean"
  | "select"
  | "json"
  | "date"
  | "datetime"
  | "email";

export interface SchemaFormField {
  name: string;
  label: string;
  description?: string;
  required: boolean;
  kind: SchemaFormFieldKind;
  type: JsonSchemaPrimitiveType | "unknown";
  format?: string;
  options: Array<{ label: string; value: string }>;
  defaultValue?: unknown;
  schema: JsonSchemaLike;
}

export interface BuildSchemaFormPayloadResult {
  data: Record<string, unknown>;
  errors: Record<string, string>;
  isValid: boolean;
}

function sentenceCase(value: string): string {
  return value
    .replace(/_/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/\b\w/g, (match) => match.toUpperCase());
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return !!value && typeof value === "object" && !Array.isArray(value);
}

function isBlank(value: unknown): boolean {
  return value === null || typeof value === "undefined" || (typeof value === "string" && value.trim() === "");
}

function normalizeSchemaType(schema: JsonSchemaLike): JsonSchemaPrimitiveType | "unknown" {
  if (Array.isArray(schema.type)) {
    const nonNull = schema.type.find((entry) => entry !== "null");
    return nonNull ?? "unknown";
  }

  if (typeof schema.type === "string") {
    return schema.type;
  }

  if (schema.enum?.length) {
    return "string";
  }

  if (schema.properties && isRecord(schema.properties)) {
    return "object";
  }

  if (schema.items) {
    return "array";
  }

  return "unknown";
}

function getSchemaFieldKind(schema: JsonSchemaLike): SchemaFormFieldKind {
  if (schema.enum?.length) return "select";

  const type = normalizeSchemaType(schema);
  const format = typeof schema.format === "string" ? schema.format : undefined;

  if (type === "boolean") return "boolean";
  if (type === "number" || type === "integer") return "number";
  if (format === "date") return "date";
  if (format === "date-time") return "datetime";
  if (format === "email") return "email";
  if (type === "object" || type === "array") return "json";
  if (format === "textarea") return "textarea";

  const title = `${schema.title ?? ""} ${schema.description ?? ""}`.toLowerCase();
  if (/(description|body|content|message|note|summary|instructions)/.test(title)) {
    return "textarea";
  }

  return "text";
}

function formatDateInputValue(value: unknown): string {
  if (typeof value === "string") {
    return value.includes("T") ? value.slice(0, 10) : value;
  }

  if (value instanceof Date && !Number.isNaN(value.getTime())) {
    return value.toISOString().slice(0, 10);
  }

  return String(value);
}

function formatDateTimeLocalInputValue(value: unknown): string {
  const date = value instanceof Date ? value : new Date(String(value));
  if (Number.isNaN(date.getTime())) {
    return String(value);
  }

  const pad = (part: number) => String(part).padStart(2, "0");
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}T${pad(date.getHours())}:${pad(date.getMinutes())}`;
}

export function buildSchemaFormFields(
  schema: JsonSchemaLike | null | undefined,
  uiSchema?: Record<string, unknown> | null,
): SchemaFormField[] {
  if (!schema || !isRecord(schema.properties)) return [];

  const required = Array.isArray(schema.required) ? schema.required : [];
  const order = Array.isArray(uiSchema?.["ui:order"])
    ? (uiSchema?.["ui:order"] as unknown[]).filter((entry): entry is string => typeof entry === "string")
    : [];
  const orderIndex = new Map(order.map((name, index) => [name, index]));

  const fields = Object.entries(schema.properties).map(([name, propertySchema]) => {
    const property = isRecord(propertySchema) ? propertySchema as JsonSchemaLike : {};
    const uiFieldConfig = isRecord(uiSchema?.[name]) ? uiSchema?.[name] as Record<string, unknown> : {};
    const widget = typeof uiFieldConfig["ui:widget"] === "string" ? uiFieldConfig["ui:widget"] : undefined;
    const kind = widget === "textarea" ? "textarea" : getSchemaFieldKind(property);

    return {
      name,
      label: typeof property.title === "string" && property.title.trim().length > 0
        ? property.title
        : sentenceCase(name),
      description: typeof property.description === "string" ? property.description : undefined,
      required: required.includes(name),
      kind,
      type: normalizeSchemaType(property),
      format: typeof property.format === "string" ? property.format : undefined,
      options: (property.enum ?? []).map((value) => ({
        label: typeof value === "string" ? value : JSON.stringify(value),
        value: typeof value === "string" ? value : JSON.stringify(value),
      })),
      defaultValue: property.default,
      schema: property,
    } satisfies SchemaFormField;
  });

  return fields.sort((left, right) => {
    const leftIndex = orderIndex.get(left.name);
    const rightIndex = orderIndex.get(right.name);

    if (typeof leftIndex === "number" && typeof rightIndex === "number") {
      return leftIndex - rightIndex;
    }
    if (typeof leftIndex === "number") return -1;
    if (typeof rightIndex === "number") return 1;
    return left.label.localeCompare(right.label);
  });
}

export function formatSchemaFieldValueForForm(field: SchemaFormField, value: unknown): unknown {
  if (value === null || typeof value === "undefined") {
    if (field.kind === "boolean") return false;
    return "";
  }

  if (field.kind === "boolean") return Boolean(value);
  if (field.kind === "number") return String(value);
  if (field.kind === "date") return formatDateInputValue(value);
  if (field.kind === "datetime") return formatDateTimeLocalInputValue(value);
  if (field.kind === "json") {
    if (typeof value === "string") return value;
    try {
      return JSON.stringify(value, null, 2);
    } catch {
      return String(value);
    }
  }

  return String(value);
}

export function buildSchemaFormValues(
  schema: JsonSchemaLike | null | undefined,
  values: Record<string, unknown> = {},
  uiSchema?: Record<string, unknown> | null,
): Record<string, unknown> {
  const fields = buildSchemaFormFields(schema, uiSchema);
  const next: Record<string, unknown> = {};

  fields.forEach((field) => {
    const provided = values[field.name];
    const source = typeof provided !== "undefined" ? provided : field.defaultValue;
    next[field.name] = formatSchemaFieldValueForForm(field, source);
  });

  return next;
}

export function buildSchemaFormPayload(
  schema: JsonSchemaLike | null | undefined,
  values: Record<string, unknown>,
  uiSchema?: Record<string, unknown> | null,
): BuildSchemaFormPayloadResult {
  const fields = buildSchemaFormFields(schema, uiSchema);
  const data: Record<string, unknown> = {};
  const errors: Record<string, string> = {};

  fields.forEach((field) => {
    const rawValue = values[field.name];

    if (field.kind === "boolean") {
      data[field.name] = Boolean(rawValue);
      return;
    }

    if (isBlank(rawValue)) {
      if (field.required) {
        errors[field.name] = `${field.label} is required.`;
      }
      return;
    }

    if (field.kind === "number") {
      const parsed = Number(rawValue);
      if (!Number.isFinite(parsed)) {
        errors[field.name] = `${field.label} must be a valid number.`;
        return;
      }

      if (field.type === "integer" && !Number.isInteger(parsed)) {
        errors[field.name] = `${field.label} must be a whole number.`;
        return;
      }

      data[field.name] = parsed;
      return;
    }

    if (field.kind === "json") {
      try {
        data[field.name] = typeof rawValue === "string" ? JSON.parse(rawValue) : rawValue;
      } catch {
        errors[field.name] = `${field.label} must be valid JSON.`;
      }
      return;
    }

    data[field.name] = rawValue;
  });

  return {
    data,
    errors,
    isValid: Object.keys(errors).length === 0,
  };
}
