from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.keyword_operand_keyword import KeywordOperandKeyword






T = TypeVar("T", bound="KeywordOperand")



@_attrs_define
class KeywordOperand:
    """ An operand that is a JQL keyword. See [Advanced searching - keywords
    reference](https://confluence.atlassian.com/jiracorecloud/advanced-searching-keywords-
    reference-765593717.html#Advancedsearching-keywordsreference-EMPTYEMPTY) for more information about operand
    keywords.

        Attributes:
            keyword (KeywordOperandKeyword): The keyword that is the operand value.
     """

    keyword: KeywordOperandKeyword
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "keyword": keyword,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keyword = KeywordOperandKeyword(d.pop("keyword"))




        keyword_operand = cls(
            keyword=keyword,
        )


        keyword_operand.additional_properties = d
        return keyword_operand

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
