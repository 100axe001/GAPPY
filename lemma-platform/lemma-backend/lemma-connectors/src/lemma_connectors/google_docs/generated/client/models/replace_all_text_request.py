from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.substring_match_criteria import SubstringMatchCriteria





T = TypeVar("T", bound="ReplaceAllTextRequest")



@_attrs_define
class ReplaceAllTextRequest:
    """ Replaces all instances of text matching a criteria with replace text.

        Attributes:
            contains_text (SubstringMatchCriteria | Unset): A criteria that matches a specific string of text in the
                document.
            replace_text (str | Unset): The text that will replace the matched text.
     """

    contains_text: SubstringMatchCriteria | Unset = UNSET
    replace_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.substring_match_criteria import SubstringMatchCriteria
        contains_text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contains_text, Unset):
            contains_text = self.contains_text.to_dict()

        replace_text = self.replace_text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if contains_text is not UNSET:
            field_dict["containsText"] = contains_text
        if replace_text is not UNSET:
            field_dict["replaceText"] = replace_text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.substring_match_criteria import SubstringMatchCriteria
        d = dict(src_dict)
        _contains_text = d.pop("containsText", UNSET)
        contains_text: SubstringMatchCriteria | Unset
        if isinstance(_contains_text,  Unset):
            contains_text = UNSET
        else:
            contains_text = SubstringMatchCriteria.from_dict(_contains_text)




        replace_text = d.pop("replaceText", UNSET)

        replace_all_text_request = cls(
            contains_text=contains_text,
            replace_text=replace_text,
        )


        replace_all_text_request.additional_properties = d
        return replace_all_text_request

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
