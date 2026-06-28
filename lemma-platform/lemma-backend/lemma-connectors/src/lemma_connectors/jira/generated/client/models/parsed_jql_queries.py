from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.parsed_jql_query import ParsedJqlQuery





T = TypeVar("T", bound="ParsedJqlQueries")



@_attrs_define
class ParsedJqlQueries:
    """ A list of parsed JQL queries.

        Attributes:
            queries (list[ParsedJqlQuery]): A list of parsed JQL queries.
     """

    queries: list[ParsedJqlQuery]





    def to_dict(self) -> dict[str, Any]:
        from ..models.parsed_jql_query import ParsedJqlQuery
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
        from ..models.parsed_jql_query import ParsedJqlQuery
        d = dict(src_dict)
        queries = []
        _queries = d.pop("queries")
        for queries_item_data in (_queries):
            queries_item = ParsedJqlQuery.from_dict(queries_item_data)



            queries.append(queries_item)


        parsed_jql_queries = cls(
            queries=queries,
        )

        return parsed_jql_queries

