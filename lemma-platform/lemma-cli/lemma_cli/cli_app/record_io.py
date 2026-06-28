"""Shared record import/export IO: read/write CSV, JSONL, and JSON arrays, and
page a table's rows out of the backend. Used by the `records` commands and by
the pod-bundle `--with-data` flow so both round-trip rows identically."""

from __future__ import annotations

import csv
import io
import json
import re
from pathlib import Path
from typing import Any

# Default ceiling on rows pulled per table; bulk endpoints have no server cap,
# so the client bounds the volume (and the bundle keeps exports modest).
RECORD_EXPORT_DEFAULT_LIMIT = 10_000
_RECORD_EXPORT_PAGE = 1_000


def coerce_csv_value(value: str) -> object | None:
    """Light type coercion for CSV cells: empty -> omitted, true/false -> bool,
    ints/floats -> numbers, JSON-looking objects/arrays -> parsed, else the raw
    string. JSONL/JSON rows are already typed and skip this.

    Numeric coercion is conservative — a number is only parsed when it round-
    trips exactly, so identifiers like "007", "1_000", or "+1-555" survive as
    strings instead of silently becoming 7, 1000, or an error."""
    if value == "":
        return None
    s = value.strip()
    low = s.lower()
    if low in {"true", "false"}:
        return low == "true"
    if re.fullmatch(r"-?[0-9]+", s) and str(int(s)) == s:
        return int(s)
    if re.fullmatch(r"-?[0-9]+\.[0-9]+", s):
        return float(s)
    if s[:1] in "[{" and s[-1:] in "]}":
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            return value
    return value


def read_record_rows(path: Path, fmt: str | None) -> list[dict]:
    """Read rows from a CSV, JSONL, or JSON-array file."""
    suffix = (fmt or path.suffix.lstrip(".")).lower()
    text = path.read_text(encoding="utf-8")
    if suffix in {"jsonl", "ndjson"}:
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    if suffix == "json":
        data = json.loads(text)
        return data if isinstance(data, list) else [data]
    rows: list[dict] = []
    for raw in csv.DictReader(text.splitlines()):
        rows.append(
            {
                key: value
                for key, value in (
                    (key, coerce_csv_value(value)) for key, value in raw.items()
                )
                if value is not None
            }
        )
    return rows


def fetch_records_capped(pod_sdk: Any, table: str, limit: int) -> list[dict]:
    """Page through a table's records (offset paging) up to ``limit`` rows."""
    from ..cli_core.io import to_plain

    rows: list[dict] = []
    offset = 0
    while len(rows) < limit:
        want = min(_RECORD_EXPORT_PAGE, limit - len(rows))
        batch = to_plain(pod_sdk.records.list(table, limit=want, offset=offset))
        items = batch.get("items") or []
        rows.extend(items)
        offset += len(items)
        total = batch.get("total")
        if not items or len(items) < want:
            break
        if total is not None and offset >= total:
            break
    return rows[:limit]


def _csv_cell(value: object) -> str:
    """Render a record value as a CSV cell: complex values become JSON text so
    they survive a round-trip; None becomes an empty cell."""
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def write_export_rows(path: Path, rows: list[dict], fmt: str | None) -> None:
    """Write records to ``path`` as CSV (default), JSONL, or a JSON array."""
    suffix = (fmt or path.suffix.lstrip(".")).lower()
    if suffix in {"jsonl", "ndjson"}:
        body = "\n".join(json.dumps(row, ensure_ascii=False) for row in rows)
        path.write_text(body + ("\n" if rows else ""), encoding="utf-8")
        return
    if suffix == "json":
        path.write_text(
            json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        return
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow({key: _csv_cell(row.get(key)) for key in fieldnames})
    path.write_text(buffer.getvalue(), encoding="utf-8")
