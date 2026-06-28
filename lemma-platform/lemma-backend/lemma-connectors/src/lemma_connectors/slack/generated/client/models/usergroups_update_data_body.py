from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UsergroupsUpdateDataBody")



@_attrs_define
class UsergroupsUpdateDataBody:
    """ 
        Attributes:
            usergroup (str): The encoded ID of the User Group to update.
            handle (str | Unset): A mention handle. Must be unique among channels, users and User Groups.
            description (str | Unset): A short description of the User Group.
            channels (str | Unset): A comma separated string of encoded channel IDs for which the User Group uses as a
                default.
            include_count (bool | Unset): Include the number of users in the User Group.
            name (str | Unset): A name for the User Group. Must be unique among User Groups.
     """

    usergroup: str
    handle: str | Unset = UNSET
    description: str | Unset = UNSET
    channels: str | Unset = UNSET
    include_count: bool | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        usergroup = self.usergroup

        handle = self.handle

        description = self.description

        channels = self.channels

        include_count = self.include_count

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "usergroup": usergroup,
        })
        if handle is not UNSET:
            field_dict["handle"] = handle
        if description is not UNSET:
            field_dict["description"] = description
        if channels is not UNSET:
            field_dict["channels"] = channels
        if include_count is not UNSET:
            field_dict["include_count"] = include_count
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usergroup = d.pop("usergroup")

        handle = d.pop("handle", UNSET)

        description = d.pop("description", UNSET)

        channels = d.pop("channels", UNSET)

        include_count = d.pop("include_count", UNSET)

        name = d.pop("name", UNSET)

        usergroups_update_data_body = cls(
            usergroup=usergroup,
            handle=handle,
            description=description,
            channels=channels,
            include_count=include_count,
            name=name,
        )


        usergroups_update_data_body.additional_properties = d
        return usergroups_update_data_body

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
