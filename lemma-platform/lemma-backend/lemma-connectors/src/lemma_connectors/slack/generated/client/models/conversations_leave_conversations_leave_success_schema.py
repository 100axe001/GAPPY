from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConversationsLeaveConversationsLeaveSuccessSchema")



@_attrs_define
class ConversationsLeaveConversationsLeaveSuccessSchema:
    """ Schema for successful response from conversations.leave method

        Attributes:
            ok (bool):
            not_in_channel (bool | Unset):
     """

    ok: bool
    not_in_channel: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        not_in_channel = self.not_in_channel


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
        })
        if not_in_channel is not UNSET:
            field_dict["not_in_channel"] = not_in_channel

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        not_in_channel = d.pop("not_in_channel", UNSET)

        conversations_leave_conversations_leave_success_schema = cls(
            ok=ok,
            not_in_channel=not_in_channel,
        )

        return conversations_leave_conversations_leave_success_schema

