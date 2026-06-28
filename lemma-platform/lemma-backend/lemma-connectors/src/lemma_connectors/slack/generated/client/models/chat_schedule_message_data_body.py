from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatScheduleMessageDataBody")



@_attrs_define
class ChatScheduleMessageDataBody:
    """ 
        Attributes:
            channel (str | Unset): Channel, private group, or DM channel to send message to. Can be an encoded ID, or a
                name. See [below](#channels) for more details.
            text (str | Unset): How this field works and whether it is required depends on other fields you use in your API
                call. [See below](#text_usage) for more detail.
            post_at (str | Unset): Unix EPOCH timestamp of time in future to send the message.
            parse (str | Unset): Change how messages are treated. Defaults to `none`. See
                [chat.postMessage](chat.postMessage#formatting).
            as_user (bool | Unset): Pass true to post the message as the authed user, instead of as a bot. Defaults to
                false. See [chat.postMessage](chat.postMessage#authorship).
            link_names (bool | Unset): Find and link channel names and usernames.
            attachments (str | Unset): A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks (str | Unset): A JSON-based array of structured blocks, presented as a URL-encoded string.
            unfurl_links (bool | Unset): Pass true to enable unfurling of primarily text-based content.
            unfurl_media (bool | Unset): Pass false to disable unfurling of media content.
            thread_ts (float | Unset): Provide another message's `ts` value to make this message a reply. Avoid using a
                reply's `ts` value; use its parent instead.
            reply_broadcast (bool | Unset): Used in conjunction with `thread_ts` and indicates whether reply should be made
                visible to everyone in the channel or conversation. Defaults to `false`.
     """

    channel: str | Unset = UNSET
    text: str | Unset = UNSET
    post_at: str | Unset = UNSET
    parse: str | Unset = UNSET
    as_user: bool | Unset = UNSET
    link_names: bool | Unset = UNSET
    attachments: str | Unset = UNSET
    blocks: str | Unset = UNSET
    unfurl_links: bool | Unset = UNSET
    unfurl_media: bool | Unset = UNSET
    thread_ts: float | Unset = UNSET
    reply_broadcast: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        text = self.text

        post_at = self.post_at

        parse = self.parse

        as_user = self.as_user

        link_names = self.link_names

        attachments = self.attachments

        blocks = self.blocks

        unfurl_links = self.unfurl_links

        unfurl_media = self.unfurl_media

        thread_ts = self.thread_ts

        reply_broadcast = self.reply_broadcast


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if text is not UNSET:
            field_dict["text"] = text
        if post_at is not UNSET:
            field_dict["post_at"] = post_at
        if parse is not UNSET:
            field_dict["parse"] = parse
        if as_user is not UNSET:
            field_dict["as_user"] = as_user
        if link_names is not UNSET:
            field_dict["link_names"] = link_names
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if unfurl_links is not UNSET:
            field_dict["unfurl_links"] = unfurl_links
        if unfurl_media is not UNSET:
            field_dict["unfurl_media"] = unfurl_media
        if thread_ts is not UNSET:
            field_dict["thread_ts"] = thread_ts
        if reply_broadcast is not UNSET:
            field_dict["reply_broadcast"] = reply_broadcast

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        text = d.pop("text", UNSET)

        post_at = d.pop("post_at", UNSET)

        parse = d.pop("parse", UNSET)

        as_user = d.pop("as_user", UNSET)

        link_names = d.pop("link_names", UNSET)

        attachments = d.pop("attachments", UNSET)

        blocks = d.pop("blocks", UNSET)

        unfurl_links = d.pop("unfurl_links", UNSET)

        unfurl_media = d.pop("unfurl_media", UNSET)

        thread_ts = d.pop("thread_ts", UNSET)

        reply_broadcast = d.pop("reply_broadcast", UNSET)

        chat_schedule_message_data_body = cls(
            channel=channel,
            text=text,
            post_at=post_at,
            parse=parse,
            as_user=as_user,
            link_names=link_names,
            attachments=attachments,
            blocks=blocks,
            unfurl_links=unfurl_links,
            unfurl_media=unfurl_media,
            thread_ts=thread_ts,
            reply_broadcast=reply_broadcast,
        )


        chat_schedule_message_data_body.additional_properties = d
        return chat_schedule_message_data_body

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
