export type PreviewField = {
    key: string;
    label: string;
    value: string;
};

export function isRecord(value: unknown): value is Record<string, unknown> {
    return !!value && typeof value === 'object' && !Array.isArray(value);
}

function hasPreviewValue(value: unknown): boolean {
    if (value === null || typeof value === 'undefined') return false;
    if (typeof value === 'string') return value.trim().length > 0;
    if (Array.isArray(value)) return value.length > 0;
    if (isRecord(value)) return Object.keys(value).length > 0;
    return true;
}

export function formatFieldLabel(key: string): string {
    return key
        .replace(/[_-]+/g, ' ')
        .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
        .replace(/\s+/g, ' ')
        .trim()
        .replace(/\b\w/g, (char) => char.toUpperCase());
}

export function formatPreviewValue(value: unknown): string {
    if (typeof value === 'string') return value.trim();
    if (typeof value === 'number' || typeof value === 'boolean') return String(value);
    if (Array.isArray(value)) {
        return value
            .map((item) => formatPreviewValue(item))
            .filter(Boolean)
            .join(', ');
    }
    if (isRecord(value)) {
        try {
            return JSON.stringify(value);
        } catch {
            return '';
        }
    }
    return '';
}

function getSchemaOrderedKeys(schema: unknown): string[] {
    if (!isRecord(schema) || !isRecord(schema.properties)) return [];
    return Object.keys(schema.properties);
}

export function getPreviewFields(inputData: unknown, schema?: unknown): PreviewField[] {
    if (!isRecord(inputData)) return [];

    const schemaKeys = getSchemaOrderedKeys(schema);
    const orderedKeys = schemaKeys.length > 0
        ? [
            ...schemaKeys,
            ...Object.keys(inputData).filter((key) => !schemaKeys.includes(key)),
        ]
        : Object.keys(inputData);

    return orderedKeys
        .filter((key) => hasPreviewValue(inputData[key]))
        .map((key) => ({
            key,
            label: formatFieldLabel(key),
            value: formatPreviewValue(inputData[key]),
        }))
        .filter((field) => field.value.length > 0);
}

export function truncatePreview(text: string, maxLength: number): string {
    const normalized = text.replace(/\s+/g, ' ').trim();
    if (normalized.length <= maxLength) return normalized;
    return `${normalized.slice(0, maxLength - 1).trim()}...`;
}
