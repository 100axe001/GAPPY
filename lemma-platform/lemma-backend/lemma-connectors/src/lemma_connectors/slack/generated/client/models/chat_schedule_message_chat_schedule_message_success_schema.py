from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.chat_schedule_message_chat_schedule_message_success_schema_message import ChatScheduleMessageChatScheduleMessageSuccessSchemaMessage





T = TypeVar("T", bound="ChatScheduleMessageChatScheduleMessageSuccessSchema")



@_attrs_define
class ChatScheduleMessageChatScheduleMessageSuccessSchema:
    """ Schema for successful response of chat.scheduleMessage method

        Attributes:
            channel (str):
            message (ChatScheduleMessageChatScheduleMessageSuccessSchemaMessage):
            ok (bool):
            post_at (int):
            scheduled_message_id (str):
     """

    channel: str
    message: ChatScheduleMessageChatScheduleMessageSuccessSchemaMessage
    ok: bool
    post_at: int
    scheduled_message_id: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_schedule_message_chat_schedule_message_success_schema_message import ChatScheduleMessageChatScheduleMessageSuccessSchemaMessage
        channel = self.channel

        message = self.message.to_dict()

        ok = self.ok

        post_at = self.post_at

        scheduled_message_id = self.scheduled_message_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel": channel,
            "message": message,
            "ok": ok,
            "post_at": post_at,
            "scheduled_message_id": scheduled_message_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_schedule_message_chat_schedule_message_success_schema_message import ChatScheduleMessageChatScheduleMessageSuccessSchemaMessage
        d = dict(src_dict)
        channel = d.pop("channel")

        message = ChatScheduleMessageChatScheduleMessageSuccessSchemaMessage.from_dict(d.pop("message"))




        ok = d.pop("ok")

        post_at = d.pop("post_at")

        scheduled_message_id = d.pop("scheduled_message_id")

        chat_schedule_message_chat_schedule_message_success_schema = cls(
            channel=channel,
            message=message,
            ok=ok,
            post_at=post_at,
            scheduled_message_id=scheduled_message_id,
        )

        return chat_schedule_message_chat_schedule_message_success_schema

