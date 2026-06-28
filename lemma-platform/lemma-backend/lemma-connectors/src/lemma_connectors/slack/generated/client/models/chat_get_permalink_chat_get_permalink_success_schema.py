from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ChatGetPermalinkChatGetPermalinkSuccessSchema")



@_attrs_define
class ChatGetPermalinkChatGetPermalinkSuccessSchema:
    """ Schema for successful response chat.getPermalink

        Attributes:
            channel (str):
            ok (bool):
            permalink (str):
     """

    channel: str
    ok: bool
    permalink: str





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ok = self.ok

        permalink = self.permalink


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel": channel,
            "ok": ok,
            "permalink": permalink,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel")

        ok = d.pop("ok")

        permalink = d.pop("permalink")

        chat_get_permalink_chat_get_permalink_success_schema = cls(
            channel=channel,
            ok=ok,
            permalink=permalink,
        )

        return chat_get_permalink_chat_get_permalink_success_schema

