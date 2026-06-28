from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.message import Message





T = TypeVar("T", bound="Thread")



@_attrs_define
class Thread:
    """ A collection of messages representing a conversation.

        Attributes:
            history_id (str | Unset): The ID of the last history record that modified this thread.
            id (str | Unset): The unique ID of the thread.
            messages (list[Message] | Unset): The list of messages in the thread.
            snippet (str | Unset): A short part of the message text.
     """

    history_id: str | Unset = UNSET
    id: str | Unset = UNSET
    messages: list[Message] | Unset = UNSET
    snippet: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.message import Message
        history_id = self.history_id

        id = self.id

        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)



        snippet = self.snippet


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if history_id is not UNSET:
            field_dict["historyId"] = history_id
        if id is not UNSET:
            field_dict["id"] = id
        if messages is not UNSET:
            field_dict["messages"] = messages
        if snippet is not UNSET:
            field_dict["snippet"] = snippet

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message
        d = dict(src_dict)
        history_id = d.pop("historyId", UNSET)

        id = d.pop("id", UNSET)

        _messages = d.pop("messages", UNSET)
        messages: list[Message] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = Message.from_dict(messages_item_data)



                messages.append(messages_item)


        snippet = d.pop("snippet", UNSET)

        thread = cls(
            history_id=history_id,
            id=id,
            messages=messages,
            snippet=snippet,
        )


        thread.additional_properties = d
        return thread

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
