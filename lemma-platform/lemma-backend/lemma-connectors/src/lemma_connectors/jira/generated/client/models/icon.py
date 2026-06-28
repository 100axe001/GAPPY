from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Icon")



@_attrs_define
class Icon:
    r""" An icon. If no icon is defined:

     *  for a status icon, no status icon displays in Jira.
     *  for the remote object icon, the default link icon displays in Jira.

        Attributes:
            link (str | Unset): The URL of the tooltip, used only for a status icon. If not set, the status icon in Jira is
                not clickable.
            title (str | Unset): The title of the icon. This is used as follows:

                 *  For a status icon it is used as a tooltip on the icon. If not set, the status icon doesn't display a tooltip
                in Jira.
                 *  For the remote object icon it is used in conjunction with the application name to display a tooltip for the
                link's icon. The tooltip takes the format "\[application name\] icon title". Blank itemsare excluded from the
                tooltip title. If both items are blank, the icon tooltop displays as "Web Link".
            url16x16 (str | Unset): The URL of an icon that displays at 16x16 pixel in Jira.
     """

    link: str | Unset = UNSET
    title: str | Unset = UNSET
    url16x16: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        link = self.link

        title = self.title

        url16x16 = self.url16x16


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        icon = cls(
            link=link,
            title=title,
            url16x16=url16x16,
        )


        icon.additional_properties = d
        return icon

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
