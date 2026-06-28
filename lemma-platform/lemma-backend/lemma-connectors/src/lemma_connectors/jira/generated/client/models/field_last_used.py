from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.field_last_used_type import FieldLastUsedType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="FieldLastUsed")



@_attrs_define
class FieldLastUsed:
    r""" Information about the most recent use of a field.

        Attributes:
            type_ (FieldLastUsedType | Unset): Last used value type:

                 *  *TRACKED*: field is tracked and a last used date is available.
                 *  *NOT\_TRACKED*: field is not tracked, last used date is not available.
                 *  *NO\_INFORMATION*: field is tracked, but no last used date is available.
            value (datetime.datetime | Unset): The date when the value of the field last changed.
     """

    type_: FieldLastUsedType | Unset = UNSET
    value: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        value: str | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: FieldLastUsedType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = FieldLastUsedType(_type_)




        _value = d.pop("value", UNSET)
        value: datetime.datetime | Unset
        if isinstance(_value,  Unset):
            value = UNSET
        else:
            value = isoparse(_value)




        field_last_used = cls(
            type_=type_,
            value=value,
        )

        return field_last_used

