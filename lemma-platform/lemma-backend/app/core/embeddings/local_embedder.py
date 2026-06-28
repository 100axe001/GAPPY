"""Local embedding providers for development and test environments."""

from __future__ import annotations

from typing import Any
from typing import List

import anyio

from app.core.config import settings
from app.core.embeddings.embeddings import Embedder


class FastEmbedLocalEmbedder(Embedder):
    """CPU-only local semantic embeddings backed by FastEmbed/ONNX."""

    def __init__(
        self,
        *,
        model_name: str | None = None,
        dimension: int | None = None,
        batch_size: int = 32,
        model: Any | None = None,
    ):
        self.model_name = model_name or settings.local_embedding_model
        self.dimension = dimension or settings.embedding_dimension
        self.batch_size = batch_size
        self._model = model

    async def embed(self, text: str) -> List[float]:
        embeddings = await self.embed_batch([text])
        return embeddings[0]

    async def embed_batch(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        return await anyio.to_thread.run_sync(self._encode_batch, list(texts))

    def _load_model(self):
        if self._model is None:
            from fastembed import TextEmbedding

            self._model = TextEmbedding(model_name=self.model_name)
        return self._model

    def _encode_batch(self, texts: list[str]) -> list[list[float]]:
        model = self._load_model()
        raw_embeddings = list(model.embed(texts, batch_size=self.batch_size))
        vectors = [
            [float(value) for value in self._as_list(vector)]
            for vector in raw_embeddings
        ]
        for vector in vectors:
            if len(vector) != self.dimension:
                raise ValueError(
                    f"Local embedding model {self.model_name!r} returned "
                    f"{len(vector)} dimensions; expected {self.dimension}. "
                    "Set EMBEDDING_DIMENSION to match the model."
                )
        return vectors

    def _as_list(self, vector: Any) -> list[float]:
        if hasattr(vector, "tolist"):
            return vector.tolist()
        return list(vector)
