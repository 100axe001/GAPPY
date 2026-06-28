from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.issue_matches_for_jql import IssueMatchesForJQL





T = TypeVar("T", bound="IssueMatches")



@_attrs_define
class IssueMatches:
    """ A list of matched issues or errors for each JQL query, in the order the JQL queries were passed.

        Attributes:
            matches (list[IssueMatchesForJQL]):
     """

    matches: list[IssueMatchesForJQL]





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_matches_for_jql import IssueMatchesForJQL
        matches = []
        for matches_item_data in self.matches:
            matches_item = matches_item_data.to_dict()
            matches.append(matches_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "matches": matches,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_matches_for_jql import IssueMatchesForJQL
        d = dict(src_dict)
        matches = []
        _matches = d.pop("matches")
        for matches_item_data in (_matches):
            matches_item = IssueMatchesForJQL.from_dict(matches_item_data)



            matches.append(matches_item)


        issue_matches = cls(
            matches=matches,
        )

        return issue_matches

