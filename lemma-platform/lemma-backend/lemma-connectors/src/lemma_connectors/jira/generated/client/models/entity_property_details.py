from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="EntityPropertyDetails")



@_attrs_define
class EntityPropertyDetails:
    """ 
        Attributes:
            entity_id (float): The entity property ID. Example: 123.
            key (str): The entity property key. Example: mykey.
            value (str): The new value of the entity property. Example: newValue.
     """

    entity_id: float
    key: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        key = self.key

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "entityId": entity_id,
            "key": key,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_id = d.pop("entityId")

        key = d.pop("key")

        value = d.pop("value")

        entity_property_details = cls(
            entity_id=entity_id,
            key=key,
            value=value,
        )


        entity_property_details.additional_properties = d
        return entity_property_details

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
