from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.function_reference_data_is_list import FunctionReferenceDataIsList
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FunctionReferenceData")



@_attrs_define
class FunctionReferenceData:
    """ Details of functions that can be used in advanced searches.

        Attributes:
            display_name (str | Unset): The display name of the function.
            is_list (FunctionReferenceDataIsList | Unset): Whether the function can take a list of arguments.
            types (list[str] | Unset): The data types returned by the function.
            value (str | Unset): The function identifier.
     """

    display_name: str | Unset = UNSET
    is_list: FunctionReferenceDataIsList | Unset = UNSET
    types: list[str] | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        is_list: str | Unset = UNSET
        if not isinstance(self.is_list, Unset):
            is_list = self.is_list.value


        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = self.types



        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if is_list is not UNSET:
            field_dict["isList"] = is_list
        if types is not UNSET:
            field_dict["types"] = types
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        _is_list = d.pop("isList", UNSET)
        is_list: FunctionReferenceDataIsList | Unset
        if isinstance(_is_list,  Unset):
            is_list = UNSET
        else:
            is_list = FunctionReferenceDataIsList(_is_list)




        types = cast(list[str], d.pop("types", UNSET))


        value = d.pop("value", UNSET)

        function_reference_data = cls(
            display_name=display_name,
            is_list=is_list,
            types=types,
            value=value,
        )

        return function_reference_data

