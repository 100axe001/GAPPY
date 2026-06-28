from __future__ import annotations

from collections.abc import Awaitable, Callable, Mapping
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

from lemma_connectors.core.descriptors import OperationDescriptor

InputT = TypeVar("InputT", bound=BaseModel)
OutputT = TypeVar("OutputT", bound=BaseModel)


class Operation(Generic[InputT, OutputT]):
    descriptor: OperationDescriptor

    async def execute(self, data: InputT | Mapping[str, Any]) -> OutputT:
        raise NotImplementedError


class FunctionalOperation(Operation[InputT, OutputT]):
    def __init__(
        self,
        *,
        descriptor: OperationDescriptor,
        handler: Callable[[InputT], Awaitable[OutputT]],
    ):
        self.descriptor = descriptor
        self._handler = handler

    async def execute(self, data: InputT | Mapping[str, Any]) -> OutputT:
        if isinstance(data, BaseModel):
            validated = self.descriptor.input_model.model_validate(
                data.model_dump(
                    by_alias=True,
                    exclude_none=True,
                    exclude_unset=True,
                )
            )
        else:
            validated = self.descriptor.input_model.model_validate(data)
        return await self._handler(validated)
