"""Service for filtering schedule events using LLM."""

from __future__ import annotations

import json
from typing import Any, Dict, Tuple

from pydantic_ai import Agent as PydanticAIAgent
from pydantic_ai.output import StructuredDict

from app.core.log.log import get_logger
from app.modules.agent.services.runtime_model_factory import (
    default_system_runtime,
    require_pydantic_ai_model_from_runtime_profile,
)
from app.modules.pod.infrastructure.pod_reads import resolve_pod_organization_id
from app.modules.schedule.domain.schedule import ScheduleEntity
from app.modules.usage.domain.errors import UsageLimitExceededError
from app.modules.usage.services.pydantic_ai_tracking import (
    record_pydantic_ai_result_usage,
    reserve_usage_for_runtime,
)
from app.modules.usage.services.usage_context import UsageExecutionContext

logger = get_logger(__name__)


# Default schema when none is provided - requires should_proceed field
DEFAULT_FILTER_SCHEMA = {
    "type": "object",
    "properties": {
        "should_proceed": {
            "type": "boolean",
            "description": "Whether the flow should proceed based on this event",
        },
        "reason": {
            "type": "string",
            "description": "Brief explanation for the decision",
        },
    },
    "required": ["should_proceed"],
}


class ScheduleFilterService:
    """Service for filtering schedule events using LLM.

    When a schedule event arrives, this service can optionally filter/process it
    through an LLM to determine whether to start a flow and extract structured data.

    The LLM is given:
    - A filter instruction (prompt)
    - The event payload
    - An output schema (must include should_proceed boolean)

    Returns:
    - Whether to proceed (based on should_proceed in LLM output)
    - The structured output from LLM (if proceeding)
    """

    def __init__(self):
        """Initialize the filter service."""

    async def filter_event(
        self,
        instruction: str,
        output_schema: Dict[str, Any] | None,
        event_payload: Dict[str, Any],
        schedule: ScheduleEntity | None = None,
    ) -> Tuple[bool, Dict[str, Any] | None]:
        """Filter/process an event using LLM.

        Args:
            instruction: The LLM instruction for processing the event.
                Should describe what events to accept/reject and what data to extract.
            output_schema: JSON schema for structured output. Must include a
                'should_proceed' boolean field. If None, uses default schema.
            event_payload: The raw event payload from the schedule.

        Returns:
            Tuple of (should_proceed, structured_output or None).
            If should_proceed is False, structured_output will be None.
        """
        try:
            # Ensure output schema has should_proceed field
            schema = self._prepare_schema(output_schema)

            # Build the prompt
            system_prompt = self._build_system_prompt(instruction)
            user_message = self._build_user_message(event_payload)

            resolved_runtime = await default_system_runtime()
            runtime_profile = resolved_runtime.public_snapshot()
            model = require_pydantic_ai_model_from_runtime_profile(
                runtime_profile=runtime_profile,
                runtime_credentials=resolved_runtime.credentials or {},
                fallback_model_name=resolved_runtime.model_name_for_harness,
            )

            # Create agent with structured output
            agent = PydanticAIAgent(
                model,
                system_prompt=system_prompt,
                output_type=StructuredDict(schema),
            )

            usage_context = await self._usage_context_for_schedule(schedule)
            usage_reservation = None
            if usage_context is not None:
                usage_reservation = await reserve_usage_for_runtime(
                    organization_id=usage_context.organization_id,
                    user_id=usage_context.user_id,
                    runtime_profile=runtime_profile,
                )
            result = None
            try:
                result = await agent.run(user_message)
                if usage_context is not None:
                    await record_pydantic_ai_result_usage(
                        ctx=usage_context,
                        runtime_profile=runtime_profile,
                        result=result,
                        status="COMPLETED",
                        reservation=usage_reservation,
                        metadata={"helper": "schedule_filter"},
                    )
            except Exception:
                if usage_context is not None:
                    await record_pydantic_ai_result_usage(
                        ctx=usage_context,
                        runtime_profile=runtime_profile,
                        result=result,
                        status="FAILED",
                        reservation=usage_reservation,
                        metadata={"helper": "schedule_filter"},
                    )
                raise
            output = result.output

            # Extract should_proceed
            should_proceed = output.get("should_proceed", False)

            if not should_proceed:
                reason = output.get(
                    "reason", "LLM determined event should not trigger flow"
                )
                logger.info(f"Event filtered out: {reason}")
                return False, None

            logger.info("Event passed filter, proceeding with structured output")
            return True, output

        except UsageLimitExceededError:
            raise
        except Exception as e:
            logger.error(f"Error in schedule filter: {e}", exc_info=True)
            # On error, skip the event (fail-safe)
            return False, None

    async def _usage_context_for_schedule(
        self,
        schedule: ScheduleEntity | None,
    ) -> UsageExecutionContext | None:
        if schedule is None:
            return None
        organization_id = await self._organization_id_for_schedule(schedule)
        return UsageExecutionContext(
            user_id=schedule.user_id,
            organization_id=organization_id,
            pod_id=schedule.pod_id,
            agent_id=schedule.agent_id,
            source_type="schedule_filter",
            source_id=str(schedule.id) if schedule.id else None,
            workload_type="schedule",
            workload_id=schedule.id,
        )

    async def _organization_id_for_schedule(
        self,
        schedule: ScheduleEntity,
    ):
        if schedule.pod_id is None:
            return None
        return await resolve_pod_organization_id(schedule.pod_id)

    def _prepare_schema(self, output_schema: Dict[str, Any] | None) -> Dict[str, Any]:
        """Prepare the output schema, ensuring it has should_proceed field."""
        if not output_schema:
            return DEFAULT_FILTER_SCHEMA

        # Ensure should_proceed is in the schema
        schema = output_schema.copy()
        if "properties" not in schema:
            schema["properties"] = {}

        if "should_proceed" not in schema["properties"]:
            schema["properties"]["should_proceed"] = {
                "type": "boolean",
                "description": "Whether the flow should proceed based on this event",
            }

        if "required" not in schema:
            schema["required"] = []

        if "should_proceed" not in schema["required"]:
            schema["required"].append("should_proceed")

        return schema

    def _build_system_prompt(self, instruction: str) -> str:
        """Build the system prompt for the filter agent."""
        return f"""You are an event filter for a workflow automation system.

Your task is to analyze incoming events and determine:
1. Whether the event should schedule the workflow (set should_proceed to true/false)
2. Extract relevant structured data from the event

IMPORTANT: 
- Set should_proceed to TRUE only if the event matches the criteria
- Set should_proceed to FALSE if the event should be skipped/ignored
- Extract data according to the output schema

FILTER INSTRUCTION:
{instruction}
"""

    def _build_user_message(self, event_payload: Dict[str, Any]) -> str:
        """Build the user message with the event payload."""
        payload_str = json.dumps(event_payload, indent=2, default=str)
        return f"""Analyze the following event and determine if it should schedule the workflow.

EVENT PAYLOAD:
```json
{payload_str}
```

Based on the filter instruction, analyze this event and provide your structured response.
        """
