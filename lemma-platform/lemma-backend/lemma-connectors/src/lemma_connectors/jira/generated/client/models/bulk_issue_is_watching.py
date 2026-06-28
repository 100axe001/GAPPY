from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_issue_is_watching_issues_is_watching import BulkIssueIsWatchingIssuesIsWatching





T = TypeVar("T", bound="BulkIssueIsWatching")



@_attrs_define
class BulkIssueIsWatching:
    """ A container for the watch status of a list of issues.

        Attributes:
            issues_is_watching (BulkIssueIsWatchingIssuesIsWatching | Unset): The map of issue ID to boolean watch status.
     """

    issues_is_watching: BulkIssueIsWatchingIssuesIsWatching | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_issue_is_watching_issues_is_watching import BulkIssueIsWatchingIssuesIsWatching
        issues_is_watching: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issues_is_watching, Unset):
            issues_is_watching = self.issues_is_watching.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issues_is_watching is not UNSET:
            field_dict["issuesIsWatching"] = issues_is_watching

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_issue_is_watching_issues_is_watching import BulkIssueIsWatchingIssuesIsWatching
        d = dict(src_dict)
        _issues_is_watching = d.pop("issuesIsWatching", UNSET)
        issues_is_watching: BulkIssueIsWatchingIssuesIsWatching | Unset
        if isinstance(_issues_is_watching,  Unset):
            issues_is_watching = UNSET
        else:
            issues_is_watching = BulkIssueIsWatchingIssuesIsWatching.from_dict(_issues_is_watching)




        bulk_issue_is_watching = cls(
            issues_is_watching=issues_is_watching,
        )

        return bulk_issue_is_watching

