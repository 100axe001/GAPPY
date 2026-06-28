const RESERVED_APP_PAGE_SLUGS = new Set([
    'new',
    'view',
    'pages',
    'settings',
    'api',
]);

export function normalizeAppPageSlug(raw: string): string {
    const normalized = raw
        .trim()
        .toLowerCase()
        .replace(/[_\s]+/g, '-')
        .replace(/[^a-z0-9-]/g, '')
        .replace(/-+/g, '-')
        .replace(/^-+|-+$/g, '');

    return normalized || 'page';
}

export function createUniqueAppPageSlug(input: {
    title?: string;
    preferredSlug?: string;
    existingSlugs?: Iterable<string>;
}): string {
    const baseCandidate = input.preferredSlug || input.title || 'page';
    const base = normalizeAppPageSlug(baseCandidate);
    const taken = new Set(
        Array.from(input.existingSlugs || [])
            .map((slug) => normalizeAppPageSlug(slug))
    );

    let candidate = base;
    if (RESERVED_APP_PAGE_SLUGS.has(candidate)) {
        candidate = `${candidate}-1`;
    }

    if (!taken.has(candidate)) {
        return candidate;
    }

    let index = 2;
    while (true) {
        const next = `${base}-${index}`;
        if (!taken.has(next) && !RESERVED_APP_PAGE_SLUGS.has(next)) {
            return next;
        }
        index += 1;
    }
}

export function isReservedAppPageSlug(slug: string): boolean {
    return RESERVED_APP_PAGE_SLUGS.has(normalizeAppPageSlug(slug));
}
