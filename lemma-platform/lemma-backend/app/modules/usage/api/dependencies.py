"""Usage API dependencies."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends

from app.core.api.dependencies import UoWDep
from app.modules.usage.services.usage_service import UsageService
from app.modules.usage.services.usage_service_factory import build_usage_service


def get_usage_service(uow: UoWDep) -> UsageService:
    return build_usage_service(uow)


UsageServiceDep = Annotated[UsageService, Depends(get_usage_service)]
