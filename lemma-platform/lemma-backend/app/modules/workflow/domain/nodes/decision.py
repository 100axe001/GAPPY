"""Decision node configuration."""

from typing import List, Literal

from pydantic import BaseModel, Field

from app.modules.workflow.domain.nodes.base import BaseNode, NodeType


class DecisionRule(BaseModel):
    condition: str = Field(
        ...,
        description=(
            "JMESPath condition evaluated against the run context. The first "
            "rule whose condition is truthy selects the next node. "
            "Example: `collect_input.decision == 'approved'`."
        ),
    )
    next_node_id: str


class DecisionNodeConfig(BaseModel):
    """Configuration for Decision node."""

    rules: List[DecisionRule] = Field(default_factory=list)


class DecisionNode(BaseNode):
    """Decision node. Routes to the first rule whose condition is truthy;
    falls through to the default outgoing edge when no rule matches."""

    type: Literal[NodeType.DECISION] = NodeType.DECISION
    config: DecisionNodeConfig
