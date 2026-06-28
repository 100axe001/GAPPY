from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source import DataSource
  from ..models.data_source_refresh_schedule import DataSourceRefreshSchedule
  from ..models.developer_metadata import DeveloperMetadata
  from ..models.named_range import NamedRange
  from ..models.sheet import Sheet
  from ..models.spreadsheet_properties import SpreadsheetProperties





T = TypeVar("T", bound="Spreadsheet")



@_attrs_define
class Spreadsheet:
    """ Resource that represents a spreadsheet.

        Attributes:
            data_source_schedules (list[DataSourceRefreshSchedule] | Unset): Output only. A list of data source refresh
                schedules.
            data_sources (list[DataSource] | Unset): A list of external data sources connected with the spreadsheet.
            developer_metadata (list[DeveloperMetadata] | Unset): The developer metadata associated with a spreadsheet.
            named_ranges (list[NamedRange] | Unset): The named ranges defined in a spreadsheet.
            properties (SpreadsheetProperties | Unset): Properties of a spreadsheet.
            sheets (list[Sheet] | Unset): The sheets that are part of a spreadsheet.
            spreadsheet_id (str | Unset): The ID of the spreadsheet. This field is read-only.
            spreadsheet_url (str | Unset): The url of the spreadsheet. This field is read-only.
     """

    data_source_schedules: list[DataSourceRefreshSchedule] | Unset = UNSET
    data_sources: list[DataSource] | Unset = UNSET
    developer_metadata: list[DeveloperMetadata] | Unset = UNSET
    named_ranges: list[NamedRange] | Unset = UNSET
    properties: SpreadsheetProperties | Unset = UNSET
    sheets: list[Sheet] | Unset = UNSET
    spreadsheet_id: str | Unset = UNSET
    spreadsheet_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source import DataSource
        from ..models.data_source_refresh_schedule import DataSourceRefreshSchedule
        from ..models.developer_metadata import DeveloperMetadata
        from ..models.named_range import NamedRange
        from ..models.sheet import Sheet
        from ..models.spreadsheet_properties import SpreadsheetProperties
        data_source_schedules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_source_schedules, Unset):
            data_source_schedules = []
            for data_source_schedules_item_data in self.data_source_schedules:
                data_source_schedules_item = data_source_schedules_item_data.to_dict()
                data_source_schedules.append(data_source_schedules_item)



        data_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_sources, Unset):
            data_sources = []
            for data_sources_item_data in self.data_sources:
                data_sources_item = data_sources_item_data.to_dict()
                data_sources.append(data_sources_item)



        developer_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.developer_metadata, Unset):
            developer_metadata = []
            for developer_metadata_item_data in self.developer_metadata:
                developer_metadata_item = developer_metadata_item_data.to_dict()
                developer_metadata.append(developer_metadata_item)



        named_ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.named_ranges, Unset):
            named_ranges = []
            for named_ranges_item_data in self.named_ranges:
                named_ranges_item = named_ranges_item_data.to_dict()
                named_ranges.append(named_ranges_item)



        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        sheets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sheets, Unset):
            sheets = []
            for sheets_item_data in self.sheets:
                sheets_item = sheets_item_data.to_dict()
                sheets.append(sheets_item)



        spreadsheet_id = self.spreadsheet_id

        spreadsheet_url = self.spreadsheet_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_source_schedules is not UNSET:
            field_dict["dataSourceSchedules"] = data_source_schedules
        if data_sources is not UNSET:
            field_dict["dataSources"] = data_sources
        if developer_metadata is not UNSET:
            field_dict["developerMetadata"] = developer_metadata
        if named_ranges is not UNSET:
            field_dict["namedRanges"] = named_ranges
        if properties is not UNSET:
            field_dict["properties"] = properties
        if sheets is not UNSET:
            field_dict["sheets"] = sheets
        if spreadsheet_id is not UNSET:
            field_dict["spreadsheetId"] = spreadsheet_id
        if spreadsheet_url is not UNSET:
            field_dict["spreadsheetUrl"] = spreadsheet_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source import DataSource
        from ..models.data_source_refresh_schedule import DataSourceRefreshSchedule
        from ..models.developer_metadata import DeveloperMetadata
        from ..models.named_range import NamedRange
        from ..models.sheet import Sheet
        from ..models.spreadsheet_properties import SpreadsheetProperties
        d = dict(src_dict)
        _data_source_schedules = d.pop("dataSourceSchedules", UNSET)
        data_source_schedules: list[DataSourceRefreshSchedule] | Unset = UNSET
        if _data_source_schedules is not UNSET:
            data_source_schedules = []
            for data_source_schedules_item_data in _data_source_schedules:
                data_source_schedules_item = DataSourceRefreshSchedule.from_dict(data_source_schedules_item_data)



                data_source_schedules.append(data_source_schedules_item)


        _data_sources = d.pop("dataSources", UNSET)
        data_sources: list[DataSource] | Unset = UNSET
        if _data_sources is not UNSET:
            data_sources = []
            for data_sources_item_data in _data_sources:
                data_sources_item = DataSource.from_dict(data_sources_item_data)



                data_sources.append(data_sources_item)


        _developer_metadata = d.pop("developerMetadata", UNSET)
        developer_metadata: list[DeveloperMetadata] | Unset = UNSET
        if _developer_metadata is not UNSET:
            developer_metadata = []
            for developer_metadata_item_data in _developer_metadata:
                developer_metadata_item = DeveloperMetadata.from_dict(developer_metadata_item_data)



                developer_metadata.append(developer_metadata_item)


        _named_ranges = d.pop("namedRanges", UNSET)
        named_ranges: list[NamedRange] | Unset = UNSET
        if _named_ranges is not UNSET:
            named_ranges = []
            for named_ranges_item_data in _named_ranges:
                named_ranges_item = NamedRange.from_dict(named_ranges_item_data)



                named_ranges.append(named_ranges_item)


        _properties = d.pop("properties", UNSET)
        properties: SpreadsheetProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = SpreadsheetProperties.from_dict(_properties)




        _sheets = d.pop("sheets", UNSET)
        sheets: list[Sheet] | Unset = UNSET
        if _sheets is not UNSET:
            sheets = []
            for sheets_item_data in _sheets:
                sheets_item = Sheet.from_dict(sheets_item_data)



                sheets.append(sheets_item)


        spreadsheet_id = d.pop("spreadsheetId", UNSET)

        spreadsheet_url = d.pop("spreadsheetUrl", UNSET)

        spreadsheet = cls(
            data_source_schedules=data_source_schedules,
            data_sources=data_sources,
            developer_metadata=developer_metadata,
            named_ranges=named_ranges,
            properties=properties,
            sheets=sheets,
            spreadsheet_id=spreadsheet_id,
            spreadsheet_url=spreadsheet_url,
        )


        spreadsheet.additional_properties = d
        return spreadsheet

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
