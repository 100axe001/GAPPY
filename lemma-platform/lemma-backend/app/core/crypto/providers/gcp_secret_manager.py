"""Google Secret Manager key provider — keyring storage, local crypto.

The Fernet keyring (a JSON array of ``{kid,key,primary}``) is stored as a Secret
Manager secret. It is fetched once and cached; crypto then happens in-process
exactly like the static provider — no per-operation cloud call, so no event-loop
blocking on the hot path. Rotation = add a new primary key to the secret's JSON
(a new secret version), then re-encrypt data forward.

Simpler to operate than Cloud KMS, with the tradeoff that the raw keyring is
loaded into process memory (Secret Manager encrypts it at rest with Google-managed
keys, and access is IAM-gated + audit-logged).
"""

from __future__ import annotations

import threading

from app.core.config import settings
from app.core.crypto.envelope import ALG_FERNET
from app.core.crypto.keys import parse_keyset
from app.core.crypto.ports import KeyProvider, Keyring


class GcpSecretManagerKeyProvider(KeyProvider):
    name = "gcp_secret_manager"

    def __init__(self, secret_name: str | None = None) -> None:
        self._secret_name = secret_name or settings.gcp_secret_manager_secret_name
        if not self._secret_name:
            raise RuntimeError(
                "GCP_SECRET_MANAGER_SECRET_NAME is required for "
                "secret_key_provider=gcp_secret_manager (projects/…/secrets/…)"
            )
        self._lock = threading.Lock()
        self._keyring: Keyring | None = None

    def _load(self) -> Keyring:
        if self._keyring is None:
            with self._lock:
                if self._keyring is None:
                    from google.cloud import secretmanager

                    client = secretmanager.SecretManagerServiceClient()
                    name = self._secret_name
                    if "/versions/" not in name:
                        name = f"{name}/versions/latest"
                    response = client.access_secret_version(request={"name": name})
                    raw = response.payload.data.decode("utf-8")
                    self._keyring = parse_keyset(raw)
        return self._keyring

    @property
    def encryption_alg(self) -> str:
        return ALG_FERNET

    @property
    def primary_kid(self) -> str:
        return self._load().primary_kid

    def encryption_keyring(self) -> Keyring:
        return self._load()

    def signing_keyring(self) -> Keyring:
        return self._load()
