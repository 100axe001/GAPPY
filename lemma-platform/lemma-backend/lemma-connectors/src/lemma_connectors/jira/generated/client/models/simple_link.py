from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SimpleLink")



@_attrs_define
class SimpleLink:
    """ Details about the operations available in this version.

        Attributes:
            href (str | Unset):
            icon_class (str | Unset):
            id (str | Unset):
            label (str | Unset):
            style_class (str | Unset):
            title (str | Unset):
            weight (int | Unset):
     """

    href: str | Unset = UNSET
    icon_class: str | Unset = UNSET
    id: str | Unset = UNSET
    label: str | Unset = UNSET
    style_class: str | Unset = UNSET
    title: str | Unset = UNSET
    weight: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        href = self.href

        icon_class = self.icon_class

        id = self.id

        label = self.label

        style_class = self.style_class

        title = self.title

        weight = self.weight


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if href is not UNSET:
            field_dict["href"] = href
        if icon_class is not UNSET:
            field_dict["iconClass"] = icon_class
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if style_class is not UNSET:
            field_dict["styleClass"] = style_class
        if title is not UNSET:
            field_dict["title"] = title
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href", UNSET)

        icon_class = d.pop("iconClass", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        style_class = d.pop("styleClass", UNSET)

        title = d.pop("title", UNSET)

        weight = d.pop("weight", UNSET)

        simple_link = cls(
            href=href,
            icon_class=icon_class,
            id=id,
            label=label,
            style_class=style_class,
            title=title,
            weight=weight,
        )

        return simple_link

