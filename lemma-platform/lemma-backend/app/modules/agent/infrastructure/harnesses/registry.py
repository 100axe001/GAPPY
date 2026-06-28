"""Harness registry."""

from app.modules.agent.domain.errors import HarnessNotFoundError
from app.modules.agent.domain.ports import Harness
from app.modules.agent.domain.value_objects import HarnessKind


class HarnessRegistry:
    """Resolve harnesses by kind."""

    def __init__(self, harnesses: list[Harness]):
        self._harnesses = {harness.kind: harness for harness in harnesses}

    def get(self, kind: HarnessKind) -> Harness:
        harness = self._harnesses.get(kind)
        if harness is None:
            raise HarnessNotFoundError(f"No harness registered for {kind.value}")
        return harness
