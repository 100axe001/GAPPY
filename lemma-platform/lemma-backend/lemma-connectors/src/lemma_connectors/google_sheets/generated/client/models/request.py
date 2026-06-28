from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.add_banding_request import AddBandingRequest
  from ..models.add_chart_request import AddChartRequest
  from ..models.add_conditional_format_rule_request import AddConditionalFormatRuleRequest
  from ..models.add_data_source_request import AddDataSourceRequest
  from ..models.add_dimension_group_request import AddDimensionGroupRequest
  from ..models.add_filter_view_request import AddFilterViewRequest
  from ..models.add_named_range_request import AddNamedRangeRequest
  from ..models.add_protected_range_request import AddProtectedRangeRequest
  from ..models.add_sheet_request import AddSheetRequest
  from ..models.add_slicer_request import AddSlicerRequest
  from ..models.append_cells_request import AppendCellsRequest
  from ..models.append_dimension_request import AppendDimensionRequest
  from ..models.auto_fill_request import AutoFillRequest
  from ..models.auto_resize_dimensions_request import AutoResizeDimensionsRequest
  from ..models.clear_basic_filter_request import ClearBasicFilterRequest
  from ..models.copy_paste_request import CopyPasteRequest
  from ..models.create_developer_metadata_request import CreateDeveloperMetadataRequest
  from ..models.cut_paste_request import CutPasteRequest
  from ..models.delete_banding_request import DeleteBandingRequest
  from ..models.delete_conditional_format_rule_request import DeleteConditionalFormatRuleRequest
  from ..models.delete_data_source_request import DeleteDataSourceRequest
  from ..models.delete_developer_metadata_request import DeleteDeveloperMetadataRequest
  from ..models.delete_dimension_group_request import DeleteDimensionGroupRequest
  from ..models.delete_dimension_request import DeleteDimensionRequest
  from ..models.delete_duplicates_request import DeleteDuplicatesRequest
  from ..models.delete_embedded_object_request import DeleteEmbeddedObjectRequest
  from ..models.delete_filter_view_request import DeleteFilterViewRequest
  from ..models.delete_named_range_request import DeleteNamedRangeRequest
  from ..models.delete_protected_range_request import DeleteProtectedRangeRequest
  from ..models.delete_range_request import DeleteRangeRequest
  from ..models.delete_sheet_request import DeleteSheetRequest
  from ..models.duplicate_filter_view_request import DuplicateFilterViewRequest
  from ..models.duplicate_sheet_request import DuplicateSheetRequest
  from ..models.find_replace_request import FindReplaceRequest
  from ..models.insert_dimension_request import InsertDimensionRequest
  from ..models.insert_range_request import InsertRangeRequest
  from ..models.merge_cells_request import MergeCellsRequest
  from ..models.move_dimension_request import MoveDimensionRequest
  from ..models.paste_data_request import PasteDataRequest
  from ..models.randomize_range_request import RandomizeRangeRequest
  from ..models.refresh_data_source_request import RefreshDataSourceRequest
  from ..models.repeat_cell_request import RepeatCellRequest
  from ..models.set_basic_filter_request import SetBasicFilterRequest
  from ..models.set_data_validation_request import SetDataValidationRequest
  from ..models.sort_range_request import SortRangeRequest
  from ..models.text_to_columns_request import TextToColumnsRequest
  from ..models.trim_whitespace_request import TrimWhitespaceRequest
  from ..models.unmerge_cells_request import UnmergeCellsRequest
  from ..models.update_banding_request import UpdateBandingRequest
  from ..models.update_borders_request import UpdateBordersRequest
  from ..models.update_cells_request import UpdateCellsRequest
  from ..models.update_chart_spec_request import UpdateChartSpecRequest
  from ..models.update_conditional_format_rule_request import UpdateConditionalFormatRuleRequest
  from ..models.update_data_source_request import UpdateDataSourceRequest
  from ..models.update_developer_metadata_request import UpdateDeveloperMetadataRequest
  from ..models.update_dimension_group_request import UpdateDimensionGroupRequest
  from ..models.update_dimension_properties_request import UpdateDimensionPropertiesRequest
  from ..models.update_embedded_object_border_request import UpdateEmbeddedObjectBorderRequest
  from ..models.update_embedded_object_position_request import UpdateEmbeddedObjectPositionRequest
  from ..models.update_filter_view_request import UpdateFilterViewRequest
  from ..models.update_named_range_request import UpdateNamedRangeRequest
  from ..models.update_protected_range_request import UpdateProtectedRangeRequest
  from ..models.update_sheet_properties_request import UpdateSheetPropertiesRequest
  from ..models.update_slicer_spec_request import UpdateSlicerSpecRequest
  from ..models.update_spreadsheet_properties_request import UpdateSpreadsheetPropertiesRequest





T = TypeVar("T", bound="Request")



