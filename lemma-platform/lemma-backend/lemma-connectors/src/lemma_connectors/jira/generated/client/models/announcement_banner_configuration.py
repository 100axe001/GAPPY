from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.announcement_banner_configuration_visibility import AnnouncementBannerConfigurationVisibility
from ..types import UNSET, Unset






T = TypeVar("T", bound="AnnouncementBannerConfiguration")



@_attrs_define
class AnnouncementBannerConfiguration:
    """ Announcement banner configuration.

        Attributes:
            hash_id (str | Unset): Hash of the banner data. The client detects updates by comparing hash IDs.
            is_dismissible (bool | Unset): Flag indicating if the announcement banner can be dismissed by the user.
            is_enabled (bool | Unset): Flag indicating if the announcement banner is enabled or not.
            message (str | Unset): The text on the announcement banner.
            visibility (AnnouncementBannerConfigurationVisibility | Unset): Visibility of the announcement banner.
     """

    hash_id: str | Unset = UNSET
    is_dismissible: bool | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    message: str | Unset = UNSET
    visibility: AnnouncementBannerConfigurationVisibility | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        hash_id = self.hash_id

        is_dismissible = self.is_dismissible

        is_enabled = self.is_enabled

        message = self.message

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if hash_id is not UNSET:
            field_dict["hashId"] = hash_id
        if is_dismissible is not UNSET:
            field_dict["isDismissible"] = is_dismissible
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if message is not UNSET:
            field_dict["message"] = message
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_id = d.pop("hashId", UNSET)

        is_dismissible = d.pop("isDismissible", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        message = d.pop("message", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: AnnouncementBannerConfigurationVisibility | Unset
        if isinstance(_visibility,  Unset):
            visibility = UNSET
        else:
            visibility = AnnouncementBannerConfigurationVisibility(_visibility)




        announcement_banner_configuration = cls(
            hash_id=hash_id,
            is_dismissible=is_dismissible,
            is_enabled=is_enabled,
            message=message,
            visibility=visibility,
        )

        return announcement_banner_configuration

