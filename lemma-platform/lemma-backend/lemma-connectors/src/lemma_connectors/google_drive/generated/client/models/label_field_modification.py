from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="LabelFieldModification")



@_attrs_define
class LabelFieldModification:
    """ A modification to a label's field.

        Attributes:
            field_id (str | Unset): The ID of the Field to be modified.
            kind (str | Unset): This is always drive#labelFieldModification. Default: 'drive#labelFieldModification'.
            set_date_values (list[datetime.date] | Unset): Replaces a dateString field with these new values. The values
                must be strings in the RFC 3339 full-date format: YYYY-MM-DD.
            set_integer_values (list[str] | Unset): Replaces an integer field with these new values.
            set_selection_values (list[str] | Unset): Replaces a selection field with these new values.
            set_text_values (list[str] | Unset): Replaces a text field with these new values.
            set_user_values (list[str] | Unset): Replaces a user field with these new values. The values must be valid email
                addresses.
            unset_values (bool | Unset): Unsets the values for this field.
     """

    field_id: str | Unset = UNSET
    kind: str | Unset = 'drive#labelFieldModification'
    set_date_values: list[datetime.date] | Unset = UNSET
    set_integer_values: list[str] | Unset = UNSET
    set_selection_values: list[str] | Unset = UNSET
    set_text_values: list[str] | Unset = UNSET
    set_user_values: list[str] | Unset = UNSET
    unset_values: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        kind = self.kind

        set_date_values: list[str] | Unset = UNSET
        if not isinstance(self.set_date_values, Unset):
            set_date_values = []
            for set_date_values_item_data in self.set_date_values:
                set_date_values_item = set_date_values_item_data.isoformat()
                set_date_values.append(set_date_values_item)



        set_integer_values: list[str] | Unset = UNSET
        if not isinstance(self.set_integer_values, Unset):
            set_integer_values = self.set_integer_values



        set_selection_values: list[str] | Unset = UNSET
        if not isinstance(self.set_selection_values, Unset):
            set_selection_values = self.set_selection_values



        set_text_values: list[str] | Unset = UNSET
        if not isinstance(self.set_text_values, Unset):
            set_text_values = self.set_text_values



        set_user_values: list[str] | Unset = UNSET
        if not isinstance(self.set_user_values, Unset):
            set_user_values = self.set_user_values



        unset_values = self.unset_values


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if set_date_values is not UNSET:
            field_dict["setDateValues"] = set_date_values
        if set_integer_values is not UNSET:
            field_dict["setIntegerValues"] = set_integer_values
        if set_selection_values is not UNSET:
            field_dict["setSelectionValues"] = set_selection_values
        if set_text_values is not UNSET:
            field_dict["setTextValues"] = set_text_values
        if set_user_values is not UNSET:
            field_dict["setUserValues"] = set_user_values
        if unset_values is not UNSET:
            field_dict["unsetValues"] = unset_values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("fieldId", UNSET)

        kind = d.pop("kind", UNSET)

        _set_date_values = d.pop("setDateValues", UNSET)
        set_date_values: list[datetime.date] | Unset = UNSET
        if _set_date_values is not UNSET:
            set_date_values = []
            for set_date_values_item_data in _set_date_values:
                set_date_values_item = isoparse(set_date_values_item_data).date()



                set_date_values.append(set_date_values_item)


        set_integer_values = cast(list[str], d.pop("setIntegerValues", UNSET))


        set_selection_values = cast(list[str], d.pop("setSelectionValues", UNSET))


        set_text_values = cast(list[str], d.pop("setTextValues", UNSET))


        set_user_values = cast(list[str], d.pop("setUserValues", UNSET))


        unset_values = d.pop("unsetValues", UNSET)

        label_field_modification = cls(
            field_id=field_id,
            kind=kind,
            set_date_values=set_date_values,
            set_integer_values=set_integer_values,
            set_selection_values=set_selection_values,
            set_text_values=set_text_values,
            set_user_values=set_user_values,
            unset_values=unset_values,
        )


        label_field_modification.additional_properties = d
        return label_field_modification

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
