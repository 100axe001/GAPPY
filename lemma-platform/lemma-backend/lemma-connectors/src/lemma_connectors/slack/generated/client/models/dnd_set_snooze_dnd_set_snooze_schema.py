from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DndSetSnoozeDndSetSnoozeSchema")



@_attrs_define
class DndSetSnoozeDndSetSnoozeSchema:
    """ Schema for successful response from dnd.setSnooze method

        Attributes:
            ok (bool):
            snooze_enabled (bool):
            snooze_endtime (int):
            snooze_remaining (int):
     """

    ok: bool
    snooze_enabled: bool
    snooze_endtime: int
    snooze_remaining: int





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        snooze_enabled = self.snooze_enabled

        snooze_endtime = self.snooze_endtime

        snooze_remaining = self.snooze_remaining


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "snooze_enabled": snooze_enabled,
            "snooze_endtime": snooze_endtime,
            "snooze_remaining": snooze_remaining,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        snooze_enabled = d.pop("snooze_enabled")

        snooze_endtime = d.pop("snooze_endtime")

        snooze_remaining = d.pop("snooze_remaining")

        dnd_set_snooze_dnd_set_snooze_schema = cls(
            ok=ok,
            snooze_enabled=snooze_enabled,
            snooze_endtime=snooze_endtime,
            snooze_remaining=snooze_remaining,
        )

        return dnd_set_snooze_dnd_set_snooze_schema

