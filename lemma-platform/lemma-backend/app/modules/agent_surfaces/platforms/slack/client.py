from __future__ import annotations

from typing import Any

from slack_sdk.web.async_client import AsyncWebClient


def slack_access_token(credentials: dict[str, Any]) -> str | None:
    if credentials.get("access_token"):
        return str(credentials["access_token"])
    if credentials.get("bot_token"):
        return str(credentials["bot_token"])
    raw_response = credentials.get("raw_response") or {}
    token = raw_response.get("access_token")
    return str(token) if token else None


def slack_base_url(credentials: dict[str, Any]) -> str | None:
    if credentials.get("api_base_url"):
        return _normalize_base_url(str(credentials["api_base_url"]))
    raw_response = credentials.get("raw_response") or {}
    value = raw_response.get("api_base_url")
    return _normalize_base_url(str(value)) if value else None


def build_slack_client(credentials: dict[str, Any]) -> AsyncWebClient:
    kwargs: dict[str, Any] = {}
    token = slack_access_token(credentials)
    if token:
        kwargs["token"] = token
    base_url = slack_base_url(credentials)
    if base_url:
        kwargs["base_url"] = base_url
    return AsyncWebClient(**kwargs)


def slack_scopes(credentials: dict[str, Any]) -> set[str]:
    raw_values: list[str] = []
    for candidate in (
        credentials.get("scope"),
        credentials.get("scopes"),
        (credentials.get("raw_response") or {}).get("scope"),
        (credentials.get("raw_response") or {}).get("scopes"),
    ):
        if isinstance(candidate, str):
            raw_values.extend(candidate.split(","))
        elif isinstance(candidate, list):
            raw_values.extend(str(item) for item in candidate)
    return {value.strip() for value in raw_values if value and value.strip()}


def slack_supports_customized_messages(credentials: dict[str, Any]) -> bool:
    return "chat:write.customize" in slack_scopes(credentials)


def slack_customized_message_kwargs(
    credentials: dict[str, Any],
    agent_display_name: str | None,
) -> dict[str, Any]:
    normalized_name = str(agent_display_name or "").strip()
    if not normalized_name or not slack_supports_customized_messages(credentials):
        return {}
    return {"username": normalized_name}


def _normalize_base_url(value: str) -> str:
    return value if value.endswith("/") else f"{value}/"
