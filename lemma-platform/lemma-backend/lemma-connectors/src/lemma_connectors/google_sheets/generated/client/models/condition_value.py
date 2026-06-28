from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.condition_value_relative_date import ConditionValueRelativeDate
from ..types import UNSET, Unset






T = TypeVar("T", bound="ConditionValue")



@_attrs_define
class ConditionValue:
    """ The value of the condition.

        Attributes:
            relative_date (ConditionValueRelativeDate | Unset): A relative date (based on the current date). Valid only if
                the type is DATE_BEFORE, DATE_AFTER, DATE_ON_OR_BEFORE or DATE_ON_OR_AFTER. Relative dates are not supported in
                data validation. They are supported only in conditional formatting and conditional filters.
            user_entered_value (str | Unset): A value the condition is based on. The value is parsed as if the user typed
                into a cell. Formulas are supported (and must begin with an `=` or a '+').
     """

    relative_date: ConditionValueRelativeDate | Unset = UNSET
    user_entered_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        relative_date: str | Unset = UNSET
        if not isinstance(self.relative_date, Unset):
            relative_date = self.relative_date.value


        user_entered_value = self.user_entered_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if relative_date is not UNSET:
            field_dict["relativeDate"] = relative_date
        if user_entered_value is not UNSET:
            field_dict["userEnteredValue"] = user_entered_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _relative_date = d.pop("relativeDate", UNSET)
        relative_date: ConditionValueRelativeDate | Unset
        if isinstance(_relative_date,  Unset):
            relative_date = UNSET
        else:
            relative_date = ConditionValueRelativeDate(_relative_date)




        user_entered_value = d.pop("userEnteredValue", UNSET)

        condition_value = cls(
            relative_date=relative_date,
            user_entered_value=user_entered_value,
        )


        condition_value.additional_properties = d
        return condition_value

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
