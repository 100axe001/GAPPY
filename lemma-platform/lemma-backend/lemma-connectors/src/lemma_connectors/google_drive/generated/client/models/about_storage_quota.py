from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AboutStorageQuota")



@_attrs_define
class AboutStorageQuota:
    """ The user's storage quota limits and usage. All fields are measured in bytes.

        Attributes:
            limit (str | Unset): The usage limit, if applicable. This will not be present if the user has unlimited storage.
            usage (str | Unset): The total usage across all services.
            usage_in_drive (str | Unset): The usage by all files in Google Drive.
            usage_in_drive_trash (str | Unset): The usage by trashed files in Google Drive.
     """

    limit: str | Unset = UNSET
    usage: str | Unset = UNSET
    usage_in_drive: str | Unset = UNSET
    usage_in_drive_trash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        usage = self.usage

        usage_in_drive = self.usage_in_drive

        usage_in_drive_trash = self.usage_in_drive_trash


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if usage is not UNSET:
            field_dict["usage"] = usage
        if usage_in_drive is not UNSET:
            field_dict["usageInDrive"] = usage_in_drive
        if usage_in_drive_trash is not UNSET:
            field_dict["usageInDriveTrash"] = usage_in_drive_trash

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        usage = d.pop("usage", UNSET)

        usage_in_drive = d.pop("usageInDrive", UNSET)

        usage_in_drive_trash = d.pop("usageInDriveTrash", UNSET)

        about_storage_quota = cls(
            limit=limit,
            usage=usage,
            usage_in_drive=usage_in_drive,
            usage_in_drive_trash=usage_in_drive_trash,
        )


        about_storage_quota.additional_properties = d
        return about_storage_quota

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
