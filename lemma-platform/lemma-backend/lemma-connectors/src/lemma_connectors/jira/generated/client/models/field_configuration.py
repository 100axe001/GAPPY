from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FieldConfiguration")



@_attrs_define
class FieldConfiguration:
    """ Details of a field configuration.

        Attributes:
            description (str): The description of the field configuration.
            id (int): The ID of the field configuration.
            name (str): The name of the field configuration.
            is_default (bool | Unset): Whether the field configuration is the default.
     """

    description: str
    id: int
    name: str
    is_default: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        name = self.name

        is_default = self.is_default


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "description": description,
            "id": id,
            "name": name,
        })
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        is_default = d.pop("isDefault", UNSET)

        field_configuration = cls(
            description=description,
            id=id,
            name=name,
            is_default=is_default,
        )

        return field_configuration

