"""Scheduler API package."""

from app.modules.schedule.scheduler.api.scheduler_controller import (
    router as scheduler_router,
)

__all__ = ["scheduler_router"]
