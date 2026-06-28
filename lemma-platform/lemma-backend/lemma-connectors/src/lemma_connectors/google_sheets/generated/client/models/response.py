from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.add_banding_response import AddBandingResponse
  from ..models.add_chart_response import AddChartResponse
  from ..models.add_data_source_response import AddDataSourceResponse
  from ..models.add_dimension_group_response import AddDimensionGroupResponse
  from ..models.add_filter_view_response import AddFilterViewResponse
  from ..models.add_named_range_response import AddNamedRangeResponse
  from ..models.add_protected_range_response import AddProtectedRangeResponse
  from ..models.add_sheet_response import AddSheetResponse
  from ..models.add_slicer_response import AddSlicerResponse
  from ..models.create_developer_metadata_response import CreateDeveloperMetadataResponse
  from ..models.delete_conditional_format_rule_response import DeleteConditionalFormatRuleResponse
  from ..models.delete_developer_metadata_response import DeleteDeveloperMetadataResponse
  from ..models.delete_dimension_group_response import DeleteDimensionGroupResponse
  from ..models.delete_duplicates_response import DeleteDuplicatesResponse
  from ..models.duplicate_filter_view_response import DuplicateFilterViewResponse
  from ..models.duplicate_sheet_response import DuplicateSheetResponse
  from ..models.find_replace_response import FindReplaceResponse
  from ..models.refresh_data_source_response import RefreshDataSourceResponse
  from ..models.trim_whitespace_response import TrimWhitespaceResponse
  from ..models.update_conditional_format_rule_response import UpdateConditionalFormatRuleResponse
  from ..models.update_data_source_response import UpdateDataSourceResponse
  from ..models.update_developer_metadata_response import UpdateDeveloperMetadataResponse
  from ..models.update_embedded_object_position_response import UpdateEmbeddedObjectPositionResponse





T = TypeVar("T", bound="Response")



