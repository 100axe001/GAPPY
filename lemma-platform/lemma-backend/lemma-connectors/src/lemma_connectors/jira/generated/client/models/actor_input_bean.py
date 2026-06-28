from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ActorInputBean")



@_attrs_define
class ActorInputBean:
    """ 
        Attributes:
            group (list[str] | Unset): The name of the group to add as a default actor. This parameter cannot be used with
                the `groupId` parameter. As a group's name can change,use of `groupId` is recommended. This parameter accepts a
                comma-separated list. For example, `"group":["project-admin", "jira-developers"]`.
            group_id (list[str] | Unset): The ID of the group to add as a default actor. This parameter cannot be used with
                the `group` parameter This parameter accepts a comma-separated list. For example,
                `"groupId":["77f6ab39-e755-4570-a6ae-2d7a8df0bcb8", "0c011f85-69ed-49c4-a801-3b18d0f771bc"]`.
            user (list[str] | Unset): The account IDs of the users to add as default actors. This parameter accepts a comma-
                separated list. For example, `"user":["5b10a2844c20165700ede21g", "5b109f2e9729b51b54dc274d"]`.
     """

    group: list[str] | Unset = UNSET
    group_id: list[str] | Unset = UNSET
    user: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        group: list[str] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group



        group_id: list[str] | Unset = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = self.group_id



        user: list[str] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group is not UNSET:
            field_dict["group"] = group
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group = cast(list[str], d.pop("group", UNSET))


        group_id = cast(list[str], d.pop("groupId", UNSET))


        user = cast(list[str], d.pop("user", UNSET))


        actor_input_bean = cls(
            group=group,
            group_id=group_id,
            user=user,
        )

        return actor_input_bean

