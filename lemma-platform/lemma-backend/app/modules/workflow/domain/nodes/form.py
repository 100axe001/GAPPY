"""Form node configuration (human input)."""

from typing import Any, Dict, Literal
from uuid import UUID

from pydantic import BaseModel, Field

from app.modules.workflow.domain.nodes.base import BaseNode, NodeType


class FormNodeConfig(BaseModel):
    """Configuration for Form node (user input)."""

    input_schema: Dict[str, Any] = Field(description="JSON Schema for user input")
    ui_schema: Dict[str, Any] | None = Field(
        default=None, description="UI configuration"
    )
    assignee_pod_member_id: UUID | None = Field(
        default=None,
        description="Pod member assigned to submit this form.",
    )
    assignee_pod_member_id_expression: str | None = Field(
        default=None,
        description=(
            "Optional JMESPath expression resolving to a pod member id. "
            "Takes precedence over assignee_pod_member_id."
        ),
    )


class FormNode(BaseNode):
    """Form node for user input. The run waits on it until the form is
    submitted via the form-submit endpoint."""

    type: Literal[NodeType.FORM] = NodeType.FORM
    config: FormNodeConfig
