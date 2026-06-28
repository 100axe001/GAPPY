from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldOption")



@_attrs_define
class CustomFieldOption:
    """ Details of a custom option for a field.

        Attributes:
            self_ (str | Unset): The URL of these custom field option details.
            value (str | Unset): The value of the custom field option.
     """

    self_: str | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if self_ is not UNSET:
            field_dict["self"] = self_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        self_ = d.pop("self", UNSET)

        value = d.pop("value", UNSET)

        custom_field_option = cls(
            self_=self_,
            value=value,
        )

        return custom_field_option

