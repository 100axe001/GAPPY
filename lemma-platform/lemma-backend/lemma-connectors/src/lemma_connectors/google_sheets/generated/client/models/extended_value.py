from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.error_value import ErrorValue





T = TypeVar("T", bound="ExtendedValue")



@_attrs_define
class ExtendedValue:
    """ The kinds of value that a cell in a spreadsheet can have.

        Attributes:
            bool_value (bool | Unset): Represents a boolean value.
            error_value (ErrorValue | Unset): An error in a cell.
            formula_value (str | Unset): Represents a formula.
            number_value (float | Unset): Represents a double value. Note: Dates, Times and DateTimes are represented as
                doubles in SERIAL_NUMBER format.
            string_value (str | Unset): Represents a string value. Leading single quotes are not included. For example, if
                the user typed `'123` into the UI, this would be represented as a `stringValue` of `"123"`.
     """

    bool_value: bool | Unset = UNSET
    error_value: ErrorValue | Unset = UNSET
    formula_value: str | Unset = UNSET
    number_value: float | Unset = UNSET
    string_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_value import ErrorValue
        bool_value = self.bool_value

        error_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_value, Unset):
            error_value = self.error_value.to_dict()

        formula_value = self.formula_value

        number_value = self.number_value

        string_value = self.string_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bool_value is not UNSET:
            field_dict["boolValue"] = bool_value
        if error_value is not UNSET:
            field_dict["errorValue"] = error_value
        if formula_value is not UNSET:
            field_dict["formulaValue"] = formula_value
        if number_value is not UNSET:
            field_dict["numberValue"] = number_value
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_value import ErrorValue
        d = dict(src_dict)
        bool_value = d.pop("boolValue", UNSET)

        _error_value = d.pop("errorValue", UNSET)
        error_value: ErrorValue | Unset
        if isinstance(_error_value,  Unset):
            error_value = UNSET
        else:
            error_value = ErrorValue.from_dict(_error_value)




        formula_value = d.pop("formulaValue", UNSET)

        number_value = d.pop("numberValue", UNSET)

        string_value = d.pop("stringValue", UNSET)

        extended_value = cls(
            bool_value=bool_value,
            error_value=error_value,
            formula_value=formula_value,
            number_value=number_value,
            string_value=string_value,
        )


        extended_value.additional_properties = d
        return extended_value

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
