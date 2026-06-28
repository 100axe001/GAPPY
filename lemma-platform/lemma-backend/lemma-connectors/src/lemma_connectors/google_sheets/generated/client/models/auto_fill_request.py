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
  from ..models.source_and_destination import SourceAndDestination





T = TypeVar("T", bound="AutoFillRequest")



@_attrs_define
class AutoFillRequest:
    """ Fills in more data based on existing data.

        Attributes:
            range_ (GridRange | Unset): A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the
                start index is inclusive and the end index is exclusive -- [start_index, end_index). Missing indexes indicate
                the range is unbounded on that side. For example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 ==
                sheet_id: 123456, start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index: 1`
                `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2, end_row_index: 4, start_column_index: 0,
                end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index: 0, end_column_index: 2` `Sheet1!A5:B
                == sheet_id: 123456, start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 == sheet_id:
                123456` The start index must always be less than or equal to the end index. If the start index equals the end
                index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as
                `#REF!`.
            source_and_destination (SourceAndDestination | Unset): A combination of a source range and how to extend that
                source.
            use_alternate_series (bool | Unset): True if we should generate data with the "alternate" series. This differs
                based on the type and amount of source data.
     """

    range_: GridRange | Unset = UNSET
    source_and_destination: SourceAndDestination | Unset = UNSET
    use_alternate_series: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_range import GridRange
        from ..models.source_and_destination import SourceAndDestination
        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        source_and_destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_and_destination, Unset):
            source_and_destination = self.source_and_destination.to_dict()

        use_alternate_series = self.use_alternate_series


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if range_ is not UNSET:
            field_dict["range"] = range_
        if source_and_destination is not UNSET:
            field_dict["sourceAndDestination"] = source_and_destination
        if use_alternate_series is not UNSET:
            field_dict["useAlternateSeries"] = use_alternate_series

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_range import GridRange
        from ..models.source_and_destination import SourceAndDestination
        d = dict(src_dict)
        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        _source_and_destination = d.pop("sourceAndDestination", UNSET)
        source_and_destination: SourceAndDestination | Unset
        if isinstance(_source_and_destination,  Unset):
            source_and_destination = UNSET
        else:
            source_and_destination = SourceAndDestination.from_dict(_source_and_destination)




        use_alternate_series = d.pop("useAlternateSeries", UNSET)

        auto_fill_request = cls(
            range_=range_,
            source_and_destination=source_and_destination,
            use_alternate_series=use_alternate_series,
        )


        auto_fill_request.additional_properties = d
        return auto_fill_request

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
