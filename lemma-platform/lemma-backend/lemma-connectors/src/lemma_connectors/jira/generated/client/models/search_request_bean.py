from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_request_bean_validate_query import SearchRequestBeanValidateQuery
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchRequestBean")



@_attrs_define
class SearchRequestBean:
    """ 
        Attributes:
            expand (list[str] | Unset): Use [expand](em>#expansion) to include additional information about issues in the
                response. Note that, unlike the majority of instances where `expand` is specified, `expand` is defined as a list
                of values. The expand options are:

                 *  `renderedFields` Returns field values rendered in HTML format.
                 *  `names` Returns the display name of each field.
                 *  `schema` Returns the schema describing a field type.
                 *  `transitions` Returns all possible transitions for the issue.
                 *  `operations` Returns all possible operations for the issue.
                 *  `editmeta` Returns information about how each field can be edited.
                 *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent.
                 *  `versionedRepresentations` Instead of `fields`, returns `versionedRepresentations` a JSON array containing
                each version of a field's value, with the highest numbered item representing the most recent version.
            fields (list[str] | Unset): A list of fields to return for each issue, use it to retrieve a subset of fields.
                This parameter accepts a comma-separated list. Expand options include:

                 *  `*all` Returns all fields.
                 *  `*navigable` Returns navigable fields.
                 *  Any issue field, prefixed with a minus to exclude.

                The default is `*navigable`.

                Examples:

                 *  `summary,comment` Returns the summary and comments fields only.
                 *  `-description` Returns all navigable (default) fields except description.
                 *  `*all,-comment` Returns all fields except comments.

                Multiple `fields` parameters can be included in a request.

                Note: All navigable fields are returned by default. This differs from [GET issue](#api-rest-api-3-issue-
                issueIdOrKey-get) where the default is all fields.
            fields_by_keys (bool | Unset): Reference fields by their key (rather than ID). The default is `false`.
            jql (str | Unset): A [JQL](https://confluence.atlassian.com/x/egORLQ) expression.
            max_results (int | Unset): The maximum number of items to return per page. Default: 50.
            properties (list[str] | Unset): A list of up to 5 issue properties to include in the results. This parameter
                accepts a comma-separated list.
            start_at (int | Unset): The index of the first item to return in the page of results (page offset). The base
                index is `0`.
            validate_query (SearchRequestBeanValidateQuery | Unset): Determines how to validate the JQL query and treat the
                validation results. Supported values:

                 *  `strict` Returns a 400 response code if any errors are found, along with a list of all errors (and
                warnings).
                 *  `warn` Returns all errors as warnings.
                 *  `none` No validation is performed.
                 *  `true` *Deprecated* A legacy synonym for `strict`.
                 *  `false` *Deprecated* A legacy synonym for `warn`.

                The default is `strict`.

                Note: If the JQL is not correctly formed a 400 response code is returned, regardless of the `validateQuery`
                value.
     """

    expand: list[str] | Unset = UNSET
    fields: list[str] | Unset = UNSET
    fields_by_keys: bool | Unset = UNSET
    jql: str | Unset = UNSET
    max_results: int | Unset = 50
    properties: list[str] | Unset = UNSET
    start_at: int | Unset = UNSET
    validate_query: SearchRequestBeanValidateQuery | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        expand: list[str] | Unset = UNSET
        if not isinstance(self.expand, Unset):
            expand = self.expand



        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields



        fields_by_keys = self.fields_by_keys

        jql = self.jql

        max_results = self.max_results

        properties: list[str] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties



        start_at = self.start_at

        validate_query: str | Unset = UNSET
        if not isinstance(self.validate_query, Unset):
            validate_query = self.validate_query.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expand is not UNSET:
            field_dict["expand"] = expand
        if fields is not UNSET:
            field_dict["fields"] = fields
        if fields_by_keys is not UNSET:
            field_dict["fieldsByKeys"] = fields_by_keys
        if jql is not UNSET:
            field_dict["jql"] = jql
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if properties is not UNSET:
            field_dict["properties"] = properties
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if validate_query is not UNSET:
            field_dict["validateQuery"] = validate_query

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expand = cast(list[str], d.pop("expand", UNSET))


        fields = cast(list[str], d.pop("fields", UNSET))


        fields_by_keys = d.pop("fieldsByKeys", UNSET)

        jql = d.pop("jql", UNSET)

        max_results = d.pop("maxResults", UNSET)

        properties = cast(list[str], d.pop("properties", UNSET))


        start_at = d.pop("startAt", UNSET)

        _validate_query = d.pop("validateQuery", UNSET)
        validate_query: SearchRequestBeanValidateQuery | Unset
        if isinstance(_validate_query,  Unset):
            validate_query = UNSET
        else:
            validate_query = SearchRequestBeanValidateQuery(_validate_query)




        search_request_bean = cls(
            expand=expand,
            fields=fields,
            fields_by_keys=fields_by_keys,
            jql=jql,
            max_results=max_results,
            properties=properties,
            start_at=start_at,
            validate_query=validate_query,
        )

        return search_request_bean

