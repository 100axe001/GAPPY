from __future__ import annotations

from lemma_connectors.google_sheets.generated.tool_types import SheetsSpreadsheetsDeveloperMetadataGetToolInput, SheetsSpreadsheetsDeveloperMetadataGetToolOutput, SheetsSpreadsheetsDeveloperMetadataSearchToolInput, SheetsSpreadsheetsDeveloperMetadataSearchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SpreadsheetsDeveloperMetadataGetInput(SheetsSpreadsheetsDeveloperMetadataGetToolInput):
    """Operation input for `spreadsheets_developer_metadata_get`."""
    pass

class SpreadsheetsDeveloperMetadataGetOutput(SheetsSpreadsheetsDeveloperMetadataGetToolOutput):
    """Operation output for `spreadsheets_developer_metadata_get`."""
    pass

class SpreadsheetsDeveloperMetadataSearchInput(SheetsSpreadsheetsDeveloperMetadataSearchToolInput):
    """Operation input for `spreadsheets_developer_metadata_search`."""
    pass

class SpreadsheetsDeveloperMetadataSearchOutput(SheetsSpreadsheetsDeveloperMetadataSearchToolOutput):
    """Operation output for `spreadsheets_developer_metadata_search`."""
    pass

class GoogleSheetsSpreadsheetsDeveloperMetadataResource(BaseResourceClient):
    """Operations for the `spreadsheets_developer_metadata` resource."""

    @operation(
        name='spreadsheets_developer_metadata_get',
        title='SpreadsheetsDeveloperMetadataGet',
        input_model=SpreadsheetsDeveloperMetadataGetInput,
        output_model=SpreadsheetsDeveloperMetadataGetOutput,
        tools_used=('sheets_spreadsheets_developer_metadata_get',),
        tags=tuple(['spreadsheets']),
    )
    async def get(self, data: SpreadsheetsDeveloperMetadataGetInput) -> SpreadsheetsDeveloperMetadataGetOutput:
        """Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and the developer metadata's unique metadataId.

Important inputs: fields, spreadsheet_id, metadata_id"""
        tool = self._client.get_tool('sheets_spreadsheets_developer_metadata_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsDeveloperMetadataGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_developer_metadata_search',
        title='SpreadsheetsDeveloperMetadataSearch',
        input_model=SpreadsheetsDeveloperMetadataSearchInput,
        output_model=SpreadsheetsDeveloperMetadataSearchOutput,
        tools_used=('sheets_spreadsheets_developer_metadata_search',),
        tags=tuple(['spreadsheets']),
    )
    async def search(self, data: SpreadsheetsDeveloperMetadataSearchInput) -> SpreadsheetsDeveloperMetadataSearchOutput:
        """Returns all developer metadata matching the specified DataFilter. If the provided DataFilter represents a DeveloperMetadataLookup object, this will return all DeveloperMetadata entries selected by it. If the DataFilter represents a location in a spreadsheet, this will return all developer metadata associated with locations intersecting that region.

Important inputs: fields, spreadsheet_id, body"""
        tool = self._client.get_tool('sheets_spreadsheets_developer_metadata_search')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsDeveloperMetadataSearchOutput.model_validate(coerce_tool_result(result))
