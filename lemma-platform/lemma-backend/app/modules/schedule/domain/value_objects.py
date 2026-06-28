from __future__ import annotations

from enum import Enum
from typing import Iterable


class DatastoreOperation(str, Enum):
    INSERT = "INSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


def parse_datastore_operation(value: str | DatastoreOperation) -> DatastoreOperation:
    """Parse a single operation. Only INSERT, UPDATE, DELETE are accepted."""
    if isinstance(value, DatastoreOperation):
        return value
    try:
        return DatastoreOperation(value.strip().upper())
    except ValueError as exc:
        raise ValueError(
            "Invalid datastore operation. Use INSERT, UPDATE, or DELETE."
        ) from exc


def normalize_datastore_operations(
    values: Iterable[str | DatastoreOperation],
) -> list[DatastoreOperation]:
    """Validate, canonicalize, and dedupe a list of operations."""
    deduped: list[DatastoreOperation] = []
    seen: set[DatastoreOperation] = set()
    for raw in values:
        if isinstance(raw, DatastoreOperation):
            op = raw
        elif isinstance(raw, str):
            if not raw.strip():
                continue
            op = parse_datastore_operation(raw)
        else:
            raise ValueError("operations entries must be strings")
        if op not in seen:
            deduped.append(op)
            seen.add(op)
    return deduped
