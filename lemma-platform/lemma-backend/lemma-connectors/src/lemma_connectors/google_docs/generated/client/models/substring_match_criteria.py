from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubstringMatchCriteria")



@_attrs_define
class SubstringMatchCriteria:
    """ A criteria that matches a specific string of text in the document.

        Attributes:
            match_case (bool | Unset): Indicates whether the search should respect case: - `True`: the search is case
                sensitive. - `False`: the search is case insensitive.
            text (str | Unset): The text to search for in the document.
     """

    match_case: bool | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        match_case = self.match_case

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if match_case is not UNSET:
            field_dict["matchCase"] = match_case
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match_case = d.pop("matchCase", UNSET)

        text = d.pop("text", UNSET)

        substring_match_criteria = cls(
            match_case=match_case,
            text=text,
        )


        substring_match_criteria.additional_properties = d
        return substring_match_criteria

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
