from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SuggestedIssue")



@_attrs_define
class SuggestedIssue:
    """ An issue suggested for use in the issue picker auto-completion.

        Attributes:
            id (int | Unset): The ID of the issue.
            img (str | Unset): The URL of the issue type's avatar.
            key (str | Unset): The key of the issue.
            key_html (str | Unset): The key of the issue in HTML format.
            summary (str | Unset): The phrase containing the query string in HTML format, with the string highlighted with
                HTML bold tags.
            summary_text (str | Unset): The phrase containing the query string, as plain text.
     """

    id: int | Unset = UNSET
    img: str | Unset = UNSET
    key: str | Unset = UNSET
    key_html: str | Unset = UNSET
    summary: str | Unset = UNSET
    summary_text: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        img = self.img

        key = self.key

        key_html = self.key_html

        summary = self.summary

        summary_text = self.summary_text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if img is not UNSET:
            field_dict["img"] = img
        if key is not UNSET:
            field_dict["key"] = key
        if key_html is not UNSET:
            field_dict["keyHtml"] = key_html
        if summary is not UNSET:
            field_dict["summary"] = summary
        if summary_text is not UNSET:
            field_dict["summaryText"] = summary_text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        img = d.pop("img", UNSET)

        key = d.pop("key", UNSET)

        key_html = d.pop("keyHtml", UNSET)

        summary = d.pop("summary", UNSET)

        summary_text = d.pop("summaryText", UNSET)

        suggested_issue = cls(
            id=id,
            img=img,
            key=key,
            key_html=key_html,
            summary=summary,
            summary_text=summary_text,
        )

        return suggested_issue

