from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.sanitized_jql_query import SanitizedJqlQuery





T = TypeVar("T", bound="SanitizedJqlQueries")



@_attrs_define
class SanitizedJqlQueries:
    """ The sanitized JQL queries for the given account IDs.

        Attributes:
            queries (list[SanitizedJqlQuery] | Unset): The list of sanitized JQL queries.
     """

    queries: list[SanitizedJqlQuery] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.sanitized_jql_query import SanitizedJqlQuery
        queries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queries, Unset):
            queries = []
            for queries_item_data in self.queries:
                queries_item = queries_item_data.to_dict()
                queries.append(queries_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if queries is not UNSET:
            field_dict["queries"] = queries

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sanitized_jql_query import SanitizedJqlQuery
        d = dict(src_dict)
        _queries = d.pop("queries", UNSET)
        queries: list[SanitizedJqlQuery] | Unset = UNSET
        if _queries is not UNSET:
            queries = []
            for queries_item_data in _queries:
                queries_item = SanitizedJqlQuery.from_dict(queries_item_data)



                queries.append(queries_item)


        sanitized_jql_queries = cls(
            queries=queries,
        )

        return sanitized_jql_queries

