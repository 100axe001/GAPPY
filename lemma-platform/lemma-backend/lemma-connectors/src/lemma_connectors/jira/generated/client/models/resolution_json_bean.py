from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ResolutionJsonBean")



@_attrs_define
class ResolutionJsonBean:
    """ 
        Attributes:
            default (bool | Unset):
            description (str | Unset):
            icon_url (str | Unset):
            id (str | Unset):
            name (str | Unset):
            self_ (str | Unset):
     """

    default: bool | Unset = UNSET
    description: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        default = self.default

        description = self.description

        icon_url = self.icon_url

        id = self.id

        name = self.name

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
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
        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        resolution_json_bean = cls(
            default=default,
            description=description,
            icon_url=icon_url,
            id=id,
            name=name,
            self_=self_,
        )

        return resolution_json_bean

