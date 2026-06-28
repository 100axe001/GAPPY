from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ProjectInsight")



@_attrs_define
class ProjectInsight:
    """ Additional details about a project.

        Attributes:
            last_issue_update_time (datetime.datetime | Unset): The last issue update time.
            total_issue_count (int | Unset): Total issue count.
     """

    last_issue_update_time: datetime.datetime | Unset = UNSET
    total_issue_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        last_issue_update_time: str | Unset = UNSET
        if not isinstance(self.last_issue_update_time, Unset):
            last_issue_update_time = self.last_issue_update_time.isoformat()

        total_issue_count = self.total_issue_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if last_issue_update_time is not UNSET:
            field_dict["lastIssueUpdateTime"] = last_issue_update_time
        if total_issue_count is not UNSET:
            field_dict["totalIssueCount"] = total_issue_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _last_issue_update_time = d.pop("lastIssueUpdateTime", UNSET)
        last_issue_update_time: datetime.datetime | Unset
        if isinstance(_last_issue_update_time,  Unset):
            last_issue_update_time = UNSET
        else:
            last_issue_update_time = isoparse(_last_issue_update_time)




        total_issue_count = d.pop("totalIssueCount", UNSET)

        project_insight = cls(
            last_issue_update_time=last_issue_update_time,
            total_issue_count=total_issue_count,
        )

        return project_insight

