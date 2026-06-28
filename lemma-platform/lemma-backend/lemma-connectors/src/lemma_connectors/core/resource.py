from __future__ import annotations

import inspect
from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from lemma_connectors.core.descriptors import OperationDescriptor
from lemma_connectors.core.operations import FunctionalOperation


@dataclass(slots=True)
class OperationDefinition:
    name: str
    title: str
    input_model: type[BaseModel]
    output_model: type[BaseModel]
    tools_used: tuple[str, ...]
    tags: tuple[str, ...]
    input_schema_override: dict[str, Any] | None = None
    output_schema_override: dict[str, Any] | None = None


def operation(
    *,
    name: str,
    title: str,
    input_model: type[BaseModel],
    output_model: type[BaseModel],
    tools_used: tuple[str, ...],
    tags: tuple[str, ...] = (),
    input_schema_override: dict[str, Any] | None = None,
    output_schema_override: dict[str, Any] | None = None,
):
    def decorator(func):
        func.__lemma_operation__ = OperationDefinition(
            name=name,
            title=title,
            input_model=input_model,
            output_model=output_model,
            tools_used=tools_used,
            tags=tags,
            input_schema_override=input_schema_override,
            output_schema_override=output_schema_override,
        )
        return func

    return decorator


class BaseResourceClient:
    def __init__(self, integration_client: Any):
        self._client = integration_client

    def build_operations(self) -> dict[str, FunctionalOperation[Any, Any]]:
        operations: dict[str, FunctionalOperation[Any, Any]] = {}
        for _, method in inspect.getmembers(self, predicate=callable):
            definition = getattr(method, "__lemma_operation__", None)
            if definition is None:
                continue
            description = inspect.getdoc(method) or definition.title
            operations[definition.name] = FunctionalOperation(
                descriptor=OperationDescriptor(
                    name=definition.name,
                    title=definition.title,
                    description=description,
                    input_model=definition.input_model,
                    output_model=definition.output_model,
                    tools_used=definition.tools_used,
                    tags=definition.tags,
                    input_schema_override=definition.input_schema_override,
                    output_schema_override=definition.output_schema_override,
                ),
                handler=method,
            )
        return operations


def coerce_tool_result(value: Any) -> Any:
    if isinstance(value, BaseModel):
        return coerce_tool_result(value.model_dump(by_alias=True, exclude_none=True))
    if hasattr(value, "to_dict"):
        return coerce_tool_result(value.to_dict())
    if isinstance(value, list):
        return [coerce_tool_result(item) for item in value]
    if isinstance(value, dict):
        return {key: coerce_tool_result(item) for key, item in value.items()}
    return value
