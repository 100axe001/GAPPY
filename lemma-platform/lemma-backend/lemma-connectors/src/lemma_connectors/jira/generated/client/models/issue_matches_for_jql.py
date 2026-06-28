from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="IssueMatchesForJQL")



@_attrs_define
class IssueMatchesForJQL:
    """ A list of the issues matched to a JQL query or details of errors encountered during matching.

        Attributes:
            errors (list[str]): A list of errors.
            matched_issues (list[int]): A list of issue IDs.
     """

    errors: list[str]
    matched_issues: list[int]





    def to_dict(self) -> dict[str, Any]:
        errors = self.errors



        matched_issues = self.matched_issues




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "errors": errors,
            "matchedIssues": matched_issues,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        errors = cast(list[str], d.pop("errors"))


        matched_issues = cast(list[int], d.pop("matchedIssues"))


        issue_matches_for_jql = cls(
            errors=errors,
            matched_issues=matched_issues,
        )

        return issue_matches_for_jql

