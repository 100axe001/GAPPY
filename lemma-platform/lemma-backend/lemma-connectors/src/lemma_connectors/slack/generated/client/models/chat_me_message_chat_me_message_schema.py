from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatMeMessageChatMeMessageSchema")



@_attrs_define
class ChatMeMessageChatMeMessageSchema:
    """ Schema for successful response from chat.meMessage method

        Attributes:
            ok (bool):
            channel (str | Unset):
            ts (str | Unset):
     """

    ok: bool
    channel: str | Unset = UNSET
    ts: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        channel = self.channel

        ts = self.ts


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        channel = d.pop("channel", UNSET)

        ts = d.pop("ts", UNSET)

        chat_me_message_chat_me_message_schema = cls(
            ok=ok,
            channel=channel,
            ts=ts,
        )

        return chat_me_message_chat_me_message_schema

