from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldContextOption")



@_attrs_define
class CustomFieldContextOption:
    """ Details of the custom field options for a context.

        Attributes:
            disabled (bool): Whether the option is disabled.
            id (str): The ID of the custom field option.
            value (str): The value of the custom field option.
            option_id (str | Unset): For cascading options, the ID of the custom field option containing the cascading
                option.
     """

    disabled: bool
    id: str
    value: str
    option_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        disabled = self.disabled

        id = self.id

        value = self.value

        option_id = self.option_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "disabled": disabled,
            "id": id,
            "value": value,
        })
        if option_id is not UNSET:
            field_dict["optionId"] = option_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disabled = d.pop("disabled")

        id = d.pop("id")

        value = d.pop("value")

        option_id = d.pop("optionId", UNSET)

        custom_field_context_option = cls(
            disabled=disabled,
            id=id,
            value=value,
            option_id=option_id,
        )

        return custom_field_context_option

