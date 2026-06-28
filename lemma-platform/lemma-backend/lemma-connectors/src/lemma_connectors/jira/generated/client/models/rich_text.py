from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RichText")



@_attrs_define
class RichText:
    """ 
        Attributes:
            empty (bool | Unset):
            empty_adf (bool | Unset):
            finalised (bool | Unset):
            value_set (bool | Unset):
     """

    empty: bool | Unset = UNSET
    empty_adf: bool | Unset = UNSET
    finalised: bool | Unset = UNSET
    value_set: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        empty = self.empty

        empty_adf = self.empty_adf

        finalised = self.finalised

        value_set = self.value_set


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if empty is not UNSET:
            field_dict["empty"] = empty
        if empty_adf is not UNSET:
            field_dict["emptyAdf"] = empty_adf
        if finalised is not UNSET:
            field_dict["finalised"] = finalised
        if value_set is not UNSET:
            field_dict["valueSet"] = value_set

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        empty = d.pop("empty", UNSET)

        empty_adf = d.pop("emptyAdf", UNSET)

        finalised = d.pop("finalised", UNSET)

        value_set = d.pop("valueSet", UNSET)

        rich_text = cls(
            empty=empty,
            empty_adf=empty_adf,
            finalised=finalised,
            value_set=value_set,
        )


        rich_text.additional_properties = d
        return rich_text

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
