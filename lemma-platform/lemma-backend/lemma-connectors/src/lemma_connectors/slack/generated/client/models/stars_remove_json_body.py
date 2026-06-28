from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="StarsRemoveJsonBody")



@_attrs_define
class StarsRemoveJsonBody:
    """ 
        Attributes:
            channel (str | Unset): Channel to remove star from, or channel where the message to remove star from was posted
                (used with `timestamp`).
            file (str | Unset): File to remove star from.
            file_comment (str | Unset): File comment to remove star from.
            timestamp (str | Unset): Timestamp of the message to remove star from.
     """

    channel: str | Unset = UNSET
    file: str | Unset = UNSET
    file_comment: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        file = self.file

        file_comment = self.file_comment

        timestamp = self.timestamp


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if file is not UNSET:
            field_dict["file"] = file
        if file_comment is not UNSET:
            field_dict["file_comment"] = file_comment
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        file = d.pop("file", UNSET)

        file_comment = d.pop("file_comment", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        stars_remove_json_body = cls(
            channel=channel,
            file=file,
            file_comment=file_comment,
            timestamp=timestamp,
        )


        stars_remove_json_body.additional_properties = d
        return stars_remove_json_body

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
