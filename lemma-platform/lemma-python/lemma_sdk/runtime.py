from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class FunctionContext(BaseModel):
    """Runtime context passed to Lemma functions."""

    pod_id: UUID
    function_id: str
    user_id: UUID
    user_email: str | None = None
    config: Any = None
    model_config = ConfigDict(arbitrary_types_allowed=True)


__all__ = ["FunctionContext"]
