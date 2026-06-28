from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jexp_jql_issues import JexpJqlIssues





T = TypeVar("T", bound="JexpIssues")



@_attrs_define
class JexpIssues:
    """ The JQL specifying the issues available in the evaluated Jira expression under the `issues` context variable.

        Attributes:
            jql (JexpJqlIssues | Unset): The JQL specifying the issues available in the evaluated Jira expression under the
                `issues` context variable. Not all issues returned by the JQL query are loaded, only those described by the
                `startAt` and `maxResults` properties. To determine whether it is necessary to iterate to ensure all the issues
                returned by the JQL query are evaluated, inspect `meta.issues.jql.count` in the response.
     """

    jql: JexpJqlIssues | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jexp_jql_issues import JexpJqlIssues
        jql: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jql, Unset):
            jql = self.jql.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if jql is not UNSET:
            field_dict["jql"] = jql

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jexp_jql_issues import JexpJqlIssues
        d = dict(src_dict)
        _jql = d.pop("jql", UNSET)
        jql: JexpJqlIssues | Unset
        if isinstance(_jql,  Unset):
            jql = UNSET
        else:
            jql = JexpJqlIssues.from_dict(_jql)




        jexp_issues = cls(
            jql=jql,
        )

        return jexp_issues

