from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IssueTypeSchemeID")



@_attrs_define
class IssueTypeSchemeID:
    """ The ID of an issue type scheme.

        Attributes:
            issue_type_scheme_id (str): The ID of the issue type scheme.
     """

    issue_type_scheme_id: str





    def to_dict(self) -> dict[str, Any]:
        issue_type_scheme_id = self.issue_type_scheme_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeSchemeId": issue_type_scheme_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_scheme_id = d.pop("issueTypeSchemeId")

        issue_type_scheme_id = cls(
            issue_type_scheme_id=issue_type_scheme_id,
        )

        return issue_type_scheme_id

