from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FileVideoMediaMetadata")



@_attrs_define
class FileVideoMediaMetadata:
    """ Additional metadata about video media. This might not be available immediately upon upload.

        Attributes:
            duration_millis (str | Unset): The duration of the video in milliseconds.
            height (int | Unset): The height of the video in pixels.
            width (int | Unset): The width of the video in pixels.
     """

    duration_millis: str | Unset = UNSET
    height: int | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        duration_millis = self.duration_millis

        height = self.height

        width = self.width


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if duration_millis is not UNSET:
            field_dict["durationMillis"] = duration_millis
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_millis = d.pop("durationMillis", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        file_video_media_metadata = cls(
            duration_millis=duration_millis,
            height=height,
            width=width,
        )


        file_video_media_metadata.additional_properties = d
        return file_video_media_metadata

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
