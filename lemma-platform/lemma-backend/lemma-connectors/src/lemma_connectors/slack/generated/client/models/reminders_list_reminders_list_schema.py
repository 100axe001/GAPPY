from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.objs_reminder import ObjsReminder





T = TypeVar("T", bound="RemindersListRemindersListSchema")



@_attrs_define
class RemindersListRemindersListSchema:
    """ Schema for successful response from reminders.list method

        Attributes:
            ok (bool):
            reminders (list[ObjsReminder]):
     """

    ok: bool
    reminders: list[ObjsReminder]





    def to_dict(self) -> dict[str, Any]:
        from ..models.objs_reminder import ObjsReminder
        ok = self.ok

        reminders = []
        for reminders_item_data in self.reminders:
            reminders_item = reminders_item_data.to_dict()
            reminders.append(reminders_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "reminders": reminders,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.objs_reminder import ObjsReminder
        d = dict(src_dict)
        ok = d.pop("ok")

        reminders = []
        _reminders = d.pop("reminders")
        for reminders_item_data in (_reminders):
            reminders_item = ObjsReminder.from_dict(reminders_item_data)



            reminders.append(reminders_item)


        reminders_list_reminders_list_schema = cls(
            ok=ok,
            reminders=reminders,
        )

        return reminders_list_reminders_list_schema

