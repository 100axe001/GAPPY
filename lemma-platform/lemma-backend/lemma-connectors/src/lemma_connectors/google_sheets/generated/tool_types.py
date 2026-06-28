from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel

from lemma_connectors.core.results import BinaryContentResult

from lemma_connectors.google_sheets.generated.pydantic_models import AppendValuesResponse, BatchClearValuesByDataFilterRequest, BatchClearValuesByDataFilterResponse, BatchClearValuesRequest, BatchClearValuesResponse, BatchGetValuesByDataFilterRequest, BatchGetValuesByDataFilterResponse, BatchGetValuesResponse, BatchUpdateSpreadsheetRequest, BatchUpdateSpreadsheetResponse, BatchUpdateValuesByDataFilterRequest, BatchUpdateValuesByDataFilterResponse, BatchUpdateValuesRequest, BatchUpdateValuesResponse, ClearValuesRequest, ClearValuesResponse, CopySheetToAnotherSpreadsheetRequest, DeveloperMetadata, GetSpreadsheetByDataFilterRequest, SearchDeveloperMetadataRequest, SearchDeveloperMetadataResponse, SheetProperties, Spreadsheet, UpdateValuesResponse, ValueRange

class SheetsSpreadsheetsBatchUpdateToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_batch_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The spreadsheet to apply the updates to.')
    body: BatchUpdateSpreadsheetRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_batch_update`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsBatchUpdateToolOutput(BatchUpdateSpreadsheetResponse):
    """Output for tool `sheets_spreadsheets_batch_update`."""
    pass

class SheetsSpreadsheetsCreateToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    body: Spreadsheet | None = Field(default=None, description='Request body for `sheets_spreadsheets_create`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsCreateToolOutput(Spreadsheet):
    """Output for tool `sheets_spreadsheets_create`."""
    pass

class SheetsSpreadsheetsDeveloperMetadataGetToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_developer_metadata_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to retrieve metadata from.')
    metadata_id: int = Field(..., description='The ID of the developer metadata to retrieve.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsDeveloperMetadataGetToolOutput(DeveloperMetadata):
    """Output for tool `sheets_spreadsheets_developer_metadata_get`."""
    pass

class SheetsSpreadsheetsDeveloperMetadataSearchToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_developer_metadata_search`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to retrieve metadata from.')
    body: SearchDeveloperMetadataRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_developer_metadata_search`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsDeveloperMetadataSearchToolOutput(SearchDeveloperMetadataResponse):
    """Output for tool `sheets_spreadsheets_developer_metadata_search`."""
    pass

class SheetsSpreadsheetsGetToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The spreadsheet to request.')
    include_grid_data: bool | None = Field(default=None, description='True if grid data should be returned. This parameter is ignored if a field mask was set in the request.')
    ranges: list[str] | None = Field(default=None, description='The ranges to retrieve from the spreadsheet.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsGetToolOutput(Spreadsheet):
    """Output for tool `sheets_spreadsheets_get`."""
    pass

class SheetsSpreadsheetsGetByDataFilterToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_get_by_data_filter`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The spreadsheet to request.')
    body: GetSpreadsheetByDataFilterRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_get_by_data_filter`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsGetByDataFilterToolOutput(Spreadsheet):
    """Output for tool `sheets_spreadsheets_get_by_data_filter`."""
    pass

class SheetsSpreadsheetsSheetsCopyToToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_sheets_copy_to`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet containing the sheet to copy.')
    sheet_id: int = Field(..., description='The ID of the sheet to copy.')
    body: CopySheetToAnotherSpreadsheetRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_sheets_copy_to`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsSheetsCopyToToolOutput(SheetProperties):
    """Output for tool `sheets_spreadsheets_sheets_copy_to`."""
    pass

class SheetsSpreadsheetsValuesAppendToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_append`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to update.')
    range: str = Field(..., description='The [A1 notation](/sheets/api/guides/concepts#cell) of a range to search for a logical table of data. Values are appended after the last row of the table.')
    include_values_in_response: bool | None = Field(default=None, description='Determines if the update response should include the values of the cells that were appended. By default, responses do not include the updated values.')
    insert_data_option: Literal['OVERWRITE', 'INSERT_ROWS'] | None = Field(default=None, description='How the input data should be inserted.')
    response_date_time_render_option: Literal['SERIAL_NUMBER', 'FORMATTED_STRING'] | None = Field(default=None, description='Determines how dates, times, and durations in the response should be rendered. This is ignored if response_value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.')
    response_value_render_option: Literal['FORMATTED_VALUE', 'UNFORMATTED_VALUE', 'FORMULA'] | None = Field(default=None, description='Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE.')
    value_input_option: Literal['INPUT_VALUE_OPTION_UNSPECIFIED', 'RAW', 'USER_ENTERED'] | None = Field(default=None, description='How the input data should be interpreted.')
    body: ValueRange | None = Field(default=None, description='Request body for `sheets_spreadsheets_values_append`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesAppendToolOutput(AppendValuesResponse):
    """Output for tool `sheets_spreadsheets_values_append`."""
    pass

class SheetsSpreadsheetsValuesBatchClearToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_batch_clear`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to update.')
    body: BatchClearValuesRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_values_batch_clear`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesBatchClearToolOutput(BatchClearValuesResponse):
    """Output for tool `sheets_spreadsheets_values_batch_clear`."""
    pass

class SheetsSpreadsheetsValuesBatchClearByDataFilterToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_batch_clear_by_data_filter`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to update.')
    body: BatchClearValuesByDataFilterRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_values_batch_clear_by_data_filter`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesBatchClearByDataFilterToolOutput(BatchClearValuesByDataFilterResponse):
    """Output for tool `sheets_spreadsheets_values_batch_clear_by_data_filter`."""
    pass

class SheetsSpreadsheetsValuesBatchGetToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_batch_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to retrieve data from.')
    date_time_render_option: Literal['SERIAL_NUMBER', 'FORMATTED_STRING'] | None = Field(default=None, description='How dates, times, and durations should be represented in the output. This is ignored if value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.')
    major_dimension: Literal['DIMENSION_UNSPECIFIED', 'ROWS', 'COLUMNS'] | None = Field(default=None, description='The major dimension that results should use. For example, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`, then requesting `ranges=["A1:B2"],majorDimension=ROWS` returns `[[1,2],[3,4]]`, whereas requesting `ranges=["A1:B2"],majorDimension=COLUMNS` returns `[[1,3],[2,4]]`.')
    ranges: list[str] | None = Field(default=None, description='The [A1 notation or R1C1 notation](/sheets/api/guides/concepts#cell) of the range to retrieve values from.')
    value_render_option: Literal['FORMATTED_VALUE', 'UNFORMATTED_VALUE', 'FORMULA'] | None = Field(default=None, description='How values should be represented in the output. The default render option is ValueRenderOption.FORMATTED_VALUE.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesBatchGetToolOutput(BatchGetValuesResponse):
    """Output for tool `sheets_spreadsheets_values_batch_get`."""
    pass

class SheetsSpreadsheetsValuesBatchGetByDataFilterToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_batch_get_by_data_filter`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to retrieve data from.')
    body: BatchGetValuesByDataFilterRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_values_batch_get_by_data_filter`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesBatchGetByDataFilterToolOutput(BatchGetValuesByDataFilterResponse):
    """Output for tool `sheets_spreadsheets_values_batch_get_by_data_filter`."""
    pass

class SheetsSpreadsheetsValuesBatchUpdateToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_batch_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to update.')
    body: BatchUpdateValuesRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_values_batch_update`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesBatchUpdateToolOutput(BatchUpdateValuesResponse):
    """Output for tool `sheets_spreadsheets_values_batch_update`."""
    pass

class SheetsSpreadsheetsValuesBatchUpdateByDataFilterToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_batch_update_by_data_filter`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to update.')
    body: BatchUpdateValuesByDataFilterRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_values_batch_update_by_data_filter`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesBatchUpdateByDataFilterToolOutput(BatchUpdateValuesByDataFilterResponse):
    """Output for tool `sheets_spreadsheets_values_batch_update_by_data_filter`."""
    pass

class SheetsSpreadsheetsValuesClearToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_clear`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to update.')
    range: str = Field(..., description='The [A1 notation or R1C1 notation](/sheets/api/guides/concepts#cell) of the values to clear.')
    body: ClearValuesRequest | None = Field(default=None, description='Request body for `sheets_spreadsheets_values_clear`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesClearToolOutput(ClearValuesResponse):
    """Output for tool `sheets_spreadsheets_values_clear`."""
    pass

class SheetsSpreadsheetsValuesGetToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to retrieve data from.')
    range: str = Field(..., description='The [A1 notation or R1C1 notation](/sheets/api/guides/concepts#cell) of the range to retrieve values from.')
    date_time_render_option: Literal['SERIAL_NUMBER', 'FORMATTED_STRING'] | None = Field(default=None, description='How dates, times, and durations should be represented in the output. This is ignored if value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.')
    major_dimension: Literal['DIMENSION_UNSPECIFIED', 'ROWS', 'COLUMNS'] | None = Field(default=None, description='The major dimension that results should use. For example, if the spreadsheet data in Sheet1 is: `A1=1,B1=2,A2=3,B2=4`, then requesting `range=Sheet1!A1:B2?majorDimension=ROWS` returns `[[1,2],[3,4]]`, whereas requesting `range=Sheet1!A1:B2?majorDimension=COLUMNS` returns `[[1,3],[2,4]]`.')
    value_render_option: Literal['FORMATTED_VALUE', 'UNFORMATTED_VALUE', 'FORMULA'] | None = Field(default=None, description='How values should be represented in the output. The default render option is FORMATTED_VALUE.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesGetToolOutput(ValueRange):
    """Output for tool `sheets_spreadsheets_values_get`."""
    pass

class SheetsSpreadsheetsValuesUpdateToolInput(BaseModel):
    """Input for tool `sheets_spreadsheets_values_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    spreadsheet_id: str = Field(..., description='The ID of the spreadsheet to update.')
    range: str = Field(..., description='The [A1 notation](/sheets/api/guides/concepts#cell) of the values to update.')
    include_values_in_response: bool | None = Field(default=None, description='Determines if the update response should include the values of the cells that were updated. By default, responses do not include the updated values. If the range to write was larger than the range actually written, the response includes all values in the requested range (excluding trailing empty rows and columns).')
    response_date_time_render_option: Literal['SERIAL_NUMBER', 'FORMATTED_STRING'] | None = Field(default=None, description='Determines how dates, times, and durations in the response should be rendered. This is ignored if response_value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.')
    response_value_render_option: Literal['FORMATTED_VALUE', 'UNFORMATTED_VALUE', 'FORMULA'] | None = Field(default=None, description='Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE.')
    value_input_option: Literal['INPUT_VALUE_OPTION_UNSPECIFIED', 'RAW', 'USER_ENTERED'] | None = Field(default=None, description='How the input data should be interpreted.')
    body: ValueRange | None = Field(default=None, description='Request body for `sheets_spreadsheets_values_update`.')
    model_config = ConfigDict(extra='forbid')

class SheetsSpreadsheetsValuesUpdateToolOutput(UpdateValuesResponse):
    """Output for tool `sheets_spreadsheets_values_update`."""
    pass

INPUT_MODELS = {
    'sheets_spreadsheets_batch_update': SheetsSpreadsheetsBatchUpdateToolInput,
    'sheets_spreadsheets_create': SheetsSpreadsheetsCreateToolInput,
    'sheets_spreadsheets_developer_metadata_get': SheetsSpreadsheetsDeveloperMetadataGetToolInput,
    'sheets_spreadsheets_developer_metadata_search': SheetsSpreadsheetsDeveloperMetadataSearchToolInput,
    'sheets_spreadsheets_get': SheetsSpreadsheetsGetToolInput,
    'sheets_spreadsheets_get_by_data_filter': SheetsSpreadsheetsGetByDataFilterToolInput,
    'sheets_spreadsheets_sheets_copy_to': SheetsSpreadsheetsSheetsCopyToToolInput,
    'sheets_spreadsheets_values_append': SheetsSpreadsheetsValuesAppendToolInput,
    'sheets_spreadsheets_values_batch_clear': SheetsSpreadsheetsValuesBatchClearToolInput,
    'sheets_spreadsheets_values_batch_clear_by_data_filter': SheetsSpreadsheetsValuesBatchClearByDataFilterToolInput,
    'sheets_spreadsheets_values_batch_get': SheetsSpreadsheetsValuesBatchGetToolInput,
    'sheets_spreadsheets_values_batch_get_by_data_filter': SheetsSpreadsheetsValuesBatchGetByDataFilterToolInput,
    'sheets_spreadsheets_values_batch_update': SheetsSpreadsheetsValuesBatchUpdateToolInput,
    'sheets_spreadsheets_values_batch_update_by_data_filter': SheetsSpreadsheetsValuesBatchUpdateByDataFilterToolInput,
    'sheets_spreadsheets_values_clear': SheetsSpreadsheetsValuesClearToolInput,
    'sheets_spreadsheets_values_get': SheetsSpreadsheetsValuesGetToolInput,
    'sheets_spreadsheets_values_update': SheetsSpreadsheetsValuesUpdateToolInput,
}

OUTPUT_MODELS = {
    'sheets_spreadsheets_batch_update': SheetsSpreadsheetsBatchUpdateToolOutput,
    'sheets_spreadsheets_create': SheetsSpreadsheetsCreateToolOutput,
    'sheets_spreadsheets_developer_metadata_get': SheetsSpreadsheetsDeveloperMetadataGetToolOutput,
    'sheets_spreadsheets_developer_metadata_search': SheetsSpreadsheetsDeveloperMetadataSearchToolOutput,
    'sheets_spreadsheets_get': SheetsSpreadsheetsGetToolOutput,
    'sheets_spreadsheets_get_by_data_filter': SheetsSpreadsheetsGetByDataFilterToolOutput,
    'sheets_spreadsheets_sheets_copy_to': SheetsSpreadsheetsSheetsCopyToToolOutput,
    'sheets_spreadsheets_values_append': SheetsSpreadsheetsValuesAppendToolOutput,
    'sheets_spreadsheets_values_batch_clear': SheetsSpreadsheetsValuesBatchClearToolOutput,
    'sheets_spreadsheets_values_batch_clear_by_data_filter': SheetsSpreadsheetsValuesBatchClearByDataFilterToolOutput,
    'sheets_spreadsheets_values_batch_get': SheetsSpreadsheetsValuesBatchGetToolOutput,
    'sheets_spreadsheets_values_batch_get_by_data_filter': SheetsSpreadsheetsValuesBatchGetByDataFilterToolOutput,
    'sheets_spreadsheets_values_batch_update': SheetsSpreadsheetsValuesBatchUpdateToolOutput,
    'sheets_spreadsheets_values_batch_update_by_data_filter': SheetsSpreadsheetsValuesBatchUpdateByDataFilterToolOutput,
    'sheets_spreadsheets_values_clear': SheetsSpreadsheetsValuesClearToolOutput,
    'sheets_spreadsheets_values_get': SheetsSpreadsheetsValuesGetToolOutput,
    'sheets_spreadsheets_values_update': SheetsSpreadsheetsValuesUpdateToolOutput,
}
