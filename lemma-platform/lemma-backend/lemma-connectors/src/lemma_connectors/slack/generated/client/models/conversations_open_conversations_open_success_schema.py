from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConversationsOpenConversationsOpenSuccessSchema")



@_attrs_define
class ConversationsOpenConversationsOpenSuccessSchema:
    """ Schema for successful response from conversations.open method when opening channels, ims, mpims

        Attributes:
            channel (Any):
            ok (bool):
            already_open (bool | Unset):
            no_op (bool | Unset):
     """

    channel: Any
    ok: bool
    already_open: bool | Unset = UNSET
    no_op: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ok = self.ok

        already_open = self.already_open

        no_op = self.no_op


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel": channel,
            "ok": ok,
        })
        if already_open is not UNSET:
            field_dict["already_open"] = already_open
        if no_op is not UNSET:
            field_dict["no_op"] = no_op

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel")

        ok = d.pop("ok")

        already_open = d.pop("already_open", UNSET)

        no_op = d.pop("no_op", UNSET)

        conversations_open_conversations_open_success_schema = cls(
            channel=channel,
            ok=ok,
            already_open=already_open,
            no_op=no_op,
        )

        return conversations_open_conversations_open_success_schema

