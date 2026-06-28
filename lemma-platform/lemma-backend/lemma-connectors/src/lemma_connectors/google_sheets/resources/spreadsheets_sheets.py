from __future__ import annotations

from lemma_connectors.google_sheets.generated.tool_types import SheetsSpreadsheetsSheetsCopyToToolInput, SheetsSpreadsheetsSheetsCopyToToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SpreadsheetsSheetsCopyToInput(SheetsSpreadsheetsSheetsCopyToToolInput):
    """Operation input for `spreadsheets_sheets_copy_to`."""
    pass

class SpreadsheetsSheetsCopyToOutput(SheetsSpreadsheetsSheetsCopyToToolOutput):
    """Operation output for `spreadsheets_sheets_copy_to`."""
    pass

class GoogleSheetsSpreadsheetsSheetsResource(BaseResourceClient):
    """Operations for the `spreadsheets_sheets` resource."""

    @operation(
        name='spreadsheets_sheets_copy_to',
        title='SpreadsheetsSheetsCopyTo',
        input_model=SpreadsheetsSheetsCopyToInput,
        output_model=SpreadsheetsSheetsCopyToOutput,
        tools_used=('sheets_spreadsheets_sheets_copy_to',),
        tags=tuple(['spreadsheets']),
    )
    async def copy_to(self, data: SpreadsheetsSheetsCopyToInput) -> SpreadsheetsSheetsCopyToOutput:
        """Copies a single sheet from a spreadsheet to another spreadsheet. Returns the properties of the newly created sheet.

Important inputs: fields, spreadsheet_id, sheet_id, body"""
        tool = self._client.get_tool('sheets_spreadsheets_sheets_copy_to')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SpreadsheetsSheetsCopyToOutput.model_validate(coerce_tool_result(result))
