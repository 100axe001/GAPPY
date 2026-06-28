from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.group_label_type import GroupLabelType
from ..types import UNSET, Unset






T = TypeVar("T", bound="GroupLabel")



@_attrs_define
class GroupLabel:
    """ A group label.

        Attributes:
            text (str | Unset): The group label name.
            title (str | Unset): The title of the group label.
            type_ (GroupLabelType | Unset): The type of the group label.
     """

    text: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: GroupLabelType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        text = self.text

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GroupLabelType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = GroupLabelType(_type_)




        group_label = cls(
            text=text,
            title=title,
            type_=type_,
        )

        return group_label

