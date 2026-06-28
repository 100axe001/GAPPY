"""Config-driven construction of the crypto facility (cached singletons).

Mirrors the house pattern used by ``app/core/embeddings/factory.py`` and
``app/core/object_storage.py``: a ``settings.effective_*`` selector picks the
backend, concrete providers are imported lazily, and the results are cached so
the process shares one provider (and its DEK cache) and one cipher/signer.

Call :func:`reset_crypto_caches` after mutating key configuration in-process
(tests, the rotation CLI re-reading config).
"""

from __future__ import annotations

from functools import lru_cache

from app.core.config import settings
from app.core.crypto.cipher import EnvelopeSecretCipher
from app.core.crypto.keys import legacy_candidate_secrets
from app.core.crypto.ports import KeyProvider, SecretCipher, SecretSigner
from app.core.crypto.signer import HkdfSecretSigner


def _create_key_provider(kind: str) -> KeyProvider:
    if kind == "gcp_kms":
        from app.core.crypto.providers.gcp_kms import GcpKmsKeyProvider

        return GcpKmsKeyProvider()
    if kind == "gcp_secret_manager":
        from app.core.crypto.providers.gcp_secret_manager import (
            GcpSecretManagerKeyProvider,
        )

        return GcpSecretManagerKeyProvider()
    if kind == "keychain":
        from app.core.crypto.providers.keychain import KeychainKeyProvider

        return KeychainKeyProvider()
    from app.core.crypto.providers.static import StaticKeyProvider

    return StaticKeyProvider()


@lru_cache(maxsize=1)
def get_key_provider() -> KeyProvider:
    return _create_key_provider(settings.effective_secret_key_provider())


@lru_cache(maxsize=1)
def get_secret_cipher() -> SecretCipher:
    return EnvelopeSecretCipher(
        get_key_provider(), legacy_secrets=legacy_candidate_secrets()
    )


@lru_cache(maxsize=1)
def get_secret_signer() -> SecretSigner:
    return HkdfSecretSigner(get_key_provider())


def reset_crypto_caches() -> None:
    """Drop cached singletons so the next call re-reads configuration."""
    get_key_provider.cache_clear()
    get_secret_cipher.cache_clear()
    get_secret_signer.cache_clear()
