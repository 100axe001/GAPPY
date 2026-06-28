from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VersionUnresolvedIssuesCount")



@_attrs_define
class VersionUnresolvedIssuesCount:
    """ Count of a version's unresolved issues.

        Attributes:
            issues_count (int | Unset): Count of issues.
            issues_unresolved_count (int | Unset): Count of unresolved issues.
            self_ (str | Unset): The URL of these count details.
     """

    issues_count: int | Unset = UNSET
    issues_unresolved_count: int | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        issues_count = self.issues_count

        issues_unresolved_count = self.issues_unresolved_count

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issues_count is not UNSET:
            field_dict["issuesCount"] = issues_count
        if issues_unresolved_count is not UNSET:
            field_dict["issuesUnresolvedCount"] = issues_unresolved_count
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issues_count = d.pop("issuesCount", UNSET)

        issues_unresolved_count = d.pop("issuesUnresolvedCount", UNSET)

        self_ = d.pop("self", UNSET)

        version_unresolved_issues_count = cls(
            issues_count=issues_count,
            issues_unresolved_count=issues_unresolved_count,
            self_=self_,
        )

        return version_unresolved_issues_count

