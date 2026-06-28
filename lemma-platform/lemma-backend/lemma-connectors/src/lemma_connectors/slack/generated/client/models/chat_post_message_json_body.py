from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatPostMessageJsonBody")



@_attrs_define
class ChatPostMessageJsonBody:
    """ 
        Attributes:
            channel (str): Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See
                [below](#channels) for more details.
            as_user (str | Unset): Pass true to post the message as the authed user, instead of as a bot. Defaults to false.
                See [authorship](#authorship) below.
            attachments (str | Unset): A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks (str | Unset): A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji (str | Unset): Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in
                conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](#authorship) below.
            icon_url (str | Unset): URL to an image to use as the icon for this message. Must be used in conjunction with
                `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.
            link_names (bool | Unset): Find and link channel names and usernames.
            mrkdwn (bool | Unset): Disable Slack markup parsing by setting to `false`. Enabled by default.
            parse (str | Unset): Change how messages are treated. Defaults to `none`. See [below](#formatting).
            reply_broadcast (bool | Unset): Used in conjunction with `thread_ts` and indicates whether reply should be made
                visible to everyone in the channel or conversation. Defaults to `false`.
            text (str | Unset): How this field works and whether it is required depends on other fields you use in your API
                call. [See below](#text_usage) for more detail.
            thread_ts (str | Unset): Provide another message's `ts` value to make this message a reply. Avoid using a
                reply's `ts` value; use its parent instead.
            unfurl_links (bool | Unset): Pass true to enable unfurling of primarily text-based content.
            unfurl_media (bool | Unset): Pass false to disable unfurling of media content.
            username (str | Unset): Set your bot's user name. Must be used in conjunction with `as_user` set to false,
                otherwise ignored. See [authorship](#authorship) below.
     """

    channel: str
    as_user: str | Unset = UNSET
    attachments: str | Unset = UNSET
    blocks: str | Unset = UNSET
    icon_emoji: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    link_names: bool | Unset = UNSET
    mrkdwn: bool | Unset = UNSET
    parse: str | Unset = UNSET
    reply_broadcast: bool | Unset = UNSET
    text: str | Unset = UNSET
    thread_ts: str | Unset = UNSET
    unfurl_links: bool | Unset = UNSET
    unfurl_media: bool | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        as_user = self.as_user

        attachments = self.attachments

        blocks = self.blocks

        icon_emoji = self.icon_emoji

        icon_url = self.icon_url

        link_names = self.link_names

        mrkdwn = self.mrkdwn

        parse = self.parse

        reply_broadcast = self.reply_broadcast

        text = self.text

        thread_ts = self.thread_ts

        unfurl_links = self.unfurl_links

        unfurl_media = self.unfurl_media

        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channel": channel,
        })
        if as_user is not UNSET:
            field_dict["as_user"] = as_user
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if icon_emoji is not UNSET:
            field_dict["icon_emoji"] = icon_emoji
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if link_names is not UNSET:
            field_dict["link_names"] = link_names
        if mrkdwn is not UNSET:
            field_dict["mrkdwn"] = mrkdwn
        if parse is not UNSET:
            field_dict["parse"] = parse
        if reply_broadcast is not UNSET:
            field_dict["reply_broadcast"] = reply_broadcast
        if text is not UNSET:
            field_dict["text"] = text
        if thread_ts is not UNSET:
            field_dict["thread_ts"] = thread_ts
        if unfurl_links is not UNSET:
            field_dict["unfurl_links"] = unfurl_links
        if unfurl_media is not UNSET:
            field_dict["unfurl_media"] = unfurl_media
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel")

        as_user = d.pop("as_user", UNSET)

        attachments = d.pop("attachments", UNSET)

        blocks = d.pop("blocks", UNSET)

        icon_emoji = d.pop("icon_emoji", UNSET)

        icon_url = d.pop("icon_url", UNSET)

        link_names = d.pop("link_names", UNSET)

        mrkdwn = d.pop("mrkdwn", UNSET)

        parse = d.pop("parse", UNSET)

        reply_broadcast = d.pop("reply_broadcast", UNSET)

        text = d.pop("text", UNSET)

        thread_ts = d.pop("thread_ts", UNSET)

        unfurl_links = d.pop("unfurl_links", UNSET)

        unfurl_media = d.pop("unfurl_media", UNSET)

        username = d.pop("username", UNSET)

        chat_post_message_json_body = cls(
            channel=channel,
            as_user=as_user,
            attachments=attachments,
            blocks=blocks,
            icon_emoji=icon_emoji,
            icon_url=icon_url,
            link_names=link_names,
            mrkdwn=mrkdwn,
            parse=parse,
            reply_broadcast=reply_broadcast,
            text=text,
            thread_ts=thread_ts,
            unfurl_links=unfurl_links,
            unfurl_media=unfurl_media,
            username=username,
        )


        chat_post_message_json_body.additional_properties = d
        return chat_post_message_json_body

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
