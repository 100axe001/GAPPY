from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UsergroupsCreateJsonBody")



@_attrs_define
class UsergroupsCreateJsonBody:
    """ 
        Attributes:
            name (str): A name for the User Group. Must be unique among User Groups.
            channels (str | Unset): A comma separated string of encoded channel IDs for which the User Group uses as a
                default.
            description (str | Unset): A short description of the User Group.
            handle (str | Unset): A mention handle. Must be unique among channels, users and User Groups.
            include_count (bool | Unset): Include the number of users in each User Group.
     """

    name: str
    channels: str | Unset = UNSET
    description: str | Unset = UNSET
    handle: str | Unset = UNSET
    include_count: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        channels = self.channels

        description = self.description

        handle = self.handle

        include_count = self.include_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if channels is not UNSET:
            field_dict["channels"] = channels
        if description is not UNSET:
            field_dict["description"] = description
        if handle is not UNSET:
            field_dict["handle"] = handle
        if include_count is not UNSET:
            field_dict["include_count"] = include_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        channels = d.pop("channels", UNSET)

        description = d.pop("description", UNSET)

        handle = d.pop("handle", UNSET)

        include_count = d.pop("include_count", UNSET)

        usergroups_create_json_body = cls(
            name=name,
            channels=channels,
            description=description,
            handle=handle,
            include_count=include_count,
        )


        usergroups_create_json_body.additional_properties = d
        return usergroups_create_json_body

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
