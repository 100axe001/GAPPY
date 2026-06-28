from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatScheduledMessagesListChatScheduledMessagesListSchemaScheduledMessagesItem")



@_attrs_define
class ChatScheduledMessagesListChatScheduledMessagesListSchemaScheduledMessagesItem:
    """ 
        Attributes:
            channel_id (str):
            date_created (int):
            id (str):
            post_at (int):
            text (str | Unset):
     """

    channel_id: str
    date_created: int
    id: str
    post_at: int
    text: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        date_created = self.date_created

        id = self.id

        post_at = self.post_at

        text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel_id": channel_id,
            "date_created": date_created,
            "id": id,
            "post_at": post_at,
        })
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        date_created = d.pop("date_created")

        id = d.pop("id")

        post_at = d.pop("post_at")

        text = d.pop("text", UNSET)

        chat_scheduled_messages_list_chat_scheduled_messages_list_schema_scheduled_messages_item = cls(
            channel_id=channel_id,
            date_created=date_created,
            id=id,
            post_at=post_at,
            text=text,
        )

        return chat_scheduled_messages_list_chat_scheduled_messages_list_schema_scheduled_messages_item

