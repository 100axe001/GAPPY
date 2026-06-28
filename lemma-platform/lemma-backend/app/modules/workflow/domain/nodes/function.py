"""Function node configuration."""

from typing import Dict, Literal

from pydantic import BaseModel, Field

from app.modules.workflow.domain.nodes.base import BaseNode, NodeType
from app.modules.workflow.domain.nodes.bindings import InputBinding


class FunctionNodeConfig(BaseModel):
    """Configuration for Function node."""

    function_name: str = Field(
        ...,
        min_length=1,
        description="Function resource name to execute.",
        examples=["insert-expense"],
    )
    input_mapping: Dict[str, InputBinding] = Field(
        default_factory=dict,
        description=(
            "Explicit mapping from function argument key to either an expression "
            "or a literal JSON value. Strings are never auto-interpreted."
        ),
        json_schema_extra={
            "example": {
                "amount": {"type": "expression", "value": "collect_input.amount"},
                "currency": {"type": "literal", "value": "USD"},
            }
        },
    )


class FunctionNode(BaseNode):
    """Function node. Completes inline for synchronous functions or waits on
    the function run for asynchronous ones."""

    type: Literal[NodeType.FUNCTION] = NodeType.FUNCTION
    config: FunctionNodeConfig
