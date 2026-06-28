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
  from ..models.warning_collection import WarningCollection





T = TypeVar("T", bound="NestedResponse")



@_attrs_define
class NestedResponse:
    """ 
        Attributes:
            error_collection (ErrorCollection | Unset): Error messages from an operation.
            status (int | Unset):
            warning_collection (WarningCollection | Unset):
     """

    error_collection: ErrorCollection | Unset = UNSET
    status: int | Unset = UNSET
    warning_collection: WarningCollection | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_collection import ErrorCollection
        from ..models.warning_collection import WarningCollection
        error_collection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_collection, Unset):
            error_collection = self.error_collection.to_dict()

        status = self.status

        warning_collection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.warning_collection, Unset):
            warning_collection = self.warning_collection.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if error_collection is not UNSET:
            field_dict["errorCollection"] = error_collection
        if status is not UNSET:
            field_dict["status"] = status
        if warning_collection is not UNSET:
            field_dict["warningCollection"] = warning_collection

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_collection import ErrorCollection
        from ..models.warning_collection import WarningCollection
        d = dict(src_dict)
        _error_collection = d.pop("errorCollection", UNSET)
        error_collection: ErrorCollection | Unset
        if isinstance(_error_collection,  Unset):
            error_collection = UNSET
        else:
            error_collection = ErrorCollection.from_dict(_error_collection)




        status = d.pop("status", UNSET)

        _warning_collection = d.pop("warningCollection", UNSET)
        warning_collection: WarningCollection | Unset
        if isinstance(_warning_collection,  Unset):
            warning_collection = UNSET
        else:
            warning_collection = WarningCollection.from_dict(_warning_collection)




        nested_response = cls(
            error_collection=error_collection,
            status=status,
            warning_collection=warning_collection,
        )

        return nested_response

