from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension_range import DimensionRange





T = TypeVar("T", bound="MoveDimensionRequest")



@_attrs_define
class MoveDimensionRequest:
    """ Moves one or more rows or columns.

        Attributes:
            destination_index (int | Unset): The zero-based start index of where to move the source data to, based on the
                coordinates *before* the source data is removed from the grid. Existing data will be shifted down or right
                (depending on the dimension) to make room for the moved dimensions. The source dimensions are removed from the
                grid, so the the data may end up in a different index than specified. For example, given `A1..A5` of `0, 1, 2,
                3, 4` and wanting to move `"1"` and `"2"` to between `"3"` and `"4"`, the source would be `ROWS [1..3)`,and the
                destination index would be `"4"` (the zero-based index of row 5). The end result would be `A1..A5` of `0, 3, 1,
                2, 4`.
            source (DimensionRange | Unset): A range along a single dimension on a sheet. All indexes are zero-based.
                Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes indicate the
                range is unbounded on that side.
     """

    destination_index: int | Unset = UNSET
    source: DimensionRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_range import DimensionRange
        destination_index = self.destination_index

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if destination_index is not UNSET:
            field_dict["destinationIndex"] = destination_index
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_range import DimensionRange
        d = dict(src_dict)
        destination_index = d.pop("destinationIndex", UNSET)

        _source = d.pop("source", UNSET)
        source: DimensionRange | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = DimensionRange.from_dict(_source)




        move_dimension_request = cls(
            destination_index=destination_index,
            source=source,
        )


        move_dimension_request.additional_properties = d
        return move_dimension_request

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
