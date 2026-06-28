from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.sheets_chart_reference import SheetsChartReference





T = TypeVar("T", bound="LinkedContentReference")



@_attrs_define
class LinkedContentReference:
    """ A reference to the external linked source content.

        Attributes:
            sheets_chart_reference (SheetsChartReference | Unset): A reference to a linked chart embedded from Google
                Sheets.
     """

    sheets_chart_reference: SheetsChartReference | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sheets_chart_reference import SheetsChartReference
        sheets_chart_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sheets_chart_reference, Unset):
            sheets_chart_reference = self.sheets_chart_reference.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sheets_chart_reference is not UNSET:
            field_dict["sheetsChartReference"] = sheets_chart_reference

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sheets_chart_reference import SheetsChartReference
        d = dict(src_dict)
        _sheets_chart_reference = d.pop("sheetsChartReference", UNSET)
        sheets_chart_reference: SheetsChartReference | Unset
        if isinstance(_sheets_chart_reference,  Unset):
            sheets_chart_reference = UNSET
        else:
            sheets_chart_reference = SheetsChartReference.from_dict(_sheets_chart_reference)




        linked_content_reference = cls(
            sheets_chart_reference=sheets_chart_reference,
        )


        linked_content_reference.additional_properties = d
        return linked_content_reference

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
