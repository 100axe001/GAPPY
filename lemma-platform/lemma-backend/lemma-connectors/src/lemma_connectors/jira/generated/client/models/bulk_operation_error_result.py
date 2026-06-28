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





T = TypeVar("T", bound="BulkOperationErrorResult")



@_attrs_define
class BulkOperationErrorResult:
    """ 
        Attributes:
            element_errors (ErrorCollection | Unset): Error messages from an operation.
            failed_element_number (int | Unset):
            status (int | Unset):
     """

    element_errors: ErrorCollection | Unset = UNSET
    failed_element_number: int | Unset = UNSET
    status: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_collection import ErrorCollection
        element_errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_errors, Unset):
            element_errors = self.element_errors.to_dict()

        failed_element_number = self.failed_element_number

        status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if element_errors is not UNSET:
            field_dict["elementErrors"] = element_errors
        if failed_element_number is not UNSET:
            field_dict["failedElementNumber"] = failed_element_number
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_collection import ErrorCollection
        d = dict(src_dict)
        _element_errors = d.pop("elementErrors", UNSET)
        element_errors: ErrorCollection | Unset
        if isinstance(_element_errors,  Unset):
            element_errors = UNSET
        else:
            element_errors = ErrorCollection.from_dict(_element_errors)




        failed_element_number = d.pop("failedElementNumber", UNSET)

        status = d.pop("status", UNSET)

        bulk_operation_error_result = cls(
            element_errors=element_errors,
            failed_element_number=failed_element_number,
            status=status,
        )

        return bulk_operation_error_result

