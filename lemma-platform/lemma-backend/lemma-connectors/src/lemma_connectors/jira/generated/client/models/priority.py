from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Priority")



@_attrs_define
class Priority:
    """ An issue priority.

        Attributes:
            description (str | Unset): The description of the issue priority.
            icon_url (str | Unset): The URL of the icon for the issue priority.
            id (str | Unset): The ID of the issue priority.
            is_default (bool | Unset): Whether this priority is the default.
            name (str | Unset): The name of the issue priority.
            self_ (str | Unset): The URL of the issue priority.
            status_color (str | Unset): The color used to indicate the issue priority.
     """

    description: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET
    status_color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        icon_url = self.icon_url

        id = self.id

        is_default = self.is_default

        name = self.name

        self_ = self.self_

        status_color = self.status_color


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_
        if status_color is not UNSET:
            field_dict["statusColor"] = status_color

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        id = d.pop("id", UNSET)

        is_default = d.pop("isDefault", UNSET)

        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        status_color = d.pop("statusColor", UNSET)

        priority = cls(
            description=description,
            icon_url=icon_url,
            id=id,
            is_default=is_default,
            name=name,
            self_=self_,
            status_color=status_color,
        )


        priority.additional_properties = d
        return priority

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
