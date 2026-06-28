from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.message_object import MessageObject





T = TypeVar("T", bound="ConversationsHistoryConversationsHistorySuccessSchema")



@_attrs_define
class ConversationsHistoryConversationsHistorySuccessSchema:
    """ Schema for successful response from conversations.history method

        Attributes:
            channel_actions_count (int):
            channel_actions_ts (Any):
            has_more (bool):
            messages (list[MessageObject]):
            ok (bool):
            pin_count (int):
     """

    channel_actions_count: int
    channel_actions_ts: Any
    has_more: bool
    messages: list[MessageObject]
    ok: bool
    pin_count: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.message_object import MessageObject
        channel_actions_count = self.channel_actions_count

        channel_actions_ts = self.channel_actions_ts

        has_more = self.has_more

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)



        ok = self.ok

        pin_count = self.pin_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel_actions_count": channel_actions_count,
            "channel_actions_ts": channel_actions_ts,
            "has_more": has_more,
            "messages": messages,
            "ok": ok,
            "pin_count": pin_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_object import MessageObject
        d = dict(src_dict)
        channel_actions_count = d.pop("channel_actions_count")

        channel_actions_ts = d.pop("channel_actions_ts")

        has_more = d.pop("has_more")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in (_messages):
            messages_item = MessageObject.from_dict(messages_item_data)



            messages.append(messages_item)


        ok = d.pop("ok")

        pin_count = d.pop("pin_count")

        conversations_history_conversations_history_success_schema = cls(
            channel_actions_count=channel_actions_count,
            channel_actions_ts=channel_actions_ts,
            has_more=has_more,
            messages=messages,
            ok=ok,
            pin_count=pin_count,
        )

        return conversations_history_conversations_history_success_schema

