from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cell_format import CellFormat
  from ..models.data_source_formula import DataSourceFormula
  from ..models.data_source_table import DataSourceTable
  from ..models.data_validation_rule import DataValidationRule
  from ..models.extended_value import ExtendedValue
  from ..models.pivot_table import PivotTable
  from ..models.text_format_run import TextFormatRun





T = TypeVar("T", bound="CellData")



@_attrs_define
class CellData:
    """ Data about a specific cell.

        Attributes:
            data_source_formula (DataSourceFormula | Unset): A data source formula.
            data_source_table (DataSourceTable | Unset): A data source table, which allows the user to import a static table
                of data from the DataSource into Sheets. This is also known as "Extract" in the Sheets editor.
            data_validation (DataValidationRule | Unset): A data validation rule.
            effective_format (CellFormat | Unset): The format of a cell.
            effective_value (ExtendedValue | Unset): The kinds of value that a cell in a spreadsheet can have.
            formatted_value (str | Unset): The formatted value of the cell. This is the value as it's shown to the user.
                This field is read-only.
            hyperlink (str | Unset): A hyperlink this cell points to, if any. If the cell contains multiple hyperlinks, this
                field will be empty. This field is read-only. To set it, use a `=HYPERLINK` formula in the
                userEnteredValue.formulaValue field. A cell-level link can also be set from the userEnteredFormat.textFormat
                field. Alternatively, set a hyperlink in the textFormatRun.format.link field that spans the entire cell.
            note (str | Unset): Any note on the cell.
            pivot_table (PivotTable | Unset): A pivot table.
            text_format_runs (list[TextFormatRun] | Unset): Runs of rich text applied to subsections of the cell. Runs are
                only valid on user entered strings, not formulas, bools, or numbers. Properties of a run start at a specific
                index in the text and continue until the next run. Runs will inherit the properties of the cell unless
                explicitly changed. When writing, the new runs will overwrite any prior runs. When writing a new
                user_entered_value, previous runs are erased.
            user_entered_format (CellFormat | Unset): The format of a cell.
            user_entered_value (ExtendedValue | Unset): The kinds of value that a cell in a spreadsheet can have.
     """

    data_source_formula: DataSourceFormula | Unset = UNSET
    data_source_table: DataSourceTable | Unset = UNSET
    data_validation: DataValidationRule | Unset = UNSET
    effective_format: CellFormat | Unset = UNSET
    effective_value: ExtendedValue | Unset = UNSET
    formatted_value: str | Unset = UNSET
    hyperlink: str | Unset = UNSET
    note: str | Unset = UNSET
    pivot_table: PivotTable | Unset = UNSET
    text_format_runs: list[TextFormatRun] | Unset = UNSET
    user_entered_format: CellFormat | Unset = UNSET
    user_entered_value: ExtendedValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cell_format import CellFormat
        from ..models.data_source_formula import DataSourceFormula
        from ..models.data_source_table import DataSourceTable
        from ..models.data_validation_rule import DataValidationRule
        from ..models.extended_value import ExtendedValue
        from ..models.pivot_table import PivotTable
        from ..models.text_format_run import TextFormatRun
        data_source_formula: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_formula, Unset):
            data_source_formula = self.data_source_formula.to_dict()

        data_source_table: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_table, Unset):
            data_source_table = self.data_source_table.to_dict()

        data_validation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_validation, Unset):
            data_validation = self.data_validation.to_dict()

        effective_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.effective_format, Unset):
            effective_format = self.effective_format.to_dict()

        effective_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.effective_value, Unset):
            effective_value = self.effective_value.to_dict()

        formatted_value = self.formatted_value

        hyperlink = self.hyperlink

        note = self.note

        pivot_table: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pivot_table, Unset):
            pivot_table = self.pivot_table.to_dict()

        text_format_runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.text_format_runs, Unset):
            text_format_runs = []
            for text_format_runs_item_data in self.text_format_runs:
                text_format_runs_item = text_format_runs_item_data.to_dict()
                text_format_runs.append(text_format_runs_item)



        user_entered_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_entered_format, Unset):
            user_entered_format = self.user_entered_format.to_dict()

        user_entered_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_entered_value, Unset):
            user_entered_value = self.user_entered_value.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_source_formula is not UNSET:
            field_dict["dataSourceFormula"] = data_source_formula
        if data_source_table is not UNSET:
            field_dict["dataSourceTable"] = data_source_table
        if data_validation is not UNSET:
            field_dict["dataValidation"] = data_validation
        if effective_format is not UNSET:
            field_dict["effectiveFormat"] = effective_format
        if effective_value is not UNSET:
            field_dict["effectiveValue"] = effective_value
        if formatted_value is not UNSET:
            field_dict["formattedValue"] = formatted_value
        if hyperlink is not UNSET:
            field_dict["hyperlink"] = hyperlink
        if note is not UNSET:
            field_dict["note"] = note
        if pivot_table is not UNSET:
            field_dict["pivotTable"] = pivot_table
        if text_format_runs is not UNSET:
            field_dict["textFormatRuns"] = text_format_runs
        if user_entered_format is not UNSET:
            field_dict["userEnteredFormat"] = user_entered_format
        if user_entered_value is not UNSET:
            field_dict["userEnteredValue"] = user_entered_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cell_format import CellFormat
        from ..models.data_source_formula import DataSourceFormula
        from ..models.data_source_table import DataSourceTable
        from ..models.data_validation_rule import DataValidationRule
        from ..models.extended_value import ExtendedValue
        from ..models.pivot_table import PivotTable
        from ..models.text_format_run import TextFormatRun
        d = dict(src_dict)
        _data_source_formula = d.pop("dataSourceFormula", UNSET)
        data_source_formula: DataSourceFormula | Unset
        if isinstance(_data_source_formula,  Unset):
            data_source_formula = UNSET
        else:
            data_source_formula = DataSourceFormula.from_dict(_data_source_formula)




        _data_source_table = d.pop("dataSourceTable", UNSET)
        data_source_table: DataSourceTable | Unset
        if isinstance(_data_source_table,  Unset):
            data_source_table = UNSET
        else:
            data_source_table = DataSourceTable.from_dict(_data_source_table)




        _data_validation = d.pop("dataValidation", UNSET)
        data_validation: DataValidationRule | Unset
        if isinstance(_data_validation,  Unset):
            data_validation = UNSET
        else:
            data_validation = DataValidationRule.from_dict(_data_validation)




        _effective_format = d.pop("effectiveFormat", UNSET)
        effective_format: CellFormat | Unset
        if isinstance(_effective_format,  Unset):
            effective_format = UNSET
        else:
            effective_format = CellFormat.from_dict(_effective_format)




        _effective_value = d.pop("effectiveValue", UNSET)
        effective_value: ExtendedValue | Unset
        if isinstance(_effective_value,  Unset):
            effective_value = UNSET
        else:
            effective_value = ExtendedValue.from_dict(_effective_value)




        formatted_value = d.pop("formattedValue", UNSET)

        hyperlink = d.pop("hyperlink", UNSET)

        note = d.pop("note", UNSET)

        _pivot_table = d.pop("pivotTable", UNSET)
        pivot_table: PivotTable | Unset
        if isinstance(_pivot_table,  Unset):
            pivot_table = UNSET
        else:
            pivot_table = PivotTable.from_dict(_pivot_table)




        _text_format_runs = d.pop("textFormatRuns", UNSET)
        text_format_runs: list[TextFormatRun] | Unset = UNSET
        if _text_format_runs is not UNSET:
            text_format_runs = []
            for text_format_runs_item_data in _text_format_runs:
                text_format_runs_item = TextFormatRun.from_dict(text_format_runs_item_data)



                text_format_runs.append(text_format_runs_item)


        _user_entered_format = d.pop("userEnteredFormat", UNSET)
        user_entered_format: CellFormat | Unset
        if isinstance(_user_entered_format,  Unset):
            user_entered_format = UNSET
        else:
            user_entered_format = CellFormat.from_dict(_user_entered_format)




        _user_entered_value = d.pop("userEnteredValue", UNSET)
        user_entered_value: ExtendedValue | Unset
        if isinstance(_user_entered_value,  Unset):
            user_entered_value = UNSET
        else:
            user_entered_value = ExtendedValue.from_dict(_user_entered_value)




        cell_data = cls(
            data_source_formula=data_source_formula,
            data_source_table=data_source_table,
            data_validation=data_validation,
            effective_format=effective_format,
            effective_value=effective_value,
            formatted_value=formatted_value,
            hyperlink=hyperlink,
            note=note,
            pivot_table=pivot_table,
            text_format_runs=text_format_runs,
            user_entered_format=user_entered_format,
            user_entered_value=user_entered_value,
        )


        cell_data.additional_properties = d
        return cell_data

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
