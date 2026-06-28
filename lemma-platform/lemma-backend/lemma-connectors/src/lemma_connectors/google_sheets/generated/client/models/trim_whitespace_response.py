from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TrimWhitespaceResponse")



@_attrs_define
class TrimWhitespaceResponse:
    """ The result of trimming whitespace in cells.

        Attributes:
            cells_changed_count (int | Unset): The number of cells that were trimmed of whitespace.
     """

    cells_changed_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cells_changed_count = self.cells_changed_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cells_changed_count is not UNSET:
            field_dict["cellsChangedCount"] = cells_changed_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cells_changed_count = d.pop("cellsChangedCount", UNSET)

        trim_whitespace_response = cls(
            cells_changed_count=cells_changed_count,
        )


        trim_whitespace_response.additional_properties = d
        return trim_whitespace_response

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
