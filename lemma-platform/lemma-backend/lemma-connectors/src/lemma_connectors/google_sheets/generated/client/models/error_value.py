from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.error_value_type import ErrorValueType
from ..types import UNSET, Unset






T = TypeVar("T", bound="ErrorValue")



@_attrs_define
class ErrorValue:
    """ An error in a cell.

        Attributes:
            message (str | Unset): A message with more information about the error (in the spreadsheet's locale).
            type_ (ErrorValueType | Unset): The type of error.
     """

    message: str | Unset = UNSET
    type_: ErrorValueType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if message is not UNSET:
            field_dict["message"] = message
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ErrorValueType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = ErrorValueType(_type_)




        error_value = cls(
            message=message,
            type_=type_,
        )


        error_value.additional_properties = d
        return error_value

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
