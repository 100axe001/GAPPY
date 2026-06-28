from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.boolean_condition import BooleanCondition





T = TypeVar("T", bound="DataValidationRule")



@_attrs_define
class DataValidationRule:
    """ A data validation rule.

        Attributes:
            condition (BooleanCondition | Unset): A condition that can evaluate to true or false. BooleanConditions are used
                by conditional formatting, data validation, and the criteria in filters.
            input_message (str | Unset): A message to show the user when adding data to the cell.
            show_custom_ui (bool | Unset): True if the UI should be customized based on the kind of condition. If true,
                "List" conditions will show a dropdown.
            strict (bool | Unset): True if invalid data should be rejected.
     """

    condition: BooleanCondition | Unset = UNSET
    input_message: str | Unset = UNSET
    show_custom_ui: bool | Unset = UNSET
    strict: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_condition import BooleanCondition
        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        input_message = self.input_message

        show_custom_ui = self.show_custom_ui

        strict = self.strict


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if condition is not UNSET:
            field_dict["condition"] = condition
        if input_message is not UNSET:
            field_dict["inputMessage"] = input_message
        if show_custom_ui is not UNSET:
            field_dict["showCustomUi"] = show_custom_ui
        if strict is not UNSET:
            field_dict["strict"] = strict

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_condition import BooleanCondition
        d = dict(src_dict)
        _condition = d.pop("condition", UNSET)
        condition: BooleanCondition | Unset
        if isinstance(_condition,  Unset):
            condition = UNSET
        else:
            condition = BooleanCondition.from_dict(_condition)




        input_message = d.pop("inputMessage", UNSET)

        show_custom_ui = d.pop("showCustomUi", UNSET)

        strict = d.pop("strict", UNSET)

        data_validation_rule = cls(
            condition=condition,
            input_message=input_message,
            show_custom_ui=show_custom_ui,
            strict=strict,
        )


        data_validation_rule.additional_properties = d
        return data_validation_rule

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
