from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ObjsIcon")



@_attrs_define
class ObjsIcon:
    """ 
        Attributes:
            image_102 (str | Unset):
            image_132 (str | Unset):
            image_230 (str | Unset):
            image_34 (str | Unset):
            image_44 (str | Unset):
            image_68 (str | Unset):
            image_88 (str | Unset):
            image_default (bool | Unset):
     """

    image_102: str | Unset = UNSET
    image_132: str | Unset = UNSET
    image_230: str | Unset = UNSET
    image_34: str | Unset = UNSET
    image_44: str | Unset = UNSET
    image_68: str | Unset = UNSET
    image_88: str | Unset = UNSET
    image_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        image_102 = self.image_102

        image_132 = self.image_132

        image_230 = self.image_230

        image_34 = self.image_34

        image_44 = self.image_44

        image_68 = self.image_68

        image_88 = self.image_88

        image_default = self.image_default


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if image_102 is not UNSET:
            field_dict["image_102"] = image_102
        if image_132 is not UNSET:
            field_dict["image_132"] = image_132
        if image_230 is not UNSET:
            field_dict["image_230"] = image_230
        if image_34 is not UNSET:
            field_dict["image_34"] = image_34
        if image_44 is not UNSET:
            field_dict["image_44"] = image_44
        if image_68 is not UNSET:
            field_dict["image_68"] = image_68
        if image_88 is not UNSET:
            field_dict["image_88"] = image_88
        if image_default is not UNSET:
            field_dict["image_default"] = image_default

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_102 = d.pop("image_102", UNSET)

        image_132 = d.pop("image_132", UNSET)

        image_230 = d.pop("image_230", UNSET)

        image_34 = d.pop("image_34", UNSET)

        image_44 = d.pop("image_44", UNSET)

        image_68 = d.pop("image_68", UNSET)

        image_88 = d.pop("image_88", UNSET)

        image_default = d.pop("image_default", UNSET)

        objs_icon = cls(
            image_102=image_102,
            image_132=image_132,
            image_230=image_230,
            image_34=image_34,
            image_44=image_44,
            image_68=image_68,
            image_88=image_88,
            image_default=image_default,
        )


        objs_icon.additional_properties = d
        return objs_icon

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
