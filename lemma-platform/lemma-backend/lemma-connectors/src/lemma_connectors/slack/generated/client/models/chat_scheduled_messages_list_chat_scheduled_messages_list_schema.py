from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.chat_scheduled_messages_list_chat_scheduled_messages_list_schema_response_metadata import ChatScheduledMessagesListChatScheduledMessagesListSchemaResponseMetadata
  from ..models.chat_scheduled_messages_list_chat_scheduled_messages_list_schema_scheduled_messages_item import ChatScheduledMessagesListChatScheduledMessagesListSchemaScheduledMessagesItem





T = TypeVar("T", bound="ChatScheduledMessagesListChatScheduledMessagesListSchema")



@_attrs_define
class ChatScheduledMessagesListChatScheduledMessagesListSchema:
    """ Schema for successful response from chat.scheduledMessages.list method

        Attributes:
            ok (bool):
            response_metadata (ChatScheduledMessagesListChatScheduledMessagesListSchemaResponseMetadata):
            scheduled_messages (list[ChatScheduledMessagesListChatScheduledMessagesListSchemaScheduledMessagesItem]):
     """

    ok: bool
    response_metadata: ChatScheduledMessagesListChatScheduledMessagesListSchemaResponseMetadata
    scheduled_messages: list[ChatScheduledMessagesListChatScheduledMessagesListSchemaScheduledMessagesItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_scheduled_messages_list_chat_scheduled_messages_list_schema_response_metadata import ChatScheduledMessagesListChatScheduledMessagesListSchemaResponseMetadata
        from ..models.chat_scheduled_messages_list_chat_scheduled_messages_list_schema_scheduled_messages_item import ChatScheduledMessagesListChatScheduledMessagesListSchemaScheduledMessagesItem
        ok = self.ok

        response_metadata = self.response_metadata.to_dict()

        scheduled_messages = []
        for scheduled_messages_item_data in self.scheduled_messages:
            scheduled_messages_item = scheduled_messages_item_data.to_dict()
            scheduled_messages.append(scheduled_messages_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "response_metadata": response_metadata,
            "scheduled_messages": scheduled_messages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_scheduled_messages_list_chat_scheduled_messages_list_schema_response_metadata import ChatScheduledMessagesListChatScheduledMessagesListSchemaResponseMetadata
        from ..models.chat_scheduled_messages_list_chat_scheduled_messages_list_schema_scheduled_messages_item import ChatScheduledMessagesListChatScheduledMessagesListSchemaScheduledMessagesItem
        d = dict(src_dict)
        ok = d.pop("ok")

        response_metadata = ChatScheduledMessagesListChatScheduledMessagesListSchemaResponseMetadata.from_dict(d.pop("response_metadata"))




        scheduled_messages = []
        _scheduled_messages = d.pop("scheduled_messages")
        for scheduled_messages_item_data in (_scheduled_messages):
            scheduled_messages_item = ChatScheduledMessagesListChatScheduledMessagesListSchemaScheduledMessagesItem.from_dict(scheduled_messages_item_data)



            scheduled_messages.append(scheduled_messages_item)


        chat_scheduled_messages_list_chat_scheduled_messages_list_schema = cls(
            ok=ok,
            response_metadata=response_metadata,
            scheduled_messages=scheduled_messages,
        )

        return chat_scheduled_messages_list_chat_scheduled_messages_list_schema

