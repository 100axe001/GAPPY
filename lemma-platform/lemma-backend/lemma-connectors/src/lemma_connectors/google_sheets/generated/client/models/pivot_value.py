from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pivot_value_calculated_display_type import PivotValueCalculatedDisplayType
from ..models.pivot_value_summarize_function import PivotValueSummarizeFunction
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_column_reference import DataSourceColumnReference





T = TypeVar("T", bound="PivotValue")



@_attrs_define
class PivotValue:
    """ The definition of how a value in a pivot table should be calculated.

        Attributes:
            calculated_display_type (PivotValueCalculatedDisplayType | Unset): If specified, indicates that pivot values
                should be displayed as the result of a calculation with another pivot value. For example, if
                calculated_display_type is specified as PERCENT_OF_GRAND_TOTAL, all the pivot values are displayed as the
                percentage of the grand total. In the Sheets editor, this is referred to as "Show As" in the value section of a
                pivot table.
            data_source_column_reference (DataSourceColumnReference | Unset): An unique identifier that references a data
                source column.
            formula (str | Unset): A custom formula to calculate the value. The formula must start with an `=` character.
            name (str | Unset): A name to use for the value.
            source_column_offset (int | Unset): The column offset of the source range that this value reads from. For
                example, if the source was `C10:E15`, a `sourceColumnOffset` of `0` means this value refers to column `C`,
                whereas the offset `1` would refer to column `D`.
            summarize_function (PivotValueSummarizeFunction | Unset): A function to summarize the value. If formula is set,
                the only supported values are SUM and CUSTOM. If sourceColumnOffset is set, then `CUSTOM` is not supported.
     """

    calculated_display_type: PivotValueCalculatedDisplayType | Unset = UNSET
    data_source_column_reference: DataSourceColumnReference | Unset = UNSET
    formula: str | Unset = UNSET
    name: str | Unset = UNSET
    source_column_offset: int | Unset = UNSET
    summarize_function: PivotValueSummarizeFunction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_column_reference import DataSourceColumnReference
        calculated_display_type: str | Unset = UNSET
        if not isinstance(self.calculated_display_type, Unset):
            calculated_display_type = self.calculated_display_type.value


        data_source_column_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_column_reference, Unset):
            data_source_column_reference = self.data_source_column_reference.to_dict()

        formula = self.formula

        name = self.name

        source_column_offset = self.source_column_offset

        summarize_function: str | Unset = UNSET
        if not isinstance(self.summarize_function, Unset):
            summarize_function = self.summarize_function.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if calculated_display_type is not UNSET:
            field_dict["calculatedDisplayType"] = calculated_display_type
        if data_source_column_reference is not UNSET:
            field_dict["dataSourceColumnReference"] = data_source_column_reference
        if formula is not UNSET:
            field_dict["formula"] = formula
        if name is not UNSET:
            field_dict["name"] = name
        if source_column_offset is not UNSET:
            field_dict["sourceColumnOffset"] = source_column_offset
        if summarize_function is not UNSET:
            field_dict["summarizeFunction"] = summarize_function

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_column_reference import DataSourceColumnReference
        d = dict(src_dict)
        _calculated_display_type = d.pop("calculatedDisplayType", UNSET)
        calculated_display_type: PivotValueCalculatedDisplayType | Unset
        if isinstance(_calculated_display_type,  Unset):
            calculated_display_type = UNSET
        else:
            calculated_display_type = PivotValueCalculatedDisplayType(_calculated_display_type)




        _data_source_column_reference = d.pop("dataSourceColumnReference", UNSET)
        data_source_column_reference: DataSourceColumnReference | Unset
        if isinstance(_data_source_column_reference,  Unset):
            data_source_column_reference = UNSET
        else:
            data_source_column_reference = DataSourceColumnReference.from_dict(_data_source_column_reference)




        formula = d.pop("formula", UNSET)

        name = d.pop("name", UNSET)

        source_column_offset = d.pop("sourceColumnOffset", UNSET)

        _summarize_function = d.pop("summarizeFunction", UNSET)
        summarize_function: PivotValueSummarizeFunction | Unset
        if isinstance(_summarize_function,  Unset):
            summarize_function = UNSET
        else:
            summarize_function = PivotValueSummarizeFunction(_summarize_function)




        pivot_value = cls(
            calculated_display_type=calculated_display_type,
            data_source_column_reference=data_source_column_reference,
            formula=formula,
            name=name,
            source_column_offset=source_column_offset,
            summarize_function=summarize_function,
        )


        pivot_value.additional_properties = d
        return pivot_value

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
