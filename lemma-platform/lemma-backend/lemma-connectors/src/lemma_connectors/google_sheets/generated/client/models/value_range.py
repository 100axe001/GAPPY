from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.value_range_major_dimension import ValueRangeMajorDimension
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ValueRange")



@_attrs_define
class ValueRange:
    """ Data within a range of the spreadsheet.

        Attributes:
            major_dimension (ValueRangeMajorDimension | Unset): The major dimension of the values. For output, if the
                spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`, then requesting `range=A1:B2,majorDimension=ROWS` will return
                `[[1,2],[3,4]]`, whereas requesting `range=A1:B2,majorDimension=COLUMNS` will return `[[1,3],[2,4]]`. For input,
                with `range=A1:B2,majorDimension=ROWS` then `[[1,2],[3,4]]` will set `A1=1,B1=2,A2=3,B2=4`. With
                `range=A1:B2,majorDimension=COLUMNS` then `[[1,2],[3,4]]` will set `A1=1,B1=3,A2=2,B2=4`. When writing, if this
                field is not set, it defaults to ROWS.
            range_ (str | Unset): The range the values cover, in [A1 notation](/sheets/api/guides/concepts#cell). For
                output, this range indicates the entire requested range, even though the values will exclude trailing rows and
                columns. When appending values, this field represents the range to search for a table, after which values will
                be appended.
            values (list[list[Any]] | Unset): The data that was read or to be written. This is an array of arrays, the outer
                array representing all the data and each inner array representing a major dimension. Each item in the inner
                array corresponds with one cell. For output, empty trailing rows and columns will not be included. For input,
                supported value types are: bool, string, and double. Null values will be skipped. To set a cell to an empty
                value, set the string value to an empty string.
     """

    major_dimension: ValueRangeMajorDimension | Unset = UNSET
    range_: str | Unset = UNSET
    values: list[list[Any]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        major_dimension: str | Unset = UNSET
        if not isinstance(self.major_dimension, Unset):
            major_dimension = self.major_dimension.value


        range_ = self.range_

        values: list[list[Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data


                values.append(values_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if major_dimension is not UNSET:
            field_dict["majorDimension"] = major_dimension
        if range_ is not UNSET:
            field_dict["range"] = range_
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _major_dimension = d.pop("majorDimension", UNSET)
        major_dimension: ValueRangeMajorDimension | Unset
        if isinstance(_major_dimension,  Unset):
            major_dimension = UNSET
        else:
            major_dimension = ValueRangeMajorDimension(_major_dimension)




        range_ = d.pop("range", UNSET)

        _values = d.pop("values", UNSET)
        values: list[list[Any]] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = cast(list[Any], values_item_data)

                values.append(values_item)


        value_range = cls(
            major_dimension=major_dimension,
            range_=range_,
            values=values,
        )


        value_range.additional_properties = d
        return value_range

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
