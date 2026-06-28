from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FieldUpdateOperation")



@_attrs_define
class FieldUpdateOperation:
    """ Details of an operation to perform on a field.

        Attributes:
            add (Any | Unset): The value to add to the field. Example: triaged.
            copy (Any | Unset): The field value to copy from another issue. Example: {'issuelinks': {'sourceIssues':
                [{'key': 'FP-5'}]}}.
            edit (Any | Unset): The value to edit in the field. Example: {'originalEstimate': '1w 1d', 'remainingEstimate':
                '4d'}.
            remove (Any | Unset): The value to removed from the field. Example: blocker.
            set_ (Any | Unset): The value to set in the field. Example: A new summary.
     """

    add: Any | Unset = UNSET
    copy: Any | Unset = UNSET
    edit: Any | Unset = UNSET
    remove: Any | Unset = UNSET
    set_: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        add = self.add

        copy = self.copy

        edit = self.edit

        remove = self.remove

        set_ = self.set_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if add is not UNSET:
            field_dict["add"] = add
        if copy is not UNSET:
            field_dict["copy"] = copy
        if edit is not UNSET:
            field_dict["edit"] = edit
        if remove is not UNSET:
            field_dict["remove"] = remove
        if set_ is not UNSET:
            field_dict["set"] = set_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        add = d.pop("add", UNSET)

        copy = d.pop("copy", UNSET)

        edit = d.pop("edit", UNSET)

        remove = d.pop("remove", UNSET)

        set_ = d.pop("set", UNSET)

        field_update_operation = cls(
            add=add,
            copy=copy,
            edit=edit,
            remove=remove,
            set_=set_,
        )

        return field_update_operation

