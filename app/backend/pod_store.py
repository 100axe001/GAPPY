"""
Lemma-native data layer.

The core LifeOS entities — items (tasks/notes/deadlines/study material), the connection
graph, and the spaced-repetition schedule — live as records in the `lifeos` pod's datastore,
not in local Postgres. This module wraps `pod.records` and returns `Rec` objects that behave
like the old SQLAlchemy models (attribute access, parsed datetimes, `metadata_json`), so the
rest of the app changes as little as possible.

Postgres still holds users, settings/secrets, and chat conversation metadata.
"""
import datetime
from typing import Any, Dict, List, Optional

from .sdk_client import get_lemma_pod, run_sync

ITEMS = "items"
CONNECTIONS = "connections"
STUDY_REVIEWS = "study_reviews"

# Single-tenant local app: all records share one owner (matches the app's existing
# global, non-per-user item behaviour). Kept as a column so RLS/multi-user is a later flip.
DEFAULT_OWNER = "lifeos"

_DT_FIELDS = {"due_date", "created_at", "updated_at", "last_reviewed_at"}


def _parse_dt(value: Any) -> Optional[datetime.datetime]:
    if value in (None, ""):
        return None
    if isinstance(value, datetime.datetime):
        return value.replace(tzinfo=None) if value.tzinfo else value
    try:
        s = str(value).replace("Z", "+00:00")
        dt = datetime.datetime.fromisoformat(s)
        return dt.replace(tzinfo=None) if dt.tzinfo else dt
    except Exception:
        return None


def _iso(value: Any) -> Optional[str]:
    if value in (None, ""):
        return None
    if isinstance(value, datetime.datetime):
        return value.replace(tzinfo=None).isoformat()
    return str(value)


class Rec:
    """Attribute-access wrapper over a Lemma record dict."""

    def __init__(self, raw: Optional[Dict[str, Any]]):
        self._raw = dict(raw or {})

    @property
    def id(self):
        return self._raw.get("id")

    @property
    def metadata_json(self):
        return self._raw.get("metadata") or {}

    @metadata_json.setter
    def metadata_json(self, value):
        self._raw["metadata"] = value or {}

    def __getattr__(self, name):
        # Only called for names not found normally.
        raw = self.__dict__.get("_raw", {})
        if name in _DT_FIELDS:
            return _parse_dt(raw.get(name))
        return raw.get(name)

    def as_dict(self):
        return dict(self._raw)


def _norm(o) -> Dict[str, Any]:
    """Coerce an SDK response (RecordData / model / dict) into a plain dict."""
    if isinstance(o, dict):
        return o
    for attr in ("to_dict", "model_dump"):
        if hasattr(o, attr):
            try:
                return getattr(o, attr)()
            except Exception:
                pass
    return dict(o) if o else {}


async def _list(table: str, *, filter=None, sort=None, limit: int = 500) -> List[Dict[str, Any]]:
    pod = get_lemma_pod()
    resp = await run_sync(pod.records.list, table, limit=limit, filter=filter, sort=sort)
    return _norm(resp).get("items", [])


async def _create(table: str, data: Dict[str, Any]) -> Dict[str, Any]:
    pod = get_lemma_pod()
    return _norm(await run_sync(pod.records.create, table, data))


async def _get(table: str, record_id: str) -> Optional[Dict[str, Any]]:
    pod = get_lemma_pod()
    try:
        return _norm(await run_sync(pod.records.get, table, str(record_id)))
    except Exception:
        return None


async def _update(table: str, record_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    pod = get_lemma_pod()
    return _norm(await run_sync(pod.records.update, table, str(record_id), data))


async def _delete(table: str, record_id: str) -> bool:
    pod = get_lemma_pod()
    try:
        await run_sync(pod.records.delete, table, str(record_id))
        return True
    except Exception:
        return False


# ------------------------------------------------------------------ items

def _item_payload(fields: Dict[str, Any], owner_id: str) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"owner_id": owner_id}
    for key in ("type", "title", "content", "status", "category", "waiting_on", "source"):
        if fields.get(key) is not None:
            payload[key] = fields[key]
    if fields.get("priority"):
        payload["priority"] = str(fields["priority"]).lower()
    if "due_date" in fields:
        iso = _iso(fields.get("due_date"))
        if iso:
            payload["due_date"] = iso
    if fields.get("metadata_json") is not None:
        payload["metadata"] = fields["metadata_json"]
    return payload


