"""Loop node configuration."""

from typing import Literal

from pydantic import BaseModel, Field

from app.modules.workflow.domain.nodes.base import BaseNode, NodeType


class LoopNodeConfig(BaseModel):
    """Configuration for Loop node."""

    items_path: str = Field(
        description="JMESPath to an array in the run context to iterate over."
    )
    item_var_name: str = Field(
        default="item",
        description=(
            "Alias for the current item inside the loop body, available as "
            "`loop.<item_var_name>` (the item is always available as `loop.item`)."
        ),
    )
    child_node_id: str = Field(
        description="Id of the first node of the loop body executed per item."
    )


class LoopNode(BaseNode):
    """Loop node. Iterates the body chain once per item; the aggregated
    output is `{results: [...], count: n}` under the loop node id."""

    type: Literal[NodeType.LOOP] = NodeType.LOOP
    config: LoopNodeConfig
