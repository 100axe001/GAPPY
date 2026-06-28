from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ChatScheduledMessagesListChatScheduledMessagesListSchemaResponseMetadata")



@_attrs_define
class ChatScheduledMessagesListChatScheduledMessagesListSchemaResponseMetadata:
    """ 
        Attributes:
            next_cursor (str):
     """

    next_cursor: str





    def to_dict(self) -> dict[str, Any]:
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "next_cursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_cursor = d.pop("next_cursor")

        chat_scheduled_messages_list_chat_scheduled_messages_list_schema_response_metadata = cls(
            next_cursor=next_cursor,
        )

        return chat_scheduled_messages_list_chat_scheduled_messages_list_schema_response_metadata

