from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AttachmentSettings")



@_attrs_define
class AttachmentSettings:
    """ Details of the instance's attachment settings.

        Attributes:
            enabled (bool | Unset): Whether the ability to add attachments is enabled.
            upload_limit (int | Unset): The maximum size of attachments permitted, in bytes.
     """

    enabled: bool | Unset = UNSET
    upload_limit: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        upload_limit = self.upload_limit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if upload_limit is not UNSET:
            field_dict["uploadLimit"] = upload_limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        upload_limit = d.pop("uploadLimit", UNSET)

        attachment_settings = cls(
            enabled=enabled,
            upload_limit=upload_limit,
        )

        return attachment_settings

