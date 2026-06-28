from __future__ import annotations

from pydantic import BaseModel

from app.modules.agent_surfaces.domain.ingress_context import (
    AgentSurfaceContext,
)


class SurfaceProcessMessageTaskPayload(BaseModel):
    context: AgentSurfaceContext
