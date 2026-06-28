from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ColumnItem")



@_attrs_define
class ColumnItem:
    """ Details of an issue navigator column item.

        Attributes:
            label (str | Unset): The issue navigator column label.
            value (str | Unset): The issue navigator column value.
     """

    label: str | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        label = self.label

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if label is not UNSET:
            field_dict["label"] = label
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        value = d.pop("value", UNSET)

        column_item = cls(
            label=label,
            value=value,
        )

        return column_item

