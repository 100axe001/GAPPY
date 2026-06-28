from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IssueTypeSchemeMapping")



@_attrs_define
class IssueTypeSchemeMapping:
    """ Issue type scheme item.

        Attributes:
            issue_type_id (str): The ID of the issue type.
            issue_type_scheme_id (str): The ID of the issue type scheme.
     """

    issue_type_id: str
    issue_type_scheme_id: str





    def to_dict(self) -> dict[str, Any]:
        issue_type_id = self.issue_type_id

        issue_type_scheme_id = self.issue_type_scheme_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeId": issue_type_id,
            "issueTypeSchemeId": issue_type_scheme_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_id = d.pop("issueTypeId")

        issue_type_scheme_id = d.pop("issueTypeSchemeId")

        issue_type_scheme_mapping = cls(
            issue_type_id=issue_type_id,
            issue_type_scheme_id=issue_type_scheme_id,
        )

        return issue_type_scheme_mapping

