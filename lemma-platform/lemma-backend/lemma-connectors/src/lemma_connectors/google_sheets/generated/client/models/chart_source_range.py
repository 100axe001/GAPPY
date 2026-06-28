from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="ChartSourceRange")



@_attrs_define
class ChartSourceRange:
    """ Source ranges for a chart.

        Attributes:
            sources (list[GridRange] | Unset): The ranges of data for a series or domain. Exactly one dimension must have a
                length of 1, and all sources in the list must have the same dimension with length 1. The domain (if it exists) &
                all series must have the same number of source ranges. If using more than one source range, then the source
                range at a given offset must be in order and contiguous across the domain and series. For example, these are
                valid configurations: domain sources: A1:A5 series1 sources: B1:B5 series2 sources: D6:D10 domain sources:
                A1:A5, C10:C12 series1 sources: B1:B5, D10:D12 series2 sources: C1:C5, E10:E12
     """

    sources: list[GridRange] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_range import GridRange
        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        _sources = d.pop("sources", UNSET)
        sources: list[GridRange] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = GridRange.from_dict(sources_item_data)



                sources.append(sources_item)


        chart_source_range = cls(
            sources=sources,
        )


        chart_source_range.additional_properties = d
        return chart_source_range

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
