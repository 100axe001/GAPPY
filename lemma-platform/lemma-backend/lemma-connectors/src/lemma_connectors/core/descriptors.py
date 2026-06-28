from __future__ import annotations

from dataclasses import dataclass, field
import warnings
from typing import Any

from pydantic import BaseModel
from pydantic.json_schema import PydanticJsonSchemaWarning


@dataclass(slots=True)
class ToolDescriptor:
    name: str
    title: str
    description: str
    input_schema: dict[str, Any]
    output_schema: dict[str, Any]
    method: str
    path: str
    input_type: type[Any] | None = None
    output_type: type[Any] | Any | None = None
    tags: tuple[str, ...] = field(default_factory=tuple)
    deprecated: bool = False


@dataclass(slots=True)
class OperationDescriptor:
    name: str
    title: str
    description: str
    input_model: type[BaseModel]
    output_model: type[BaseModel]
    tools_used: tuple[str, ...] = field(default_factory=tuple)
    tags: tuple[str, ...] = field(default_factory=tuple)
    input_schema_override: dict[str, Any] | None = None
    output_schema_override: dict[str, Any] | None = None

    def input_schema(self) -> dict[str, Any]:
        if self.input_schema_override is not None:
            return self.input_schema_override
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message=r"Cannot update undefined schema.*skipped-discriminator",
                category=PydanticJsonSchemaWarning,
            )
            return self.input_model.model_json_schema()

    def output_schema(self) -> dict[str, Any]:
        if self.output_schema_override is not None:
            return self.output_schema_override
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message=r"Cannot update undefined schema.*skipped-discriminator",
                category=PydanticJsonSchemaWarning,
            )
            return self.output_model.model_json_schema()
