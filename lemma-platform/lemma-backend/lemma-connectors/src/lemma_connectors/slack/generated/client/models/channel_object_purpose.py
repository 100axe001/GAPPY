from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ChannelObjectPurpose")



@_attrs_define
class ChannelObjectPurpose:
    """ 
        Attributes:
            creator (str):
            last_set (int):
            value (str):
     """

    creator: str
    last_set: int
    value: str





    def to_dict(self) -> dict[str, Any]:
        creator = self.creator

        last_set = self.last_set

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "creator": creator,
            "last_set": last_set,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator = d.pop("creator")

        last_set = d.pop("last_set")

        value = d.pop("value")

        channel_object_purpose = cls(
            creator=creator,
            last_set=last_set,
            value=value,
        )

        return channel_object_purpose

