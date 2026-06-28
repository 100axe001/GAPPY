from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldOptionUpdate")



@_attrs_define
class CustomFieldOptionUpdate:
    """ Details of a custom field option for a context.

        Attributes:
            id (str): The ID of the custom field option.
            disabled (bool | Unset): Whether the option is disabled.
            value (str | Unset): The value of the custom field option.
     """

    id: str
    disabled: bool | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        disabled = self.disabled

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        disabled = d.pop("disabled", UNSET)

        value = d.pop("value", UNSET)

        custom_field_option_update = cls(
            id=id,
            disabled=disabled,
            value=value,
        )

        return custom_field_option_update

