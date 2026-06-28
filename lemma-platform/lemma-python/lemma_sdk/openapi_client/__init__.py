"""A client library for accessing Lemma Backend"""
# Lazy exports (PEP 562): `.client` pulls in httpx (~80ms), which would
# otherwise be paid by any import of a single generated model, since Python
# executes this parent package first. The CLI imports models at startup, so
# keep this package import free of the HTTP stack.
# Reapplied by scripts/generate_openapi_client.sh after regeneration.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)


def __getattr__(name: str):
    if name in __all__:
        from . import client

        value = getattr(client, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
