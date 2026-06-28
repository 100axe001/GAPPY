from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.error_collection import ErrorCollection





T = TypeVar("T", bound="SanitizedJqlQuery")



@_attrs_define
class SanitizedJqlQuery:
    """ Details of the sanitized JQL query.

        Attributes:
            account_id (None | str | Unset): The account ID of the user for whom sanitization was performed.
            errors (ErrorCollection | Unset): Error messages from an operation.
            initial_query (str | Unset): The initial query.
            sanitized_query (None | str | Unset): The sanitized query, if there were no errors.
     """

    account_id: None | str | Unset = UNSET
    errors: ErrorCollection | Unset = UNSET
    initial_query: str | Unset = UNSET
    sanitized_query: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_collection import ErrorCollection
        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        initial_query = self.initial_query

        sanitized_query: None | str | Unset
        if isinstance(self.sanitized_query, Unset):
            sanitized_query = UNSET
        else:
            sanitized_query = self.sanitized_query


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if errors is not UNSET:
            field_dict["errors"] = errors
        if initial_query is not UNSET:
            field_dict["initialQuery"] = initial_query
        if sanitized_query is not UNSET:
            field_dict["sanitizedQuery"] = sanitized_query

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_collection import ErrorCollection
        d = dict(src_dict)
        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))


        _errors = d.pop("errors", UNSET)
        errors: ErrorCollection | Unset
        if isinstance(_errors,  Unset):
            errors = UNSET
        else:
            errors = ErrorCollection.from_dict(_errors)




        initial_query = d.pop("initialQuery", UNSET)

        def _parse_sanitized_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sanitized_query = _parse_sanitized_query(d.pop("sanitizedQuery", UNSET))


        sanitized_jql_query = cls(
            account_id=account_id,
            errors=errors,
            initial_query=initial_query,
            sanitized_query=sanitized_query,
        )

        return sanitized_jql_query

