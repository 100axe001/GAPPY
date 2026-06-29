"""
Per-user application settings (LLM provider, web search, email credentials).

Secret values are encrypted at rest with the existing Fernet helper. The
frontend never receives raw secret values back — only a boolean "<key>_set"
flag indicating whether a value is stored.
"""
import logging
from typing import Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .security import encrypt_data, decrypt_data

logger = logging.getLogger("lifeos.settings")

# Declarative schema of every configurable setting.
# secret=True -> encrypted at rest and masked in API responses.
SETTING_DEFS: Dict[str, Dict[str, Any]] = {
    # --- LLM provider ---
    "llm_provider":      {"secret": False, "default": "lemma"},   # lemma | anthropic | openai
    "llm_model":         {"secret": False, "default": ""},        # optional model override
    "anthropic_api_key": {"secret": True,  "default": ""},
    "openai_api_key":    {"secret": True,  "default": ""},

    # --- Web search ---
    "web_search_provider": {"secret": False, "default": "tavily"},  # tavily | searxng
    "tavily_api_key":      {"secret": True,  "default": ""},
    "searxng_url":         {"secret": False, "default": ""},        # e.g. https://searx.example.com

    # --- Email (Gmail IMAP/SMTP with App Password) ---
    "email_address":     {"secret": False, "default": ""},
    "email_app_password": {"secret": True, "default": ""},
    "imap_host":         {"secret": False, "default": "imap.gmail.com"},
    "smtp_host":         {"secret": False, "default": "smtp.gmail.com"},
    "smtp_port":         {"secret": False, "default": "587"},

    # --- Memory ---
    "auto_memory_enabled": {"secret": False, "default": "true"},
}

SECRET_PLACEHOLDER = "__KEEP__"  # frontend sends this to leave a secret unchanged


def _is_secret(key: str) -> bool:
    return SETTING_DEFS.get(key, {}).get("secret", False)


async def get_resolved_settings(db: AsyncSession, user_id: int) -> Dict[str, str]:
    """Returns the full settings dict with secrets decrypted, for backend use only."""
    rows = await crud.get_all_settings(db, user_id)
    stored = {r.key: r for r in rows}
    resolved: Dict[str, str] = {}
    for key, defn in SETTING_DEFS.items():
        row = stored.get(key)
        if row is None or row.value is None:
            resolved[key] = defn.get("default", "")
            continue
        if defn.get("secret"):
            try:
                resolved[key] = decrypt_data(row.value)
            except Exception as e:
                logger.warning(f"Failed to decrypt setting '{key}': {e}")
                resolved[key] = ""
        else:
            resolved[key] = row.value
    return resolved


async def get_masked_settings(db: AsyncSession, user_id: int) -> Dict[str, Any]:
    """Returns settings safe to send to the client (secrets masked, with *_set flags)."""
    resolved = await get_resolved_settings(db, user_id)
    out: Dict[str, Any] = {}
    for key, defn in SETTING_DEFS.items():
        if defn.get("secret"):
            out[key] = ""  # never expose
            out[f"{key}_set"] = bool(resolved.get(key))
        else:
            out[key] = resolved.get(key, defn.get("default", ""))
    return out


async def update_settings(db: AsyncSession, user_id: int, values: Dict[str, Any]) -> Dict[str, Any]:
    """Persists provided settings. Unknown keys are ignored. Secrets are encrypted.
    A secret value equal to SECRET_PLACEHOLDER (or empty string) leaves the stored value untouched."""
    for key, raw in values.items():
        if key not in SETTING_DEFS:
            continue
        if key.endswith("_set"):
            continue
        value = "" if raw is None else str(raw)
        if _is_secret(key):
            # Don't overwrite an existing secret with a blank/placeholder submission
            if value in ("", SECRET_PLACEHOLDER):
                continue
            await crud.upsert_setting(db, user_id, key, encrypt_data(value), is_secret=True)
        else:
            await crud.upsert_setting(db, user_id, key, value, is_secret=False)
    return await get_masked_settings(db, user_id)
