"""
Real integrations, backed by Lemma's native connector catalog (no mock adapters).

The catalog (`pod.connectors.apps.list`) is live; connection state comes from
`pod.connectors.status`. Connecting an account goes through Lemma's real OAuth
connect-request. When an org auth-config isn't configured yet (e.g. Google needs
OAuth client credentials, or a valid Composio key), we surface that honestly instead
of pretending the integration works.
"""
import logging
from typing import Any, Dict, List, Optional

from ..sdk_client import get_lemma_pod, run_sync

logger = logging.getLogger("lifeos.connectors")

# Light UI hints layered on top of the live catalog.
CATEGORY = {
    "gmail": "Email", "google_calendar": "Calendar", "google_drive": "Files",
    "google_docs": "Docs", "google_sheets": "Sheets", "slack": "Chat",
    "jira": "Project", "confluence": "Docs", "teams": "Chat",
    "telegram": "Chat", "whatsapp": "Chat",
}


def _norm(o) -> Any:
    if isinstance(o, (dict, list)):
        return o
    for attr in ("to_dict", "model_dump"):
        if hasattr(o, attr):
            try:
                return getattr(o, attr)()
            except Exception:
                pass
    return o


def _norm_key(name: str) -> str:
    return (name or "").replace("_", "").replace("-", "").lower()


def _account_map(status: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    out = {}
    for acc in (status or {}).get("accounts", []) or []:
        cid = _norm_key(acc.get("connector_id") or acc.get("app") or acc.get("toolkit") or "")
        if cid:
            out[cid] = acc
    return out


async def list_integrations() -> List[Dict[str, Any]]:
    """Live catalog merged with per-account connection status."""
    pod = get_lemma_pod()
    try:
        catalog = _norm(await run_sync(pod.connectors.apps.list, limit=100))
        items = catalog.get("items", catalog) if isinstance(catalog, dict) else catalog
    except Exception as e:
        logger.warning(f"connector catalog fetch failed: {e}")
        items = []

    try:
        status = _norm(await run_sync(pod.connectors.status))
    except Exception as e:
        logger.warning(f"connector status fetch failed: {e}")
        status = {"accounts": []}
    accounts = _account_map(status)

    out = []
    for c in items:
        cid = c.get("id") or c.get("name")
        if not cid:
            continue
        acc = accounts.get(_norm_key(cid))
        caps = c.get("provider_capabilities") or []
        auth_scheme = caps[0].get("auth_scheme") if caps else None
        out.append({
            "name": cid,
            "title": c.get("title") or cid.replace("_", " ").title(),
            "description": c.get("description") or "",
            "category": CATEGORY.get(cid, "Integration"),
            "auth_scheme": auth_scheme,
            "is_connected": bool(acc),
            "account_email": (acc or {}).get("email") or (acc or {}).get("account_name") or "",
            "account_id": (acc or {}).get("id") or (acc or {}).get("account_id"),
        })
    out.sort(key=lambda x: (not x["is_connected"], x["title"]))
    return out


async def _ensure_auth_config(pod, app: str) -> Optional[str]:
    """Return the name of an auth-config for this app, creating a system-default one if possible."""
    existing = _norm(await run_sync(pod.connectors.auth_configs.list, limit=100))
    for ac in existing.get("items", existing) if isinstance(existing, dict) else existing:
        connector = ac.get("connector") or ac.get("connector_id") or ac.get("app")
        if _norm_key(connector) == _norm_key(app):
            return ac.get("name")
    name = f"{app}-lifeos"
    await run_sync(pod.connectors.create_auth_config_from_dict, {
        "connector": app, "name": name, "provider": "LEMMA", "config_source": "SYSTEM_DEFAULT",
    })
    return name


async def get_connect_url(app: str) -> str:
    pod = get_lemma_pod()
    try:
        auth_config_name = await _ensure_auth_config(pod, app)
    except Exception as e:
        raise RuntimeError(
            f"{app} needs credentials configured before it can connect. "
            f"Add OAuth client credentials (or a valid Composio API key) for this connector. [{e}]"
        )
    # Resolve auth-config id for the connect request.
    auth_config_id = None
    try:
        ac = _norm(await run_sync(pod.connectors.auth_configs.get, auth_config_name))
        auth_config_id = ac.get("id") or ac.get("auth_config_id")
    except Exception:
        pass
    resp = _norm(await run_sync(pod.connectors.connect_request, app, auth_config_id=auth_config_id))
    for key in ("redirect_url", "url", "authorization_url", "connect_url"):
        if resp.get(key):
            return resp[key]
    attrs = resp.get("attributes") or {}
    for key in ("redirect_url", "url", "authorization_url"):
        if attrs.get(key):
            return attrs[key]
    raise RuntimeError("Connector did not return an authorization URL")


async def disconnect(app: str) -> bool:
    pod = get_lemma_pod()
    try:
        status = _norm(await run_sync(pod.connectors.status))
        for acc in status.get("accounts", []):
            if _norm_key(acc.get("connector_id") or acc.get("app") or "") == _norm_key(app):
                acc_id = acc.get("id") or acc.get("account_id")
                if acc_id:
                    await run_sync(pod.connectors.accounts.delete, str(acc_id))
                    return True
    except Exception as e:
        logger.warning(f"disconnect {app} failed: {e}")
    return False


async def is_connected(app: str) -> bool:
    try:
        pod = get_lemma_pod()
        status = _norm(await run_sync(pod.connectors.status))
        return any(_norm_key(a.get("connector_id") or a.get("app") or "") == _norm_key(app)
                   for a in status.get("accounts", []))
    except Exception:
        return False
