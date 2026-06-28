from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldContextDefaultValueSingleVersionPicker")



@_attrs_define
class CustomFieldContextDefaultValueSingleVersionPicker:
    """ The default value for a version picker custom field.

        Attributes:
            type_ (str):
            version_id (str): The ID of the default version.
            version_order (str | Unset): The order the pickable versions are displayed in. If not provided, the released-
                first order is used. Available version orders are `"releasedFirst"` and `"unreleasedFirst"`.
     """

    type_: str
    version_id: str
    version_order: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        version_id = self.version_id

        version_order = self.version_order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "versionId": version_id,
        })
        if version_order is not UNSET:
            field_dict["versionOrder"] = version_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        version_id = d.pop("versionId")

        version_order = d.pop("versionOrder", UNSET)

        custom_field_context_default_value_single_version_picker = cls(
            type_=type_,
            version_id=version_id,
            version_order=version_order,
        )


        custom_field_context_default_value_single_version_picker.additional_properties = d
        return custom_field_context_default_value_single_version_picker

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
