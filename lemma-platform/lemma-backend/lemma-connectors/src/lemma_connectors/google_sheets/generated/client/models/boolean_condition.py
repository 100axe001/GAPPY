from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.boolean_condition_type import BooleanConditionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.condition_value import ConditionValue





T = TypeVar("T", bound="BooleanCondition")



@_attrs_define
class BooleanCondition:
    """ A condition that can evaluate to true or false. BooleanConditions are used by conditional formatting, data
    validation, and the criteria in filters.

        Attributes:
            type_ (BooleanConditionType | Unset): The type of condition.
            values (list[ConditionValue] | Unset): The values of the condition. The number of supported values depends on
                the condition type. Some support zero values, others one or two values, and ConditionType.ONE_OF_LIST supports
                an arbitrary number of values.
     """

    type_: BooleanConditionType | Unset = UNSET
    values: list[ConditionValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.condition_value import ConditionValue
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_value import ConditionValue
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: BooleanConditionType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = BooleanConditionType(_type_)




        _values = d.pop("values", UNSET)
        values: list[ConditionValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = ConditionValue.from_dict(values_item_data)



                values.append(values_item)


        boolean_condition = cls(
            type_=type_,
            values=values,
        )


        boolean_condition.additional_properties = d
        return boolean_condition

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
