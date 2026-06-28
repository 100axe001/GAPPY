from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AboutTeamDriveThemesItem")



@_attrs_define
class AboutTeamDriveThemesItem:
    """ 
        Attributes:
            background_image_link (str | Unset): Deprecated - use driveThemes/backgroundImageLink instead.
            color_rgb (str | Unset): Deprecated - use driveThemes/colorRgb instead.
            id (str | Unset): Deprecated - use driveThemes/id instead.
     """

    background_image_link: str | Unset = UNSET
    color_rgb: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        background_image_link = self.background_image_link

        color_rgb = self.color_rgb

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_image_link is not UNSET:
            field_dict["backgroundImageLink"] = background_image_link
        if color_rgb is not UNSET:
            field_dict["colorRgb"] = color_rgb
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        background_image_link = d.pop("backgroundImageLink", UNSET)

        color_rgb = d.pop("colorRgb", UNSET)

        id = d.pop("id", UNSET)

        about_team_drive_themes_item = cls(
            background_image_link=background_image_link,
            color_rgb=color_rgb,
            id=id,
        )


        about_team_drive_themes_item.additional_properties = d
        return about_team_drive_themes_item

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
