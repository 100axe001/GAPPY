from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="JQLQueryWithUnknownUsers")



@_attrs_define
class JQLQueryWithUnknownUsers:
    """ JQL queries that contained users that could not be found

        Attributes:
            converted_query (str | Unset): The converted query, with accountIDs instead of user identifiers, or 'unknown'
                for users that could not be found
            original_query (str | Unset): The original query, for reference
     """

    converted_query: str | Unset = UNSET
    original_query: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        converted_query = self.converted_query

        original_query = self.original_query


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if converted_query is not UNSET:
            field_dict["convertedQuery"] = converted_query
        if original_query is not UNSET:
            field_dict["originalQuery"] = original_query

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        converted_query = d.pop("convertedQuery", UNSET)

        original_query = d.pop("originalQuery", UNSET)

        jql_query_with_unknown_users = cls(
            converted_query=converted_query,
            original_query=original_query,
        )

        return jql_query_with_unknown_users

