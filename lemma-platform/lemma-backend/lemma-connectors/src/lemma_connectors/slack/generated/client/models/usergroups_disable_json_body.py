from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UsergroupsDisableJsonBody")



@_attrs_define
class UsergroupsDisableJsonBody:
    """ 
        Attributes:
            usergroup (str): The encoded ID of the User Group to disable.
            include_count (bool | Unset): Include the number of users in the User Group.
     """

    usergroup: str
    include_count: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        usergroup = self.usergroup

        include_count = self.include_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "usergroup": usergroup,
        })
        if include_count is not UNSET:
            field_dict["include_count"] = include_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usergroup = d.pop("usergroup")

        include_count = d.pop("include_count", UNSET)

        usergroups_disable_json_body = cls(
            usergroup=usergroup,
            include_count=include_count,
        )


        usergroups_disable_json_body.additional_properties = d
        return usergroups_disable_json_body

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
