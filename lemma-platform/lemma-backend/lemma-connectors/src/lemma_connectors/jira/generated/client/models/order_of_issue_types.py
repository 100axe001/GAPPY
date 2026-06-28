from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.order_of_issue_types_position import OrderOfIssueTypesPosition
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OrderOfIssueTypes")



@_attrs_define
class OrderOfIssueTypes:
    """ An ordered list of issue type IDs and information about where to move them.

        Attributes:
            issue_type_ids (list[str]): A list of the issue type IDs to move. The order of the issue type IDs in the list is
                the order they are given after the move.
            after (str | Unset): The ID of the issue type to place the moved issue types after. Required if `position` isn't
                provided.
            position (OrderOfIssueTypesPosition | Unset): The position the issue types should be moved to. Required if
                `after` isn't provided.
     """

    issue_type_ids: list[str]
    after: str | Unset = UNSET
    position: OrderOfIssueTypesPosition | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        issue_type_ids = self.issue_type_ids



        after = self.after

        position: str | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeIds": issue_type_ids,
        })
        if after is not UNSET:
            field_dict["after"] = after
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_ids = cast(list[str], d.pop("issueTypeIds"))


        after = d.pop("after", UNSET)

        _position = d.pop("position", UNSET)
        position: OrderOfIssueTypesPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = OrderOfIssueTypesPosition(_position)




        order_of_issue_types = cls(
            issue_type_ids=issue_type_ids,
            after=after,
            position=position,
        )

        return order_of_issue_types

