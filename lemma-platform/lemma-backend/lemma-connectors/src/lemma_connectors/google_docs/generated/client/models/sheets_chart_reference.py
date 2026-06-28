from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SheetsChartReference")



@_attrs_define
class SheetsChartReference:
    """ A reference to a linked chart embedded from Google Sheets.

        Attributes:
            chart_id (int | Unset): The ID of the specific chart in the Google Sheets spreadsheet that's embedded.
            spreadsheet_id (str | Unset): The ID of the Google Sheets spreadsheet that contains the source chart.
     """

    chart_id: int | Unset = UNSET
    spreadsheet_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        chart_id = self.chart_id

        spreadsheet_id = self.spreadsheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chart_id is not UNSET:
            field_dict["chartId"] = chart_id
        if spreadsheet_id is not UNSET:
            field_dict["spreadsheetId"] = spreadsheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chart_id = d.pop("chartId", UNSET)

        spreadsheet_id = d.pop("spreadsheetId", UNSET)

        sheets_chart_reference = cls(
            chart_id=chart_id,
            spreadsheet_id=spreadsheet_id,
        )


        sheets_chart_reference.additional_properties = d
        return sheets_chart_reference

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
