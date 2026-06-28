from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AddFieldBean")



@_attrs_define
class AddFieldBean:
    """ 
        Attributes:
            field_id (str): The ID of the field to add.
     """

    field_id: str





    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fieldId": field_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("fieldId")

        add_field_bean = cls(
            field_id=field_id,
        )

        return add_field_bean

