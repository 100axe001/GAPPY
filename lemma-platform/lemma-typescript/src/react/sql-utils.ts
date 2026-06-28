import type { RecordFilter } from "../types.js";

function quoteIdentifierPart(value: string): string {
  return `"${value.replace(/"/g, "\"\"")}"`;
}

export function quoteIdentifierPath(value: string): string {
  return value
    .split(".")
    .map((part) => (part === "*" ? part : quoteIdentifierPart(part)))
    .join(".");
}

export function isSimpleIdentifierPath(value: string): boolean {
  return /^[A-Za-z_][A-Za-z0-9_$]*(\.(\*|[A-Za-z_][A-Za-z0-9_$]*))*$/.test(value);
}

export function renderIdentifierPath(value: string): string {
  return isSimpleIdentifierPath(value) ? quoteIdentifierPath(value) : value;
}

export function escapeSqlString(value: string): string {
  return value.replace(/'/g, "''");
}

export function encodeSqlValue(value: unknown): string {
  if (value === null || typeof value === "undefined") return "NULL";
  if (typeof value === "boolean") return value ? "TRUE" : "FALSE";
  if (typeof value === "number") {
    if (!Number.isFinite(value)) {
      throw new Error("SQL values must be finite numbers.");
    }
    return String(value);
  }
  if (typeof value === "bigint") return String(value);
  if (value instanceof Date) return `'${escapeSqlString(value.toISOString())}'`;
  if (Array.isArray(value)) {
    return `(${value.map((entry) => encodeSqlValue(entry)).join(", ")})`;
  }
  if (typeof value === "object") {
    return `'${escapeSqlString(JSON.stringify(value))}'`;
  }
  return `'${escapeSqlString(String(value))}'`;
}

export function renderRecordFilter(filter: RecordFilter): string {
  const field = filter.field?.trim();
  if (!field) {
    throw new Error("Record filters require a field.");
  }

  const operator = filter.op.trim().toUpperCase();
  const lhs = renderIdentifierPath(field);
  const values = Array.isArray(filter.values) ? filter.values : undefined;

  if ((operator === "IN" || operator === "NOT IN") && values) {
    return `${lhs} ${operator} ${encodeSqlValue(values)}`;
  }

  if ((operator === "IS" || operator === "IS NOT") && typeof filter.value === "undefined") {
    return `${lhs} ${operator} NULL`;
  }

  return `${lhs} ${operator} ${encodeSqlValue(filter.value)}`;
}

export function renderRecordFilters(filters?: RecordFilter[]): string {
  if (!filters?.length) return "";
  return filters.map((filter) => `(${renderRecordFilter(filter)})`).join(" AND ");
}
