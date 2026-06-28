from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProjectType")



@_attrs_define
class ProjectType:
    """ Details about a project type.

        Attributes:
            color (str | Unset): The color of the project type.
            description_i18_n_key (str | Unset): The key of the project type's description.
            formatted_key (str | Unset): The formatted key of the project type.
            icon (str | Unset): The icon of the project type.
            key (str | Unset): The key of the project type.
     """

    color: str | Unset = UNSET
    description_i18_n_key: str | Unset = UNSET
    formatted_key: str | Unset = UNSET
    icon: str | Unset = UNSET
    key: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        color = self.color

        description_i18_n_key = self.description_i18_n_key

        formatted_key = self.formatted_key

        icon = self.icon

        key = self.key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if description_i18_n_key is not UNSET:
            field_dict["descriptionI18nKey"] = description_i18_n_key
        if formatted_key is not UNSET:
            field_dict["formattedKey"] = formatted_key
        if icon is not UNSET:
            field_dict["icon"] = icon
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        description_i18_n_key = d.pop("descriptionI18nKey", UNSET)

        formatted_key = d.pop("formattedKey", UNSET)

        icon = d.pop("icon", UNSET)

        key = d.pop("key", UNSET)

        project_type = cls(
            color=color,
            description_i18_n_key=description_i18_n_key,
            formatted_key=formatted_key,
            icon=icon,
            key=key,
        )

        return project_type

