from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IssuesJqlMetaDataBean")



@_attrs_define
class IssuesJqlMetaDataBean:
    """ The description of the page of issues loaded by the provided JQL query.

        Attributes:
            count (int): The number of issues that were loaded in this evaluation.
            max_results (int): The maximum number of issues that could be loaded in this evaluation.
            start_at (int): The index of the first issue.
            total_count (int): The total number of issues the JQL returned.
            validation_warnings (list[str] | Unset): Any warnings related to the JQL query. Present only if the validation
                mode was set to `warn`.
     """

    count: int
    max_results: int
    start_at: int
    total_count: int
    validation_warnings: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        max_results = self.max_results

        start_at = self.start_at

        total_count = self.total_count

        validation_warnings: list[str] | Unset = UNSET
        if not isinstance(self.validation_warnings, Unset):
            validation_warnings = self.validation_warnings




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "count": count,
            "maxResults": max_results,
            "startAt": start_at,
            "totalCount": total_count,
        })
        if validation_warnings is not UNSET:
            field_dict["validationWarnings"] = validation_warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        max_results = d.pop("maxResults")

        start_at = d.pop("startAt")

        total_count = d.pop("totalCount")

        validation_warnings = cast(list[str], d.pop("validationWarnings", UNSET))


        issues_jql_meta_data_bean = cls(
            count=count,
            max_results=max_results,
            start_at=start_at,
            total_count=total_count,
            validation_warnings=validation_warnings,
        )

        return issues_jql_meta_data_bean

