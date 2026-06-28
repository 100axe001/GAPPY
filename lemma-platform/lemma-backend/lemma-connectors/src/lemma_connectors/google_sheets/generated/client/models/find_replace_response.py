from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FindReplaceResponse")



@_attrs_define
class FindReplaceResponse:
    """ The result of the find/replace.

        Attributes:
            formulas_changed (int | Unset): The number of formula cells changed.
            occurrences_changed (int | Unset): The number of occurrences (possibly multiple within a cell) changed. For
                example, if replacing `"e"` with `"o"` in `"Google Sheets"`, this would be `"3"` because `"Google Sheets"` ->
                `"Googlo Shoots"`.
            rows_changed (int | Unset): The number of rows changed.
            sheets_changed (int | Unset): The number of sheets changed.
            values_changed (int | Unset): The number of non-formula cells changed.
     """

    formulas_changed: int | Unset = UNSET
    occurrences_changed: int | Unset = UNSET
    rows_changed: int | Unset = UNSET
    sheets_changed: int | Unset = UNSET
    values_changed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        formulas_changed = self.formulas_changed

        occurrences_changed = self.occurrences_changed

        rows_changed = self.rows_changed

        sheets_changed = self.sheets_changed

        values_changed = self.values_changed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if formulas_changed is not UNSET:
            field_dict["formulasChanged"] = formulas_changed
        if occurrences_changed is not UNSET:
            field_dict["occurrencesChanged"] = occurrences_changed
        if rows_changed is not UNSET:
            field_dict["rowsChanged"] = rows_changed
        if sheets_changed is not UNSET:
            field_dict["sheetsChanged"] = sheets_changed
        if values_changed is not UNSET:
            field_dict["valuesChanged"] = values_changed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        formulas_changed = d.pop("formulasChanged", UNSET)

        occurrences_changed = d.pop("occurrencesChanged", UNSET)

        rows_changed = d.pop("rowsChanged", UNSET)

        sheets_changed = d.pop("sheetsChanged", UNSET)

        values_changed = d.pop("valuesChanged", UNSET)

        find_replace_response = cls(
            formulas_changed=formulas_changed,
            occurrences_changed=occurrences_changed,
            rows_changed=rows_changed,
            sheets_changed=sheets_changed,
            values_changed=values_changed,
        )


        find_replace_response.additional_properties = d
        return find_replace_response

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