async def create_item(item_in, owner_id: str = DEFAULT_OWNER) -> Rec:
    data = item_in.model_dump() if hasattr(item_in, "model_dump") else dict(item_in)
    data.setdefault("status", "todo")
    data.setdefault("source", "manual")
    payload = _item_payload(data, owner_id)
    return Rec(await _create(ITEMS, payload))


async def get_item(item_id) -> Optional[Rec]:
    raw = await _get(ITEMS, item_id)
    return Rec(raw) if raw else None


async def get_items(item_type: Optional[str] = None, owner_id: str = DEFAULT_OWNER,
                    limit: int = 500) -> List[Rec]:
    flt = [{"field": "owner_id", "op": "eq", "value": owner_id}]
    if item_type:
        flt.append({"field": "type", "op": "eq", "value": item_type})
    sort = [{"field": "created_at", "direction": "desc"}]
    rows = await _list(ITEMS, filter=flt, sort=sort, limit=limit)
    return [Rec(r) for r in rows]


async def update_item(item_id, item_in, owner_id: str = DEFAULT_OWNER) -> Optional[Rec]:
    current = await get_item(item_id)
    if not current:
        return None

    update_data = item_in.model_dump(exclude_unset=True) if hasattr(item_in, "model_dump") else dict(item_in)
    was_done = current.status == "done"
    new_status = update_data.get("status")

    payload: Dict[str, Any] = {}
    for key in ("type", "title", "content", "status", "category", "waiting_on"):
        if key in update_data and update_data[key] is not None:
            payload[key] = update_data[key]
    if update_data.get("priority"):
        payload["priority"] = str(update_data["priority"]).lower()
    if "due_date" in update_data:
        payload["due_date"] = _iso(update_data["due_date"])
    if "metadata_json" in update_data and update_data["metadata_json"] is not None:
        payload["metadata"] = update_data["metadata_json"]

    updated = Rec(await _update(ITEMS, item_id, payload)) if payload else current

    # Recurring-task engine: when a recurring task is newly completed, spawn its next instance.
    if new_status == "done" and not was_done:
        meta = updated.metadata_json or {}
        if meta.get("is_recurring") is True:
            interval = meta.get("recurrence_interval", "daily")
            custom_days = meta.get("recurrence_custom_days")
            base_date = updated.due_date or datetime.datetime.utcnow()
            if interval == "weekly":
                next_due = base_date + datetime.timedelta(weeks=1)
            elif interval == "monthly":
                next_due = base_date + datetime.timedelta(days=30)
            elif interval == "custom" and custom_days:
                next_due = base_date + datetime.timedelta(days=int(custom_days))
            else:
                next_due = base_date + datetime.timedelta(days=1)

            nxt = await _create(ITEMS, _item_payload({
                "type": updated.type, "title": updated.title, "content": updated.content,
                "status": "todo", "priority": updated.priority, "due_date": next_due,
                "metadata_json": meta, "source": "recurrence",
            }, owner_id))
            await create_connection_raw(str(updated.id), str(nxt["id"]), "recurrence_next", owner_id)

    return updated


async def delete_item(item_id) -> bool:
    return await _delete(ITEMS, item_id)


# ------------------------------------------------------------ connections

async def create_connection_raw(source_id: str, target_id: str, connection_type: str,
                                owner_id: str = DEFAULT_OWNER, reason: str = "") -> Dict[str, Any]:
    return await _create(CONNECTIONS, {
        "source_id": str(source_id), "target_id": str(target_id),
        "connection_type": connection_type, "reason": reason, "owner_id": owner_id,
    })


async def create_connection(conn_in, owner_id: str = DEFAULT_OWNER) -> Rec:
    return Rec(await create_connection_raw(
        conn_in.source_id, conn_in.target_id, conn_in.connection_type, owner_id))


