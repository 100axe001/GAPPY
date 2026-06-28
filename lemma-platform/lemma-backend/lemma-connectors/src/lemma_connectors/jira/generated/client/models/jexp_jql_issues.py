from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.jexp_jql_issues_validation import JexpJqlIssuesValidation
from ..types import UNSET, Unset






T = TypeVar("T", bound="JexpJqlIssues")



@_attrs_define
class JexpJqlIssues:
    """ The JQL specifying the issues available in the evaluated Jira expression under the `issues` context variable. Not
    all issues returned by the JQL query are loaded, only those described by the `startAt` and `maxResults` properties.
    To determine whether it is necessary to iterate to ensure all the issues returned by the JQL query are evaluated,
    inspect `meta.issues.jql.count` in the response.

        Attributes:
            max_results (int | Unset): The maximum number of issues to return from the JQL query. Inspect
                `meta.issues.jql.maxResults` in the response to ensure the maximum value has not been exceeded.
            query (str | Unset): The JQL query.
            start_at (int | Unset): The index of the first issue to return from the JQL query.
            validation (JexpJqlIssuesValidation | Unset): Determines how to validate the JQL query and treat the validation
                results. Default: JexpJqlIssuesValidation.STRICT.
     """

    max_results: int | Unset = UNSET
    query: str | Unset = UNSET
    start_at: int | Unset = UNSET
    validation: JexpJqlIssuesValidation | Unset = JexpJqlIssuesValidation.STRICT





    def to_dict(self) -> dict[str, Any]:
        max_results = self.max_results

        query = self.query

        start_at = self.start_at

        validation: str | Unset = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if query is not UNSET:
            field_dict["query"] = query
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if validation is not UNSET:
            field_dict["validation"] = validation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_results = d.pop("maxResults", UNSET)

        query = d.pop("query", UNSET)

        start_at = d.pop("startAt", UNSET)

        _validation = d.pop("validation", UNSET)
        validation: JexpJqlIssuesValidation | Unset
        if isinstance(_validation,  Unset):
            validation = UNSET
        else:
            validation = JexpJqlIssuesValidation(_validation)




        jexp_jql_issues = cls(
            max_results=max_results,
            query=query,
            start_at=start_at,
            validation=validation,
        )

        return jexp_jql_issues

