// Shared JSON-Schema → form helpers used by both the standalone forms/view page
// and the inline "form over the composer" panel. Pure functions only (no JSX) so
// they can be imported from anywhere without pulling in React component deps.

import type { DisplayResourceRequest } from "./display-resource";

export type FormValues = Record<string, unknown>;
export type FormErrors = Record<string, string>;

export function asRecord(value: unknown): Record<string, unknown> {
    return value && typeof value === "object" && !Array.isArray(value)
        ? value as Record<string, unknown>
        : {};
}

export function asString(value: unknown): string | undefined {
    return typeof value === "string" && value.trim().length > 0 ? value.trim() : undefined;
}

export function humanizeLabel(value: string | undefined, fallback: string): string {
    const cleaned = (value || fallback)
        .replace(/[_-]+/g, " ")
        .replace(/\s+/g, " ")
        .trim();
    if (!cleaned) return fallback;
    return cleaned
        .split(" ")
        .map((part) => part.charAt(0).toUpperCase() + part.slice(1).toLowerCase())
        .join(" ");
}

export function schemaProperties(schema: Record<string, unknown>): Record<string, unknown> {
    return asRecord(schema.properties);
}

export function schemaRequired(schema: Record<string, unknown>): string[] {
    return Array.isArray(schema.required)
        ? schema.required.filter((entry): entry is string => typeof entry === "string")
        : [];
}

export function fieldType(field: Record<string, unknown>): string {
    const rawType = field.type;
    if (Array.isArray(rawType)) {
        return rawType.find((entry) => typeof entry === "string" && entry !== "null") as string | undefined || "string";
    }
    return typeof rawType === "string" ? rawType : "string";
}

export function initialValue(field: Record<string, unknown>): unknown {
    if ("default" in field) return field.default;
    const type = fieldType(field);
    if (type === "boolean") return false;
    if (type === "array") return "";
    if (type === "object") return "{}";
    return "";
}

export function buildInitialValues(schema: Record<string, unknown>): FormValues {
    return Object.fromEntries(
        Object.entries(schemaProperties(schema)).map(([key, rawField]) => [key, initialValue(asRecord(rawField))]),
    );
}

export function coerceValue(value: unknown, field: Record<string, unknown>): unknown {
    const type = fieldType(field);
    if (type === "integer") {
        const parsed = Number.parseInt(String(value), 10);
        return Number.isFinite(parsed) ? parsed : value;
    }
    if (type === "number") {
        const parsed = Number.parseFloat(String(value));
        return Number.isFinite(parsed) ? parsed : value;
    }
    if (type === "boolean") {
        return Boolean(value);
    }
    if (type === "array") {
        if (Array.isArray(value)) return value;
        const text = String(value || "").trim();
        if (!text) return [];
        if (text.startsWith("[")) {
            try {
                return JSON.parse(text);
            } catch {
                return text.split(/\r?\n|,/).map((entry) => entry.trim()).filter(Boolean);
            }
        }
        return text.split(/\r?\n|,/).map((entry) => entry.trim()).filter(Boolean);
    }
    if (type === "object") {
        if (value && typeof value === "object") return value;
        const text = String(value || "").trim();
        if (!text) return {};
        try {
            return JSON.parse(text);
        } catch {
            return value;
        }
    }
    return typeof value === "string" ? value.trim() : value;
}

export function isFieldEmpty(value: unknown): boolean {
    return value === null || typeof value === "undefined" || String(value).trim().length === 0;
}

export function validate(values: FormValues, schema: Record<string, unknown>): FormErrors {
    const properties = schemaProperties(schema);
    const required = new Set(schemaRequired(schema));
    const errors: FormErrors = {};

    Object.entries(properties).forEach(([key, rawField]) => {
        if (!required.has(key)) return;
        const field = asRecord(rawField);
        const value = values[key];
        if (fieldType(field) === "boolean") return;
        if (isFieldEmpty(value)) {
            errors[key] = "Required";
        }
    });

    return errors;
}

export function coerceFormValues(values: FormValues, schema: Record<string, unknown>): FormValues {
    return Object.fromEntries(
        Object.entries(schemaProperties(schema)).map(([key, rawField]) => [
            key,
            coerceValue(values[key], asRecord(rawField)),
        ]),
    );
}

export function formatSubmittedFormMessage({
    request,
    values,
}: {
    request: DisplayResourceRequest;
    values: FormValues;
}): string {
    const label = request.name || asString(request.jsonSchema?.title) || "Form";
    return [
        `Submitted form: ${label}`,
        "",
        "Please continue with these answers.",
        "",
        "```json",
        JSON.stringify(values, null, 2),
        "```",
    ].join("\n");
}
