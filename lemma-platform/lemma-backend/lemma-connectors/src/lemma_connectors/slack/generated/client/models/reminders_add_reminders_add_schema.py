from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.objs_reminder import ObjsReminder





T = TypeVar("T", bound="RemindersAddRemindersAddSchema")



@_attrs_define
class RemindersAddRemindersAddSchema:
    """ Schema for successful response from reminders.add method

        Attributes:
            ok (bool):
            reminder (ObjsReminder):
     """

    ok: bool
    reminder: ObjsReminder





    def to_dict(self) -> dict[str, Any]:
        from ..models.objs_reminder import ObjsReminder
        ok = self.ok

        reminder = self.reminder.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "reminder": reminder,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.objs_reminder import ObjsReminder
        d = dict(src_dict)
        ok = d.pop("ok")

        reminder = ObjsReminder.from_dict(d.pop("reminder"))




        reminders_add_reminders_add_schema = cls(
            ok=ok,
            reminder=reminder,
        )

        return reminders_add_reminders_add_schema

