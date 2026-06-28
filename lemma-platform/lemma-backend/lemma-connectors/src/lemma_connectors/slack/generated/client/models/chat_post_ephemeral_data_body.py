from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatPostEphemeralDataBody")



@_attrs_define
class ChatPostEphemeralDataBody:
    """ 
        Attributes:
            channel (str): Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.
            user (str): `id` of the user who will receive the ephemeral message. The user should be in the channel specified
                by the `channel` argument.
            as_user (bool | Unset): Pass true to post the message as the authed user. Defaults to true if the chat:write:bot
                scope is not included. Otherwise, defaults to false.
            attachments (str | Unset): A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks (str | Unset): A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji (str | Unset): Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in
                conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](#authorship) below.
            icon_url (str | Unset): URL to an image to use as the icon for this message. Must be used in conjunction with
                `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.
            link_names (bool | Unset): Find and link channel names and usernames.
            parse (str | Unset): Change how messages are treated. Defaults to `none`. See [below](#formatting).
            text (str | Unset): How this field works and whether it is required depends on other fields you use in your API
                call. [See below](#text_usage) for more detail.
            thread_ts (str | Unset): Provide another message's `ts` value to post this message in a thread. Avoid using a
                reply's `ts` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is
                already an active thread.
            username (str | Unset): Set your bot's user name. Must be used in conjunction with `as_user` set to false,
                otherwise ignored. See [authorship](#authorship) below.
     """

    channel: str
    user: str
    as_user: bool | Unset = UNSET
    attachments: str | Unset = UNSET
    blocks: str | Unset = UNSET
    icon_emoji: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    link_names: bool | Unset = UNSET
    parse: str | Unset = UNSET
    text: str | Unset = UNSET
    thread_ts: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        user = self.user

        as_user = self.as_user

        attachments = self.attachments

        blocks = self.blocks

        icon_emoji = self.icon_emoji

        icon_url = self.icon_url

        link_names = self.link_names

        parse = self.parse

        text = self.text

        thread_ts = self.thread_ts

        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channel": channel,
            "user": user,
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
        if parse is not UNSET:
            field_dict["parse"] = parse
        if text is not UNSET:
            field_dict["text"] = text
        if thread_ts is not UNSET:
            field_dict["thread_ts"] = thread_ts
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel")

        user = d.pop("user")

        as_user = d.pop("as_user", UNSET)

        attachments = d.pop("attachments", UNSET)

        blocks = d.pop("blocks", UNSET)

        icon_emoji = d.pop("icon_emoji", UNSET)

        icon_url = d.pop("icon_url", UNSET)

        link_names = d.pop("link_names", UNSET)

        parse = d.pop("parse", UNSET)

        text = d.pop("text", UNSET)

        thread_ts = d.pop("thread_ts", UNSET)

        username = d.pop("username", UNSET)

        chat_post_ephemeral_data_body = cls(
            channel=channel,
            user=user,
            as_user=as_user,
            attachments=attachments,
            blocks=blocks,
            icon_emoji=icon_emoji,
            icon_url=icon_url,
            link_names=link_names,
            parse=parse,
            text=text,
            thread_ts=thread_ts,
            username=username,
        )


        chat_post_ephemeral_data_body.additional_properties = d
        return chat_post_ephemeral_data_body

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
