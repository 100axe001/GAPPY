from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AnnouncementBannerConfigurationUpdate")



@_attrs_define
class AnnouncementBannerConfigurationUpdate:
    """ Configuration of the announcement banner.

        Attributes:
            is_dismissible (bool | Unset): Flag indicating if the announcement banner can be dismissed by the user.
            is_enabled (bool | Unset): Flag indicating if the announcement banner is enabled or not.
            message (str | Unset): The text on the announcement banner.
            visibility (str | Unset): Visibility of the announcement banner. Can be public or private.
     """

    is_dismissible: bool | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    message: str | Unset = UNSET
    visibility: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_dismissible = self.is_dismissible

        is_enabled = self.is_enabled

        message = self.message

        visibility = self.visibility


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
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
        is_dismissible = d.pop("isDismissible", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        message = d.pop("message", UNSET)

        visibility = d.pop("visibility", UNSET)

        announcement_banner_configuration_update = cls(
            is_dismissible=is_dismissible,
            is_enabled=is_enabled,
            message=message,
            visibility=visibility,
        )

        return announcement_banner_configuration_update