@_attrs_define
class Response:
    """ A single response from an update.

        Attributes:
            add_banding (AddBandingResponse | Unset): The result of adding a banded range.
            add_chart (AddChartResponse | Unset): The result of adding a chart to a spreadsheet.
            add_data_source (AddDataSourceResponse | Unset): The result of adding a data source.
            add_dimension_group (AddDimensionGroupResponse | Unset): The result of adding a group.
            add_filter_view (AddFilterViewResponse | Unset): The result of adding a filter view.
            add_named_range (AddNamedRangeResponse | Unset): The result of adding a named range.
            add_protected_range (AddProtectedRangeResponse | Unset): The result of adding a new protected range.
            add_sheet (AddSheetResponse | Unset): The result of adding a sheet.
            add_slicer (AddSlicerResponse | Unset): The result of adding a slicer to a spreadsheet.
            create_developer_metadata (CreateDeveloperMetadataResponse | Unset): The response from creating developer
                metadata.
            delete_conditional_format_rule (DeleteConditionalFormatRuleResponse | Unset): The result of deleting a
                conditional format rule.
            delete_developer_metadata (DeleteDeveloperMetadataResponse | Unset): The response from deleting developer
                metadata.
            delete_dimension_group (DeleteDimensionGroupResponse | Unset): The result of deleting a group.
            delete_duplicates (DeleteDuplicatesResponse | Unset): The result of removing duplicates in a range.
            duplicate_filter_view (DuplicateFilterViewResponse | Unset): The result of a filter view being duplicated.
            duplicate_sheet (DuplicateSheetResponse | Unset): The result of duplicating a sheet.
            find_replace (FindReplaceResponse | Unset): The result of the find/replace.
            refresh_data_source (RefreshDataSourceResponse | Unset): The response from refreshing one or multiple data
                source objects.
            trim_whitespace (TrimWhitespaceResponse | Unset): The result of trimming whitespace in cells.
            update_conditional_format_rule (UpdateConditionalFormatRuleResponse | Unset): The result of updating a
                conditional format rule.
            update_data_source (UpdateDataSourceResponse | Unset): The response from updating data source.
            update_developer_metadata (UpdateDeveloperMetadataResponse | Unset): The response from updating developer
                metadata.
            update_embedded_object_position (UpdateEmbeddedObjectPositionResponse | Unset): The result of updating an
                embedded object's position.
     """

    add_banding: AddBandingResponse | Unset = UNSET
    add_chart: AddChartResponse | Unset = UNSET
    add_data_source: AddDataSourceResponse | Unset = UNSET
    add_dimension_group: AddDimensionGroupResponse | Unset = UNSET
    add_filter_view: AddFilterViewResponse | Unset = UNSET
    add_named_range: AddNamedRangeResponse | Unset = UNSET
    add_protected_range: AddProtectedRangeResponse | Unset = UNSET
    add_sheet: AddSheetResponse | Unset = UNSET
    add_slicer: AddSlicerResponse | Unset = UNSET
    create_developer_metadata: CreateDeveloperMetadataResponse | Unset = UNSET
    delete_conditional_format_rule: DeleteConditionalFormatRuleResponse | Unset = UNSET
    delete_developer_metadata: DeleteDeveloperMetadataResponse | Unset = UNSET
    delete_dimension_group: DeleteDimensionGroupResponse | Unset = UNSET
    delete_duplicates: DeleteDuplicatesResponse | Unset = UNSET
    duplicate_filter_view: DuplicateFilterViewResponse | Unset = UNSET
    duplicate_sheet: DuplicateSheetResponse | Unset = UNSET
    find_replace: FindReplaceResponse | Unset = UNSET
    refresh_data_source: RefreshDataSourceResponse | Unset = UNSET
    trim_whitespace: TrimWhitespaceResponse | Unset = UNSET
    update_conditional_format_rule: UpdateConditionalFormatRuleResponse | Unset = UNSET
    update_data_source: UpdateDataSourceResponse | Unset = UNSET
    update_developer_metadata: UpdateDeveloperMetadataResponse | Unset = UNSET
    update_embedded_object_position: UpdateEmbeddedObjectPositionResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.add_banding_response import AddBandingResponse
        from ..models.add_chart_response import AddChartResponse
        from ..models.add_data_source_response import AddDataSourceResponse
        from ..models.add_dimension_group_response import AddDimensionGroupResponse
        from ..models.add_filter_view_response import AddFilterViewResponse
        from ..models.add_named_range_response import AddNamedRangeResponse
        from ..models.add_protected_range_response import AddProtectedRangeResponse
        from ..models.add_sheet_response import AddSheetResponse
        from ..models.add_slicer_response import AddSlicerResponse
        from ..models.create_developer_metadata_response import CreateDeveloperMetadataResponse
        from ..models.delete_conditional_format_rule_response import DeleteConditionalFormatRuleResponse
        from ..models.delete_developer_metadata_response import DeleteDeveloperMetadataResponse
        from ..models.delete_dimension_group_response import DeleteDimensionGroupResponse
        from ..models.delete_duplicates_response import DeleteDuplicatesResponse
        from ..models.duplicate_filter_view_response import DuplicateFilterViewResponse
        from ..models.duplicate_sheet_response import DuplicateSheetResponse
        from ..models.find_replace_response import FindReplaceResponse
        from ..models.refresh_data_source_response import RefreshDataSourceResponse
        from ..models.trim_whitespace_response import TrimWhitespaceResponse
        from ..models.update_conditional_format_rule_response import UpdateConditionalFormatRuleResponse
        from ..models.update_data_source_response import UpdateDataSourceResponse
        from ..models.update_developer_metadata_response import UpdateDeveloperMetadataResponse
        from ..models.update_embedded_object_position_response import UpdateEmbeddedObjectPositionResponse
        add_banding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_banding, Unset):
            add_banding = self.add_banding.to_dict()

        add_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_chart, Unset):
            add_chart = self.add_chart.to_dict()

        add_data_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_data_source, Unset):
            add_data_source = self.add_data_source.to_dict()

        add_dimension_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_dimension_group, Unset):
            add_dimension_group = self.add_dimension_group.to_dict()

        add_filter_view: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_filter_view, Unset):
            add_filter_view = self.add_filter_view.to_dict()

        add_named_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_named_range, Unset):
            add_named_range = self.add_named_range.to_dict()

        add_protected_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_protected_range, Unset):
            add_protected_range = self.add_protected_range.to_dict()

        add_sheet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_sheet, Unset):
            add_sheet = self.add_sheet.to_dict()

        add_slicer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_slicer, Unset):
            add_slicer = self.add_slicer.to_dict()

        create_developer_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_developer_metadata, Unset):
            create_developer_metadata = self.create_developer_metadata.to_dict()

        delete_conditional_format_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_conditional_format_rule, Unset):
            delete_conditional_format_rule = self.delete_conditional_format_rule.to_dict()

        delete_developer_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_developer_metadata, Unset):
            delete_developer_metadata = self.delete_developer_metadata.to_dict()

        delete_dimension_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_dimension_group, Unset):
            delete_dimension_group = self.delete_dimension_group.to_dict()

        delete_duplicates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_duplicates, Unset):
            delete_duplicates = self.delete_duplicates.to_dict()

        duplicate_filter_view: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duplicate_filter_view, Unset):
            duplicate_filter_view = self.duplicate_filter_view.to_dict()

        duplicate_sheet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duplicate_sheet, Unset):
            duplicate_sheet = self.duplicate_sheet.to_dict()

        find_replace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.find_replace, Unset):
            find_replace = self.find_replace.to_dict()

        refresh_data_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refresh_data_source, Unset):
            refresh_data_source = self.refresh_data_source.to_dict()

        trim_whitespace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trim_whitespace, Unset):
            trim_whitespace = self.trim_whitespace.to_dict()

        update_conditional_format_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_conditional_format_rule, Unset):
            update_conditional_format_rule = self.update_conditional_format_rule.to_dict()

        update_data_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_data_source, Unset):
            update_data_source = self.update_data_source.to_dict()

        update_developer_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_developer_metadata, Unset):
            update_developer_metadata = self.update_developer_metadata.to_dict()

        update_embedded_object_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_embedded_object_position, Unset):
            update_embedded_object_position = self.update_embedded_object_position.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if add_banding is not UNSET:
            field_dict["addBanding"] = add_banding
        if add_chart is not UNSET:
            field_dict["addChart"] = add_chart
        if add_data_source is not UNSET:
            field_dict["addDataSource"] = add_data_source
        if add_dimension_group is not UNSET:
            field_dict["addDimensionGroup"] = add_dimension_group
        if add_filter_view is not UNSET:
            field_dict["addFilterView"] = add_filter_view
        if add_named_range is not UNSET:
            field_dict["addNamedRange"] = add_named_range
        if add_protected_range is not UNSET:
            field_dict["addProtectedRange"] = add_protected_range
        if add_sheet is not UNSET:
            field_dict["addSheet"] = add_sheet
        if add_slicer is not UNSET:
            field_dict["addSlicer"] = add_slicer
        if create_developer_metadata is not UNSET:
            field_dict["createDeveloperMetadata"] = create_developer_metadata
        if delete_conditional_format_rule is not UNSET:
            field_dict["deleteConditionalFormatRule"] = delete_conditional_format_rule
        if delete_developer_metadata is not UNSET:
            field_dict["deleteDeveloperMetadata"] = delete_developer_metadata
        if delete_dimension_group is not UNSET:
            field_dict["deleteDimensionGroup"] = delete_dimension_group
        if delete_duplicates is not UNSET:
            field_dict["deleteDuplicates"] = delete_duplicates
        if duplicate_filter_view is not UNSET:
            field_dict["duplicateFilterView"] = duplicate_filter_view
        if duplicate_sheet is not UNSET:
            field_dict["duplicateSheet"] = duplicate_sheet
        if find_replace is not UNSET:
            field_dict["findReplace"] = find_replace
        if refresh_data_source is not UNSET:
            field_dict["refreshDataSource"] = refresh_data_source
        if trim_whitespace is not UNSET:
            field_dict["trimWhitespace"] = trim_whitespace
        if update_conditional_format_rule is not UNSET:
            field_dict["updateConditionalFormatRule"] = update_conditional_format_rule
        if update_data_source is not UNSET:
            field_dict["updateDataSource"] = update_data_source
        if update_developer_metadata is not UNSET:
            field_dict["updateDeveloperMetadata"] = update_developer_metadata
        if update_embedded_object_position is not UNSET:
            field_dict["updateEmbeddedObjectPosition"] = update_embedded_object_position

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_banding_response import AddBandingResponse
        from ..models.add_chart_response import AddChartResponse
        from ..models.add_data_source_response import AddDataSourceResponse
        from ..models.add_dimension_group_response import AddDimensionGroupResponse
        from ..models.add_filter_view_response import AddFilterViewResponse
        from ..models.add_named_range_response import AddNamedRangeResponse
        from ..models.add_protected_range_response import AddProtectedRangeResponse
        from ..models.add_sheet_response import AddSheetResponse
        from ..models.add_slicer_response import AddSlicerResponse
        from ..models.create_developer_metadata_response import CreateDeveloperMetadataResponse
        from ..models.delete_conditional_format_rule_response import DeleteConditionalFormatRuleResponse
        from ..models.delete_developer_metadata_response import DeleteDeveloperMetadataResponse
        from ..models.delete_dimension_group_response import DeleteDimensionGroupResponse
        from ..models.delete_duplicates_response import DeleteDuplicatesResponse
        from ..models.duplicate_filter_view_response import DuplicateFilterViewResponse
        from ..models.duplicate_sheet_response import DuplicateSheetResponse
        from ..models.find_replace_response import FindReplaceResponse
        from ..models.refresh_data_source_response import RefreshDataSourceResponse
        from ..models.trim_whitespace_response import TrimWhitespaceResponse
        from ..models.update_conditional_format_rule_response import UpdateConditionalFormatRuleResponse
        from ..models.update_data_source_response import UpdateDataSourceResponse
        from ..models.update_developer_metadata_response import UpdateDeveloperMetadataResponse
        from ..models.update_embedded_object_position_response import UpdateEmbeddedObjectPositionResponse
        d = dict(src_dict)
        _add_banding = d.pop("addBanding", UNSET)
        add_banding: AddBandingResponse | Unset
        if isinstance(_add_banding,  Unset):
            add_banding = UNSET
        else:
            add_banding = AddBandingResponse.from_dict(_add_banding)




        _add_chart = d.pop("addChart", UNSET)
        add_chart: AddChartResponse | Unset
        if isinstance(_add_chart,  Unset):
            add_chart = UNSET
        else:
            add_chart = AddChartResponse.from_dict(_add_chart)




        _add_data_source = d.pop("addDataSource", UNSET)
        add_data_source: AddDataSourceResponse | Unset
        if isinstance(_add_data_source,  Unset):
            add_data_source = UNSET
        else:
            add_data_source = AddDataSourceResponse.from_dict(_add_data_source)




        _add_dimension_group = d.pop("addDimensionGroup", UNSET)
        add_dimension_group: AddDimensionGroupResponse | Unset
        if isinstance(_add_dimension_group,  Unset):
            add_dimension_group = UNSET
        else:
            add_dimension_group = AddDimensionGroupResponse.from_dict(_add_dimension_group)




        _add_filter_view = d.pop("addFilterView", UNSET)
        add_filter_view: AddFilterViewResponse | Unset
        if isinstance(_add_filter_view,  Unset):
            add_filter_view = UNSET
        else:
            add_filter_view = AddFilterViewResponse.from_dict(_add_filter_view)




        _add_named_range = d.pop("addNamedRange", UNSET)
        add_named_range: AddNamedRangeResponse | Unset
        if isinstance(_add_named_range,  Unset):
            add_named_range = UNSET
        else:
            add_named_range = AddNamedRangeResponse.from_dict(_add_named_range)




        _add_protected_range = d.pop("addProtectedRange", UNSET)
        add_protected_range: AddProtectedRangeResponse | Unset
        if isinstance(_add_protected_range,  Unset):
            add_protected_range = UNSET
        else:
            add_protected_range = AddProtectedRangeResponse.from_dict(_add_protected_range)




        _add_sheet = d.pop("addSheet", UNSET)
        add_sheet: AddSheetResponse | Unset
        if isinstance(_add_sheet,  Unset):
            add_sheet = UNSET
        else:
            add_sheet = AddSheetResponse.from_dict(_add_sheet)




        _add_slicer = d.pop("addSlicer", UNSET)
        add_slicer: AddSlicerResponse | Unset
        if isinstance(_add_slicer,  Unset):
            add_slicer = UNSET
        else:
            add_slicer = AddSlicerResponse.from_dict(_add_slicer)




        _create_developer_metadata = d.pop("createDeveloperMetadata", UNSET)
        create_developer_metadata: CreateDeveloperMetadataResponse | Unset
        if isinstance(_create_developer_metadata,  Unset):
            create_developer_metadata = UNSET
        else:
            create_developer_metadata = CreateDeveloperMetadataResponse.from_dict(_create_developer_metadata)




        _delete_conditional_format_rule = d.pop("deleteConditionalFormatRule", UNSET)
        delete_conditional_format_rule: DeleteConditionalFormatRuleResponse | Unset
        if isinstance(_delete_conditional_format_rule,  Unset):
            delete_conditional_format_rule = UNSET
        else:
            delete_conditional_format_rule = DeleteConditionalFormatRuleResponse.from_dict(_delete_conditional_format_rule)




        _delete_developer_metadata = d.pop("deleteDeveloperMetadata", UNSET)
        delete_developer_metadata: DeleteDeveloperMetadataResponse | Unset
        if isinstance(_delete_developer_metadata,  Unset):
            delete_developer_metadata = UNSET
        else:
            delete_developer_metadata = DeleteDeveloperMetadataResponse.from_dict(_delete_developer_metadata)




        _delete_dimension_group = d.pop("deleteDimensionGroup", UNSET)
        delete_dimension_group: DeleteDimensionGroupResponse | Unset
        if isinstance(_delete_dimension_group,  Unset):
            delete_dimension_group = UNSET
        else:
            delete_dimension_group = DeleteDimensionGroupResponse.from_dict(_delete_dimension_group)




        _delete_duplicates = d.pop("deleteDuplicates", UNSET)
        delete_duplicates: DeleteDuplicatesResponse | Unset
        if isinstance(_delete_duplicates,  Unset):
            delete_duplicates = UNSET
        else:
            delete_duplicates = DeleteDuplicatesResponse.from_dict(_delete_duplicates)




        _duplicate_filter_view = d.pop("duplicateFilterView", UNSET)
        duplicate_filter_view: DuplicateFilterViewResponse | Unset
        if isinstance(_duplicate_filter_view,  Unset):
            duplicate_filter_view = UNSET
        else:
            duplicate_filter_view = DuplicateFilterViewResponse.from_dict(_duplicate_filter_view)




        _duplicate_sheet = d.pop("duplicateSheet", UNSET)
        duplicate_sheet: DuplicateSheetResponse | Unset
        if isinstance(_duplicate_sheet,  Unset):
            duplicate_sheet = UNSET
        else:
            duplicate_sheet = DuplicateSheetResponse.from_dict(_duplicate_sheet)




        _find_replace = d.pop("findReplace", UNSET)
        find_replace: FindReplaceResponse | Unset
        if isinstance(_find_replace,  Unset):
            find_replace = UNSET
        else:
            find_replace = FindReplaceResponse.from_dict(_find_replace)




        _refresh_data_source = d.pop("refreshDataSource", UNSET)
        refresh_data_source: RefreshDataSourceResponse | Unset
        if isinstance(_refresh_data_source,  Unset):
            refresh_data_source = UNSET
        else:
            refresh_data_source = RefreshDataSourceResponse.from_dict(_refresh_data_source)




        _trim_whitespace = d.pop("trimWhitespace", UNSET)
        trim_whitespace: TrimWhitespaceResponse | Unset
        if isinstance(_trim_whitespace,  Unset):
            trim_whitespace = UNSET
        else:
            trim_whitespace = TrimWhitespaceResponse.from_dict(_trim_whitespace)




        _update_conditional_format_rule = d.pop("updateConditionalFormatRule", UNSET)
        update_conditional_format_rule: UpdateConditionalFormatRuleResponse | Unset
        if isinstance(_update_conditional_format_rule,  Unset):
            update_conditional_format_rule = UNSET
        else:
            update_conditional_format_rule = UpdateConditionalFormatRuleResponse.from_dict(_update_conditional_format_rule)




        _update_data_source = d.pop("updateDataSource", UNSET)
        update_data_source: UpdateDataSourceResponse | Unset
        if isinstance(_update_data_source,  Unset):
            update_data_source = UNSET
        else:
            update_data_source = UpdateDataSourceResponse.from_dict(_update_data_source)




        _update_developer_metadata = d.pop("updateDeveloperMetadata", UNSET)
        update_developer_metadata: UpdateDeveloperMetadataResponse | Unset
        if isinstance(_update_developer_metadata,  Unset):
            update_developer_metadata = UNSET
        else:
            update_developer_metadata = UpdateDeveloperMetadataResponse.from_dict(_update_developer_metadata)




        _update_embedded_object_position = d.pop("updateEmbeddedObjectPosition", UNSET)
        update_embedded_object_position: UpdateEmbeddedObjectPositionResponse | Unset
        if isinstance(_update_embedded_object_position,  Unset):
            update_embedded_object_position = UNSET
        else:
            update_embedded_object_position = UpdateEmbeddedObjectPositionResponse.from_dict(_update_embedded_object_position)




        response = cls(
            add_banding=add_banding,
            add_chart=add_chart,
            add_data_source=add_data_source,
            add_dimension_group=add_dimension_group,
            add_filter_view=add_filter_view,
            add_named_range=add_named_range,
            add_protected_range=add_protected_range,
            add_sheet=add_sheet,
            add_slicer=add_slicer,
            create_developer_metadata=create_developer_metadata,
            delete_conditional_format_rule=delete_conditional_format_rule,
            delete_developer_metadata=delete_developer_metadata,
            delete_dimension_group=delete_dimension_group,
            delete_duplicates=delete_duplicates,
            duplicate_filter_view=duplicate_filter_view,
            duplicate_sheet=duplicate_sheet,
            find_replace=find_replace,
            refresh_data_source=refresh_data_source,
            trim_whitespace=trim_whitespace,
            update_conditional_format_rule=update_conditional_format_rule,
            update_data_source=update_data_source,
            update_developer_metadata=update_developer_metadata,
            update_embedded_object_position=update_embedded_object_position,
        )


        response.additional_properties = d
        return response

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
