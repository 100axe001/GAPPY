"""Agent node configuration."""

from typing import Dict, Literal

from pydantic import BaseModel, Field

from app.modules.workflow.domain.nodes.base import BaseNode, NodeType
from app.modules.workflow.domain.nodes.bindings import InputBinding


class AgentNodeConfig(BaseModel):
    """Configuration for Agent node."""

    agent_name: str = Field(
        ...,
        min_length=1,
        description="Agent resource name to execute.",
        examples=["expense-parser"],
    )
    input_mapping: Dict[str, InputBinding] = Field(
        default_factory=dict,
        description=(
            "Explicit mapping from agent input key to either an expression or "
            "a literal JSON value. Strings are never auto-interpreted."
        ),
        json_schema_extra={
            "example": {
                "issue_key": {"type": "expression", "value": "start.payload.issue.key"},
                "channel": {"type": "literal", "value": "finance"},
            }
        },
    )


class AgentNode(BaseNode):
    """Agent node. The run waits on the agent conversation to complete."""

    type: Literal[NodeType.AGENT] = NodeType.AGENT
    config: AgentNodeConfig
