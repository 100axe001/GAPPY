from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FileShortcutDetails")



@_attrs_define
class FileShortcutDetails:
    """ Shortcut file details. Only populated for shortcut files, which have the mimeType field set to
    application/vnd.google-apps.shortcut.

        Attributes:
            target_id (str | Unset): The ID of the file that this shortcut points to.
            target_mime_type (str | Unset): The MIME type of the file that this shortcut points to. The value of this field
                is a snapshot of the target's MIME type, captured when the shortcut is created.
            target_resource_key (str | Unset): The ResourceKey for the target file.
     """

    target_id: str | Unset = UNSET
    target_mime_type: str | Unset = UNSET
    target_resource_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id

        target_mime_type = self.target_mime_type

        target_resource_key = self.target_resource_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if target_mime_type is not UNSET:
            field_dict["targetMimeType"] = target_mime_type
        if target_resource_key is not UNSET:
            field_dict["targetResourceKey"] = target_resource_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_id = d.pop("targetId", UNSET)

        target_mime_type = d.pop("targetMimeType", UNSET)

        target_resource_key = d.pop("targetResourceKey", UNSET)

        file_shortcut_details = cls(
            target_id=target_id,
            target_mime_type=target_mime_type,
            target_resource_key=target_resource_key,
        )


        file_shortcut_details.additional_properties = d
        return file_shortcut_details

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
