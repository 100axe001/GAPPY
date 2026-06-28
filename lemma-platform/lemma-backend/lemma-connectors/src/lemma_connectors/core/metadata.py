from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ToolParameterMetadata(BaseModel):
    name: str
    python_name: str | None = None
    location: Literal["path", "query", "header"]
    required: bool = False
    description: str | None = None
    schema_definition: dict[str, Any] = Field(default_factory=dict, alias="schema")
    schema_ref: str | None = None


class RequestBodyMetadata(BaseModel):
    required: bool = False
    content_type: str = "application/json"
    schema_definition: dict[str, Any] = Field(default_factory=dict, alias="schema")
    schema_ref: str | None = None


class ToolMetadata(BaseModel):
    name: str
    method: str
    path: str
    module_path: str
    title: str
    operation_id: str | None = None
    description: str
    tags: list[str] = Field(default_factory=list)
    deprecated: bool = False
    parameters: list[ToolParameterMetadata] = Field(default_factory=list)
    request_body: RequestBodyMetadata | None = None
    response_schema: dict[str, Any] = Field(default_factory=dict)
    response_schema_ref: str | None = None
    response_content_type: str = "application/json"
    binary_response_hint: bool = False

    def input_schema(self) -> dict[str, Any]:
        properties: dict[str, Any] = {}
        required: list[str] = []
        for parameter in self.parameters:
            properties[parameter.name] = parameter.schema_definition or {"type": "string"}
            if parameter.description:
                properties[parameter.name].setdefault("description", parameter.description)
            if parameter.required:
                required.append(parameter.name)
        if self.request_body is not None:
            properties["body"] = (
                self.request_body.schema_definition or {"type": "object"}
            )
            if self.request_body.required:
                required.append("body")
        schema: dict[str, Any] = {
            "type": "object",
            "title": self.title,
            "properties": properties,
            "additionalProperties": False,
        }
        if required:
            schema["required"] = required
        return schema
