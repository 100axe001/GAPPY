from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.banded_range import BandedRange
  from ..models.basic_filter import BasicFilter
  from ..models.conditional_format_rule import ConditionalFormatRule
  from ..models.developer_metadata import DeveloperMetadata
  from ..models.dimension_group import DimensionGroup
  from ..models.embedded_chart import EmbeddedChart
  from ..models.filter_view import FilterView
  from ..models.grid_data import GridData
  from ..models.grid_range import GridRange
  from ..models.protected_range import ProtectedRange
  from ..models.sheet_properties import SheetProperties
  from ..models.slicer import Slicer





T = TypeVar("T", bound="Sheet")



@_attrs_define
class Sheet:
    """ A sheet in a spreadsheet.

        Attributes:
            banded_ranges (list[BandedRange] | Unset): The banded (alternating colors) ranges on this sheet.
            basic_filter (BasicFilter | Unset): The default filter associated with a sheet.
            charts (list[EmbeddedChart] | Unset): The specifications of every chart on this sheet.
            column_groups (list[DimensionGroup] | Unset): All column groups on this sheet, ordered by increasing range start
                index, then by group depth.
            conditional_formats (list[ConditionalFormatRule] | Unset): The conditional format rules in this sheet.
            data (list[GridData] | Unset): Data in the grid, if this is a grid sheet. The number of GridData objects
                returned is dependent on the number of ranges requested on this sheet. For example, if this is representing
                `Sheet1`, and the spreadsheet was requested with ranges `Sheet1!A1:C10` and `Sheet1!D15:E20`, then the first
                GridData will have a startRow/startColumn of `0`, while the second one will have `startRow 14` (zero-based row
                15), and `startColumn 3` (zero-based column D). For a DATA_SOURCE sheet, you can not request a specific range,
                the GridData contains all the values.
            developer_metadata (list[DeveloperMetadata] | Unset): The developer metadata associated with a sheet.
            filter_views (list[FilterView] | Unset): The filter views in this sheet.
            merges (list[GridRange] | Unset): The ranges that are merged together.
            properties (SheetProperties | Unset): Properties of a sheet.
            protected_ranges (list[ProtectedRange] | Unset): The protected ranges in this sheet.
            row_groups (list[DimensionGroup] | Unset): All row groups on this sheet, ordered by increasing range start
                index, then by group depth.
            slicers (list[Slicer] | Unset): The slicers on this sheet.
     """

    banded_ranges: list[BandedRange] | Unset = UNSET
    basic_filter: BasicFilter | Unset = UNSET
    charts: list[EmbeddedChart] | Unset = UNSET
    column_groups: list[DimensionGroup] | Unset = UNSET
    conditional_formats: list[ConditionalFormatRule] | Unset = UNSET
    data: list[GridData] | Unset = UNSET
    developer_metadata: list[DeveloperMetadata] | Unset = UNSET
    filter_views: list[FilterView] | Unset = UNSET
    merges: list[GridRange] | Unset = UNSET
    properties: SheetProperties | Unset = UNSET
    protected_ranges: list[ProtectedRange] | Unset = UNSET
    row_groups: list[DimensionGroup] | Unset = UNSET
    slicers: list[Slicer] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.banded_range import BandedRange
        from ..models.basic_filter import BasicFilter
        from ..models.conditional_format_rule import ConditionalFormatRule
        from ..models.developer_metadata import DeveloperMetadata
        from ..models.dimension_group import DimensionGroup
        from ..models.embedded_chart import EmbeddedChart
        from ..models.filter_view import FilterView
        from ..models.grid_data import GridData
        from ..models.grid_range import GridRange
        from ..models.protected_range import ProtectedRange
        from ..models.sheet_properties import SheetProperties
        from ..models.slicer import Slicer
        banded_ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.banded_ranges, Unset):
            banded_ranges = []
            for banded_ranges_item_data in self.banded_ranges:
                banded_ranges_item = banded_ranges_item_data.to_dict()
                banded_ranges.append(banded_ranges_item)



        basic_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_filter, Unset):
            basic_filter = self.basic_filter.to_dict()

        charts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.charts, Unset):
            charts = []
            for charts_item_data in self.charts:
                charts_item = charts_item_data.to_dict()
                charts.append(charts_item)



        column_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.column_groups, Unset):
            column_groups = []
            for column_groups_item_data in self.column_groups:
                column_groups_item = column_groups_item_data.to_dict()
                column_groups.append(column_groups_item)



        conditional_formats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditional_formats, Unset):
            conditional_formats = []
            for conditional_formats_item_data in self.conditional_formats:
                conditional_formats_item = conditional_formats_item_data.to_dict()
                conditional_formats.append(conditional_formats_item)



        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        developer_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.developer_metadata, Unset):
            developer_metadata = []
            for developer_metadata_item_data in self.developer_metadata:
                developer_metadata_item = developer_metadata_item_data.to_dict()
                developer_metadata.append(developer_metadata_item)



        filter_views: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_views, Unset):
            filter_views = []
            for filter_views_item_data in self.filter_views:
                filter_views_item = filter_views_item_data.to_dict()
                filter_views.append(filter_views_item)



        merges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.merges, Unset):
            merges = []
            for merges_item_data in self.merges:
                merges_item = merges_item_data.to_dict()
                merges.append(merges_item)



        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        protected_ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.protected_ranges, Unset):
            protected_ranges = []
            for protected_ranges_item_data in self.protected_ranges:
                protected_ranges_item = protected_ranges_item_data.to_dict()
                protected_ranges.append(protected_ranges_item)



        row_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row_groups, Unset):
            row_groups = []
            for row_groups_item_data in self.row_groups:
                row_groups_item = row_groups_item_data.to_dict()
                row_groups.append(row_groups_item)



        slicers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.slicers, Unset):
            slicers = []
            for slicers_item_data in self.slicers:
                slicers_item = slicers_item_data.to_dict()
                slicers.append(slicers_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if banded_ranges is not UNSET:
            field_dict["bandedRanges"] = banded_ranges
        if basic_filter is not UNSET:
            field_dict["basicFilter"] = basic_filter
        if charts is not UNSET:
            field_dict["charts"] = charts
        if column_groups is not UNSET:
            field_dict["columnGroups"] = column_groups
        if conditional_formats is not UNSET:
            field_dict["conditionalFormats"] = conditional_formats
        if data is not UNSET:
            field_dict["data"] = data
        if developer_metadata is not UNSET:
            field_dict["developerMetadata"] = developer_metadata
        if filter_views is not UNSET:
            field_dict["filterViews"] = filter_views
        if merges is not UNSET:
            field_dict["merges"] = merges
        if properties is not UNSET:
            field_dict["properties"] = properties
        if protected_ranges is not UNSET:
            field_dict["protectedRanges"] = protected_ranges
        if row_groups is not UNSET:
            field_dict["rowGroups"] = row_groups
        if slicers is not UNSET:
            field_dict["slicers"] = slicers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.banded_range import BandedRange
        from ..models.basic_filter import BasicFilter
        from ..models.conditional_format_rule import ConditionalFormatRule
        from ..models.developer_metadata import DeveloperMetadata
        from ..models.dimension_group import DimensionGroup
        from ..models.embedded_chart import EmbeddedChart
        from ..models.filter_view import FilterView
        from ..models.grid_data import GridData
        from ..models.grid_range import GridRange
        from ..models.protected_range import ProtectedRange
        from ..models.sheet_properties import SheetProperties
        from ..models.slicer import Slicer
        d = dict(src_dict)
        _banded_ranges = d.pop("bandedRanges", UNSET)
        banded_ranges: list[BandedRange] | Unset = UNSET
        if _banded_ranges is not UNSET:
            banded_ranges = []
            for banded_ranges_item_data in _banded_ranges:
                banded_ranges_item = BandedRange.from_dict(banded_ranges_item_data)



                banded_ranges.append(banded_ranges_item)


        _basic_filter = d.pop("basicFilter", UNSET)
        basic_filter: BasicFilter | Unset
        if isinstance(_basic_filter,  Unset):
            basic_filter = UNSET
        else:
            basic_filter = BasicFilter.from_dict(_basic_filter)




        _charts = d.pop("charts", UNSET)
        charts: list[EmbeddedChart] | Unset = UNSET
        if _charts is not UNSET:
            charts = []
            for charts_item_data in _charts:
                charts_item = EmbeddedChart.from_dict(charts_item_data)



                charts.append(charts_item)


        _column_groups = d.pop("columnGroups", UNSET)
        column_groups: list[DimensionGroup] | Unset = UNSET
        if _column_groups is not UNSET:
            column_groups = []
            for column_groups_item_data in _column_groups:
                column_groups_item = DimensionGroup.from_dict(column_groups_item_data)



                column_groups.append(column_groups_item)


        _conditional_formats = d.pop("conditionalFormats", UNSET)
        conditional_formats: list[ConditionalFormatRule] | Unset = UNSET
        if _conditional_formats is not UNSET:
            conditional_formats = []
            for conditional_formats_item_data in _conditional_formats:
                conditional_formats_item = ConditionalFormatRule.from_dict(conditional_formats_item_data)



                conditional_formats.append(conditional_formats_item)


        _data = d.pop("data", UNSET)
        data: list[GridData] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = GridData.from_dict(data_item_data)



                data.append(data_item)


        _developer_metadata = d.pop("developerMetadata", UNSET)
        developer_metadata: list[DeveloperMetadata] | Unset = UNSET
        if _developer_metadata is not UNSET:
            developer_metadata = []
            for developer_metadata_item_data in _developer_metadata:
                developer_metadata_item = DeveloperMetadata.from_dict(developer_metadata_item_data)



                developer_metadata.append(developer_metadata_item)


        _filter_views = d.pop("filterViews", UNSET)
        filter_views: list[FilterView] | Unset = UNSET
        if _filter_views is not UNSET:
            filter_views = []
            for filter_views_item_data in _filter_views:
                filter_views_item = FilterView.from_dict(filter_views_item_data)



                filter_views.append(filter_views_item)


        _merges = d.pop("merges", UNSET)
        merges: list[GridRange] | Unset = UNSET
        if _merges is not UNSET:
            merges = []
            for merges_item_data in _merges:
                merges_item = GridRange.from_dict(merges_item_data)



                merges.append(merges_item)


        _properties = d.pop("properties", UNSET)
        properties: SheetProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = SheetProperties.from_dict(_properties)




        _protected_ranges = d.pop("protectedRanges", UNSET)
        protected_ranges: list[ProtectedRange] | Unset = UNSET
        if _protected_ranges is not UNSET:
            protected_ranges = []
            for protected_ranges_item_data in _protected_ranges:
                protected_ranges_item = ProtectedRange.from_dict(protected_ranges_item_data)



                protected_ranges.append(protected_ranges_item)


        _row_groups = d.pop("rowGroups", UNSET)
        row_groups: list[DimensionGroup] | Unset = UNSET
        if _row_groups is not UNSET:
            row_groups = []
            for row_groups_item_data in _row_groups:
                row_groups_item = DimensionGroup.from_dict(row_groups_item_data)



                row_groups.append(row_groups_item)


        _slicers = d.pop("slicers", UNSET)
        slicers: list[Slicer] | Unset = UNSET
        if _slicers is not UNSET:
            slicers = []
            for slicers_item_data in _slicers:
                slicers_item = Slicer.from_dict(slicers_item_data)



                slicers.append(slicers_item)


        sheet = cls(
            banded_ranges=banded_ranges,
            basic_filter=basic_filter,
            charts=charts,
            column_groups=column_groups,
            conditional_formats=conditional_formats,
            data=data,
            developer_metadata=developer_metadata,
            filter_views=filter_views,
            merges=merges,
            properties=properties,
            protected_ranges=protected_ranges,
            row_groups=row_groups,
            slicers=slicers,
        )


        sheet.additional_properties = d
        return sheet

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
