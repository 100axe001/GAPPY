from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IconBean")



@_attrs_define
class IconBean:
    """ An icon.

        Attributes:
            link (str | Unset): The URL of the tooltip, used only for a status icon.
            title (str | Unset): The title of the icon, for use as a tooltip on the icon.
            url16x16 (str | Unset): The URL of a 16x16 pixel icon.
     """

    link: str | Unset = UNSET
    title: str | Unset = UNSET
    url16x16: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        link = self.link

        title = self.title

        url16x16 = self.url16x16


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if link is not UNSET:
            field_dict["link"] = link
        if title is not UNSET:
            field_dict["title"] = title
        if url16x16 is not UNSET:
            field_dict["url16x16"] = url16x16

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        link = d.pop("link", UNSET)

        title = d.pop("title", UNSET)

        url16x16 = d.pop("url16x16", UNSET)

        icon_bean = cls(
            link=link,
            title=title,
            url16x16=url16x16,
        )

        return icon_bean

