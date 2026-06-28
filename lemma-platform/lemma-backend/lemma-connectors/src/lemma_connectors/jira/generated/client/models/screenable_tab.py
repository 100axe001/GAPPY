from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ScreenableTab")



@_attrs_define
class ScreenableTab:
    """ A screen tab.

        Attributes:
            name (str): The name of the screen tab. The maximum length is 255 characters.
            id (int | Unset): The ID of the screen tab.
     """

    name: str
    id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        screenable_tab = cls(
            name=name,
            id=id,
        )

        return screenable_tab

