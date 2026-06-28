from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ChatDeleteChatDeleteSuccessSchema")



@_attrs_define
class ChatDeleteChatDeleteSuccessSchema:
    """ Schema for successful response of chat.delete method

        Attributes:
            channel (str):
            ok (bool):
            ts (str):
     """

    channel: str
    ok: bool
    ts: str





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ok = self.ok

        ts = self.ts


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel": channel,
            "ok": ok,
            "ts": ts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel")

        ok = d.pop("ok")

        ts = d.pop("ts")

        chat_delete_chat_delete_success_schema = cls(
            channel=channel,
            ok=ok,
            ts=ts,
        )

        return chat_delete_chat_delete_success_schema

