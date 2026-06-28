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
  from ..models.dimension_properties import DimensionProperties
  from ..models.dimension_range import DimensionRange





T = TypeVar("T", bound="UpdateDimensionPropertiesRequest")



@_attrs_define
class UpdateDimensionPropertiesRequest:
    """ Updates properties of dimensions within the specified range.

        Attributes:
            data_source_sheet_range (DataSourceSheetDimensionRange | Unset): A range along a single dimension on a
                DATA_SOURCE sheet.
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `properties` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every
                field.
            properties (DimensionProperties | Unset): Properties about a dimension.
            range_ (DimensionRange | Unset): A range along a single dimension on a sheet. All indexes are zero-based.
                Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes indicate the
                range is unbounded on that side.
     """

    data_source_sheet_range: DataSourceSheetDimensionRange | Unset = UNSET
    fields: str | Unset = UNSET
    properties: DimensionProperties | Unset = UNSET
    range_: DimensionRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_sheet_dimension_range import DataSourceSheetDimensionRange
        from ..models.dimension_properties import DimensionProperties
        from ..models.dimension_range import DimensionRange
        data_source_sheet_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_sheet_range, Unset):
            data_source_sheet_range = self.data_source_sheet_range.to_dict()

        fields = self.fields

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_source_sheet_range is not UNSET:
            field_dict["dataSourceSheetRange"] = data_source_sheet_range
        if fields is not UNSET:
            field_dict["fields"] = fields
        if properties is not UNSET:
            field_dict["properties"] = properties
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_sheet_dimension_range import DataSourceSheetDimensionRange
        from ..models.dimension_properties import DimensionProperties
        from ..models.dimension_range import DimensionRange
        d = dict(src_dict)
        _data_source_sheet_range = d.pop("dataSourceSheetRange", UNSET)
        data_source_sheet_range: DataSourceSheetDimensionRange | Unset
        if isinstance(_data_source_sheet_range,  Unset):
            data_source_sheet_range = UNSET
        else:
            data_source_sheet_range = DataSourceSheetDimensionRange.from_dict(_data_source_sheet_range)




        fields = d.pop("fields", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: DimensionProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = DimensionProperties.from_dict(_properties)




        _range_ = d.pop("range", UNSET)
        range_: DimensionRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = DimensionRange.from_dict(_range_)




        update_dimension_properties_request = cls(
            data_source_sheet_range=data_source_sheet_range,
            fields=fields,
            properties=properties,
            range_=range_,
        )


        update_dimension_properties_request.additional_properties = d
        return update_dimension_properties_request

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
