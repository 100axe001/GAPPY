from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.chat_update_chat_update_success_schema_message_object import ChatUpdateChatUpdateSuccessSchemaMessageObject





T = TypeVar("T", bound="ChatUpdateChatUpdateSuccessSchema")



@_attrs_define
class ChatUpdateChatUpdateSuccessSchema:
    """ Schema for successful response of chat.update method

        Attributes:
            channel (str):
            message (ChatUpdateChatUpdateSuccessSchemaMessageObject):
            ok (bool):
            text (str):
            ts (str):
     """

    channel: str
    message: ChatUpdateChatUpdateSuccessSchemaMessageObject
    ok: bool
    text: str
    ts: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_update_chat_update_success_schema_message_object import ChatUpdateChatUpdateSuccessSchemaMessageObject
        channel = self.channel

        message = self.message.to_dict()

        ok = self.ok

        text = self.text

        ts = self.ts


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel": channel,
            "message": message,
            "ok": ok,
            "text": text,
            "ts": ts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_update_chat_update_success_schema_message_object import ChatUpdateChatUpdateSuccessSchemaMessageObject
        d = dict(src_dict)
        channel = d.pop("channel")

        message = ChatUpdateChatUpdateSuccessSchemaMessageObject.from_dict(d.pop("message"))




        ok = d.pop("ok")

        text = d.pop("text")

        ts = d.pop("ts")

        chat_update_chat_update_success_schema = cls(
            channel=channel,
            message=message,
            ok=ok,
            text=text,
            ts=ts,
        )

        return chat_update_chat_update_success_schema

