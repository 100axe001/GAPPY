from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="JqlQueryToSanitize")



@_attrs_define
class JqlQueryToSanitize:
    """ The JQL query to sanitize for the account ID. If the account ID is null, sanitizing is performed for an anonymous
    user.

        Attributes:
            query (str): The query to sanitize.
            account_id (None | str | Unset): The account ID of the user, which uniquely identifies the user across all
                Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
     """

    query: str
    account_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        query = self.query

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "query": query,
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))


        jql_query_to_sanitize = cls(
            query=query,
            account_id=account_id,
        )

        return jql_query_to_sanitize

