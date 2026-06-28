"""Node execution outcomes.

Executors return exactly one of these; the stepper interprets them. Failures
are raised as NodeExecutionError, never returned.
"""

from dataclasses import dataclass, field
from typing import Any, Union

from app.modules.workflow.domain.wait import WaitRequest


@dataclass
class Advance:
    """Node finished; follow the outgoing edge."""

    output: dict[str, Any] = field(default_factory=dict)


@dataclass
class Branch:
    """Node finished and selected the next node (decision)."""

    next_node_id: str | None
    output: dict[str, Any] = field(default_factory=dict)


@dataclass
class Suspend:
    """Node is waiting on an external party; persist a wait row."""

    wait: WaitRequest
    output: dict[str, Any] = field(default_factory=dict)


@dataclass
class StartLoop:
    """Loop node resolved its items; the stepper drives the iterations."""

    items: list[Any]
    body_node_id: str
    item_var: str = "item"


@dataclass
class Halt:
    """End node; complete the run."""

    output: dict[str, Any] = field(default_factory=dict)


NodeOutcome = Union[Advance, Branch, Suspend, StartLoop, Halt]
