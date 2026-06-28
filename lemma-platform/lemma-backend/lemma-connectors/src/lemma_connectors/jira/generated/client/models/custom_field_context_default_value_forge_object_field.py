from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_field_context_default_value_forge_object_field_object import CustomFieldContextDefaultValueForgeObjectFieldObject





T = TypeVar("T", bound="CustomFieldContextDefaultValueForgeObjectField")



@_attrs_define
class CustomFieldContextDefaultValueForgeObjectField:
    """ The default value for a Forge object custom field.

        Attributes:
            type_ (str):
            object_ (CustomFieldContextDefaultValueForgeObjectFieldObject | Unset): The default JSON object.
     """

    type_: str
    object_: CustomFieldContextDefaultValueForgeObjectFieldObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_field_context_default_value_forge_object_field_object import CustomFieldContextDefaultValueForgeObjectFieldObject
        type_ = self.type_

        object_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_context_default_value_forge_object_field_object import CustomFieldContextDefaultValueForgeObjectFieldObject
        d = dict(src_dict)
        type_ = d.pop("type")

        _object_ = d.pop("object", UNSET)
        object_: CustomFieldContextDefaultValueForgeObjectFieldObject | Unset
        if isinstance(_object_,  Unset):
            object_ = UNSET
        else:
            object_ = CustomFieldContextDefaultValueForgeObjectFieldObject.from_dict(_object_)




        custom_field_context_default_value_forge_object_field = cls(
            type_=type_,
            object_=object_,
        )


        custom_field_context_default_value_forge_object_field.additional_properties = d
        return custom_field_context_default_value_forge_object_field

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
