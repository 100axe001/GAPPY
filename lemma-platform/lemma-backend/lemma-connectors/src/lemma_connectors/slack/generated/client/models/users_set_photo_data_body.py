from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UsersSetPhotoDataBody")



@_attrs_define
class UsersSetPhotoDataBody:
    """ 
        Attributes:
            token (str): Authentication token. Requires scope: `users.profile:write`
            crop_w (str | Unset): Width/height of crop box (always square)
            crop_x (str | Unset): X coordinate of top-left corner of crop box
            crop_y (str | Unset): Y coordinate of top-left corner of crop box
            image (str | Unset): File contents via `multipart/form-data`.
     """

    token: str
    crop_w: str | Unset = UNSET
    crop_x: str | Unset = UNSET
    crop_y: str | Unset = UNSET
    image: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        token = self.token

        crop_w = self.crop_w

        crop_x = self.crop_x

        crop_y = self.crop_y

        image = self.image


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "token": token,
        })
        if crop_w is not UNSET:
            field_dict["crop_w"] = crop_w
        if crop_x is not UNSET:
            field_dict["crop_x"] = crop_x
        if crop_y is not UNSET:
            field_dict["crop_y"] = crop_y
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        crop_w = d.pop("crop_w", UNSET)

        crop_x = d.pop("crop_x", UNSET)

        crop_y = d.pop("crop_y", UNSET)

        image = d.pop("image", UNSET)

        users_set_photo_data_body = cls(
            token=token,
            crop_w=crop_w,
            crop_x=crop_x,
            crop_y=crop_y,
            image=image,
        )


        users_set_photo_data_body.additional_properties = d
        return users_set_photo_data_body

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
