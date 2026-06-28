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





T = TypeVar("T", bound="ListMessagesResponse")



@_attrs_define
class ListMessagesResponse:
    """ 
        Attributes:
            messages (list[Message] | Unset): List of messages. Note that each message resource contains only an `id` and a
                `threadId`. Additional message details can be fetched using the messages.get method.
            next_page_token (str | Unset): Token to retrieve the next page of results in the list.
            result_size_estimate (int | Unset): Estimated total number of results.
     """

    messages: list[Message] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    result_size_estimate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.message import Message
        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)



        next_page_token = self.next_page_token

        result_size_estimate = self.result_size_estimate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if messages is not UNSET:
            field_dict["messages"] = messages
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if result_size_estimate is not UNSET:
            field_dict["resultSizeEstimate"] = result_size_estimate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message
        d = dict(src_dict)
        _messages = d.pop("messages", UNSET)
        messages: list[Message] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = Message.from_dict(messages_item_data)



                messages.append(messages_item)


        next_page_token = d.pop("nextPageToken", UNSET)

        result_size_estimate = d.pop("resultSizeEstimate", UNSET)

        list_messages_response = cls(
            messages=messages,
            next_page_token=next_page_token,
            result_size_estimate=result_size_estimate,
        )


        list_messages_response.additional_properties = d
        return list_messages_response

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
