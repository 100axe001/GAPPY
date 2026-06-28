from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IconUploadResponse")


@_attrs_define
class IconUploadResponse:
    """Response payload for uploaded icons.

    Attributes:
        content_type (str):
        icon_url (str):
        storage_path (str):
    """

    content_type: str
    icon_url: str
    storage_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        icon_url = self.icon_url

        storage_path = self.storage_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "icon_url": icon_url,
                "storage_path": storage_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type")

        icon_url = d.pop("icon_url")

        storage_path = d.pop("storage_path")

        icon_upload_response = cls(
            content_type=content_type,
            icon_url=icon_url,
            storage_path=storage_path,
        )

        icon_upload_response.additional_properties = d
        return icon_upload_response

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
