from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversations_create_conversations_create_error_schema_error import ConversationsCreateConversationsCreateErrorSchemaError
from ..types import UNSET, Unset






T = TypeVar("T", bound="ConversationsCreateConversationsCreateErrorSchema")



@_attrs_define
class ConversationsCreateConversationsCreateErrorSchema:
    """ Schema for error response from conversations.create method

        Attributes:
            error (ConversationsCreateConversationsCreateErrorSchemaError):
            ok (bool):
            callstack (str | Unset): Note: PHP callstack is only visible in dev/qa
            detail (str | Unset):
            needed (str | Unset):
            provided (str | Unset):
     """

    error: ConversationsCreateConversationsCreateErrorSchemaError
    ok: bool
    callstack: str | Unset = UNSET
    detail: str | Unset = UNSET
    needed: str | Unset = UNSET
    provided: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        ok = self.ok

        callstack = self.callstack

        detail = self.detail

        needed = self.needed

        provided = self.provided


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "ok": ok,
        })
        if callstack is not UNSET:
            field_dict["callstack"] = callstack
        if detail is not UNSET:
            field_dict["detail"] = detail
        if needed is not UNSET:
            field_dict["needed"] = needed
        if provided is not UNSET:
            field_dict["provided"] = provided

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = ConversationsCreateConversationsCreateErrorSchemaError(d.pop("error"))




        ok = d.pop("ok")

        callstack = d.pop("callstack", UNSET)

        detail = d.pop("detail", UNSET)

        needed = d.pop("needed", UNSET)

        provided = d.pop("provided", UNSET)

        conversations_create_conversations_create_error_schema = cls(
            error=error,
            ok=ok,
            callstack=callstack,
            detail=detail,
            needed=needed,
            provided=provided,
        )

        return conversations_create_conversations_create_error_schema

