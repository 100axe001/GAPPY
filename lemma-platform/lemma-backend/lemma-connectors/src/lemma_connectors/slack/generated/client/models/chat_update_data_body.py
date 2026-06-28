from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatUpdateDataBody")



@_attrs_define
class ChatUpdateDataBody:
    """ 
        Attributes:
            channel (str): Channel containing the message to be updated.
            ts (str): Timestamp of the message to be updated.
            as_user (str | Unset): Pass true to update the message as the authed user. [Bot users](/bot-users) in this
                context are considered authed users.
            attachments (str | Unset): A JSON-based array of structured attachments, presented as a URL-encoded string. This
                field is required when not presenting `text`. If you don't include this field, the message's previous
                `attachments` will be retained. To remove previous `attachments`, include an empty array for this field.
            blocks (str | Unset): A JSON-based array of [structured blocks](/block-kit/building), presented as a URL-encoded
                string. If you don't include this field, the message's previous `blocks` will be retained. To remove previous
                `blocks`, include an empty array for this field.
            link_names (str | Unset): Find and link channel names and usernames. Defaults to `none`. If you do not specify a
                value for this field, the original value set for the message will be overwritten with the default, `none`.
            parse (str | Unset): Change how messages are treated. Defaults to `client`, unlike `chat.postMessage`. Accepts
                either `none` or `full`. If you do not specify a value for this field, the original value set for the message
                will be overwritten with the default, `client`.
            text (str | Unset): New text for the message, using the [default formatting
                rules](/reference/surfaces/formatting). It's not required when presenting `blocks` or `attachments`.
     """

    channel: str
    ts: str
    as_user: str | Unset = UNSET
    attachments: str | Unset = UNSET
    blocks: str | Unset = UNSET
    link_names: str | Unset = UNSET
    parse: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ts = self.ts

        as_user = self.as_user

        attachments = self.attachments

        blocks = self.blocks

        link_names = self.link_names

        parse = self.parse

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channel": channel,
            "ts": ts,
        })
        if as_user is not UNSET:
            field_dict["as_user"] = as_user
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if link_names is not UNSET:
            field_dict["link_names"] = link_names
        if parse is not UNSET:
            field_dict["parse"] = parse
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel")

        ts = d.pop("ts")

        as_user = d.pop("as_user", UNSET)

        attachments = d.pop("attachments", UNSET)

        blocks = d.pop("blocks", UNSET)

        link_names = d.pop("link_names", UNSET)

        parse = d.pop("parse", UNSET)

        text = d.pop("text", UNSET)

        chat_update_data_body = cls(
            channel=channel,
            ts=ts,
            as_user=as_user,
            attachments=attachments,
            blocks=blocks,
            link_names=link_names,
            parse=parse,
            text=text,
        )


        chat_update_data_body.additional_properties = d
        return chat_update_data_body

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
