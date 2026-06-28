from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="JQLPersonalDataMigrationRequest")



@_attrs_define
class JQLPersonalDataMigrationRequest:
    """ The JQL queries to be converted.

        Attributes:
            query_strings (list[str] | Unset): A list of queries with user identifiers. Maximum of 100 queries.
     """

    query_strings: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        query_strings: list[str] | Unset = UNSET
        if not isinstance(self.query_strings, Unset):
            query_strings = self.query_strings




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if query_strings is not UNSET:
            field_dict["queryStrings"] = query_strings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query_strings = cast(list[str], d.pop("queryStrings", UNSET))


        jql_personal_data_migration_request = cls(
            query_strings=query_strings,
        )

        return jql_personal_data_migration_request

