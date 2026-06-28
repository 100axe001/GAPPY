from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ComponentIssuesCount")



@_attrs_define
class ComponentIssuesCount:
    """ Count of issues assigned to a component.

        Attributes:
            issue_count (int | Unset): The count of issues assigned to a component.
            self_ (str | Unset): The URL for this count of issues for a component.
     """

    issue_count: int | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        issue_count = self.issue_count

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issue_count is not UNSET:
            field_dict["issueCount"] = issue_count
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_count = d.pop("issueCount", UNSET)

        self_ = d.pop("self", UNSET)

        component_issues_count = cls(
            issue_count=issue_count,
            self_=self_,
        )

        return component_issues_count

