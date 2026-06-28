from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.error_collection_errors import ErrorCollectionErrors





T = TypeVar("T", bound="ErrorCollection")



@_attrs_define
class ErrorCollection:
    """ Error messages from an operation.

        Attributes:
            error_messages (list[str] | Unset): The list of error messages produced by this operation. For example, "input
                parameter 'key' must be provided"
            errors (ErrorCollectionErrors | Unset): The list of errors by parameter returned by the operation. For
                example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase
                alphanumeric characters."
            status (int | Unset):
     """

    error_messages: list[str] | Unset = UNSET
    errors: ErrorCollectionErrors | Unset = UNSET
    status: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_collection_errors import ErrorCollectionErrors
        error_messages: list[str] | Unset = UNSET
        if not isinstance(self.error_messages, Unset):
            error_messages = self.error_messages



        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if error_messages is not UNSET:
            field_dict["errorMessages"] = error_messages
        if errors is not UNSET:
            field_dict["errors"] = errors
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_collection_errors import ErrorCollectionErrors
        d = dict(src_dict)
        error_messages = cast(list[str], d.pop("errorMessages", UNSET))


        _errors = d.pop("errors", UNSET)
        errors: ErrorCollectionErrors | Unset
        if isinstance(_errors,  Unset):
            errors = UNSET
        else:
            errors = ErrorCollectionErrors.from_dict(_errors)




        status = d.pop("status", UNSET)

        error_collection = cls(
            error_messages=error_messages,
            errors=errors,
            status=status,
        )

        return error_collection

