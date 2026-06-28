from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ConversationsRepliesConversationsRepliesSuccessSchema")



@_attrs_define
class ConversationsRepliesConversationsRepliesSuccessSchema:
    """ Schema for successful response from conversations.replies method

        Attributes:
            messages (list[Any]):
            ok (bool):
            has_more (bool | Unset):
     """

    messages: list[Any]
    ok: bool
    has_more: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        messages = self.messages



        ok = self.ok

        has_more = self.has_more


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "messages": messages,
            "ok": ok,
        })
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        messages = cast(list[Any], d.pop("messages"))


        ok = d.pop("ok")

        has_more = d.pop("has_more", UNSET)

        conversations_replies_conversations_replies_success_schema = cls(
            messages=messages,
            ok=ok,
            has_more=has_more,
        )

        return conversations_replies_conversations_replies_success_schema

