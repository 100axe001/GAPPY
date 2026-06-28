from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ScreenDetails")



@_attrs_define
class ScreenDetails:
    """ Details of a screen.

        Attributes:
            name (str): The name of the screen. The name must be unique. The maximum length is 255 characters.
            description (str | Unset): The description of the screen. The maximum length is 255 characters.
     """

    name: str
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        screen_details = cls(
            name=name,
            description=description,
        )

        return screen_details

