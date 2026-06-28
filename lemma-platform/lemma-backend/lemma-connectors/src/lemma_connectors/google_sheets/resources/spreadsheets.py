from __future__ import annotations

from lemma_connectors.google_sheets.generated.tool_types import SheetsSpreadsheetsBatchUpdateToolInput, SheetsSpreadsheetsBatchUpdateToolOutput, SheetsSpreadsheetsCreateToolInput, SheetsSpreadsheetsCreateToolOutput, SheetsSpreadsheetsGetByDataFilterToolInput, SheetsSpreadsheetsGetByDataFilterToolOutput, SheetsSpreadsheetsGetToolInput, SheetsSpreadsheetsGetToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SpreadsheetsBatchUpdateInput(SheetsSpreadsheetsBatchUpdateToolInput):
    """Operation input for `spreadsheets_batch_update`."""
    pass

class SpreadsheetsBatchUpdateOutput(SheetsSpreadsheetsBatchUpdateToolOutput):
    """Operation output for `spreadsheets_batch_update`."""
    pass

class SpreadsheetsCreateInput(SheetsSpreadsheetsCreateToolInput):
    """Operation input for `spreadsheets_create`."""
    pass

class SpreadsheetsCreateOutput(SheetsSpreadsheetsCreateToolOutput):
    """Operation output for `spreadsheets_create`."""
    pass

class SpreadsheetsGetInput(SheetsSpreadsheetsGetToolInput):
    """Operation input for `spreadsheets_get`."""
    pass

class SpreadsheetsGetOutput(SheetsSpreadsheetsGetToolOutput):
    """Operation output for `spreadsheets_get`."""
    pass

class SpreadsheetsGetByDataFilterInput(SheetsSpreadsheetsGetByDataFilterToolInput):
    """Operation input for `spreadsheets_get_by_data_filter`."""
    pass

class SpreadsheetsGetByDataFilterOutput(SheetsSpreadsheetsGetByDataFilterToolOutput):
    """Operation output for `spreadsheets_get_by_data_filter`."""
    pass

class GoogleSheetsSpreadsheetsResource(BaseResourceClient):
    """Operations for the `spreadsheets` resource."""

    @operation(
        name='spreadsheets_batch_update',
        title='SpreadsheetsBatchUpdate',
        input_model=SpreadsheetsBatchUpdateInput,
        output_model=SpreadsheetsBatchUpdateOutput,
        tools_used=('sheets_spreadsheets_batch_update',),
        tags=tuple(['spreadsheets']),
    )
    async def batch_update(self, data: SpreadsheetsBatchUpdateInput) -> SpreadsheetsBatchUpdateOutput:
        """Applies one or more updates to the spreadsheet. Each request is validated before being applied. If any request is not valid then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. The replies will mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the response will have 2 empty replies, the actual reply, and another empty reply, in that order. Due to the collaborative nature of spreadsheets, it is not guaranteed that the spreadsheet will reflect exactly your changes after this completes, however it is guaranteed that the updates in the request will be applied together atomically. Your changes may be altered with respect to collaborator changes. If there are no collaborators, the spreadsheet should reflect your changes.

Important inputs: fields, spreadsheet_id, body"""
        tool = self._client.get_tool('sheets_spreadsheets_batch_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsBatchUpdateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_create',
        title='SpreadsheetsCreate',
        input_model=SpreadsheetsCreateInput,
        output_model=SpreadsheetsCreateOutput,
        tools_used=('sheets_spreadsheets_create',),
        tags=tuple(['spreadsheets']),
    )
    async def create(self, data: SpreadsheetsCreateInput) -> SpreadsheetsCreateOutput:
        """Creates a spreadsheet, returning the newly created spreadsheet.

Important inputs: fields, body"""
        tool = self._client.get_tool('sheets_spreadsheets_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_get',
        title='SpreadsheetsGet',
        input_model=SpreadsheetsGetInput,
        output_model=SpreadsheetsGetOutput,
        tools_used=('sheets_spreadsheets_get',),
        tags=tuple(['spreadsheets']),
    )
    async def get(self, data: SpreadsheetsGetInput) -> SpreadsheetsGetOutput:
        """Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default, data within grids is not returned. You can include grid data in one of 2 ways: * Specify a [field mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to true. If a field mask is set, the `includeGridData` parameter is ignored For large spreadsheets, as a best practice, retrieve only the specific spreadsheet fields that you want. To retrieve only subsets of spreadsheet data, use the ranges URL parameter. Ranges are specified using [A1 notation](/sheets/api/guides/concepts#cell). You can define a single cell (for example, `A1`) or multiple cells (for example, `A1:D5`). You can also get cells from other sheets within the same spreadsheet (for example, `Sheet2!A1:C4`) or retrieve multiple ranges at once (for example, `?ranges=A1:D5&ranges=Sheet2!A1:C4`). Limiting the range returns only the portions of the spreadsheet that intersect the requested ranges.

Important inputs: fields, spreadsheet_id, include_grid_data, ranges"""
        tool = self._client.get_tool('sheets_spreadsheets_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_get_by_data_filter',
        title='SpreadsheetsGetByDataFilter',
        input_model=SpreadsheetsGetByDataFilterInput,
        output_model=SpreadsheetsGetByDataFilterOutput,
        tools_used=('sheets_spreadsheets_get_by_data_filter',),
        tags=tuple(['spreadsheets']),
    )
    async def get_by_data_filter(self, data: SpreadsheetsGetByDataFilterInput) -> SpreadsheetsGetByDataFilterOutput:
        """Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. This method differs from GetSpreadsheet in that it allows selecting which subsets of spreadsheet data to return by specifying a dataFilters parameter. Multiple DataFilters can be specified. Specifying one or more data filters returns the portions of the spreadsheet that intersect ranges matched by any of the filters. By default, data within grids is not returned. You can include grid data one of 2 ways: * Specify a [field mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using the `fields` URL parameter in HTTP * Set the includeGridData parameter to true. If a field mask is set, the `includeGridData` parameter is ignored For large spreadsheets, as a best practice, retrieve only the specific spreadsheet fields that you want.

Important inputs: fields, spreadsheet_id, body"""
        tool = self._client.get_tool('sheets_spreadsheets_get_by_data_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsGetByDataFilterOutput.model_validate(coerce_tool_result(result))
