"""Form node executor: suspend on a HUMAN wait."""

from uuid import UUID

from app.modules.workflow.domain.errors import NodeExecutionError
from app.modules.workflow.domain.nodes import FormNode
from app.modules.workflow.domain.schema_template import (
    resolve_schema_template,
    validate_resolved_schema,
)
from app.modules.workflow.domain.wait import WaitRequest, WorkflowRunWaitType
from app.modules.workflow.execution.outcome import NodeOutcome, Suspend
from app.modules.workflow.execution.step_context import StepContext


class FormExecutor:
    async def execute(self, node: FormNode, step: StepContext) -> NodeOutcome:
        assigned_member_id = node.config.assignee_pod_member_id
        if node.config.assignee_pod_member_id_expression:
            resolved = step.context.resolve_required(
                node.config.assignee_pod_member_id_expression
            )
            try:
                assigned_member_id = UUID(str(resolved))
            except ValueError as exc:
                raise NodeExecutionError(
                    node.id,
                    "assignee expression resolved to "
                    f"{resolved!r}, which is not a pod member id",
                ) from exc

        # input_schema/ui_schema are templates: any value may be a typed input
        # binding ({"type": "expression", "value": "<jmespath>"}), the same form
        # input_mapping uses, resolved against the run context. We resolve once
        # here so the *concrete* schema rides on the wait and every consumer
        # (frontend, CLI, SDK) renders from the wait row alone.
        resolved_schema = resolve_schema_template(
            node.config.input_schema, step.context
        )
        validate_resolved_schema(node.id, resolved_schema)
        resolved_ui_schema = resolve_schema_template(
            node.config.ui_schema, step.context
        )
        return Suspend(
            wait=WaitRequest(
                wait_type=WorkflowRunWaitType.HUMAN,
                assigned_pod_member_id=assigned_member_id,
                payload={
                    "input_schema": resolved_schema,
                    "ui_schema": resolved_ui_schema,
                },
            )
        )
