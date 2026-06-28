from __future__ import annotations

from lemma_connectors.google_sheets.generated.tool_types import SheetsSpreadsheetsValuesAppendToolInput, SheetsSpreadsheetsValuesAppendToolOutput, SheetsSpreadsheetsValuesBatchClearByDataFilterToolInput, SheetsSpreadsheetsValuesBatchClearByDataFilterToolOutput, SheetsSpreadsheetsValuesBatchClearToolInput, SheetsSpreadsheetsValuesBatchClearToolOutput, SheetsSpreadsheetsValuesBatchGetByDataFilterToolInput, SheetsSpreadsheetsValuesBatchGetByDataFilterToolOutput, SheetsSpreadsheetsValuesBatchGetToolInput, SheetsSpreadsheetsValuesBatchGetToolOutput, SheetsSpreadsheetsValuesBatchUpdateByDataFilterToolInput, SheetsSpreadsheetsValuesBatchUpdateByDataFilterToolOutput, SheetsSpreadsheetsValuesBatchUpdateToolInput, SheetsSpreadsheetsValuesBatchUpdateToolOutput, SheetsSpreadsheetsValuesClearToolInput, SheetsSpreadsheetsValuesClearToolOutput, SheetsSpreadsheetsValuesGetToolInput, SheetsSpreadsheetsValuesGetToolOutput, SheetsSpreadsheetsValuesUpdateToolInput, SheetsSpreadsheetsValuesUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SpreadsheetsValuesAppendInput(SheetsSpreadsheetsValuesAppendToolInput):
    """Operation input for `spreadsheets_values_append`."""
    pass

class SpreadsheetsValuesAppendOutput(SheetsSpreadsheetsValuesAppendToolOutput):
    """Operation output for `spreadsheets_values_append`."""
    pass

class SpreadsheetsValuesBatchClearInput(SheetsSpreadsheetsValuesBatchClearToolInput):
    """Operation input for `spreadsheets_values_batch_clear`."""
    pass

class SpreadsheetsValuesBatchClearOutput(SheetsSpreadsheetsValuesBatchClearToolOutput):
    """Operation output for `spreadsheets_values_batch_clear`."""
    pass

class SpreadsheetsValuesBatchClearByDataFilterInput(SheetsSpreadsheetsValuesBatchClearByDataFilterToolInput):
    """Operation input for `spreadsheets_values_batch_clear_by_data_filter`."""
    pass

class SpreadsheetsValuesBatchClearByDataFilterOutput(SheetsSpreadsheetsValuesBatchClearByDataFilterToolOutput):
    """Operation output for `spreadsheets_values_batch_clear_by_data_filter`."""
    pass

class SpreadsheetsValuesBatchGetInput(SheetsSpreadsheetsValuesBatchGetToolInput):
    """Operation input for `spreadsheets_values_batch_get`."""
    pass

class SpreadsheetsValuesBatchGetOutput(SheetsSpreadsheetsValuesBatchGetToolOutput):
    """Operation output for `spreadsheets_values_batch_get`."""
    pass

class SpreadsheetsValuesBatchGetByDataFilterInput(SheetsSpreadsheetsValuesBatchGetByDataFilterToolInput):
    """Operation input for `spreadsheets_values_batch_get_by_data_filter`."""
    pass

class SpreadsheetsValuesBatchGetByDataFilterOutput(SheetsSpreadsheetsValuesBatchGetByDataFilterToolOutput):
    """Operation output for `spreadsheets_values_batch_get_by_data_filter`."""
    pass

class SpreadsheetsValuesBatchUpdateInput(SheetsSpreadsheetsValuesBatchUpdateToolInput):
    """Operation input for `spreadsheets_values_batch_update`."""
    pass

class SpreadsheetsValuesBatchUpdateOutput(SheetsSpreadsheetsValuesBatchUpdateToolOutput):
    """Operation output for `spreadsheets_values_batch_update`."""
    pass

class SpreadsheetsValuesBatchUpdateByDataFilterInput(SheetsSpreadsheetsValuesBatchUpdateByDataFilterToolInput):
    """Operation input for `spreadsheets_values_batch_update_by_data_filter`."""
    pass

class SpreadsheetsValuesBatchUpdateByDataFilterOutput(SheetsSpreadsheetsValuesBatchUpdateByDataFilterToolOutput):
    """Operation output for `spreadsheets_values_batch_update_by_data_filter`."""
    pass

class SpreadsheetsValuesClearInput(SheetsSpreadsheetsValuesClearToolInput):
    """Operation input for `spreadsheets_values_clear`."""
    pass

class SpreadsheetsValuesClearOutput(SheetsSpreadsheetsValuesClearToolOutput):
    """Operation output for `spreadsheets_values_clear`."""
    pass

