from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReactionsRemoveDataBody")



@_attrs_define
class ReactionsRemoveDataBody:
    """ 
        Attributes:
            name (str): Reaction (emoji) name.
            file (str | Unset): File to remove reaction from.
            file_comment (str | Unset): File comment to remove reaction from.
            channel (str | Unset): Channel where the message to remove reaction from was posted.
            timestamp (str | Unset): Timestamp of the message to remove reaction from.
     """

    name: str
    file: str | Unset = UNSET
    file_comment: str | Unset = UNSET
    channel: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        file = self.file

        file_comment = self.file_comment

        channel = self.channel

        timestamp = self.timestamp


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if file is not UNSET:
            field_dict["file"] = file
        if file_comment is not UNSET:
            field_dict["file_comment"] = file_comment
        if channel is not UNSET:
            field_dict["channel"] = channel
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        file = d.pop("file", UNSET)

        file_comment = d.pop("file_comment", UNSET)

        channel = d.pop("channel", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        reactions_remove_data_body = cls(
            name=name,
            file=file,
            file_comment=file_comment,
            channel=channel,
            timestamp=timestamp,
        )


        reactions_remove_data_body.additional_properties = d
        return reactions_remove_data_body

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
