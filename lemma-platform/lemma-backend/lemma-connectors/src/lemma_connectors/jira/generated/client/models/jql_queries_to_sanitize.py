from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.jql_query_to_sanitize import JqlQueryToSanitize





T = TypeVar("T", bound="JqlQueriesToSanitize")



@_attrs_define
class JqlQueriesToSanitize:
    """ The list of JQL queries to sanitize for the given account IDs.

        Attributes:
            queries (list[JqlQueryToSanitize]): The list of JQL queries to sanitize. Must contain unique values. Maximum of
                20 queries.
     """

    queries: list[JqlQueryToSanitize]





    def to_dict(self) -> dict[str, Any]:
        from ..models.jql_query_to_sanitize import JqlQueryToSanitize
        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "queries": queries,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jql_query_to_sanitize import JqlQueryToSanitize
        d = dict(src_dict)
        queries = []
        _queries = d.pop("queries")
        for queries_item_data in (_queries):
            queries_item = JqlQueryToSanitize.from_dict(queries_item_data)



            queries.append(queries_item)


        jql_queries_to_sanitize = cls(
            queries=queries,
        )

        return jql_queries_to_sanitize

