export interface ForeignKeyReference {
  table: string;
  column: string;
}

export interface JoinedRecordsSource {
  table: string;
  alias?: string;
}

export interface JoinedRecordsColumnRef {
  table?: string;
  column: string;
}

export interface JoinedRecordsSelectField {
  table?: string;
  column?: string;
  expression?: string;
  as?: string;
}

export interface JoinedRecordsJoinCondition {
  left: string | JoinedRecordsColumnRef;
  right: string | JoinedRecordsColumnRef;
  operator?: "=" | "!=" | "<>" | ">" | ">=" | "<" | "<=";
}

export interface JoinedRecordsJoin {
  type?: "inner" | "left" | "left outer" | "right" | "right outer" | "full" | "full outer";
  table: string;
  alias?: string;
  on: string | JoinedRecordsJoinCondition;
}

export interface JoinedRecordsFilter {
  field?: string | JoinedRecordsColumnRef;
  expression?: string;
  operator?: "=" | "!=" | "<>" | ">" | ">=" | "<" | "<=" | "LIKE" | "ILIKE" | "IN" | "NOT IN" | "IS" | "IS NOT";
  value?: unknown;
  values?: unknown[];
}

export interface JoinedRecordsOrderBy {
  field?: string | JoinedRecordsColumnRef;
  expression?: string;
  direction?: "asc" | "desc";
  nulls?: "first" | "last";
}

export interface JoinedRecordsQueryDefinition {
  from: string | JoinedRecordsSource;
  select?: Array<string | JoinedRecordsSelectField>;
  joins?: JoinedRecordsJoin[];
  filters?: JoinedRecordsFilter[];
  orderBy?: Array<string | JoinedRecordsOrderBy>;
  limit?: number;
  offset?: number;
  distinct?: boolean;
}

function quoteIdentifierPart(value: string): string {
  return `"${value.replace(/"/g, "\"\"")}"`;
}

function quoteIdentifierPath(value: string): string {
  return value
    .split(".")
    .map((part) => (part === "*" ? part : quoteIdentifierPart(part)))
    .join(".");
}

function isSimpleIdentifierPath(value: string): boolean {
  return /^[A-Za-z_][A-Za-z0-9_$]*(\.(\*|[A-Za-z_][A-Za-z0-9_$]*))*$/.test(value);
}

function renderIdentifierOrExpression(value: string): string {
  return isSimpleIdentifierPath(value) ? quoteIdentifierPath(value) : value;
}

function renderColumnRef(value: string | JoinedRecordsColumnRef): string {
  if (typeof value === "string") {
    return renderIdentifierOrExpression(value);
  }

  const tablePrefix = value.table ? `${quoteIdentifierPart(value.table)}.` : "";
  if (value.column === "*") {
    return `${tablePrefix}*`;
  }
  return `${tablePrefix}${quoteIdentifierPart(value.column)}`;
}

function renderSource(source: string | JoinedRecordsSource): string {
  if (typeof source === "string") {
    return renderIdentifierOrExpression(source);
  }

  const renderedTable = quoteIdentifierPart(source.table);
  if (!source.alias) return renderedTable;
  return `${renderedTable} AS ${quoteIdentifierPart(source.alias)}`;
}

