from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.message_object import MessageObject





T = TypeVar("T", bound="ChatPostMessageChatPostMessageSuccessSchema")



@_attrs_define
class ChatPostMessageChatPostMessageSuccessSchema:
    """ Schema for successful response of chat.postMessage method

        Attributes:
            channel (str):
            message (MessageObject):
            ok (bool):
            ts (str):
     """

    channel: str
    message: MessageObject
    ok: bool
    ts: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.message_object import MessageObject
        channel = self.channel

        message = self.message.to_dict()

        ok = self.ok

        ts = self.ts


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel": channel,
            "message": message,
            "ok": ok,
            "ts": ts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_object import MessageObject
        d = dict(src_dict)
        channel = d.pop("channel")

        message = MessageObject.from_dict(d.pop("message"))




        ok = d.pop("ok")

        ts = d.pop("ts")

        chat_post_message_chat_post_message_success_schema = cls(
            channel=channel,
            message=message,
            ok=ok,
            ts=ts,
        )

        return chat_post_message_chat_post_message_success_schema