async def _detail(conn: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    source = await get_item(conn.get("source_id"))
    target = await get_item(conn.get("target_id"))
    if not source or not target:
        return None
    return {
        "id": conn.get("id"),
        "source_id": conn.get("source_id"),
        "target_id": conn.get("target_id"),
        "connection_type": conn.get("connection_type"),
        "created_at": _parse_dt(conn.get("created_at")) or datetime.datetime.utcnow(),
        "source_title": source.title, "source_type": source.type,
        "target_title": target.title, "target_type": target.type,
    }


async def get_connections(owner_id: str = DEFAULT_OWNER, limit: int = 200) -> List[Dict[str, Any]]:
    flt = [{"field": "owner_id", "op": "eq", "value": owner_id}]
    rows = await _list(CONNECTIONS, filter=flt, limit=limit)
    out = []
    for c in rows:
        d = await _detail(c)
        if d:
            out.append(d)
    return out


async def get_connections_by_item_id(item_id, owner_id: str = DEFAULT_OWNER) -> List[Dict[str, Any]]:
    rows = await _list(CONNECTIONS, filter=[{"field": "owner_id", "op": "eq", "value": owner_id}], limit=500)
    sid = str(item_id)
    out = []
    for c in rows:
        if str(c.get("source_id")) == sid or str(c.get("target_id")) == sid:
            d = await _detail(c)
            if d:
                out.append(d)
    return out


async def delete_connection(connection_id) -> bool:
    return await _delete(CONNECTIONS, connection_id)


# --------------------------------------------------------- study reviews

_INTERVALS = {1: 3, 3: 7, 7: 14, 14: 30, 30: 30}


async def get_study_review_by_concept(concept_id, owner_id: str = DEFAULT_OWNER) -> Optional[Rec]:
    rows = await _list(STUDY_REVIEWS, filter=[
        {"field": "owner_id", "op": "eq", "value": owner_id},
        {"field": "concept_id", "op": "eq", "value": str(concept_id)},
    ], limit=1)
    return Rec(rows[0]) if rows else None


async def create_study_review(concept_id, owner_id: str = DEFAULT_OWNER,
                              concept_title: str = "") -> Rec:
    existing = await get_study_review_by_concept(concept_id, owner_id)
    if existing:
        return existing
    due = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    return Rec(await _create(STUDY_REVIEWS, {
        "concept_id": str(concept_id), "concept_title": concept_title,
        "interval_days": 1, "due_date": _iso(due), "status": "learning", "owner_id": owner_id,
    }))


async def get_due_study_reviews(owner_id: str = DEFAULT_OWNER) -> List[Dict[str, Any]]:
    now = datetime.datetime.utcnow()
    rows = await _list(STUDY_REVIEWS, filter=[{"field": "owner_id", "op": "eq", "value": owner_id}], limit=500)
    enriched = []
    for r in rows:
        due = _parse_dt(r.get("due_date"))
        if due and due > now:
            continue
        concept = await get_item(r.get("concept_id"))
        enriched.append({
            "id": r.get("id"),
            "user_id": owner_id,
            "concept_id": r.get("concept_id"),
            "interval_days": r.get("interval_days") or 1,
            "due_date": due or now,
            "last_reviewed_at": _parse_dt(r.get("last_reviewed_at")),
            "status": r.get("status") or "learning",
            "created_at": _parse_dt(r.get("created_at")) or now,
            "concept_title": (concept.title if concept else r.get("concept_title")) or "Concept",
            "concept_content": concept.content if concept else "",
        })
    return enriched


async def update_study_review(review_id, score: int) -> Optional[Rec]:
    raw = await _get(STUDY_REVIEWS, review_id)
    if not raw:
        return None
    interval = raw.get("interval_days") or 1
    if score >= 2:
        interval = _INTERVALS.get(interval, 1)
        status = "learned" if interval == 30 else "learning"
    else:
        interval = 1
        status = "learning"
    now = datetime.datetime.utcnow()
    payload = {
        "interval_days": interval,
        "status": status,
        "last_reviewed_at": _iso(now),
        "due_date": _iso(now + datetime.timedelta(days=interval)),
    }
    return Rec(await _update(STUDY_REVIEWS, review_id, payload))
