from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="JqlQueriesToParse")



@_attrs_define
class JqlQueriesToParse:
    """ A list of JQL queries to parse.

        Attributes:
            queries (list[str]): A list of queries to parse.
     """

    queries: list[str]





    def to_dict(self) -> dict[str, Any]:
        queries = self.queries




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "queries": queries,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        queries = cast(list[str], d.pop("queries"))


        jql_queries_to_parse = cls(
            queries=queries,
        )

        return jql_queries_to_parse

