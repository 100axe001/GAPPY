from __future__ import annotations

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class OAuth2Credentials(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "Bearer"
    expires_at: datetime | None = None
    scopes: list[str] = Field(default_factory=list)
    base_url: str | None = None
    cloud_id: str | None = None


class ApiKeyCredentials(BaseModel):
    api_key: str
    location: Literal["header", "query"] = "query"
    name: str = "key"
    prefix: str | None = None


class NoAuthCredentials(BaseModel):
    pass


CredentialTypes = OAuth2Credentials | ApiKeyCredentials | NoAuthCredentials


@dataclass(slots=True)
class ResolvedAuth:
    headers: dict[str, str]
    query_params: dict[str, str]


def resolve_auth(credentials: CredentialTypes | None) -> ResolvedAuth:
    if credentials is None or isinstance(credentials, NoAuthCredentials):
        return ResolvedAuth(headers={}, query_params={})
    if isinstance(credentials, OAuth2Credentials):
        token_value = credentials.access_token
        if credentials.token_type:
            token_value = f"{credentials.token_type} {token_value}"
        return ResolvedAuth(
            headers={"Authorization": token_value},
            query_params={},
        )
    if isinstance(credentials, ApiKeyCredentials):
        if credentials.location == "header":
            value = credentials.api_key
            if credentials.prefix:
                value = f"{credentials.prefix} {value}"
            return ResolvedAuth(headers={credentials.name: value}, query_params={})
        return ResolvedAuth(
            headers={},
            query_params={credentials.name: credentials.api_key},
        )
    raise TypeError(f"Unsupported credentials type: {type(credentials)!r}")
