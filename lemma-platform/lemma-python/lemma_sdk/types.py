from __future__ import annotations

from typing import TypeAlias

JsonPrimitive: TypeAlias = str | int | float | bool | None
JsonValue: TypeAlias = JsonPrimitive | list["JsonValue"] | dict[str, "JsonValue"]
JsonObject: TypeAlias = dict[str, JsonValue]

RecordData: TypeAlias = JsonObject
FunctionInput: TypeAlias = JsonObject
FunctionOutput: TypeAlias = JsonValue
ConnectorPayload: TypeAlias = JsonObject
Metadata: TypeAlias = JsonObject
