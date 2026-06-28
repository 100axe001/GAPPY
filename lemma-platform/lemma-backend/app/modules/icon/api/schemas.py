"""Schemas for icon upload APIs."""

from pydantic import BaseModel


class IconUploadResponse(BaseModel):
    """Response payload for uploaded icons."""

    icon_url: str
    storage_path: str
    content_type: str
