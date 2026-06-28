from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jql_query_with_unknown_users import JQLQueryWithUnknownUsers





T = TypeVar("T", bound="ConvertedJQLQueries")



@_attrs_define
class ConvertedJQLQueries:
    """ The converted JQL queries.

        Attributes:
            queries_with_unknown_users (list[JQLQueryWithUnknownUsers] | Unset): List of queries containing user information
                that could not be mapped to an existing user
            query_strings (list[str] | Unset): The list of converted query strings with account IDs in place of user
                identifiers.
     """

    queries_with_unknown_users: list[JQLQueryWithUnknownUsers] | Unset = UNSET
    query_strings: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jql_query_with_unknown_users import JQLQueryWithUnknownUsers
        queries_with_unknown_users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queries_with_unknown_users, Unset):
            queries_with_unknown_users = []
            for queries_with_unknown_users_item_data in self.queries_with_unknown_users:
                queries_with_unknown_users_item = queries_with_unknown_users_item_data.to_dict()
                queries_with_unknown_users.append(queries_with_unknown_users_item)



        query_strings: list[str] | Unset = UNSET
        if not isinstance(self.query_strings, Unset):
            query_strings = self.query_strings




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if queries_with_unknown_users is not UNSET:
            field_dict["queriesWithUnknownUsers"] = queries_with_unknown_users
        if query_strings is not UNSET:
            field_dict["queryStrings"] = query_strings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jql_query_with_unknown_users import JQLQueryWithUnknownUsers
        d = dict(src_dict)
        _queries_with_unknown_users = d.pop("queriesWithUnknownUsers", UNSET)
        queries_with_unknown_users: list[JQLQueryWithUnknownUsers] | Unset = UNSET
        if _queries_with_unknown_users is not UNSET:
            queries_with_unknown_users = []
            for queries_with_unknown_users_item_data in _queries_with_unknown_users:
                queries_with_unknown_users_item = JQLQueryWithUnknownUsers.from_dict(queries_with_unknown_users_item_data)



                queries_with_unknown_users.append(queries_with_unknown_users_item)


        query_strings = cast(list[str], d.pop("queryStrings", UNSET))


        converted_jql_queries = cls(
            queries_with_unknown_users=queries_with_unknown_users,
            query_strings=query_strings,
        )

        return converted_jql_queries

