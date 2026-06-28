from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.found_group import FoundGroup





T = TypeVar("T", bound="FoundGroups")



@_attrs_define
class FoundGroups:
    """ The list of groups found in a search, including header text (Showing X of Y matching groups) and total of matched
    groups.

        Attributes:
            groups (list[FoundGroup] | Unset):
            header (str | Unset): Header text indicating the number of groups in the response and the total number of groups
                found in the search.
            total (int | Unset): The total number of groups found in the search.
     """

    groups: list[FoundGroup] | Unset = UNSET
    header: str | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.found_group import FoundGroup
        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)



        header = self.header

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if groups is not UNSET:
            field_dict["groups"] = groups
        if header is not UNSET:
            field_dict["header"] = header
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.found_group import FoundGroup
        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: list[FoundGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = FoundGroup.from_dict(groups_item_data)



                groups.append(groups_item)


        header = d.pop("header", UNSET)

        total = d.pop("total", UNSET)

        found_groups = cls(
            groups=groups,
            header=header,
            total=total,
        )

        return found_groups

