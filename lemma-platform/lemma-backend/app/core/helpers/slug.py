import re


def slugify(text: str) -> str:
    return text.lower().replace(" ", "-")


def normalize_resource_name(name: str) -> str:
    """Normalize a resource name to lowercase with underscores instead of spaces."""
    return name.strip().lower().replace(" ", "_")


def normalize_public_slug(value: str) -> str:
    """Normalize a public DNS-safe slug."""
    normalized = re.sub(r"[^a-z0-9]+", "-", value.strip().lower())
    normalized = re.sub(r"-{2,}", "-", normalized).strip("-")
    return normalized
