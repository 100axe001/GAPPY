from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChangedValueBean")



@_attrs_define
class ChangedValueBean:
    """ Details of names changed in the record event.

        Attributes:
            changed_from (str | Unset): The value of the field before the change.
            changed_to (str | Unset): The value of the field after the change.
            field_name (str | Unset): The name of the field changed.
     """

    changed_from: str | Unset = UNSET
    changed_to: str | Unset = UNSET
    field_name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        changed_from = self.changed_from

        changed_to = self.changed_to

        field_name = self.field_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if changed_from is not UNSET:
            field_dict["changedFrom"] = changed_from
        if changed_to is not UNSET:
            field_dict["changedTo"] = changed_to
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        changed_from = d.pop("changedFrom", UNSET)

        changed_to = d.pop("changedTo", UNSET)

        field_name = d.pop("fieldName", UNSET)

        changed_value_bean = cls(
            changed_from=changed_from,
            changed_to=changed_to,
            field_name=field_name,
        )

        return changed_value_bean

