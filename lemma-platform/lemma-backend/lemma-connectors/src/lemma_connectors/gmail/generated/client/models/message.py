from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.message_part import MessagePart





T = TypeVar("T", bound="Message")



@_attrs_define
class Message:
    """ An email message.

        Attributes:
            history_id (str | Unset): The ID of the last history record that modified this message.
            id (str | Unset): The immutable ID of the message.
            internal_date (str | Unset): The internal message creation timestamp (epoch ms), which determines ordering in
                the inbox. For normal SMTP-received email, this represents the time the message was originally accepted by
                Google, which is more reliable than the `Date` header. However, for API-migrated mail, it can be configured by
                client to be based on the `Date` header.
            label_ids (list[str] | Unset): List of IDs of labels applied to this message.
            payload (MessagePart | Unset): A single MIME message part.
            raw (str | Unset): The entire email message in an RFC 2822 formatted and base64url encoded string. Returned in
                `messages.get` and `drafts.get` responses when the `format=RAW` parameter is supplied.
            size_estimate (int | Unset): Estimated size in bytes of the message.
            snippet (str | Unset): A short part of the message text.
            thread_id (str | Unset): The ID of the thread the message belongs to. To add a message or draft to a thread, the
                following criteria must be met: 1. The requested `threadId` must be specified on the `Message` or
                `Draft.Message` you supply with your request. 2. The `References` and `In-Reply-To` headers must be set in
                compliance with the [RFC 2822](https://tools.ietf.org/html/rfc2822) standard. 3. The `Subject` headers must
                match.
     """

    history_id: str | Unset = UNSET
    id: str | Unset = UNSET
    internal_date: str | Unset = UNSET
    label_ids: list[str] | Unset = UNSET
    payload: MessagePart | Unset = UNSET
    raw: str | Unset = UNSET
    size_estimate: int | Unset = UNSET
    snippet: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.message_part import MessagePart
        history_id = self.history_id

        id = self.id

        internal_date = self.internal_date

        label_ids: list[str] | Unset = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids



        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        raw = self.raw

        size_estimate = self.size_estimate

        snippet = self.snippet

        thread_id = self.thread_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if history_id is not UNSET:
            field_dict["historyId"] = history_id
        if id is not UNSET:
            field_dict["id"] = id
        if internal_date is not UNSET:
            field_dict["internalDate"] = internal_date
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if payload is not UNSET:
            field_dict["payload"] = payload
        if raw is not UNSET:
            field_dict["raw"] = raw
        if size_estimate is not UNSET:
            field_dict["sizeEstimate"] = size_estimate
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_part import MessagePart
        d = dict(src_dict)
        history_id = d.pop("historyId", UNSET)

        id = d.pop("id", UNSET)

        internal_date = d.pop("internalDate", UNSET)

        label_ids = cast(list[str], d.pop("labelIds", UNSET))


        _payload = d.pop("payload", UNSET)
        payload: MessagePart | Unset
        if isinstance(_payload,  Unset):
            payload = UNSET
        else:
            payload = MessagePart.from_dict(_payload)




        raw = d.pop("raw", UNSET)

        size_estimate = d.pop("sizeEstimate", UNSET)

        snippet = d.pop("snippet", UNSET)

        thread_id = d.pop("threadId", UNSET)

        message = cls(
            history_id=history_id,
            id=id,
            internal_date=internal_date,
            label_ids=label_ids,
            payload=payload,
            raw=raw,
            size_estimate=size_estimate,
            snippet=snippet,
            thread_id=thread_id,
        )


        message.additional_properties = d
        return message

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
