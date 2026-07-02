import os
import json
import time
import base64
import asyncio
import threading
from pathlib import Path
from lemma_sdk import Pod

# The LifeOS pod is provisioned by pod/lifeos (see app/provision.py). Its id and org id
# are injected via env (docker-compose) with sane local defaults so the app never crashes.
DEFAULT_ORG_ID = "019f0d47-91d9-7314-9376-8a2a47900bea"
DEFAULT_POD_ID = "019f2007-060b-7316-92ad-7dd7253147b8"

_lock = threading.Lock()
_state = {"token": None, "refresh": None, "base_url": None, "org_id": None, "pod_id": None}


def _load_config_auth():
    for path in (Path("/root/.lemma/config.json"), Path.home() / ".lemma" / "config.json"):
        if path.exists():
            try:
                with open(path) as f:
                    cfg = json.load(f)
                active = cfg.get("active_server", "local")
                server = cfg.get("servers", {}).get(active, {})
                auth = server.get("auth", {})
                defaults = server.get("defaults", {})
                return {
                    "token": auth.get("access_token") or server.get("token"),
                    "refresh": auth.get("refresh_token") or server.get("refresh_token"),
                    "base_url": auth.get("base_url") or server.get("base_url"),
                    "pod_id": defaults.get("pod_id"),
                    "org_id": defaults.get("org_id"),
                }
            except Exception:
                pass
    return {}


def _jwt_exp(token: str):
    try:
        payload = token.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        data = json.loads(base64.urlsafe_b64decode(payload))
        return data.get("exp")
    except Exception:
        return None


def _resolve_base_url(cfg_base: str) -> str:
    base = os.getenv("LEMMA_BASE_URL") or cfg_base
    if os.path.exists("/.dockerenv") and (not base or "sslip.io" in (base or "") or "localhost" in (base or "")):
        base = "http://lemma-local-backend:8000"
    return base


def _refresh_token():
    """Refresh the access token using the stored refresh token (SuperTokens CLI refresh)."""
    from lemma_sdk.auth import refresh_cli_session
    rt = _state.get("refresh")
    base = _state.get("base_url")
    if not rt or not base:
        return False
    try:
        res = refresh_cli_session(base_url=base, refresh_token=rt, verify_ssl=False, timeout=15)
    except Exception:
        return False
    new_access = res.get("access_token") or (res.get("auth") or {}).get("access_token")
    new_refresh = res.get("refresh_token") or (res.get("auth") or {}).get("refresh_token")
    if new_access:
        _state["token"] = new_access
        if new_refresh:
            _state["refresh"] = new_refresh
        return True
    return False


def _ensure_state():
    if _state["token"] is None:
        cfg = _load_config_auth()
        _state["token"] = os.getenv("LEMMA_TOKEN") or cfg.get("token")
        _state["refresh"] = cfg.get("refresh")
        _state["base_url"] = _resolve_base_url(cfg.get("base_url"))
        _state["org_id"] = os.getenv("LEMMA_ORG_ID") or cfg.get("org_id") or DEFAULT_ORG_ID
        _state["pod_id"] = os.getenv("LEMMA_POD_ID") or cfg.get("pod_id") or DEFAULT_POD_ID

    # Proactively refresh if the access token is missing or within 2 min of expiry.
    exp = _jwt_exp(_state["token"] or "")
    if not _state["token"] or (exp and exp - time.time() < 120):
        _refresh_token()


def get_lemma_pod() -> Pod:
    with _lock:
        _ensure_state()
        if not _state["token"]:
            raise RuntimeError("LEMMA token not found in env or ~/.lemma/config.json")
        os.environ["LEMMA_SSL_NO_VERIFY"] = "1"
        return Pod(
            pod_id=_state["pod_id"],
            org_id=_state["org_id"],
            token=_state["token"],
            base_url=_state["base_url"],
            verify_ssl=False,
        )


def force_refresh():
    with _lock:
        return _refresh_token()


async def run_sync(fn, *args, **kwargs):
    """Run a blocking SDK call off the event loop, refreshing + retrying once on auth expiry."""
    try:
        return await asyncio.to_thread(fn, *args, **kwargs)
    except Exception as e:
        if "401" in str(e) or "expired" in str(e).lower():
            with _lock:
                _refresh_token()
            return await asyncio.to_thread(fn, *args, **kwargs)
        raise
