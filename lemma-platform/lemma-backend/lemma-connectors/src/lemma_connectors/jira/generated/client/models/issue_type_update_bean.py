from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueTypeUpdateBean")



@_attrs_define
class IssueTypeUpdateBean:
    """ 
        Attributes:
            avatar_id (int | Unset): The ID of an issue type avatar.
            description (str | Unset): The description of the issue type.
            name (str | Unset): The unique name for the issue type. The maximum length is 60 characters.
     """

    avatar_id: int | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        avatar_id = self.avatar_id

        description = self.description

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_id is not UNSET:
            field_dict["avatarId"] = avatar_id
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_id = d.pop("avatarId", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        issue_type_update_bean = cls(
            avatar_id=avatar_id,
            description=description,
            name=name,
        )

        return issue_type_update_bean

