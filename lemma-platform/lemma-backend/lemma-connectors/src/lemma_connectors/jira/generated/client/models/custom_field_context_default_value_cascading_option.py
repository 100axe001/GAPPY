from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldContextDefaultValueCascadingOption")



@_attrs_define
class CustomFieldContextDefaultValueCascadingOption:
    """ The default value for a cascading select custom field.

        Attributes:
            context_id (str): The ID of the context.
            option_id (str): The ID of the default option.
            type_ (str):
            cascading_option_id (str | Unset): The ID of the default cascading option.
     """

    context_id: str
    option_id: str
    type_: str
    cascading_option_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        option_id = self.option_id

        type_ = self.type_

        cascading_option_id = self.cascading_option_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "contextId": context_id,
            "optionId": option_id,
            "type": type_,
        })
        if cascading_option_id is not UNSET:
            field_dict["cascadingOptionId"] = cascading_option_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_id = d.pop("contextId")

        option_id = d.pop("optionId")

        type_ = d.pop("type")

        cascading_option_id = d.pop("cascadingOptionId", UNSET)

        custom_field_context_default_value_cascading_option = cls(
            context_id=context_id,
            option_id=option_id,
            type_=type_,
            cascading_option_id=cascading_option_id,
        )


        custom_field_context_default_value_cascading_option.additional_properties = d
        return custom_field_context_default_value_cascading_option

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
