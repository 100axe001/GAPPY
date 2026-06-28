from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReorderIssuePriorities")



@_attrs_define
class ReorderIssuePriorities:
    """ Change the order of issue priorities.

        Attributes:
            ids (list[str]): The list of issue IDs to be reordered. Cannot contain duplicates nor after ID.
            after (str | Unset): The ID of the priority. Required if `position` isn't provided.
            position (str | Unset): The position for issue priorities to be moved to. Required if `after` isn't provided.
     """

    ids: list[str]
    after: str | Unset = UNSET
    position: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ids = self.ids



        after = self.after

        position = self.position


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ids": ids,
        })
        if after is not UNSET:
            field_dict["after"] = after
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))


        after = d.pop("after", UNSET)

        position = d.pop("position", UNSET)

        reorder_issue_priorities = cls(
            ids=ids,
            after=after,
            position=position,
        )

        return reorder_issue_priorities

