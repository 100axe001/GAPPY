from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueTypeInfo")



@_attrs_define
class IssueTypeInfo:
    """ Details of an issue type.

        Attributes:
            avatar_id (int | Unset): The avatar of the issue type.
            id (int | Unset): The ID of the issue type.
            name (str | Unset): The name of the issue type.
     """

    avatar_id: int | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        avatar_id = self.avatar_id

        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_id is not UNSET:
            field_dict["avatarId"] = avatar_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_id = d.pop("avatarId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        issue_type_info = cls(
            avatar_id=avatar_id,
            id=id,
            name=name,
        )

        return issue_type_info