function escapeSqlString(value: string): string {
  return value.replace(/'/g, "''");
}

function encodeSqlValue(value: unknown): string {
  if (value === null || typeof value === "undefined") return "NULL";
  if (typeof value === "boolean") return value ? "TRUE" : "FALSE";
  if (typeof value === "number") {
    if (!Number.isFinite(value)) {
      throw new Error("Joined record query values must be finite numbers.");
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

function renderSelectField(field: string | JoinedRecordsSelectField): string {
  if (typeof field === "string") {
    return renderIdentifierOrExpression(field);
  }

  const base = field.expression
    ? field.expression
    : renderColumnRef({
      table: field.table,
      column: field.column || "*",
    });

  if (!field.as) return base;
  return `${base} AS ${quoteIdentifierPart(field.as)}`;
}

function renderJoinCondition(condition: string | JoinedRecordsJoinCondition): string {
  if (typeof condition === "string") {
    return condition;
  }

  return `${renderColumnRef(condition.left)} ${condition.operator ?? "="} ${renderColumnRef(condition.right)}`;
}

function renderJoin(join: JoinedRecordsJoin): string {
  const joinType = (join.type ?? "left").toUpperCase();
  const source = renderSource({ table: join.table, alias: join.alias });
  return `${joinType} JOIN ${source} ON ${renderJoinCondition(join.on)}`;
}

function renderFilter(filter: JoinedRecordsFilter): string {
  const lhs = filter.expression
    ? filter.expression
    : filter.field
      ? renderColumnRef(filter.field)
      : null;

  if (!lhs) {
    throw new Error("Joined record filters require either `expression` or `field`.");
  }

  const operator = (filter.operator ?? "=").toUpperCase();
  const values = Array.isArray(filter.values) ? filter.values : undefined;
  const rhs = values ? encodeSqlValue(values) : encodeSqlValue(filter.value);

  if ((operator === "IN" || operator === "NOT IN") && !values) {
    return `${lhs} ${operator} (${rhs})`;
  }

  return `${lhs} ${operator} ${rhs}`;
}

function renderOrderBy(orderBy: string | JoinedRecordsOrderBy): string {
  if (typeof orderBy === "string") {
    return renderIdentifierOrExpression(orderBy);
  }

  const base = orderBy.expression
    ? orderBy.expression
    : orderBy.field
      ? renderColumnRef(orderBy.field)
      : null;

  if (!base) {
    throw new Error("Joined record sort entries require either `expression` or `field`.");
  }

  const direction = (orderBy.direction ?? "asc").toUpperCase();
  const nulls = orderBy.nulls ? ` NULLS ${orderBy.nulls.toUpperCase()}` : "";
  return `${base} ${direction}${nulls}`;
}

function normalizePositiveInteger(value: unknown, field: string): number | undefined {
  if (typeof value === "undefined" || value === null) return undefined;
  const parsed = Number(value);
  if (!Number.isFinite(parsed) || parsed < 0) {
    throw new Error(`${field} must be a non-negative number.`);
  }
  return Math.floor(parsed);
}

export function parseForeignKeyReference(references: string): ForeignKeyReference | null {
  const value = references.trim();
  const separator = value.indexOf(".");
  if (separator <= 0 || separator === value.length - 1) {
    return null;
  }

  return {
    table: value.slice(0, separator),
    column: value.slice(separator + 1),
  };
}

export function buildJoinedRecordsQuery(definition: JoinedRecordsQueryDefinition): string {
  const select = definition.select?.length
    ? definition.select.map((field) => renderSelectField(field)).join(", ")
    : "*";
  const distinct = definition.distinct ? "DISTINCT " : "";
  const from = renderSource(definition.from);
  const joins = definition.joins?.length ? ` ${definition.joins.map((join) => renderJoin(join)).join(" ")}` : "";
  const where = definition.filters?.length
    ? ` WHERE ${definition.filters.map((filter) => renderFilter(filter)).join(" AND ")}`
    : "";
  const orderBy = definition.orderBy?.length
    ? ` ORDER BY ${definition.orderBy.map((entry) => renderOrderBy(entry)).join(", ")}`
    : "";
  const limit = normalizePositiveInteger(definition.limit, "limit");
  const offset = normalizePositiveInteger(definition.offset, "offset");
  const limitClause = typeof limit === "number" ? ` LIMIT ${limit}` : "";
  const offsetClause = typeof offset === "number" ? ` OFFSET ${offset}` : "";

  return `SELECT ${distinct}${select} FROM ${from}${joins}${where}${orderBy}${limitClause}${offsetClause}`.trim();
}
