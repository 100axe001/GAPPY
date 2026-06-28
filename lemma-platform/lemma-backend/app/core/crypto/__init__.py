"""System-wide secret encryption + signing.

A single, pluggable facility used across the whole backend to encrypt secrets at
rest and to sign short-lived tokens, with first-class key rotation.

Public surface (import these, not the internals):

    from app.core.crypto import get_secret_cipher, get_secret_signer

``get_secret_cipher()`` returns a :class:`SecretCipher` (``encrypt_json`` /
``decrypt_json`` / ``encrypt_str`` / ``decrypt_str``). ``get_secret_signer()``
returns a :class:`SecretSigner` (``sign`` / ``verify``). Both are cached
singletons backed by the configured :class:`KeyProvider` ("KMS").
"""

from __future__ import annotations

from app.core.crypto.factory import (
    get_key_provider,
    get_secret_cipher,
    get_secret_signer,
    reset_crypto_caches,
)
from app.core.crypto.ports import (
    KeyProvider,
    Keyring,
    KeyMaterial,
    SecretCipher,
    SecretSigner,
)

__all__ = [
    "KeyProvider",
    "Keyring",
    "KeyMaterial",
    "SecretCipher",
    "SecretSigner",
    "get_key_provider",
    "get_secret_cipher",
    "get_secret_signer",
    "reset_crypto_caches",
]
