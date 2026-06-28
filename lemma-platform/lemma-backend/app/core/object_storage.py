"""Object storage factory helpers."""

from __future__ import annotations

from pathlib import Path

from obstore.store import GCSStore, LocalStore, ObjectStore

from app.core.config import settings


def build_object_store(
    *,
    local_prefix: str | Path,
    bucket_name: str | None = None,
    force_backend: str | None = None,
) -> ObjectStore:
    backend = force_backend or settings.effective_storage_backend()
    if backend == "gcs":
        if not bucket_name:
            raise ValueError("GCS storage backend requires a bucket name")
        return GCSStore(bucket=bucket_name)

    return LocalStore(prefix=Path(local_prefix), mkdir=True)


def local_object_storage_path(*parts: str) -> Path:
    return Path(settings.local_object_storage_root).expanduser().joinpath(*parts)
