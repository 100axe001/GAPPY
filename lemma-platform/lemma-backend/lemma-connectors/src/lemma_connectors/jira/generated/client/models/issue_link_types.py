from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_link_type import IssueLinkType





T = TypeVar("T", bound="IssueLinkTypes")



@_attrs_define
class IssueLinkTypes:
    """ A list of issue link type beans.

        Attributes:
            issue_link_types (list[IssueLinkType] | Unset): The issue link type bean.
     """

    issue_link_types: list[IssueLinkType] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_link_type import IssueLinkType
        issue_link_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issue_link_types, Unset):
            issue_link_types = []
            for issue_link_types_item_data in self.issue_link_types:
                issue_link_types_item = issue_link_types_item_data.to_dict()
                issue_link_types.append(issue_link_types_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issue_link_types is not UNSET:
            field_dict["issueLinkTypes"] = issue_link_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_link_type import IssueLinkType
        d = dict(src_dict)
        _issue_link_types = d.pop("issueLinkTypes", UNSET)
        issue_link_types: list[IssueLinkType] | Unset = UNSET
        if _issue_link_types is not UNSET:
            issue_link_types = []
            for issue_link_types_item_data in _issue_link_types:
                issue_link_types_item = IssueLinkType.from_dict(issue_link_types_item_data)



                issue_link_types.append(issue_link_types_item)


        issue_link_types = cls(
            issue_link_types=issue_link_types,
        )

        return issue_link_types

