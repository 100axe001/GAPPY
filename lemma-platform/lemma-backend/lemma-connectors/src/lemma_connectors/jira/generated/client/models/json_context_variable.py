from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.json_context_variable_value import JsonContextVariableValue





T = TypeVar("T", bound="JsonContextVariable")



@_attrs_define
class JsonContextVariable:
    """ A JSON object with custom content.

        Attributes:
            type_ (str): Type of custom context variable.
            value (JsonContextVariableValue | Unset): A JSON object containing custom content.
     """

    type_: str
    value: JsonContextVariableValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.json_context_variable_value import JsonContextVariableValue
        type_ = self.type_

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_context_variable_value import JsonContextVariableValue
        d = dict(src_dict)
        type_ = d.pop("type")

        _value = d.pop("value", UNSET)
        value: JsonContextVariableValue | Unset
        if isinstance(_value,  Unset):
            value = UNSET
        else:
            value = JsonContextVariableValue.from_dict(_value)




        json_context_variable = cls(
            type_=type_,
            value=value,
        )


        json_context_variable.additional_properties = d
        return json_context_variable

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
