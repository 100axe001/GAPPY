from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_bean import IssueBean
  from ..models.search_results_names import SearchResultsNames
  from ..models.search_results_schema import SearchResultsSchema





T = TypeVar("T", bound="SearchResults")



@_attrs_define
class SearchResults:
    """ The result of a JQL search.

        Attributes:
            expand (str | Unset): Expand options that include additional search result details in the response.
            issues (list[IssueBean] | Unset): The list of issues found by the search.
            max_results (int | Unset): The maximum number of results that could be on the page.
            names (SearchResultsNames | Unset): The ID and name of each field in the search results.
            schema (SearchResultsSchema | Unset): The schema describing the field types in the search results.
            start_at (int | Unset): The index of the first item returned on the page.
            total (int | Unset): The number of results on the page.
            warning_messages (list[str] | Unset): Any warnings related to the JQL query.
     """

    expand: str | Unset = UNSET
    issues: list[IssueBean] | Unset = UNSET
    max_results: int | Unset = UNSET
    names: SearchResultsNames | Unset = UNSET
    schema: SearchResultsSchema | Unset = UNSET
    start_at: int | Unset = UNSET
    total: int | Unset = UNSET
    warning_messages: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_bean import IssueBean
        from ..models.search_results_names import SearchResultsNames
        from ..models.search_results_schema import SearchResultsSchema
        expand = self.expand

        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)



        max_results = self.max_results

        names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.names, Unset):
            names = self.names.to_dict()

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        start_at = self.start_at

        total = self.total

        warning_messages: list[str] | Unset = UNSET
        if not isinstance(self.warning_messages, Unset):
            warning_messages = self.warning_messages




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expand is not UNSET:
            field_dict["expand"] = expand
        if issues is not UNSET:
            field_dict["issues"] = issues
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if names is not UNSET:
            field_dict["names"] = names
        if schema is not UNSET:
            field_dict["schema"] = schema
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if total is not UNSET:
            field_dict["total"] = total
        if warning_messages is not UNSET:
            field_dict["warningMessages"] = warning_messages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_bean import IssueBean
        from ..models.search_results_names import SearchResultsNames
        from ..models.search_results_schema import SearchResultsSchema
        d = dict(src_dict)
        expand = d.pop("expand", UNSET)

        _issues = d.pop("issues", UNSET)
        issues: list[IssueBean] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = IssueBean.from_dict(issues_item_data)



                issues.append(issues_item)


        max_results = d.pop("maxResults", UNSET)

        _names = d.pop("names", UNSET)
        names: SearchResultsNames | Unset
        if isinstance(_names,  Unset):
            names = UNSET
        else:
            names = SearchResultsNames.from_dict(_names)




        _schema = d.pop("schema", UNSET)
        schema: SearchResultsSchema | Unset
        if isinstance(_schema,  Unset):
            schema = UNSET
        else:
            schema = SearchResultsSchema.from_dict(_schema)




        start_at = d.pop("startAt", UNSET)

        total = d.pop("total", UNSET)

        warning_messages = cast(list[str], d.pop("warningMessages", UNSET))


        search_results = cls(
            expand=expand,
            issues=issues,
            max_results=max_results,
            names=names,
            schema=schema,
            start_at=start_at,
            total=total,
            warning_messages=warning_messages,
        )

        return search_results

