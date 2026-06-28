from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.append_dimension_request_dimension import AppendDimensionRequestDimension
from ..types import UNSET, Unset






T = TypeVar("T", bound="AppendDimensionRequest")



@_attrs_define
class AppendDimensionRequest:
    """ Appends rows or columns to the end of a sheet.

        Attributes:
            dimension (AppendDimensionRequestDimension | Unset): Whether rows or columns should be appended.
            length (int | Unset): The number of rows or columns to append.
            sheet_id (int | Unset): The sheet to append rows or columns to.
     """

    dimension: AppendDimensionRequestDimension | Unset = UNSET
    length: int | Unset = UNSET
    sheet_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dimension: str | Unset = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.value


        length = self.length

        sheet_id = self.sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if length is not UNSET:
            field_dict["length"] = length
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _dimension = d.pop("dimension", UNSET)
        dimension: AppendDimensionRequestDimension | Unset
        if isinstance(_dimension,  Unset):
            dimension = UNSET
        else:
            dimension = AppendDimensionRequestDimension(_dimension)




        length = d.pop("length", UNSET)

        sheet_id = d.pop("sheetId", UNSET)

        append_dimension_request = cls(
            dimension=dimension,
            length=length,
            sheet_id=sheet_id,
        )


        append_dimension_request.additional_properties = d
        return append_dimension_request

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
