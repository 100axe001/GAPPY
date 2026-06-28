from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChangeDetails")



@_attrs_define
class ChangeDetails:
    """ A change item.

        Attributes:
            field (str | Unset): The name of the field changed.
            field_id (str | Unset): The ID of the field changed.
            fieldtype (str | Unset): The type of the field changed.
            from_ (str | Unset): The details of the original value.
            from_string (str | Unset): The details of the original value as a string.
            to (str | Unset): The details of the new value.
     """

    field: str | Unset = UNSET
    field_id: str | Unset = UNSET
    fieldtype: str | Unset = UNSET
    from_: str | Unset = UNSET
    from_string: str | Unset = UNSET
    to: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field = self.field

        field_id = self.field_id

        fieldtype = self.fieldtype

        from_ = self.from_

        from_string = self.from_string

        to = self.to


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if field is not UNSET:
            field_dict["field"] = field
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if fieldtype is not UNSET:
            field_dict["fieldtype"] = fieldtype
        if from_ is not UNSET:
            field_dict["from"] = from_
        if from_string is not UNSET:
            field_dict["fromString"] = from_string
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field", UNSET)

        field_id = d.pop("fieldId", UNSET)

        fieldtype = d.pop("fieldtype", UNSET)

        from_ = d.pop("from", UNSET)

        from_string = d.pop("fromString", UNSET)

        to = d.pop("to", UNSET)

        change_details = cls(
            field=field,
            field_id=field_id,
            fieldtype=fieldtype,
            from_=from_,
            from_string=from_string,
            to=to,
        )

        return change_details

