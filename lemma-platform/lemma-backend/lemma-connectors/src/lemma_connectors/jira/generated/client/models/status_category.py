from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="StatusCategory")



@_attrs_define
class StatusCategory:
    """ A status category.

        Attributes:
            color_name (str | Unset): The name of the color used to represent the status category.
            id (int | Unset): The ID of the status category.
            key (str | Unset): The key of the status category.
            name (str | Unset): The name of the status category.
            self_ (str | Unset): The URL of the status category.
     """

    color_name: str | Unset = UNSET
    id: int | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        color_name = self.color_name

        id = self.id

        key = self.key

        name = self.name

        self_ = self.self_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if color_name is not UNSET:
            field_dict["colorName"] = color_name
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color_name = d.pop("colorName", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        status_category = cls(
            color_name=color_name,
            id=id,
            key=key,
            name=name,
            self_=self_,
        )


        status_category.additional_properties = d
        return status_category

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
