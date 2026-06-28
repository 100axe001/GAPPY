from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Resolution")



@_attrs_define
class Resolution:
    """ Details of an issue resolution.

        Attributes:
            description (str | Unset): The description of the issue resolution.
            id (str | Unset): The ID of the issue resolution.
            name (str | Unset): The name of the issue resolution.
            self_ (str | Unset): The URL of the issue resolution.
     """

    description: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        name = self.name

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        resolution = cls(
            description=description,
            id=id,
            name=name,
            self_=self_,
        )

        return resolution

