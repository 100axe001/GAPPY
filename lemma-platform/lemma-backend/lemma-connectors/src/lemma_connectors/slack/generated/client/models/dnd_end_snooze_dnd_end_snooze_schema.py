from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DndEndSnoozeDndEndSnoozeSchema")



@_attrs_define
class DndEndSnoozeDndEndSnoozeSchema:
    """ Schema for successful response from dnd.endSnooze method

        Attributes:
            dnd_enabled (bool):
            next_dnd_end_ts (int):
            next_dnd_start_ts (int):
            ok (bool):
            snooze_enabled (bool):
     """

    dnd_enabled: bool
    next_dnd_end_ts: int
    next_dnd_start_ts: int
    ok: bool
    snooze_enabled: bool





    def to_dict(self) -> dict[str, Any]:
        dnd_enabled = self.dnd_enabled

        next_dnd_end_ts = self.next_dnd_end_ts

        next_dnd_start_ts = self.next_dnd_start_ts

        ok = self.ok

        snooze_enabled = self.snooze_enabled


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "dnd_enabled": dnd_enabled,
            "next_dnd_end_ts": next_dnd_end_ts,
            "next_dnd_start_ts": next_dnd_start_ts,
            "ok": ok,
            "snooze_enabled": snooze_enabled,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dnd_enabled = d.pop("dnd_enabled")

        next_dnd_end_ts = d.pop("next_dnd_end_ts")

        next_dnd_start_ts = d.pop("next_dnd_start_ts")

        ok = d.pop("ok")

        snooze_enabled = d.pop("snooze_enabled")

        dnd_end_snooze_dnd_end_snooze_schema = cls(
            dnd_enabled=dnd_enabled,
            next_dnd_end_ts=next_dnd_end_ts,
            next_dnd_start_ts=next_dnd_start_ts,
            ok=ok,
            snooze_enabled=snooze_enabled,
        )

        return dnd_end_snooze_dnd_end_snooze_schema