class SpreadsheetsValuesGetInput(SheetsSpreadsheetsValuesGetToolInput):
    """Operation input for `spreadsheets_values_get`."""
    pass

class SpreadsheetsValuesGetOutput(SheetsSpreadsheetsValuesGetToolOutput):
    """Operation output for `spreadsheets_values_get`."""
    pass

class SpreadsheetsValuesUpdateInput(SheetsSpreadsheetsValuesUpdateToolInput):
    """Operation input for `spreadsheets_values_update`."""
    pass

class SpreadsheetsValuesUpdateOutput(SheetsSpreadsheetsValuesUpdateToolOutput):
    """Operation output for `spreadsheets_values_update`."""
    pass

class GoogleSheetsSpreadsheetsValuesResource(BaseResourceClient):
    """Operations for the `spreadsheets_values` resource."""

    @operation(
        name='spreadsheets_values_append',
        title='SpreadsheetsValuesAppend',
        input_model=SpreadsheetsValuesAppendInput,
        output_model=SpreadsheetsValuesAppendOutput,
        tools_used=('sheets_spreadsheets_values_append',),
        tags=tuple(['spreadsheets']),
    )
    async def append(self, data: SpreadsheetsValuesAppendInput) -> SpreadsheetsValuesAppendOutput:
        """Appends values to a spreadsheet. The input range is used to search for existing data and find a "table" within that range. Values will be appended to the next row of the table, starting with the first column of the table. See the [guide](/sheets/api/guides/values#appending_values) and [sample code](/sheets/api/samples/writing#append_values) for specific details of how tables are detected and data is appended. The caller must specify the spreadsheet ID, range, and a valueInputOption. The `valueInputOption` only controls how the input data will be added to the sheet (column-wise or row-wise), it does not influence what cell the data starts being written to.

Important inputs: fields, spreadsheet_id, range, include_values_in_response, insert_data_option, response_date_time_render_option, response_value_render_option, value_input_option, body"""
        tool = self._client.get_tool('sheets_spreadsheets_values_append')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesAppendOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_values_batch_clear',
        title='SpreadsheetsValuesBatchClear',
        input_model=SpreadsheetsValuesBatchClearInput,
        output_model=SpreadsheetsValuesBatchClearOutput,
        tools_used=('sheets_spreadsheets_values_batch_clear',),
        tags=tuple(['spreadsheets']),
    )
    async def batch_clear(self, data: SpreadsheetsValuesBatchClearInput) -> SpreadsheetsValuesBatchClearOutput:
        """Clears one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID and one or more ranges. Only values are cleared -- all other properties of the cell (such as formatting and data validation) are kept.

Important inputs: fields, spreadsheet_id, body"""
        tool = self._client.get_tool('sheets_spreadsheets_values_batch_clear')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesBatchClearOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_values_batch_clear_by_data_filter',
        title='SpreadsheetsValuesBatchClearByDataFilter',
        input_model=SpreadsheetsValuesBatchClearByDataFilterInput,
        output_model=SpreadsheetsValuesBatchClearByDataFilterOutput,
        tools_used=('sheets_spreadsheets_values_batch_clear_by_data_filter',),
        tags=tuple(['spreadsheets']),
    )
    async def batch_clear_by_data_filter(self, data: SpreadsheetsValuesBatchClearByDataFilterInput) -> SpreadsheetsValuesBatchClearByDataFilterOutput:
        """Clears one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID and one or more DataFilters. Ranges matching any of the specified data filters will be cleared. Only values are cleared -- all other properties of the cell (such as formatting, data validation, etc..) are kept.

Important inputs: fields, spreadsheet_id, body"""
        tool = self._client.get_tool('sheets_spreadsheets_values_batch_clear_by_data_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesBatchClearByDataFilterOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_values_batch_get',
        title='SpreadsheetsValuesBatchGet',
        input_model=SpreadsheetsValuesBatchGetInput,
        output_model=SpreadsheetsValuesBatchGetOutput,
        tools_used=('sheets_spreadsheets_values_batch_get',),
        tags=tuple(['spreadsheets']),
    )
    async def batch_get(self, data: SpreadsheetsValuesBatchGetInput) -> SpreadsheetsValuesBatchGetOutput:
        """Returns one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID and one or more ranges.

Important inputs: fields, spreadsheet_id, date_time_render_option, major_dimension, ranges, value_render_option"""
        tool = self._client.get_tool('sheets_spreadsheets_values_batch_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesBatchGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_values_batch_get_by_data_filter',
        title='SpreadsheetsValuesBatchGetByDataFilter',
        input_model=SpreadsheetsValuesBatchGetByDataFilterInput,
        output_model=SpreadsheetsValuesBatchGetByDataFilterOutput,
        tools_used=('sheets_spreadsheets_values_batch_get_by_data_filter',),
        tags=tuple(['spreadsheets']),
    )
    async def batch_get_by_data_filter(self, data: SpreadsheetsValuesBatchGetByDataFilterInput) -> SpreadsheetsValuesBatchGetByDataFilterOutput:
        """Returns one or more ranges of values that match the specified data filters. The caller must specify the spreadsheet ID and one or more DataFilters. Ranges that match any of the data filters in the request will be returned.

Important inputs: fields, spreadsheet_id, body"""
        tool = self._client.get_tool('sheets_spreadsheets_values_batch_get_by_data_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesBatchGetByDataFilterOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_values_batch_update',
        title='SpreadsheetsValuesBatchUpdate',
        input_model=SpreadsheetsValuesBatchUpdateInput,
        output_model=SpreadsheetsValuesBatchUpdateOutput,
        tools_used=('sheets_spreadsheets_values_batch_update',),
        tags=tuple(['spreadsheets']),
    )
    async def batch_update(self, data: SpreadsheetsValuesBatchUpdateInput) -> SpreadsheetsValuesBatchUpdateOutput:
        """Sets values in one or more ranges of a spreadsheet. The caller must specify the spreadsheet ID, a valueInputOption, and one or more ValueRanges.

Important inputs: fields, spreadsheet_id, body"""
        tool = self._client.get_tool('sheets_spreadsheets_values_batch_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesBatchUpdateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_values_batch_update_by_data_filter',
        title='SpreadsheetsValuesBatchUpdateByDataFilter',
        input_model=SpreadsheetsValuesBatchUpdateByDataFilterInput,
        output_model=SpreadsheetsValuesBatchUpdateByDataFilterOutput,
        tools_used=('sheets_spreadsheets_values_batch_update_by_data_filter',),
        tags=tuple(['spreadsheets']),
    )
    async def batch_update_by_data_filter(self, data: SpreadsheetsValuesBatchUpdateByDataFilterInput) -> SpreadsheetsValuesBatchUpdateByDataFilterOutput:
        """Sets values in one or more ranges of a spreadsheet. The caller must specify the spreadsheet ID, a valueInputOption, and one or more DataFilterValueRanges.

Important inputs: fields, spreadsheet_id, body"""
        tool = self._client.get_tool('sheets_spreadsheets_values_batch_update_by_data_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesBatchUpdateByDataFilterOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_values_clear',
        title='SpreadsheetsValuesClear',
        input_model=SpreadsheetsValuesClearInput,
        output_model=SpreadsheetsValuesClearOutput,
        tools_used=('sheets_spreadsheets_values_clear',),
        tags=tuple(['spreadsheets']),
    )
    async def clear(self, data: SpreadsheetsValuesClearInput) -> SpreadsheetsValuesClearOutput:
        """Clears values from a spreadsheet. The caller must specify the spreadsheet ID and range. Only values are cleared -- all other properties of the cell (such as formatting, data validation, etc..) are kept.

Important inputs: fields, spreadsheet_id, range, body"""
        tool = self._client.get_tool('sheets_spreadsheets_values_clear')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesClearOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_values_get',
        title='SpreadsheetsValuesGet',
        input_model=SpreadsheetsValuesGetInput,
        output_model=SpreadsheetsValuesGetOutput,
        tools_used=('sheets_spreadsheets_values_get',),
        tags=tuple(['spreadsheets']),
    )
    async def get(self, data: SpreadsheetsValuesGetInput) -> SpreadsheetsValuesGetOutput:
        """Returns a range of values from a spreadsheet. The caller must specify the spreadsheet ID and a range.

Important inputs: fields, spreadsheet_id, range, date_time_render_option, major_dimension, value_render_option"""
        tool = self._client.get_tool('sheets_spreadsheets_values_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='spreadsheets_values_update',
        title='SpreadsheetsValuesUpdate',
        input_model=SpreadsheetsValuesUpdateInput,
        output_model=SpreadsheetsValuesUpdateOutput,
        tools_used=('sheets_spreadsheets_values_update',),
        tags=tuple(['spreadsheets']),
    )
    async def update(self, data: SpreadsheetsValuesUpdateInput) -> SpreadsheetsValuesUpdateOutput:
        """Sets values in a range of a spreadsheet. The caller must specify the spreadsheet ID, range, and a valueInputOption.

Important inputs: fields, spreadsheet_id, range, include_values_in_response, response_date_time_render_option, response_value_render_option, value_input_option, body"""
        tool = self._client.get_tool('sheets_spreadsheets_values_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsValuesUpdateOutput.model_validate(coerce_tool_result(result))
