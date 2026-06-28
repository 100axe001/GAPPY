from __future__ import annotations

from typing import Annotated, Any, Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field


class SurfacePlatformWebhookIngress(BaseModel):
    ingress_type: Literal["platform_webhook"] = "platform_webhook"
    source: str
    payload: dict[str, Any]
    headers: dict[str, str] = Field(default_factory=dict)


class SurfaceDirectWebhookIngress(BaseModel):
    ingress_type: Literal["surface_webhook"] = "surface_webhook"
    surface_id: UUID
    payload: dict[str, Any]
    headers: dict[str, str] = Field(default_factory=dict)


class SurfaceScheduleIngress(BaseModel):
    ingress_type: Literal["schedule"] = "schedule"
    schedule_id: UUID
    payload: dict[str, Any]
    account_id: UUID | None = None
    pod_id: UUID | None = None
    user_id: UUID | None = None


SurfaceIngressRequest = Annotated[
    Union[
        SurfacePlatformWebhookIngress,
        SurfaceDirectWebhookIngress,
        SurfaceScheduleIngress,
    ],
    Field(discriminator="ingress_type"),
]
