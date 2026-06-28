from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AvatarUrlsBean")



@_attrs_define
class AvatarUrlsBean:
    """ 
        Attributes:
            field_16x16 (str | Unset): The URL of the item's 16x16 pixel avatar.
            field_24x24 (str | Unset): The URL of the item's 24x24 pixel avatar.
            field_32x32 (str | Unset): The URL of the item's 32x32 pixel avatar.
            field_48x48 (str | Unset): The URL of the item's 48x48 pixel avatar.
     """

    field_16x16: str | Unset = UNSET
    field_24x24: str | Unset = UNSET
    field_32x32: str | Unset = UNSET
    field_48x48: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_16x16 = self.field_16x16

        field_24x24 = self.field_24x24

        field_32x32 = self.field_32x32

        field_48x48 = self.field_48x48


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if field_16x16 is not UNSET:
            field_dict["16x16"] = field_16x16
        if field_24x24 is not UNSET:
            field_dict["24x24"] = field_24x24
        if field_32x32 is not UNSET:
            field_dict["32x32"] = field_32x32
        if field_48x48 is not UNSET:
            field_dict["48x48"] = field_48x48

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_16x16 = d.pop("16x16", UNSET)

        field_24x24 = d.pop("24x24", UNSET)

        field_32x32 = d.pop("32x32", UNSET)

        field_48x48 = d.pop("48x48", UNSET)

        avatar_urls_bean = cls(
            field_16x16=field_16x16,
            field_24x24=field_24x24,
            field_32x32=field_32x32,
            field_48x48=field_48x48,
        )

        return avatar_urls_bean

