from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="LanguageSettings")



@_attrs_define
class LanguageSettings:
    """ Language settings for an account. These settings correspond to the "Language settings" feature in the web interface.

        Attributes:
            display_language (str | Unset): The language to display Gmail in, formatted as an RFC 3066 Language Tag (for
                example `en-GB`, `fr` or `ja` for British English, French, or Japanese respectively). The set of languages
                supported by Gmail evolves over time, so please refer to the "Language" dropdown in the Gmail settings for all
                available options, as described in the language settings help article. A table of sample values is also provided
                in the Managing Language Settings guide Not all Gmail clients can display the same set of languages. In the case
                that a user's display language is not available for use on a particular client, said client automatically
                chooses to display in the closest supported variant (or a reasonable default).
     """

    display_language: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_language = self.display_language


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_language is not UNSET:
            field_dict["displayLanguage"] = display_language

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_language = d.pop("displayLanguage", UNSET)

        language_settings = cls(
            display_language=display_language,
        )


        language_settings.additional_properties = d
        return language_settings

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
