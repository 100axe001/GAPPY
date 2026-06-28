from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldOptionCreate")



@_attrs_define
class CustomFieldOptionCreate:
    """ Details of a custom field option to create.

        Attributes:
            value (str): The value of the custom field option.
            disabled (bool | Unset): Whether the option is disabled.
            option_id (str | Unset): For cascading options, the ID of the custom field object containing the cascading
                option.
     """

    value: str
    disabled: bool | Unset = UNSET
    option_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        value = self.value

        disabled = self.disabled

        option_id = self.option_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "value": value,
        })
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if option_id is not UNSET:
            field_dict["optionId"] = option_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        disabled = d.pop("disabled", UNSET)

        option_id = d.pop("optionId", UNSET)

        custom_field_option_create = cls(
            value=value,
            disabled=disabled,
            option_id=option_id,
        )

        return custom_field_option_create

