from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="IssueTypeIds")



@_attrs_define
class IssueTypeIds:
    """ The list of issue type IDs.

        Attributes:
            issue_type_ids (list[str]): The list of issue type IDs.
     """

    issue_type_ids: list[str]





    def to_dict(self) -> dict[str, Any]:
        issue_type_ids = self.issue_type_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeIds": issue_type_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_ids = cast(list[str], d.pop("issueTypeIds"))


        issue_type_ids = cls(
            issue_type_ids=issue_type_ids,
        )

        return issue_type_ids