@_attrs_define
class Request:
    """ A single kind of update to apply to a spreadsheet.

        Attributes:
            add_banding (AddBandingRequest | Unset): Adds a new banded range to the spreadsheet.
            add_chart (AddChartRequest | Unset): Adds a chart to a sheet in the spreadsheet.
            add_conditional_format_rule (AddConditionalFormatRuleRequest | Unset): Adds a new conditional format rule at the
                given index. All subsequent rules' indexes are incremented.
            add_data_source (AddDataSourceRequest | Unset): Adds a data source. After the data source is added successfully,
                an associated DATA_SOURCE sheet is created and an execution is triggered to refresh the sheet to read data from
                the data source. The request requires an additional `bigquery.readonly` OAuth scope.
            add_dimension_group (AddDimensionGroupRequest | Unset): Creates a group over the specified range. If the
                requested range is a superset of the range of an existing group G, then the depth of G is incremented and this
                new group G' has the depth of that group. For example, a group [C:D, depth 1] + [B:E] results in groups [B:E,
                depth 1] and [C:D, depth 2]. If the requested range is a subset of the range of an existing group G, then the
                depth of the new group G' becomes one greater than the depth of G. For example, a group [B:E, depth 1] + [C:D]
                results in groups [B:E, depth 1] and [C:D, depth 2]. If the requested range starts before and ends within, or
                starts within and ends after, the range of an existing group G, then the range of the existing group G becomes
                the union of the ranges, and the new group G' has depth one greater than the depth of G and range as the
                intersection of the ranges. For example, a group [B:D, depth 1] + [C:E] results in groups [B:E, depth 1] and
                [C:D, depth 2].
            add_filter_view (AddFilterViewRequest | Unset): Adds a filter view.
            add_named_range (AddNamedRangeRequest | Unset): Adds a named range to the spreadsheet.
            add_protected_range (AddProtectedRangeRequest | Unset): Adds a new protected range.
            add_sheet (AddSheetRequest | Unset): Adds a new sheet. When a sheet is added at a given index, all subsequent
                sheets' indexes are incremented. To add an object sheet, use AddChartRequest instead and specify
                EmbeddedObjectPosition.sheetId or EmbeddedObjectPosition.newSheet.
            add_slicer (AddSlicerRequest | Unset): Adds a slicer to a sheet in the spreadsheet.
            append_cells (AppendCellsRequest | Unset): Adds new cells after the last row with data in a sheet, inserting new
                rows into the sheet if necessary.
            append_dimension (AppendDimensionRequest | Unset): Appends rows or columns to the end of a sheet.
            auto_fill (AutoFillRequest | Unset): Fills in more data based on existing data.
            auto_resize_dimensions (AutoResizeDimensionsRequest | Unset): Automatically resizes one or more dimensions based
                on the contents of the cells in that dimension.
            clear_basic_filter (ClearBasicFilterRequest | Unset): Clears the basic filter, if any exists on the sheet.
            copy_paste (CopyPasteRequest | Unset): Copies data from the source to the destination.
            create_developer_metadata (CreateDeveloperMetadataRequest | Unset): A request to create developer metadata.
            cut_paste (CutPasteRequest | Unset): Moves data from the source to the destination.
            delete_banding (DeleteBandingRequest | Unset): Removes the banded range with the given ID from the spreadsheet.
            delete_conditional_format_rule (DeleteConditionalFormatRuleRequest | Unset): Deletes a conditional format rule
                at the given index. All subsequent rules' indexes are decremented.
            delete_data_source (DeleteDataSourceRequest | Unset): Deletes a data source. The request also deletes the
                associated data source sheet, and unlinks all associated data source objects.
            delete_developer_metadata (DeleteDeveloperMetadataRequest | Unset): A request to delete developer metadata.
            delete_dimension (DeleteDimensionRequest | Unset): Deletes the dimensions from the sheet.
            delete_dimension_group (DeleteDimensionGroupRequest | Unset): Deletes a group over the specified range by
                decrementing the depth of the dimensions in the range. For example, assume the sheet has a depth-1 group over
                B:E and a depth-2 group over C:D. Deleting a group over D:E leaves the sheet with a depth-1 group over B:D and a
                depth-2 group over C:C.
            delete_duplicates (DeleteDuplicatesRequest | Unset): Removes rows within this range that contain values in the
                specified columns that are duplicates of values in any previous row. Rows with identical values but different
                letter cases, formatting, or formulas are considered to be duplicates. This request also removes duplicate rows
                hidden from view (for example, due to a filter). When removing duplicates, the first instance of each duplicate
                row scanning from the top downwards is kept in the resulting range. Content outside of the specified range isn't
                removed, and rows considered duplicates do not have to be adjacent to each other in the range.
            delete_embedded_object (DeleteEmbeddedObjectRequest | Unset): Deletes the embedded object with the given ID.
            delete_filter_view (DeleteFilterViewRequest | Unset): Deletes a particular filter view.
            delete_named_range (DeleteNamedRangeRequest | Unset): Removes the named range with the given ID from the
                spreadsheet.
            delete_protected_range (DeleteProtectedRangeRequest | Unset): Deletes the protected range with the given ID.
            delete_range (DeleteRangeRequest | Unset): Deletes a range of cells, shifting other cells into the deleted area.
            delete_sheet (DeleteSheetRequest | Unset): Deletes the requested sheet.
            duplicate_filter_view (DuplicateFilterViewRequest | Unset): Duplicates a particular filter view.
            duplicate_sheet (DuplicateSheetRequest | Unset): Duplicates the contents of a sheet.
            find_replace (FindReplaceRequest | Unset): Finds and replaces data in cells over a range, sheet, or all sheets.
            insert_dimension (InsertDimensionRequest | Unset): Inserts rows or columns in a sheet at a particular index.
            insert_range (InsertRangeRequest | Unset): Inserts cells into a range, shifting the existing cells over or down.
            merge_cells (MergeCellsRequest | Unset): Merges all cells in the range.
            move_dimension (MoveDimensionRequest | Unset): Moves one or more rows or columns.
            paste_data (PasteDataRequest | Unset): Inserts data into the spreadsheet starting at the specified coordinate.
            randomize_range (RandomizeRangeRequest | Unset): Randomizes the order of the rows in a range.
            refresh_data_source (RefreshDataSourceRequest | Unset): Refreshes one or multiple data source objects in the
                spreadsheet by the specified references. The request requires an additional `bigquery.readonly` OAuth scope. If
                there are multiple refresh requests referencing the same data source objects in one batch, only the last refresh
                request is processed, and all those requests will have the same response accordingly.
            repeat_cell (RepeatCellRequest | Unset): Updates all cells in the range to the values in the given Cell object.
                Only the fields listed in the fields field are updated; others are unchanged. If writing a cell with a formula,
                the formula's ranges will automatically increment for each field in the range. For example, if writing a cell
                with formula `=A1` into range B2:C4, B2 would be `=A1`, B3 would be `=A2`, B4 would be `=A3`, C2 would be `=B1`,
                C3 would be `=B2`, C4 would be `=B3`. To keep the formula's ranges static, use the `$` indicator. For example,
                use the formula `=$A$1` to prevent both the row and the column from incrementing.
            set_basic_filter (SetBasicFilterRequest | Unset): Sets the basic filter associated with a sheet.
            set_data_validation (SetDataValidationRequest | Unset): Sets a data validation rule to every cell in the range.
                To clear validation in a range, call this with no rule specified.
            sort_range (SortRangeRequest | Unset): Sorts data in rows based on a sort order per column.
            text_to_columns (TextToColumnsRequest | Unset): Splits a column of text into multiple columns, based on a
                delimiter in each cell.
            trim_whitespace (TrimWhitespaceRequest | Unset): Trims the whitespace (such as spaces, tabs, or new lines) in
                every cell in the specified range. This request removes all whitespace from the start and end of each cell's
                text, and reduces any subsequence of remaining whitespace characters to a single space. If the resulting trimmed
                text starts with a '+' or '=' character, the text remains as a string value and isn't interpreted as a formula.
            unmerge_cells (UnmergeCellsRequest | Unset): Unmerges cells in the given range.
            update_banding (UpdateBandingRequest | Unset): Updates properties of the supplied banded range.
            update_borders (UpdateBordersRequest | Unset): Updates the borders of a range. If a field is not set in the
                request, that means the border remains as-is. For example, with two subsequent UpdateBordersRequest: 1. range:
                A1:A5 `{ top: RED, bottom: WHITE }` 2. range: A1:A5 `{ left: BLUE }` That would result in A1:A5 having a borders
                of `{ top: RED, bottom: WHITE, left: BLUE }`. If you want to clear a border, explicitly set the style to NONE.
            update_cells (UpdateCellsRequest | Unset): Updates all cells in a range with new data.
            update_chart_spec (UpdateChartSpecRequest | Unset): Updates a chart's specifications. (This does not move or
                resize a chart. To move or resize a chart, use UpdateEmbeddedObjectPositionRequest.)
            update_conditional_format_rule (UpdateConditionalFormatRuleRequest | Unset): Updates a conditional format rule
                at the given index, or moves a conditional format rule to another index.
            update_data_source (UpdateDataSourceRequest | Unset): Updates a data source. After the data source is updated
                successfully, an execution is triggered to refresh the associated DATA_SOURCE sheet to read data from the
                updated data source. The request requires an additional `bigquery.readonly` OAuth scope.
            update_developer_metadata (UpdateDeveloperMetadataRequest | Unset): A request to update properties of developer
                metadata. Updates the properties of the developer metadata selected by the filters to the values provided in the
                DeveloperMetadata resource. Callers must specify the properties they wish to update in the fields parameter, as
                well as specify at least one DataFilter matching the metadata they wish to update.
            update_dimension_group (UpdateDimensionGroupRequest | Unset): Updates the state of the specified group.
            update_dimension_properties (UpdateDimensionPropertiesRequest | Unset): Updates properties of dimensions within
                the specified range.
            update_embedded_object_border (UpdateEmbeddedObjectBorderRequest | Unset): Updates an embedded object's border
                property.
            update_embedded_object_position (UpdateEmbeddedObjectPositionRequest | Unset): Update an embedded object's
                position (such as a moving or resizing a chart or image).
            update_filter_view (UpdateFilterViewRequest | Unset): Updates properties of the filter view.
            update_named_range (UpdateNamedRangeRequest | Unset): Updates properties of the named range with the specified
                namedRangeId.
            update_protected_range (UpdateProtectedRangeRequest | Unset): Updates an existing protected range with the
                specified protectedRangeId.
            update_sheet_properties (UpdateSheetPropertiesRequest | Unset): Updates properties of the sheet with the
                specified sheetId.
            update_slicer_spec (UpdateSlicerSpecRequest | Unset): Updates a slicer's specifications. (This does not move or
                resize a slicer. To move or resize a slicer use UpdateEmbeddedObjectPositionRequest.
            update_spreadsheet_properties (UpdateSpreadsheetPropertiesRequest | Unset): Updates properties of a spreadsheet.
     """

    add_banding: AddBandingRequest | Unset = UNSET
    add_chart: AddChartRequest | Unset = UNSET
    add_conditional_format_rule: AddConditionalFormatRuleRequest | Unset = UNSET
    add_data_source: AddDataSourceRequest | Unset = UNSET
    add_dimension_group: AddDimensionGroupRequest | Unset = UNSET
    add_filter_view: AddFilterViewRequest | Unset = UNSET
    add_named_range: AddNamedRangeRequest | Unset = UNSET
    add_protected_range: AddProtectedRangeRequest | Unset = UNSET
    add_sheet: AddSheetRequest | Unset = UNSET
    add_slicer: AddSlicerRequest | Unset = UNSET
    append_cells: AppendCellsRequest | Unset = UNSET
    append_dimension: AppendDimensionRequest | Unset = UNSET
    auto_fill: AutoFillRequest | Unset = UNSET
    auto_resize_dimensions: AutoResizeDimensionsRequest | Unset = UNSET
    clear_basic_filter: ClearBasicFilterRequest | Unset = UNSET
    copy_paste: CopyPasteRequest | Unset = UNSET
    create_developer_metadata: CreateDeveloperMetadataRequest | Unset = UNSET
    cut_paste: CutPasteRequest | Unset = UNSET
    delete_banding: DeleteBandingRequest | Unset = UNSET
    delete_conditional_format_rule: DeleteConditionalFormatRuleRequest | Unset = UNSET
    delete_data_source: DeleteDataSourceRequest | Unset = UNSET
    delete_developer_metadata: DeleteDeveloperMetadataRequest | Unset = UNSET
    delete_dimension: DeleteDimensionRequest | Unset = UNSET
    delete_dimension_group: DeleteDimensionGroupRequest | Unset = UNSET
    delete_duplicates: DeleteDuplicatesRequest | Unset = UNSET
    delete_embedded_object: DeleteEmbeddedObjectRequest | Unset = UNSET
    delete_filter_view: DeleteFilterViewRequest | Unset = UNSET
    delete_named_range: DeleteNamedRangeRequest | Unset = UNSET
    delete_protected_range: DeleteProtectedRangeRequest | Unset = UNSET
    delete_range: DeleteRangeRequest | Unset = UNSET
    delete_sheet: DeleteSheetRequest | Unset = UNSET
    duplicate_filter_view: DuplicateFilterViewRequest | Unset = UNSET
    duplicate_sheet: DuplicateSheetRequest | Unset = UNSET
    find_replace: FindReplaceRequest | Unset = UNSET
    insert_dimension: InsertDimensionRequest | Unset = UNSET
    insert_range: InsertRangeRequest | Unset = UNSET
    merge_cells: MergeCellsRequest | Unset = UNSET
    move_dimension: MoveDimensionRequest | Unset = UNSET
    paste_data: PasteDataRequest | Unset = UNSET
    randomize_range: RandomizeRangeRequest | Unset = UNSET
    refresh_data_source: RefreshDataSourceRequest | Unset = UNSET
    repeat_cell: RepeatCellRequest | Unset = UNSET
    set_basic_filter: SetBasicFilterRequest | Unset = UNSET
    set_data_validation: SetDataValidationRequest | Unset = UNSET
    sort_range: SortRangeRequest | Unset = UNSET
    text_to_columns: TextToColumnsRequest | Unset = UNSET
    trim_whitespace: TrimWhitespaceRequest | Unset = UNSET
    unmerge_cells: UnmergeCellsRequest | Unset = UNSET
    update_banding: UpdateBandingRequest | Unset = UNSET
    update_borders: UpdateBordersRequest | Unset = UNSET
    update_cells: UpdateCellsRequest | Unset = UNSET
    update_chart_spec: UpdateChartSpecRequest | Unset = UNSET
    update_conditional_format_rule: UpdateConditionalFormatRuleRequest | Unset = UNSET
    update_data_source: UpdateDataSourceRequest | Unset = UNSET
    update_developer_metadata: UpdateDeveloperMetadataRequest | Unset = UNSET
    update_dimension_group: UpdateDimensionGroupRequest | Unset = UNSET
    update_dimension_properties: UpdateDimensionPropertiesRequest | Unset = UNSET
    update_embedded_object_border: UpdateEmbeddedObjectBorderRequest | Unset = UNSET
    update_embedded_object_position: UpdateEmbeddedObjectPositionRequest | Unset = UNSET
    update_filter_view: UpdateFilterViewRequest | Unset = UNSET
    update_named_range: UpdateNamedRangeRequest | Unset = UNSET
    update_protected_range: UpdateProtectedRangeRequest | Unset = UNSET
    update_sheet_properties: UpdateSheetPropertiesRequest | Unset = UNSET
    update_slicer_spec: UpdateSlicerSpecRequest | Unset = UNSET
    update_spreadsheet_properties: UpdateSpreadsheetPropertiesRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.add_banding_request import AddBandingRequest
        from ..models.add_chart_request import AddChartRequest
        from ..models.add_conditional_format_rule_request import AddConditionalFormatRuleRequest
        from ..models.add_data_source_request import AddDataSourceRequest
        from ..models.add_dimension_group_request import AddDimensionGroupRequest
        from ..models.add_filter_view_request import AddFilterViewRequest
        from ..models.add_named_range_request import AddNamedRangeRequest
        from ..models.add_protected_range_request import AddProtectedRangeRequest
        from ..models.add_sheet_request import AddSheetRequest
        from ..models.add_slicer_request import AddSlicerRequest
        from ..models.append_cells_request import AppendCellsRequest
        from ..models.append_dimension_request import AppendDimensionRequest
        from ..models.auto_fill_request import AutoFillRequest
        from ..models.auto_resize_dimensions_request import AutoResizeDimensionsRequest
        from ..models.clear_basic_filter_request import ClearBasicFilterRequest
        from ..models.copy_paste_request import CopyPasteRequest
        from ..models.create_developer_metadata_request import CreateDeveloperMetadataRequest
        from ..models.cut_paste_request import CutPasteRequest
        from ..models.delete_banding_request import DeleteBandingRequest
        from ..models.delete_conditional_format_rule_request import DeleteConditionalFormatRuleRequest
        from ..models.delete_data_source_request import DeleteDataSourceRequest
        from ..models.delete_developer_metadata_request import DeleteDeveloperMetadataRequest
        from ..models.delete_dimension_group_request import DeleteDimensionGroupRequest
        from ..models.delete_dimension_request import DeleteDimensionRequest
        from ..models.delete_duplicates_request import DeleteDuplicatesRequest
        from ..models.delete_embedded_object_request import DeleteEmbeddedObjectRequest
        from ..models.delete_filter_view_request import DeleteFilterViewRequest
        from ..models.delete_named_range_request import DeleteNamedRangeRequest
        from ..models.delete_protected_range_request import DeleteProtectedRangeRequest
        from ..models.delete_range_request import DeleteRangeRequest
        from ..models.delete_sheet_request import DeleteSheetRequest
        from ..models.duplicate_filter_view_request import DuplicateFilterViewRequest
        from ..models.duplicate_sheet_request import DuplicateSheetRequest
        from ..models.find_replace_request import FindReplaceRequest
        from ..models.insert_dimension_request import InsertDimensionRequest
        from ..models.insert_range_request import InsertRangeRequest
        from ..models.merge_cells_request import MergeCellsRequest
        from ..models.move_dimension_request import MoveDimensionRequest
        from ..models.paste_data_request import PasteDataRequest
        from ..models.randomize_range_request import RandomizeRangeRequest
        from ..models.refresh_data_source_request import RefreshDataSourceRequest
        from ..models.repeat_cell_request import RepeatCellRequest
        from ..models.set_basic_filter_request import SetBasicFilterRequest
        from ..models.set_data_validation_request import SetDataValidationRequest
        from ..models.sort_range_request import SortRangeRequest
        from ..models.text_to_columns_request import TextToColumnsRequest
        from ..models.trim_whitespace_request import TrimWhitespaceRequest
        from ..models.unmerge_cells_request import UnmergeCellsRequest
        from ..models.update_banding_request import UpdateBandingRequest
        from ..models.update_borders_request import UpdateBordersRequest
        from ..models.update_cells_request import UpdateCellsRequest
        from ..models.update_chart_spec_request import UpdateChartSpecRequest
        from ..models.update_conditional_format_rule_request import UpdateConditionalFormatRuleRequest
        from ..models.update_data_source_request import UpdateDataSourceRequest
        from ..models.update_developer_metadata_request import UpdateDeveloperMetadataRequest
        from ..models.update_dimension_group_request import UpdateDimensionGroupRequest
        from ..models.update_dimension_properties_request import UpdateDimensionPropertiesRequest
        from ..models.update_embedded_object_border_request import UpdateEmbeddedObjectBorderRequest
        from ..models.update_embedded_object_position_request import UpdateEmbeddedObjectPositionRequest
        from ..models.update_filter_view_request import UpdateFilterViewRequest
        from ..models.update_named_range_request import UpdateNamedRangeRequest
        from ..models.update_protected_range_request import UpdateProtectedRangeRequest
        from ..models.update_sheet_properties_request import UpdateSheetPropertiesRequest
        from ..models.update_slicer_spec_request import UpdateSlicerSpecRequest
        from ..models.update_spreadsheet_properties_request import UpdateSpreadsheetPropertiesRequest
        add_banding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_banding, Unset):
            add_banding = self.add_banding.to_dict()

        add_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_chart, Unset):
            add_chart = self.add_chart.to_dict()

        add_conditional_format_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_conditional_format_rule, Unset):
            add_conditional_format_rule = self.add_conditional_format_rule.to_dict()

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

        append_cells: dict[str, Any] | Unset = UNSET
        if not isinstance(self.append_cells, Unset):
            append_cells = self.append_cells.to_dict()

        append_dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.append_dimension, Unset):
            append_dimension = self.append_dimension.to_dict()

        auto_fill: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_fill, Unset):
            auto_fill = self.auto_fill.to_dict()

        auto_resize_dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_resize_dimensions, Unset):
            auto_resize_dimensions = self.auto_resize_dimensions.to_dict()

        clear_basic_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clear_basic_filter, Unset):
            clear_basic_filter = self.clear_basic_filter.to_dict()

        copy_paste: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copy_paste, Unset):
            copy_paste = self.copy_paste.to_dict()

        create_developer_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_developer_metadata, Unset):
            create_developer_metadata = self.create_developer_metadata.to_dict()

        cut_paste: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cut_paste, Unset):
            cut_paste = self.cut_paste.to_dict()

        delete_banding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_banding, Unset):
            delete_banding = self.delete_banding.to_dict()

        delete_conditional_format_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_conditional_format_rule, Unset):
            delete_conditional_format_rule = self.delete_conditional_format_rule.to_dict()

        delete_data_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_data_source, Unset):
            delete_data_source = self.delete_data_source.to_dict()

        delete_developer_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_developer_metadata, Unset):
            delete_developer_metadata = self.delete_developer_metadata.to_dict()

        delete_dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_dimension, Unset):
            delete_dimension = self.delete_dimension.to_dict()

        delete_dimension_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_dimension_group, Unset):
            delete_dimension_group = self.delete_dimension_group.to_dict()

        delete_duplicates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_duplicates, Unset):
            delete_duplicates = self.delete_duplicates.to_dict()

        delete_embedded_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_embedded_object, Unset):
            delete_embedded_object = self.delete_embedded_object.to_dict()

        delete_filter_view: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_filter_view, Unset):
            delete_filter_view = self.delete_filter_view.to_dict()

        delete_named_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_named_range, Unset):
            delete_named_range = self.delete_named_range.to_dict()

        delete_protected_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_protected_range, Unset):
            delete_protected_range = self.delete_protected_range.to_dict()

        delete_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_range, Unset):
            delete_range = self.delete_range.to_dict()

        delete_sheet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_sheet, Unset):
            delete_sheet = self.delete_sheet.to_dict()

        duplicate_filter_view: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duplicate_filter_view, Unset):
            duplicate_filter_view = self.duplicate_filter_view.to_dict()

        duplicate_sheet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duplicate_sheet, Unset):
            duplicate_sheet = self.duplicate_sheet.to_dict()

        find_replace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.find_replace, Unset):
            find_replace = self.find_replace.to_dict()

        insert_dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_dimension, Unset):
            insert_dimension = self.insert_dimension.to_dict()

        insert_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_range, Unset):
            insert_range = self.insert_range.to_dict()

        merge_cells: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge_cells, Unset):
            merge_cells = self.merge_cells.to_dict()

        move_dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.move_dimension, Unset):
            move_dimension = self.move_dimension.to_dict()

        paste_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paste_data, Unset):
            paste_data = self.paste_data.to_dict()

        randomize_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.randomize_range, Unset):
            randomize_range = self.randomize_range.to_dict()

        refresh_data_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refresh_data_source, Unset):
            refresh_data_source = self.refresh_data_source.to_dict()

        repeat_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repeat_cell, Unset):
            repeat_cell = self.repeat_cell.to_dict()

        set_basic_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_basic_filter, Unset):
            set_basic_filter = self.set_basic_filter.to_dict()

        set_data_validation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_data_validation, Unset):
            set_data_validation = self.set_data_validation.to_dict()

        sort_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort_range, Unset):
            sort_range = self.sort_range.to_dict()

        text_to_columns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_to_columns, Unset):
            text_to_columns = self.text_to_columns.to_dict()

        trim_whitespace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trim_whitespace, Unset):
            trim_whitespace = self.trim_whitespace.to_dict()

        unmerge_cells: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unmerge_cells, Unset):
            unmerge_cells = self.unmerge_cells.to_dict()

        update_banding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_banding, Unset):
            update_banding = self.update_banding.to_dict()

        update_borders: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_borders, Unset):
            update_borders = self.update_borders.to_dict()

        update_cells: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_cells, Unset):
            update_cells = self.update_cells.to_dict()

        update_chart_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_chart_spec, Unset):
            update_chart_spec = self.update_chart_spec.to_dict()

        update_conditional_format_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_conditional_format_rule, Unset):
            update_conditional_format_rule = self.update_conditional_format_rule.to_dict()

        update_data_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_data_source, Unset):
            update_data_source = self.update_data_source.to_dict()

        update_developer_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_developer_metadata, Unset):
            update_developer_metadata = self.update_developer_metadata.to_dict()

        update_dimension_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_dimension_group, Unset):
            update_dimension_group = self.update_dimension_group.to_dict()

        update_dimension_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_dimension_properties, Unset):
            update_dimension_properties = self.update_dimension_properties.to_dict()

        update_embedded_object_border: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_embedded_object_border, Unset):
            update_embedded_object_border = self.update_embedded_object_border.to_dict()

        update_embedded_object_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_embedded_object_position, Unset):
            update_embedded_object_position = self.update_embedded_object_position.to_dict()

        update_filter_view: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_filter_view, Unset):
            update_filter_view = self.update_filter_view.to_dict()

        update_named_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_named_range, Unset):
            update_named_range = self.update_named_range.to_dict()

        update_protected_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_protected_range, Unset):
            update_protected_range = self.update_protected_range.to_dict()

        update_sheet_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_sheet_properties, Unset):
            update_sheet_properties = self.update_sheet_properties.to_dict()

        update_slicer_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_slicer_spec, Unset):
            update_slicer_spec = self.update_slicer_spec.to_dict()

        update_spreadsheet_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_spreadsheet_properties, Unset):
            update_spreadsheet_properties = self.update_spreadsheet_properties.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if add_banding is not UNSET:
            field_dict["addBanding"] = add_banding
        if add_chart is not UNSET:
            field_dict["addChart"] = add_chart
        if add_conditional_format_rule is not UNSET:
            field_dict["addConditionalFormatRule"] = add_conditional_format_rule
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
        if append_cells is not UNSET:
            field_dict["appendCells"] = append_cells
        if append_dimension is not UNSET:
            field_dict["appendDimension"] = append_dimension
        if auto_fill is not UNSET:
            field_dict["autoFill"] = auto_fill
        if auto_resize_dimensions is not UNSET:
            field_dict["autoResizeDimensions"] = auto_resize_dimensions
        if clear_basic_filter is not UNSET:
            field_dict["clearBasicFilter"] = clear_basic_filter
        if copy_paste is not UNSET:
            field_dict["copyPaste"] = copy_paste
        if create_developer_metadata is not UNSET:
            field_dict["createDeveloperMetadata"] = create_developer_metadata
        if cut_paste is not UNSET:
            field_dict["cutPaste"] = cut_paste
        if delete_banding is not UNSET:
            field_dict["deleteBanding"] = delete_banding
        if delete_conditional_format_rule is not UNSET:
            field_dict["deleteConditionalFormatRule"] = delete_conditional_format_rule
        if delete_data_source is not UNSET:
            field_dict["deleteDataSource"] = delete_data_source
        if delete_developer_metadata is not UNSET:
            field_dict["deleteDeveloperMetadata"] = delete_developer_metadata
        if delete_dimension is not UNSET:
            field_dict["deleteDimension"] = delete_dimension
        if delete_dimension_group is not UNSET:
            field_dict["deleteDimensionGroup"] = delete_dimension_group
        if delete_duplicates is not UNSET:
            field_dict["deleteDuplicates"] = delete_duplicates
        if delete_embedded_object is not UNSET:
            field_dict["deleteEmbeddedObject"] = delete_embedded_object
        if delete_filter_view is not UNSET:
            field_dict["deleteFilterView"] = delete_filter_view
        if delete_named_range is not UNSET:
            field_dict["deleteNamedRange"] = delete_named_range
        if delete_protected_range is not UNSET:
            field_dict["deleteProtectedRange"] = delete_protected_range
        if delete_range is not UNSET:
            field_dict["deleteRange"] = delete_range
        if delete_sheet is not UNSET:
            field_dict["deleteSheet"] = delete_sheet
        if duplicate_filter_view is not UNSET:
            field_dict["duplicateFilterView"] = duplicate_filter_view
        if duplicate_sheet is not UNSET:
            field_dict["duplicateSheet"] = duplicate_sheet
        if find_replace is not UNSET:
            field_dict["findReplace"] = find_replace
        if insert_dimension is not UNSET:
            field_dict["insertDimension"] = insert_dimension
        if insert_range is not UNSET:
            field_dict["insertRange"] = insert_range
        if merge_cells is not UNSET:
            field_dict["mergeCells"] = merge_cells
        if move_dimension is not UNSET:
            field_dict["moveDimension"] = move_dimension
        if paste_data is not UNSET:
            field_dict["pasteData"] = paste_data
        if randomize_range is not UNSET:
            field_dict["randomizeRange"] = randomize_range
        if refresh_data_source is not UNSET:
            field_dict["refreshDataSource"] = refresh_data_source
        if repeat_cell is not UNSET:
            field_dict["repeatCell"] = repeat_cell
        if set_basic_filter is not UNSET:
            field_dict["setBasicFilter"] = set_basic_filter
        if set_data_validation is not UNSET:
            field_dict["setDataValidation"] = set_data_validation
        if sort_range is not UNSET:
            field_dict["sortRange"] = sort_range
        if text_to_columns is not UNSET:
            field_dict["textToColumns"] = text_to_columns
        if trim_whitespace is not UNSET:
            field_dict["trimWhitespace"] = trim_whitespace
        if unmerge_cells is not UNSET:
            field_dict["unmergeCells"] = unmerge_cells
        if update_banding is not UNSET:
            field_dict["updateBanding"] = update_banding
        if update_borders is not UNSET:
            field_dict["updateBorders"] = update_borders
        if update_cells is not UNSET:
            field_dict["updateCells"] = update_cells
        if update_chart_spec is not UNSET:
            field_dict["updateChartSpec"] = update_chart_spec
        if update_conditional_format_rule is not UNSET:
            field_dict["updateConditionalFormatRule"] = update_conditional_format_rule
        if update_data_source is not UNSET:
            field_dict["updateDataSource"] = update_data_source
        if update_developer_metadata is not UNSET:
            field_dict["updateDeveloperMetadata"] = update_developer_metadata
        if update_dimension_group is not UNSET:
            field_dict["updateDimensionGroup"] = update_dimension_group
        if update_dimension_properties is not UNSET:
            field_dict["updateDimensionProperties"] = update_dimension_properties
        if update_embedded_object_border is not UNSET:
            field_dict["updateEmbeddedObjectBorder"] = update_embedded_object_border
        if update_embedded_object_position is not UNSET:
            field_dict["updateEmbeddedObjectPosition"] = update_embedded_object_position
        if update_filter_view is not UNSET:
            field_dict["updateFilterView"] = update_filter_view
        if update_named_range is not UNSET:
            field_dict["updateNamedRange"] = update_named_range
        if update_protected_range is not UNSET:
            field_dict["updateProtectedRange"] = update_protected_range
        if update_sheet_properties is not UNSET:
            field_dict["updateSheetProperties"] = update_sheet_properties
        if update_slicer_spec is not UNSET:
            field_dict["updateSlicerSpec"] = update_slicer_spec
        if update_spreadsheet_properties is not UNSET:
            field_dict["updateSpreadsheetProperties"] = update_spreadsheet_properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_banding_request import AddBandingRequest
        from ..models.add_chart_request import AddChartRequest
        from ..models.add_conditional_format_rule_request import AddConditionalFormatRuleRequest
        from ..models.add_data_source_request import AddDataSourceRequest
        from ..models.add_dimension_group_request import AddDimensionGroupRequest
        from ..models.add_filter_view_request import AddFilterViewRequest
        from ..models.add_named_range_request import AddNamedRangeRequest
        from ..models.add_protected_range_request import AddProtectedRangeRequest
        from ..models.add_sheet_request import AddSheetRequest
        from ..models.add_slicer_request import AddSlicerRequest
        from ..models.append_cells_request import AppendCellsRequest
        from ..models.append_dimension_request import AppendDimensionRequest
        from ..models.auto_fill_request import AutoFillRequest
        from ..models.auto_resize_dimensions_request import AutoResizeDimensionsRequest
        from ..models.clear_basic_filter_request import ClearBasicFilterRequest
        from ..models.copy_paste_request import CopyPasteRequest
        from ..models.create_developer_metadata_request import CreateDeveloperMetadataRequest
        from ..models.cut_paste_request import CutPasteRequest
        from ..models.delete_banding_request import DeleteBandingRequest
        from ..models.delete_conditional_format_rule_request import DeleteConditionalFormatRuleRequest
        from ..models.delete_data_source_request import DeleteDataSourceRequest
        from ..models.delete_developer_metadata_request import DeleteDeveloperMetadataRequest
        from ..models.delete_dimension_group_request import DeleteDimensionGroupRequest
        from ..models.delete_dimension_request import DeleteDimensionRequest
        from ..models.delete_duplicates_request import DeleteDuplicatesRequest
        from ..models.delete_embedded_object_request import DeleteEmbeddedObjectRequest
        from ..models.delete_filter_view_request import DeleteFilterViewRequest
        from ..models.delete_named_range_request import DeleteNamedRangeRequest
        from ..models.delete_protected_range_request import DeleteProtectedRangeRequest
        from ..models.delete_range_request import DeleteRangeRequest
        from ..models.delete_sheet_request import DeleteSheetRequest
        from ..models.duplicate_filter_view_request import DuplicateFilterViewRequest
        from ..models.duplicate_sheet_request import DuplicateSheetRequest
        from ..models.find_replace_request import FindReplaceRequest
        from ..models.insert_dimension_request import InsertDimensionRequest
        from ..models.insert_range_request import InsertRangeRequest
        from ..models.merge_cells_request import MergeCellsRequest
        from ..models.move_dimension_request import MoveDimensionRequest
        from ..models.paste_data_request import PasteDataRequest
        from ..models.randomize_range_request import RandomizeRangeRequest
        from ..models.refresh_data_source_request import RefreshDataSourceRequest
        from ..models.repeat_cell_request import RepeatCellRequest
        from ..models.set_basic_filter_request import SetBasicFilterRequest
        from ..models.set_data_validation_request import SetDataValidationRequest
        from ..models.sort_range_request import SortRangeRequest
        from ..models.text_to_columns_request import TextToColumnsRequest
        from ..models.trim_whitespace_request import TrimWhitespaceRequest
        from ..models.unmerge_cells_request import UnmergeCellsRequest
        from ..models.update_banding_request import UpdateBandingRequest
        from ..models.update_borders_request import UpdateBordersRequest
        from ..models.update_cells_request import UpdateCellsRequest
        from ..models.update_chart_spec_request import UpdateChartSpecRequest
        from ..models.update_conditional_format_rule_request import UpdateConditionalFormatRuleRequest
        from ..models.update_data_source_request import UpdateDataSourceRequest
        from ..models.update_developer_metadata_request import UpdateDeveloperMetadataRequest
        from ..models.update_dimension_group_request import UpdateDimensionGroupRequest
        from ..models.update_dimension_properties_request import UpdateDimensionPropertiesRequest
        from ..models.update_embedded_object_border_request import UpdateEmbeddedObjectBorderRequest
        from ..models.update_embedded_object_position_request import UpdateEmbeddedObjectPositionRequest
        from ..models.update_filter_view_request import UpdateFilterViewRequest
        from ..models.update_named_range_request import UpdateNamedRangeRequest
        from ..models.update_protected_range_request import UpdateProtectedRangeRequest
        from ..models.update_sheet_properties_request import UpdateSheetPropertiesRequest
        from ..models.update_slicer_spec_request import UpdateSlicerSpecRequest
        from ..models.update_spreadsheet_properties_request import UpdateSpreadsheetPropertiesRequest
        d = dict(src_dict)
        _add_banding = d.pop("addBanding", UNSET)
        add_banding: AddBandingRequest | Unset
        if isinstance(_add_banding,  Unset):
            add_banding = UNSET
        else:
            add_banding = AddBandingRequest.from_dict(_add_banding)




        _add_chart = d.pop("addChart", UNSET)
        add_chart: AddChartRequest | Unset
        if isinstance(_add_chart,  Unset):
            add_chart = UNSET
        else:
            add_chart = AddChartRequest.from_dict(_add_chart)




        _add_conditional_format_rule = d.pop("addConditionalFormatRule", UNSET)
        add_conditional_format_rule: AddConditionalFormatRuleRequest | Unset
        if isinstance(_add_conditional_format_rule,  Unset):
            add_conditional_format_rule = UNSET
        else:
            add_conditional_format_rule = AddConditionalFormatRuleRequest.from_dict(_add_conditional_format_rule)




        _add_data_source = d.pop("addDataSource", UNSET)
        add_data_source: AddDataSourceRequest | Unset
        if isinstance(_add_data_source,  Unset):
            add_data_source = UNSET
        else:
            add_data_source = AddDataSourceRequest.from_dict(_add_data_source)




        _add_dimension_group = d.pop("addDimensionGroup", UNSET)
        add_dimension_group: AddDimensionGroupRequest | Unset
        if isinstance(_add_dimension_group,  Unset):
            add_dimension_group = UNSET
        else:
            add_dimension_group = AddDimensionGroupRequest.from_dict(_add_dimension_group)




        _add_filter_view = d.pop("addFilterView", UNSET)
        add_filter_view: AddFilterViewRequest | Unset
        if isinstance(_add_filter_view,  Unset):
            add_filter_view = UNSET
        else:
            add_filter_view = AddFilterViewRequest.from_dict(_add_filter_view)




        _add_named_range = d.pop("addNamedRange", UNSET)
        add_named_range: AddNamedRangeRequest | Unset
        if isinstance(_add_named_range,  Unset):
            add_named_range = UNSET
        else:
            add_named_range = AddNamedRangeRequest.from_dict(_add_named_range)




        _add_protected_range = d.pop("addProtectedRange", UNSET)
        add_protected_range: AddProtectedRangeRequest | Unset
        if isinstance(_add_protected_range,  Unset):
            add_protected_range = UNSET
        else:
            add_protected_range = AddProtectedRangeRequest.from_dict(_add_protected_range)




        _add_sheet = d.pop("addSheet", UNSET)
        add_sheet: AddSheetRequest | Unset
        if isinstance(_add_sheet,  Unset):
            add_sheet = UNSET
        else:
            add_sheet = AddSheetRequest.from_dict(_add_sheet)




        _add_slicer = d.pop("addSlicer", UNSET)
        add_slicer: AddSlicerRequest | Unset
        if isinstance(_add_slicer,  Unset):
            add_slicer = UNSET
        else:
            add_slicer = AddSlicerRequest.from_dict(_add_slicer)




        _append_cells = d.pop("appendCells", UNSET)
        append_cells: AppendCellsRequest | Unset
        if isinstance(_append_cells,  Unset):
            append_cells = UNSET
        else:
            append_cells = AppendCellsRequest.from_dict(_append_cells)




        _append_dimension = d.pop("appendDimension", UNSET)
        append_dimension: AppendDimensionRequest | Unset
        if isinstance(_append_dimension,  Unset):
            append_dimension = UNSET
        else:
            append_dimension = AppendDimensionRequest.from_dict(_append_dimension)




        _auto_fill = d.pop("autoFill", UNSET)
        auto_fill: AutoFillRequest | Unset
        if isinstance(_auto_fill,  Unset):
            auto_fill = UNSET
        else:
            auto_fill = AutoFillRequest.from_dict(_auto_fill)




        _auto_resize_dimensions = d.pop("autoResizeDimensions", UNSET)
        auto_resize_dimensions: AutoResizeDimensionsRequest | Unset
        if isinstance(_auto_resize_dimensions,  Unset):
            auto_resize_dimensions = UNSET
        else:
            auto_resize_dimensions = AutoResizeDimensionsRequest.from_dict(_auto_resize_dimensions)




        _clear_basic_filter = d.pop("clearBasicFilter", UNSET)
        clear_basic_filter: ClearBasicFilterRequest | Unset
        if isinstance(_clear_basic_filter,  Unset):
            clear_basic_filter = UNSET
        else:
            clear_basic_filter = ClearBasicFilterRequest.from_dict(_clear_basic_filter)




        _copy_paste = d.pop("copyPaste", UNSET)
        copy_paste: CopyPasteRequest | Unset
        if isinstance(_copy_paste,  Unset):
            copy_paste = UNSET
        else:
            copy_paste = CopyPasteRequest.from_dict(_copy_paste)




        _create_developer_metadata = d.pop("createDeveloperMetadata", UNSET)
        create_developer_metadata: CreateDeveloperMetadataRequest | Unset
        if isinstance(_create_developer_metadata,  Unset):
            create_developer_metadata = UNSET
        else:
            create_developer_metadata = CreateDeveloperMetadataRequest.from_dict(_create_developer_metadata)




        _cut_paste = d.pop("cutPaste", UNSET)
        cut_paste: CutPasteRequest | Unset
        if isinstance(_cut_paste,  Unset):
            cut_paste = UNSET
        else:
            cut_paste = CutPasteRequest.from_dict(_cut_paste)




        _delete_banding = d.pop("deleteBanding", UNSET)
        delete_banding: DeleteBandingRequest | Unset
        if isinstance(_delete_banding,  Unset):
            delete_banding = UNSET
        else:
            delete_banding = DeleteBandingRequest.from_dict(_delete_banding)




        _delete_conditional_format_rule = d.pop("deleteConditionalFormatRule", UNSET)
        delete_conditional_format_rule: DeleteConditionalFormatRuleRequest | Unset
        if isinstance(_delete_conditional_format_rule,  Unset):
            delete_conditional_format_rule = UNSET
        else:
            delete_conditional_format_rule = DeleteConditionalFormatRuleRequest.from_dict(_delete_conditional_format_rule)




        _delete_data_source = d.pop("deleteDataSource", UNSET)
        delete_data_source: DeleteDataSourceRequest | Unset
        if isinstance(_delete_data_source,  Unset):
            delete_data_source = UNSET
        else:
            delete_data_source = DeleteDataSourceRequest.from_dict(_delete_data_source)




        _delete_developer_metadata = d.pop("deleteDeveloperMetadata", UNSET)
        delete_developer_metadata: DeleteDeveloperMetadataRequest | Unset
        if isinstance(_delete_developer_metadata,  Unset):
            delete_developer_metadata = UNSET
        else:
            delete_developer_metadata = DeleteDeveloperMetadataRequest.from_dict(_delete_developer_metadata)




        _delete_dimension = d.pop("deleteDimension", UNSET)
        delete_dimension: DeleteDimensionRequest | Unset
        if isinstance(_delete_dimension,  Unset):
            delete_dimension = UNSET
        else:
            delete_dimension = DeleteDimensionRequest.from_dict(_delete_dimension)




        _delete_dimension_group = d.pop("deleteDimensionGroup", UNSET)
        delete_dimension_group: DeleteDimensionGroupRequest | Unset
        if isinstance(_delete_dimension_group,  Unset):
            delete_dimension_group = UNSET
        else:
            delete_dimension_group = DeleteDimensionGroupRequest.from_dict(_delete_dimension_group)




        _delete_duplicates = d.pop("deleteDuplicates", UNSET)
        delete_duplicates: DeleteDuplicatesRequest | Unset
        if isinstance(_delete_duplicates,  Unset):
            delete_duplicates = UNSET
        else:
            delete_duplicates = DeleteDuplicatesRequest.from_dict(_delete_duplicates)




        _delete_embedded_object = d.pop("deleteEmbeddedObject", UNSET)
        delete_embedded_object: DeleteEmbeddedObjectRequest | Unset
        if isinstance(_delete_embedded_object,  Unset):
            delete_embedded_object = UNSET
        else:
            delete_embedded_object = DeleteEmbeddedObjectRequest.from_dict(_delete_embedded_object)




        _delete_filter_view = d.pop("deleteFilterView", UNSET)
        delete_filter_view: DeleteFilterViewRequest | Unset
        if isinstance(_delete_filter_view,  Unset):
            delete_filter_view = UNSET
        else:
            delete_filter_view = DeleteFilterViewRequest.from_dict(_delete_filter_view)




        _delete_named_range = d.pop("deleteNamedRange", UNSET)
        delete_named_range: DeleteNamedRangeRequest | Unset
        if isinstance(_delete_named_range,  Unset):
            delete_named_range = UNSET
        else:
            delete_named_range = DeleteNamedRangeRequest.from_dict(_delete_named_range)




        _delete_protected_range = d.pop("deleteProtectedRange", UNSET)
        delete_protected_range: DeleteProtectedRangeRequest | Unset
        if isinstance(_delete_protected_range,  Unset):
            delete_protected_range = UNSET
        else:
            delete_protected_range = DeleteProtectedRangeRequest.from_dict(_delete_protected_range)




        _delete_range = d.pop("deleteRange", UNSET)
        delete_range: DeleteRangeRequest | Unset
        if isinstance(_delete_range,  Unset):
            delete_range = UNSET
        else:
            delete_range = DeleteRangeRequest.from_dict(_delete_range)




        _delete_sheet = d.pop("deleteSheet", UNSET)
        delete_sheet: DeleteSheetRequest | Unset
        if isinstance(_delete_sheet,  Unset):
            delete_sheet = UNSET
        else:
            delete_sheet = DeleteSheetRequest.from_dict(_delete_sheet)




        _duplicate_filter_view = d.pop("duplicateFilterView", UNSET)
        duplicate_filter_view: DuplicateFilterViewRequest | Unset
        if isinstance(_duplicate_filter_view,  Unset):
            duplicate_filter_view = UNSET
        else:
            duplicate_filter_view = DuplicateFilterViewRequest.from_dict(_duplicate_filter_view)




        _duplicate_sheet = d.pop("duplicateSheet", UNSET)
        duplicate_sheet: DuplicateSheetRequest | Unset
        if isinstance(_duplicate_sheet,  Unset):
            duplicate_sheet = UNSET
        else:
            duplicate_sheet = DuplicateSheetRequest.from_dict(_duplicate_sheet)




        _find_replace = d.pop("findReplace", UNSET)
        find_replace: FindReplaceRequest | Unset
        if isinstance(_find_replace,  Unset):
            find_replace = UNSET
        else:
            find_replace = FindReplaceRequest.from_dict(_find_replace)




        _insert_dimension = d.pop("insertDimension", UNSET)
        insert_dimension: InsertDimensionRequest | Unset
        if isinstance(_insert_dimension,  Unset):
            insert_dimension = UNSET
        else:
            insert_dimension = InsertDimensionRequest.from_dict(_insert_dimension)




        _insert_range = d.pop("insertRange", UNSET)
        insert_range: InsertRangeRequest | Unset
        if isinstance(_insert_range,  Unset):
            insert_range = UNSET
        else:
            insert_range = InsertRangeRequest.from_dict(_insert_range)




        _merge_cells = d.pop("mergeCells", UNSET)
        merge_cells: MergeCellsRequest | Unset
        if isinstance(_merge_cells,  Unset):
            merge_cells = UNSET
        else:
            merge_cells = MergeCellsRequest.from_dict(_merge_cells)




        _move_dimension = d.pop("moveDimension", UNSET)
        move_dimension: MoveDimensionRequest | Unset
        if isinstance(_move_dimension,  Unset):
            move_dimension = UNSET
        else:
            move_dimension = MoveDimensionRequest.from_dict(_move_dimension)




        _paste_data = d.pop("pasteData", UNSET)
        paste_data: PasteDataRequest | Unset
        if isinstance(_paste_data,  Unset):
            paste_data = UNSET
        else:
            paste_data = PasteDataRequest.from_dict(_paste_data)




        _randomize_range = d.pop("randomizeRange", UNSET)
        randomize_range: RandomizeRangeRequest | Unset
        if isinstance(_randomize_range,  Unset):
            randomize_range = UNSET
        else:
            randomize_range = RandomizeRangeRequest.from_dict(_randomize_range)




        _refresh_data_source = d.pop("refreshDataSource", UNSET)
        refresh_data_source: RefreshDataSourceRequest | Unset
        if isinstance(_refresh_data_source,  Unset):
            refresh_data_source = UNSET
        else:
            refresh_data_source = RefreshDataSourceRequest.from_dict(_refresh_data_source)




        _repeat_cell = d.pop("repeatCell", UNSET)
        repeat_cell: RepeatCellRequest | Unset
        if isinstance(_repeat_cell,  Unset):
            repeat_cell = UNSET
        else:
            repeat_cell = RepeatCellRequest.from_dict(_repeat_cell)




        _set_basic_filter = d.pop("setBasicFilter", UNSET)
        set_basic_filter: SetBasicFilterRequest | Unset
        if isinstance(_set_basic_filter,  Unset):
            set_basic_filter = UNSET
        else:
            set_basic_filter = SetBasicFilterRequest.from_dict(_set_basic_filter)




        _set_data_validation = d.pop("setDataValidation", UNSET)
        set_data_validation: SetDataValidationRequest | Unset
        if isinstance(_set_data_validation,  Unset):
            set_data_validation = UNSET
        else:
            set_data_validation = SetDataValidationRequest.from_dict(_set_data_validation)




        _sort_range = d.pop("sortRange", UNSET)
        sort_range: SortRangeRequest | Unset
        if isinstance(_sort_range,  Unset):
            sort_range = UNSET
        else:
            sort_range = SortRangeRequest.from_dict(_sort_range)




        _text_to_columns = d.pop("textToColumns", UNSET)
        text_to_columns: TextToColumnsRequest | Unset
        if isinstance(_text_to_columns,  Unset):
            text_to_columns = UNSET
        else:
            text_to_columns = TextToColumnsRequest.from_dict(_text_to_columns)




        _trim_whitespace = d.pop("trimWhitespace", UNSET)
        trim_whitespace: TrimWhitespaceRequest | Unset
        if isinstance(_trim_whitespace,  Unset):
            trim_whitespace = UNSET
        else:
            trim_whitespace = TrimWhitespaceRequest.from_dict(_trim_whitespace)




        _unmerge_cells = d.pop("unmergeCells", UNSET)
        unmerge_cells: UnmergeCellsRequest | Unset
        if isinstance(_unmerge_cells,  Unset):
            unmerge_cells = UNSET
        else:
            unmerge_cells = UnmergeCellsRequest.from_dict(_unmerge_cells)




        _update_banding = d.pop("updateBanding", UNSET)
        update_banding: UpdateBandingRequest | Unset
        if isinstance(_update_banding,  Unset):
            update_banding = UNSET
        else:
            update_banding = UpdateBandingRequest.from_dict(_update_banding)




        _update_borders = d.pop("updateBorders", UNSET)
        update_borders: UpdateBordersRequest | Unset
        if isinstance(_update_borders,  Unset):
            update_borders = UNSET
        else:
            update_borders = UpdateBordersRequest.from_dict(_update_borders)




        _update_cells = d.pop("updateCells", UNSET)
        update_cells: UpdateCellsRequest | Unset
        if isinstance(_update_cells,  Unset):
            update_cells = UNSET
        else:
            update_cells = UpdateCellsRequest.from_dict(_update_cells)




        _update_chart_spec = d.pop("updateChartSpec", UNSET)
        update_chart_spec: UpdateChartSpecRequest | Unset
        if isinstance(_update_chart_spec,  Unset):
            update_chart_spec = UNSET
        else:
            update_chart_spec = UpdateChartSpecRequest.from_dict(_update_chart_spec)




        _update_conditional_format_rule = d.pop("updateConditionalFormatRule", UNSET)
        update_conditional_format_rule: UpdateConditionalFormatRuleRequest | Unset
        if isinstance(_update_conditional_format_rule,  Unset):
            update_conditional_format_rule = UNSET
        else:
            update_conditional_format_rule = UpdateConditionalFormatRuleRequest.from_dict(_update_conditional_format_rule)




        _update_data_source = d.pop("updateDataSource", UNSET)
        update_data_source: UpdateDataSourceRequest | Unset
        if isinstance(_update_data_source,  Unset):
            update_data_source = UNSET
        else:
            update_data_source = UpdateDataSourceRequest.from_dict(_update_data_source)




        _update_developer_metadata = d.pop("updateDeveloperMetadata", UNSET)
        update_developer_metadata: UpdateDeveloperMetadataRequest | Unset
        if isinstance(_update_developer_metadata,  Unset):
            update_developer_metadata = UNSET
        else:
            update_developer_metadata = UpdateDeveloperMetadataRequest.from_dict(_update_developer_metadata)




        _update_dimension_group = d.pop("updateDimensionGroup", UNSET)
        update_dimension_group: UpdateDimensionGroupRequest | Unset
        if isinstance(_update_dimension_group,  Unset):
            update_dimension_group = UNSET
        else:
            update_dimension_group = UpdateDimensionGroupRequest.from_dict(_update_dimension_group)




        _update_dimension_properties = d.pop("updateDimensionProperties", UNSET)
        update_dimension_properties: UpdateDimensionPropertiesRequest | Unset
        if isinstance(_update_dimension_properties,  Unset):
            update_dimension_properties = UNSET
        else:
            update_dimension_properties = UpdateDimensionPropertiesRequest.from_dict(_update_dimension_properties)




        _update_embedded_object_border = d.pop("updateEmbeddedObjectBorder", UNSET)
        update_embedded_object_border: UpdateEmbeddedObjectBorderRequest | Unset
        if isinstance(_update_embedded_object_border,  Unset):
            update_embedded_object_border = UNSET
        else:
            update_embedded_object_border = UpdateEmbeddedObjectBorderRequest.from_dict(_update_embedded_object_border)




        _update_embedded_object_position = d.pop("updateEmbeddedObjectPosition", UNSET)
        update_embedded_object_position: UpdateEmbeddedObjectPositionRequest | Unset
        if isinstance(_update_embedded_object_position,  Unset):
            update_embedded_object_position = UNSET
        else:
            update_embedded_object_position = UpdateEmbeddedObjectPositionRequest.from_dict(_update_embedded_object_position)




        _update_filter_view = d.pop("updateFilterView", UNSET)
        update_filter_view: UpdateFilterViewRequest | Unset
        if isinstance(_update_filter_view,  Unset):
            update_filter_view = UNSET
        else:
            update_filter_view = UpdateFilterViewRequest.from_dict(_update_filter_view)




        _update_named_range = d.pop("updateNamedRange", UNSET)
        update_named_range: UpdateNamedRangeRequest | Unset
        if isinstance(_update_named_range,  Unset):
            update_named_range = UNSET
        else:
            update_named_range = UpdateNamedRangeRequest.from_dict(_update_named_range)




        _update_protected_range = d.pop("updateProtectedRange", UNSET)
        update_protected_range: UpdateProtectedRangeRequest | Unset
        if isinstance(_update_protected_range,  Unset):
            update_protected_range = UNSET
        else:
            update_protected_range = UpdateProtectedRangeRequest.from_dict(_update_protected_range)




        _update_sheet_properties = d.pop("updateSheetProperties", UNSET)
        update_sheet_properties: UpdateSheetPropertiesRequest | Unset
        if isinstance(_update_sheet_properties,  Unset):
            update_sheet_properties = UNSET
        else:
            update_sheet_properties = UpdateSheetPropertiesRequest.from_dict(_update_sheet_properties)




        _update_slicer_spec = d.pop("updateSlicerSpec", UNSET)
        update_slicer_spec: UpdateSlicerSpecRequest | Unset
        if isinstance(_update_slicer_spec,  Unset):
            update_slicer_spec = UNSET
        else:
            update_slicer_spec = UpdateSlicerSpecRequest.from_dict(_update_slicer_spec)




        _update_spreadsheet_properties = d.pop("updateSpreadsheetProperties", UNSET)
        update_spreadsheet_properties: UpdateSpreadsheetPropertiesRequest | Unset
        if isinstance(_update_spreadsheet_properties,  Unset):
            update_spreadsheet_properties = UNSET
        else:
            update_spreadsheet_properties = UpdateSpreadsheetPropertiesRequest.from_dict(_update_spreadsheet_properties)




        request = cls(
            add_banding=add_banding,
            add_chart=add_chart,
            add_conditional_format_rule=add_conditional_format_rule,
            add_data_source=add_data_source,
            add_dimension_group=add_dimension_group,
            add_filter_view=add_filter_view,
            add_named_range=add_named_range,
            add_protected_range=add_protected_range,
            add_sheet=add_sheet,
            add_slicer=add_slicer,
            append_cells=append_cells,
            append_dimension=append_dimension,
            auto_fill=auto_fill,
            auto_resize_dimensions=auto_resize_dimensions,
            clear_basic_filter=clear_basic_filter,
            copy_paste=copy_paste,
            create_developer_metadata=create_developer_metadata,
            cut_paste=cut_paste,
            delete_banding=delete_banding,
            delete_conditional_format_rule=delete_conditional_format_rule,
            delete_data_source=delete_data_source,
            delete_developer_metadata=delete_developer_metadata,
            delete_dimension=delete_dimension,
            delete_dimension_group=delete_dimension_group,
            delete_duplicates=delete_duplicates,
            delete_embedded_object=delete_embedded_object,
            delete_filter_view=delete_filter_view,
            delete_named_range=delete_named_range,
            delete_protected_range=delete_protected_range,
            delete_range=delete_range,
            delete_sheet=delete_sheet,
            duplicate_filter_view=duplicate_filter_view,
            duplicate_sheet=duplicate_sheet,
            find_replace=find_replace,
            insert_dimension=insert_dimension,
            insert_range=insert_range,
            merge_cells=merge_cells,
            move_dimension=move_dimension,
            paste_data=paste_data,
            randomize_range=randomize_range,
            refresh_data_source=refresh_data_source,
            repeat_cell=repeat_cell,
            set_basic_filter=set_basic_filter,
            set_data_validation=set_data_validation,
            sort_range=sort_range,
            text_to_columns=text_to_columns,
            trim_whitespace=trim_whitespace,
            unmerge_cells=unmerge_cells,
            update_banding=update_banding,
            update_borders=update_borders,
            update_cells=update_cells,
            update_chart_spec=update_chart_spec,
            update_conditional_format_rule=update_conditional_format_rule,
            update_data_source=update_data_source,
            update_developer_metadata=update_developer_metadata,
            update_dimension_group=update_dimension_group,
            update_dimension_properties=update_dimension_properties,
            update_embedded_object_border=update_embedded_object_border,
            update_embedded_object_position=update_embedded_object_position,
            update_filter_view=update_filter_view,
            update_named_range=update_named_range,
            update_protected_range=update_protected_range,
            update_sheet_properties=update_sheet_properties,
            update_slicer_spec=update_slicer_spec,
            update_spreadsheet_properties=update_spreadsheet_properties,
        )


        request.additional_properties = d
        return request

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
