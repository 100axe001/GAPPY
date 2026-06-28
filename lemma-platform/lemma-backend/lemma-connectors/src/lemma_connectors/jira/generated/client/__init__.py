
""" A client library for accessing The Jira Cloud platform REST API """
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
