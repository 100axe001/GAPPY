from __future__ import annotations

import argparse
import json
import keyword
import re
from pathlib import Path
from typing import Any


def snake_case(value: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = value.replace("-", "_").replace(".", "_")
    value = re.sub(r"[^a-zA-Z0-9_]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value.lower()


def pascal_case(value: str) -> str:
    return "".join(part.capitalize() for part in snake_case(value).split("_") if part)


def safe_identifier(value: str) -> str:
    value = snake_case(value)
    if keyword.iskeyword(value):
        return f"{value}_"
    return value or "field_"


def is_json_media_type(media_type: str | None) -> bool:
    if not media_type:
        return False
    normalized = media_type.split(";", 1)[0].strip().lower()
    return normalized == "application/json" or normalized.endswith("+json")


def is_binary_response(tool: dict[str, Any]) -> bool:
    return bool(tool.get("binary_response_hint")) or not is_json_media_type(
        tool.get("response_content_type")
    )


def resolve_named_model(
    *,
    tool: dict[str, Any],
    schema_ref: str | None,
    registry: dict[str, Any],
    purpose: str,
) -> str | None:
    if schema_ref:
        schema_name = registry["schema_refs"].get(schema_ref)
        if schema_name:
            return schema_name
    return ((registry["operations"].get(tool["name"]) or {}).get(purpose)) or None


def type_expr_from_schema(
    *,
    tool: dict[str, Any],
    schema: dict[str, Any],
    schema_ref: str | None,
    registry: dict[str, Any],
    purpose: str,
    model_imports: set[str],
    typing_imports: set[str],
) -> str:
    named_model = None
    if purpose in {"request", "response"}:
        named_model = resolve_named_model(
            tool=tool,
            schema_ref=schema_ref,
            registry=registry,
            purpose=purpose,
        )
    elif schema_ref:
        named_model = registry["schema_refs"].get(schema_ref)
    if named_model is not None:
        model_imports.add(named_model)
        return named_model

    if "enum" in schema:
        typing_imports.add("Literal")
        values = ", ".join(repr(value) for value in schema["enum"])
        return f"Literal[{values}]"

    schema_type = schema.get("type")
    if schema_type == "string":
        return "str"
    if schema_type == "integer":
        return "int"
    if schema_type == "number":
        return "float"
    if schema_type == "boolean":
        return "bool"
    if schema_type == "array":
        item_expr = type_expr_from_schema(
            tool=tool,
            schema=schema.get("items") or {},
            schema_ref=None,
            registry=registry,
            purpose=purpose,
            model_imports=model_imports,
            typing_imports=typing_imports,
        )
        return f"list[{item_expr}]"
    if schema_type == "object":
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            value_expr = type_expr_from_schema(
                tool=tool,
                schema=additional,
                schema_ref=None,
                registry=registry,
                purpose=purpose,
                model_imports=model_imports,
                typing_imports=typing_imports,
            )
            return f"dict[str, {value_expr}]"
        return "dict[str, object]"

    return "object"


def field_code(
    *,
    name: str,
    type_expr: str,
    description: str | None,
    required: bool,
) -> str:
    field_args: list[str] = []
    if description:
        field_args.append(f"description={description!r}")
    if required:
        return f"    {name}: {type_expr} = Field(...{', ' if field_args else ''}{', '.join(field_args)})"
    if field_args:
        return f"    {name}: {type_expr} | None = Field(default=None, {', '.join(field_args)})"
    return f"    {name}: {type_expr} | None = None"


def build_input_model(
    *,
    tool: dict[str, Any],
    registry: dict[str, Any],
    model_imports: set[str],
    typing_imports: set[str],
) -> str:
    class_name = f"{pascal_case(tool['name'])}ToolInput"
    lines = [f"class {class_name}(BaseModel):", f'    """Input for tool `{tool["name"]}`."""']
    for parameter in tool.get("parameters") or []:
        field_name = safe_identifier(parameter.get("python_name") or parameter["name"])
        type_expr = type_expr_from_schema(
            tool=tool,
            schema=parameter.get("schema") or {},
            schema_ref=parameter.get("schema_ref"),
            registry=registry,
            purpose="parameter",
            model_imports=model_imports,
            typing_imports=typing_imports,
        )
        lines.append(
            field_code(
                name=field_name,
                type_expr=type_expr,
                description=parameter.get("description"),
                required=parameter.get("required", False),
            )
        )
    request_body = tool.get("request_body")
    if request_body is not None:
        type_expr = type_expr_from_schema(
            tool=tool,
            schema=request_body.get("schema") or {},
            schema_ref=request_body.get("schema_ref"),
            registry=registry,
            purpose="request",
            model_imports=model_imports,
            typing_imports=typing_imports,
        )
        lines.append(
            field_code(
                name="body",
                type_expr=type_expr,
                description=f"Request body for `{tool['name']}`.",
                required=request_body.get("required", False),
            )
        )
    lines.append("    model_config = ConfigDict(extra='forbid')")
    return "\n".join(lines)


def build_output_model(
    *,
    tool: dict[str, Any],
    registry: dict[str, Any],
    model_imports: set[str],
    typing_imports: set[str],
) -> str:
    class_name = f"{pascal_case(tool['name'])}ToolOutput"
    if is_binary_response(tool):
        return "\n".join(
            [
                f"class {class_name}(BinaryContentResult):",
                f'    """Binary output for tool `{tool["name"]}`."""',
                "    pass",
            ]
        )
    type_expr = type_expr_from_schema(
        tool=tool,
        schema=tool.get("response_schema") or {},
        schema_ref=tool.get("response_schema_ref"),
        registry=registry,
        purpose="response",
        model_imports=model_imports,
        typing_imports=typing_imports,
    )
    if type_expr in model_imports and type_expr not in set(registry.get("enum_names", [])):
        return "\n".join(
            [
                f"class {class_name}({type_expr}):",
                f'    """Output for tool `{tool["name"]}`."""',
                "    pass",
            ]
        )
    return "\n".join(
        [
            f"class {class_name}(RootModel[{type_expr}]):",
            f'    """Output for tool `{tool["name"]}`."""',
            "    pass",
        ]
    )


def build_module(metadata: dict[str, Any], registry: dict[str, Any]) -> str:
    model_imports: set[str] = set()
    typing_imports: set[str] = set()
    sections: list[str] = []

    input_map_lines = ["INPUT_MODELS = {"]
    output_map_lines = ["OUTPUT_MODELS = {"]

    for tool in metadata["tools"]:
        sections.append(
            build_input_model(
                tool=tool,
                registry=registry,
                model_imports=model_imports,
                typing_imports=typing_imports,
            )
        )
        sections.append("")
        sections.append(
            build_output_model(
                tool=tool,
                registry=registry,
                model_imports=model_imports,
                typing_imports=typing_imports,
            )
        )
        sections.append("")
        class_base = pascal_case(tool["name"])
        input_map_lines.append(f"    {tool['name']!r}: {class_base}ToolInput,")
        output_map_lines.append(f"    {tool['name']!r}: {class_base}ToolOutput,")

    input_map_lines.append("}")
    output_map_lines.append("}")

    typing_line = ""
    if typing_imports:
        typing_line = f"from typing import {', '.join(sorted(typing_imports))}"

    model_import_line = ""
    if model_imports:
        model_import_line = (
            f"from {registry['module_path']} import {', '.join(sorted(model_imports))}"
        )

    lines = [
        "from __future__ import annotations",
        "",
    ]
    if typing_line:
        lines.extend([typing_line, ""])
    lines.extend(
        [
            "from pydantic import BaseModel, ConfigDict, Field, RootModel",
            "",
            "from lemma_connectors.core.results import BinaryContentResult",
            "",
        ]
    )
    if model_import_line:
        lines.extend([model_import_line, ""])
    lines.extend(sections)
    lines.extend(input_map_lines)
    lines.append("")
    lines.extend(output_map_lines)
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata", required=True)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    metadata = json.loads(Path(args.metadata).read_text())
    registry = json.loads(Path(args.registry).read_text())
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_module(metadata, registry))


if __name__ == "__main__":
    main()
