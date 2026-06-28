from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversations_unarchive_conversations_unarchive_error_schema_error import ConversationsUnarchiveConversationsUnarchiveErrorSchemaError
from ..types import UNSET, Unset






T = TypeVar("T", bound="ConversationsUnarchiveConversationsUnarchiveErrorSchema")



@_attrs_define
class ConversationsUnarchiveConversationsUnarchiveErrorSchema:
    """ Schema for error response from conversations.unarchive method

        Attributes:
            error (ConversationsUnarchiveConversationsUnarchiveErrorSchemaError):
            ok (bool):
            callstack (str | Unset): Note: PHP callstack is only visible in dev/qa
            needed (str | Unset):
            provided (str | Unset):
     """

    error: ConversationsUnarchiveConversationsUnarchiveErrorSchemaError
    ok: bool
    callstack: str | Unset = UNSET
    needed: str | Unset = UNSET
    provided: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        ok = self.ok

        callstack = self.callstack

        needed = self.needed

        provided = self.provided


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "ok": ok,
        })
        if callstack is not UNSET:
            field_dict["callstack"] = callstack
        if needed is not UNSET:
            field_dict["needed"] = needed
        if provided is not UNSET:
            field_dict["provided"] = provided

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = ConversationsUnarchiveConversationsUnarchiveErrorSchemaError(d.pop("error"))




        ok = d.pop("ok")

        callstack = d.pop("callstack", UNSET)

        needed = d.pop("needed", UNSET)

        provided = d.pop("provided", UNSET)

        conversations_unarchive_conversations_unarchive_error_schema = cls(
            error=error,
            ok=ok,
            callstack=callstack,
            needed=needed,
            provided=provided,
        )

        return conversations_unarchive_conversations_unarchive_error_schema

