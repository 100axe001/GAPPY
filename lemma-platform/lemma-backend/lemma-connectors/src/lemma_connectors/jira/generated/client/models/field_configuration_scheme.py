from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FieldConfigurationScheme")



@_attrs_define
class FieldConfigurationScheme:
    """ Details of a field configuration scheme.

        Attributes:
            id (str): The ID of the field configuration scheme.
            name (str): The name of the field configuration scheme.
            description (str | Unset): The description of the field configuration scheme.
     """

    id: str
    name: str
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        field_configuration_scheme = cls(
            id=id,
            name=name,
            description=description,
        )

        return field_configuration_scheme

