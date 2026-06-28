from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="IssuesAndJQLQueries")



@_attrs_define
class IssuesAndJQLQueries:
    """ List of issues and JQL queries.

        Attributes:
            issue_ids (list[int]): A list of issue IDs.
            jqls (list[str]): A list of JQL queries.
     """

    issue_ids: list[int]
    jqls: list[str]





    def to_dict(self) -> dict[str, Any]:
        issue_ids = self.issue_ids



        jqls = self.jqls




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueIds": issue_ids,
            "jqls": jqls,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_ids = cast(list[int], d.pop("issueIds"))


        jqls = cast(list[str], d.pop("jqls"))


        issues_and_jql_queries = cls(
            issue_ids=issue_ids,
            jqls=jqls,
        )

        return issues_and_jql_queries

