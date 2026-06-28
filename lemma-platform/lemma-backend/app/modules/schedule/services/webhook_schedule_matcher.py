"""Matching logic for webhook events against stored schedules."""

from __future__ import annotations

from typing import Any, Dict, List

from app.modules.connectors.infrastructure.repositories.connector_trigger_repository import (
    ConnectorTriggerRepository,
)
from app.modules.schedule.domain.schedule import ScheduleEntity, ScheduleType
from app.modules.schedule.repositories.schedule_repository import ScheduleRepository
from app.core.log.log import get_logger

logger = get_logger(__name__)


class WebhookScheduleMatcher:
    """Find matching webhook schedules for platform events."""

    def __init__(
        self,
        connector_trigger_repository: ConnectorTriggerRepository,
        schedule_repository: ScheduleRepository | None = None,
    ):
        self.schedule_repository = schedule_repository
        if self.schedule_repository is None:
            raise ValueError("schedule_repository is required")
        self.connector_trigger_repository = connector_trigger_repository

    async def match(self, source: str, metadata: Dict[str, Any]) -> List[ScheduleEntity]:
        logger.info("Matching webhook for source", source=source, metadata=metadata)
        if source == "composio":
            provider_id = metadata.get("provider_id")
            if not provider_id:
                logger.warning("Composio webhook missing provider_id in metadata")
                return []

            return await self.schedule_repository.find_by_config(
                schedule_type=ScheduleType.WEBHOOK,
                criteria={"provider_trigger_id": provider_id},
            )

        if source == "slack":
            event_type = metadata.get("event_type")
            bot_id = metadata.get("bot_id")

            if bot_id:
                logger.info("Skipping schedule for message from bot_id: %s", bot_id)
                return []

            if not event_type:
                logger.warning("Slack webhook missing event_type")
                return []

            app_triggers = await self.connector_trigger_repository.get_by_app_name_and_event_type(
                app_name="slack",
                event_type=str(event_type),
            )
            logger.info(
                "Found %d connector triggers for slack webhook",
                len(app_triggers),
            )

            matching: list[ScheduleEntity] = []
            seen_ids = set()
            for app_trigger in app_triggers:
                keys_to_match = app_trigger.config_field_names
                payload = {key: metadata.get(key) for key in keys_to_match}
                matched = await self.schedule_repository.find_schedules_by_config(
                    schedule_type=ScheduleType.WEBHOOK,
                    connector_trigger_id=app_trigger.id,
                    **payload,
                )
                for schedule in matched:
                    if schedule.id in seen_ids:
                        continue
                    seen_ids.add(schedule.id)
                    matching.append(schedule)
            return matching

        logger.info("No matching schedules found for %s webhook", source)
        return []
