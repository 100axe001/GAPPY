from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="IssueList")



@_attrs_define
class IssueList:
    """ A list of issue IDs.

        Attributes:
            issue_ids (list[str]): The list of issue IDs.
     """

    issue_ids: list[str]





    def to_dict(self) -> dict[str, Any]:
        issue_ids = self.issue_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueIds": issue_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_ids = cast(list[str], d.pop("issueIds"))


        issue_list = cls(
            issue_ids=issue_ids,
        )

        return issue_list

