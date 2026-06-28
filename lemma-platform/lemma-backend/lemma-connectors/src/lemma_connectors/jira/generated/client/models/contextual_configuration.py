from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ContextualConfiguration")



@_attrs_define
class ContextualConfiguration:
    """ Details of the contextual configuration for a custom field.

        Attributes:
            field_context_id (str): The ID of the field context the configuration is associated with.
            id (str): The ID of the configuration.
            configuration (Any | Unset): The field configuration.
            schema (Any | Unset): The field value schema.
     """

    field_context_id: str
    id: str
    configuration: Any | Unset = UNSET
    schema: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_context_id = self.field_context_id

        id = self.id

        configuration = self.configuration

        schema = self.schema


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fieldContextId": field_context_id,
            "id": id,
        })
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_context_id = d.pop("fieldContextId")

        id = d.pop("id")

        configuration = d.pop("configuration", UNSET)

        schema = d.pop("schema", UNSET)

        contextual_configuration = cls(
            field_context_id=field_context_id,
            id=id,
            configuration=configuration,
            schema=schema,
        )

        return contextual_configuration

