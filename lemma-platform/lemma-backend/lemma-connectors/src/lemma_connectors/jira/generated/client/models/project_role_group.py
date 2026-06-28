from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProjectRoleGroup")



@_attrs_define
class ProjectRoleGroup:
    """ Details of the group associated with the role.

        Attributes:
            display_name (str | Unset): The display name of the group.
            group_id (str | Unset): The ID of the group.
            name (str | Unset): The name of the group. As a group's name can change, use of `groupId` is recommended to
                identify the group.
     """

    display_name: str | Unset = UNSET
    group_id: str | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        group_id = self.group_id

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        group_id = d.pop("groupId", UNSET)

        name = d.pop("name", UNSET)

        project_role_group = cls(
            display_name=display_name,
            group_id=group_id,
            name=name,
        )

        return project_role_group

