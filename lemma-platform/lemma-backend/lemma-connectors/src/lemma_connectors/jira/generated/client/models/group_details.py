from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GroupDetails")



@_attrs_define
class GroupDetails:
    """ Details about a group.

        Attributes:
            group_id (None | str | Unset): The ID of the group, which uniquely identifies the group across all Atlassian
                products. For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*.
            name (str | Unset): The name of the group.
     """

    group_id: None | str | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))


        name = d.pop("name", UNSET)

        group_details = cls(
            group_id=group_id,
            name=name,
        )

        return group_details

