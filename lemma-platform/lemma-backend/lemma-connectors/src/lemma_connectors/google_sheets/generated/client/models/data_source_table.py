from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.data_source_table_column_selection_type import DataSourceTableColumnSelectionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_execution_status import DataExecutionStatus
  from ..models.data_source_column_reference import DataSourceColumnReference
  from ..models.filter_spec import FilterSpec
  from ..models.sort_spec import SortSpec





T = TypeVar("T", bound="DataSourceTable")



@_attrs_define
class DataSourceTable:
    """ A data source table, which allows the user to import a static table of data from the DataSource into Sheets. This is
    also known as "Extract" in the Sheets editor.

        Attributes:
            column_selection_type (DataSourceTableColumnSelectionType | Unset): The type to select columns for the data
                source table. Defaults to SELECTED.
            columns (list[DataSourceColumnReference] | Unset): Columns selected for the data source table. The
                column_selection_type must be SELECTED.
            data_execution_status (DataExecutionStatus | Unset): The data execution status. A data execution is created to
                sync a data source object with the latest data from a DataSource. It is usually scheduled to run at background,
                you can check its state to tell if an execution completes There are several scenarios where a data execution is
                triggered to run: * Adding a data source creates an associated data source sheet as well as a data execution to
                sync the data from the data source to the sheet. * Updating a data source creates a data execution to refresh
                the associated data source sheet similarly. * You can send refresh request to explicitly refresh one or multiple
                data source objects.
            data_source_id (str | Unset): The ID of the data source the data source table is associated with.
            filter_specs (list[FilterSpec] | Unset): Filter specifications in the data source table.
            row_limit (int | Unset): The limit of rows to return. If not set, a default limit is applied. Please refer to
                the Sheets editor for the default and max limit.
            sort_specs (list[SortSpec] | Unset): Sort specifications in the data source table. The result of the data source
                table is sorted based on the sort specifications in order.
     """

    column_selection_type: DataSourceTableColumnSelectionType | Unset = UNSET
    columns: list[DataSourceColumnReference] | Unset = UNSET
    data_execution_status: DataExecutionStatus | Unset = UNSET
    data_source_id: str | Unset = UNSET
    filter_specs: list[FilterSpec] | Unset = UNSET
    row_limit: int | Unset = UNSET
    sort_specs: list[SortSpec] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_execution_status import DataExecutionStatus
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.filter_spec import FilterSpec
        from ..models.sort_spec import SortSpec
        column_selection_type: str | Unset = UNSET
        if not isinstance(self.column_selection_type, Unset):
            column_selection_type = self.column_selection_type.value


        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)



        data_execution_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_execution_status, Unset):
            data_execution_status = self.data_execution_status.to_dict()

        data_source_id = self.data_source_id

        filter_specs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_specs, Unset):
            filter_specs = []
            for filter_specs_item_data in self.filter_specs:
                filter_specs_item = filter_specs_item_data.to_dict()
                filter_specs.append(filter_specs_item)



        row_limit = self.row_limit

        sort_specs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sort_specs, Unset):
            sort_specs = []
            for sort_specs_item_data in self.sort_specs:
                sort_specs_item = sort_specs_item_data.to_dict()
                sort_specs.append(sort_specs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_selection_type is not UNSET:
            field_dict["columnSelectionType"] = column_selection_type
        if columns is not UNSET:
            field_dict["columns"] = columns
        if data_execution_status is not UNSET:
            field_dict["dataExecutionStatus"] = data_execution_status
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if filter_specs is not UNSET:
            field_dict["filterSpecs"] = filter_specs
        if row_limit is not UNSET:
            field_dict["rowLimit"] = row_limit
        if sort_specs is not UNSET:
            field_dict["sortSpecs"] = sort_specs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_execution_status import DataExecutionStatus
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.filter_spec import FilterSpec
        from ..models.sort_spec import SortSpec
        d = dict(src_dict)
        _column_selection_type = d.pop("columnSelectionType", UNSET)
        column_selection_type: DataSourceTableColumnSelectionType | Unset
        if isinstance(_column_selection_type,  Unset):
            column_selection_type = UNSET
        else:
            column_selection_type = DataSourceTableColumnSelectionType(_column_selection_type)




        _columns = d.pop("columns", UNSET)
        columns: list[DataSourceColumnReference] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = DataSourceColumnReference.from_dict(columns_item_data)



                columns.append(columns_item)


        _data_execution_status = d.pop("dataExecutionStatus", UNSET)
        data_execution_status: DataExecutionStatus | Unset
        if isinstance(_data_execution_status,  Unset):
            data_execution_status = UNSET
        else:
            data_execution_status = DataExecutionStatus.from_dict(_data_execution_status)




        data_source_id = d.pop("dataSourceId", UNSET)

        _filter_specs = d.pop("filterSpecs", UNSET)
        filter_specs: list[FilterSpec] | Unset = UNSET
        if _filter_specs is not UNSET:
            filter_specs = []
            for filter_specs_item_data in _filter_specs:
                filter_specs_item = FilterSpec.from_dict(filter_specs_item_data)



                filter_specs.append(filter_specs_item)


        row_limit = d.pop("rowLimit", UNSET)

        _sort_specs = d.pop("sortSpecs", UNSET)
        sort_specs: list[SortSpec] | Unset = UNSET
        if _sort_specs is not UNSET:
            sort_specs = []
            for sort_specs_item_data in _sort_specs:
                sort_specs_item = SortSpec.from_dict(sort_specs_item_data)



                sort_specs.append(sort_specs_item)


        data_source_table = cls(
            column_selection_type=column_selection_type,
            columns=columns,
            data_execution_status=data_execution_status,
            data_source_id=data_source_id,
            filter_specs=filter_specs,
            row_limit=row_limit,
            sort_specs=sort_specs,
        )


        data_source_table.additional_properties = d
        return data_source_table

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
