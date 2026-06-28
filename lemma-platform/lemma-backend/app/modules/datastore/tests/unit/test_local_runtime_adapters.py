from __future__ import annotations

from pathlib import Path

import pytest

from app.core.config import settings
from app.core.embeddings.embeddings import Embedder
from app.core.embeddings.factory import create_embedder
from app.core.embeddings.local_embedder import FastEmbedLocalEmbedder
from app.modules.datastore.infrastructure.storage import (
    GCSDatastoreStorage,
    LocalDatastoreStorage,
    create_datastore_storage,
)


def test_local_environment_uses_local_storage_and_embeddings(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
):
    monkeypatch.setattr(settings, "environment", "local")
    monkeypatch.setattr(settings, "storage_backend", "auto")
    monkeypatch.setattr(settings, "embedding_provider", "auto")
    monkeypatch.setattr(settings, "local_object_storage_root", str(tmp_path))
    monkeypatch.setattr(settings, "gcs_storage_bucket", "cloud-bucket")

    assert settings.effective_storage_backend() == "local"
    assert isinstance(create_datastore_storage(), LocalDatastoreStorage)
    assert settings.effective_embedding_provider() == "local"
    assert isinstance(create_embedder(), Embedder)
    assert create_embedder() is create_embedder()


@pytest.mark.asyncio
async def test_fastembed_local_embedder_normalizes_model_vectors():
    class FakeFastEmbed:
        def embed(self, texts, **kwargs):
            assert kwargs["batch_size"] == 32
            return [[1.0, 0.5, -0.25] for _ in texts]

    embedder = FastEmbedLocalEmbedder(
        dimension=3,
        model=FakeFastEmbed(),
    )

    first = await embedder.embed("local embeddings are local")
    batch = await embedder.embed_batch(["one", "two"])

    assert first == [1.0, 0.5, -0.25]
    assert batch == [[1.0, 0.5, -0.25], [1.0, 0.5, -0.25]]


@pytest.mark.asyncio
async def test_fastembed_local_embedder_rejects_wrong_dimension():
    class FakeFastEmbed:
        def embed(self, texts, **kwargs):
            return [[1.0, 0.5] for _ in texts]

    embedder = FastEmbedLocalEmbedder(
        dimension=3,
        model=FakeFastEmbed(),
    )

    with pytest.raises(ValueError, match="expected 3"):
        await embedder.embed("too short")


def test_production_with_bucket_uses_gcs_storage(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr(settings, "environment", "production")
    monkeypatch.setattr(settings, "storage_backend", "auto")
    monkeypatch.setattr(settings, "gcs_storage_bucket", "cloud-bucket")

    assert settings.effective_storage_backend() == "gcs"
    assert isinstance(create_datastore_storage(), GCSDatastoreStorage)


@pytest.mark.asyncio
async def test_local_datastore_storage_round_trips_with_obstore(tmp_path: Path):
    storage = LocalDatastoreStorage(tmp_path)

    assert await storage.upload_file("pod/file.txt", b"hello") is True
    assert await storage.download_file("pod/file.txt") == b"hello"
    assert await storage.delete_prefix("pod") == 1
    assert not (tmp_path / "pod" / "file.txt").exists()


@pytest.mark.asyncio
async def test_download_missing_object_raises_typed_not_found(tmp_path: Path):
    from app.modules.datastore.domain.errors import DatastoreObjectNotFoundError

    storage = LocalDatastoreStorage(tmp_path)

    with pytest.raises(DatastoreObjectNotFoundError):
        await storage.download_file("pod/does-not-exist.txt")
