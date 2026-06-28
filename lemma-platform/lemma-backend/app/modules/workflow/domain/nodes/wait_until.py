"""Wait-until node configuration."""

from typing import Literal

from pydantic import BaseModel

from app.modules.workflow.domain.nodes.base import BaseNode, NodeType


class WaitUntilNodeConfig(BaseModel):
    timeout_seconds: int


class WaitUntilNode(BaseNode):
    """Wait node. Suspends the run until the scheduler wakes it."""

    type: Literal[NodeType.WAIT_UNTIL] = NodeType.WAIT_UNTIL
    config: WaitUntilNodeConfig
