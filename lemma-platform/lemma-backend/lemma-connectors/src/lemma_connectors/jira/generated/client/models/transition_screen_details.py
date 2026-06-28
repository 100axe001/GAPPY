from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TransitionScreenDetails")



@_attrs_define
class TransitionScreenDetails:
    """ The details of a transition screen.

        Attributes:
            id (str): The ID of the screen.
            name (str | Unset): The name of the screen.
     """

    id: str
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        transition_screen_details = cls(
            id=id,
            name=name,
        )

        return transition_screen_details

