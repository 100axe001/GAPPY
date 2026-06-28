from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FieldConfigurationItem")



@_attrs_define
class FieldConfigurationItem:
    """ A field within a field configuration.

        Attributes:
            id (str): The ID of the field within the field configuration.
            description (str | Unset): The description of the field within the field configuration.
            is_hidden (bool | Unset): Whether the field is hidden in the field configuration.
            is_required (bool | Unset): Whether the field is required in the field configuration.
            renderer (str | Unset): The renderer type for the field within the field configuration.
     """

    id: str
    description: str | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    is_required: bool | Unset = UNSET
    renderer: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        is_hidden = self.is_hidden

        is_required = self.is_required

        renderer = self.renderer


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if renderer is not UNSET:
            field_dict["renderer"] = renderer

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        description = d.pop("description", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        is_required = d.pop("isRequired", UNSET)

        renderer = d.pop("renderer", UNSET)

        field_configuration_item = cls(
            id=id,
            description=description,
            is_hidden=is_hidden,
            is_required=is_required,
            renderer=renderer,
        )

        return field_configuration_item

