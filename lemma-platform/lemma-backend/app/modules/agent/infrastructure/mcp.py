"""Shared MCP constants and helpers for Lemma agent tools."""

from __future__ import annotations

LEMMA_MCP_SERVER_NAME = "lemma_tools"
LEMMA_TOOL_PREFIX = "lemma_"
LEMMA_MCP_TOKEN_ENV = "LEMMA_MCP_TOKEN"
LEMMA_MCP_AUTHORIZATION_ENV = "LEMMA_MCP_AUTHORIZATION"
LEMMA_PROVIDER_TOOL_PREFIXES = (
    f"mcp.{LEMMA_MCP_SERVER_NAME}.",
    f"mcp__{LEMMA_MCP_SERVER_NAME}__",
    f"{LEMMA_MCP_SERVER_NAME}_",
    f"{LEMMA_MCP_SERVER_NAME}.",
    "mcp.lemma-tools.",
    "mcp__lemma-tools__",
    "lemma-tools_",
    "lemma-tools.",
)


def exported_tool_name(tool_name: str) -> str:
    return f"{LEMMA_TOOL_PREFIX}{tool_name}"


def normalize_exported_tool_name(tool_name: str) -> str:
    return (
        tool_name[len(LEMMA_TOOL_PREFIX) :]
        if tool_name.startswith(LEMMA_TOOL_PREFIX)
        else tool_name
    )


def normalize_local_mcp_tool_name(tool_name: str) -> str:
    normalized = tool_name
    for prefix in LEMMA_PROVIDER_TOOL_PREFIXES:
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix) :]
            break
    return normalize_exported_tool_name(normalized)


def is_provider_scoped_lemma_mcp_tool_name(tool_name: object) -> bool:
    return isinstance(tool_name, str) and tool_name.startswith(
        LEMMA_PROVIDER_TOOL_PREFIXES
    )


def looks_like_lemma_mcp_payload(payload: object) -> bool:
    if isinstance(payload, dict):
        server_name = (
            payload.get("serverName")
            or payload.get("server_name")
            or payload.get("server")
            or payload.get("mcp_server")
            or payload.get("mcpServer")
        )
        if server_name == LEMMA_MCP_SERVER_NAME:
            return True
        for key in ("toolName", "tool_name", "tool", "name"):
            value = payload.get(key)
            if is_provider_scoped_lemma_mcp_tool_name(value):
                return True
            if isinstance(value, dict) and looks_like_lemma_mcp_payload(value):
                return True
        return any(looks_like_lemma_mcp_payload(value) for value in payload.values())
    if isinstance(payload, list):
        return any(looks_like_lemma_mcp_payload(item) for item in payload)
    return False
