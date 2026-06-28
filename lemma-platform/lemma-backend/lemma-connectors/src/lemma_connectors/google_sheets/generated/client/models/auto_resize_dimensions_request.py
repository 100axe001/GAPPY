from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_sheet_dimension_range import DataSourceSheetDimensionRange
  from ..models.dimension_range import DimensionRange





T = TypeVar("T", bound="AutoResizeDimensionsRequest")



@_attrs_define
class AutoResizeDimensionsRequest:
    """ Automatically resizes one or more dimensions based on the contents of the cells in that dimension.

        Attributes:
            data_source_sheet_dimensions (DataSourceSheetDimensionRange | Unset): A range along a single dimension on a
                DATA_SOURCE sheet.
            dimensions (DimensionRange | Unset): A range along a single dimension on a sheet. All indexes are zero-based.
                Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes indicate the
                range is unbounded on that side.
     """

    data_source_sheet_dimensions: DataSourceSheetDimensionRange | Unset = UNSET
    dimensions: DimensionRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_sheet_dimension_range import DataSourceSheetDimensionRange
        from ..models.dimension_range import DimensionRange
        data_source_sheet_dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_sheet_dimensions, Unset):
            data_source_sheet_dimensions = self.data_source_sheet_dimensions.to_dict()

        dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_source_sheet_dimensions is not UNSET:
            field_dict["dataSourceSheetDimensions"] = data_source_sheet_dimensions
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_sheet_dimension_range import DataSourceSheetDimensionRange
        from ..models.dimension_range import DimensionRange
        d = dict(src_dict)
        _data_source_sheet_dimensions = d.pop("dataSourceSheetDimensions", UNSET)
        data_source_sheet_dimensions: DataSourceSheetDimensionRange | Unset
        if isinstance(_data_source_sheet_dimensions,  Unset):
            data_source_sheet_dimensions = UNSET
        else:
            data_source_sheet_dimensions = DataSourceSheetDimensionRange.from_dict(_data_source_sheet_dimensions)




        _dimensions = d.pop("dimensions", UNSET)
        dimensions: DimensionRange | Unset
        if isinstance(_dimensions,  Unset):
            dimensions = UNSET
        else:
            dimensions = DimensionRange.from_dict(_dimensions)




        auto_resize_dimensions_request = cls(
            data_source_sheet_dimensions=data_source_sheet_dimensions,
            dimensions=dimensions,
        )


        auto_resize_dimensions_request.additional_properties = d
        return auto_resize_dimensions_request

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
