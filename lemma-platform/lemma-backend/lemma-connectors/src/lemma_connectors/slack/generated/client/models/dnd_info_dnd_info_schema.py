from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DndInfoDndInfoSchema")



@_attrs_define
class DndInfoDndInfoSchema:
    """ Schema for successful response from dnd.info method

        Attributes:
            dnd_enabled (bool):
            next_dnd_end_ts (int):
            next_dnd_start_ts (int):
            ok (bool):
            snooze_enabled (bool | Unset):
            snooze_endtime (int | Unset):
            snooze_remaining (int | Unset):
     """

    dnd_enabled: bool
    next_dnd_end_ts: int
    next_dnd_start_ts: int
    ok: bool
    snooze_enabled: bool | Unset = UNSET
    snooze_endtime: int | Unset = UNSET
    snooze_remaining: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        dnd_enabled = self.dnd_enabled

        next_dnd_end_ts = self.next_dnd_end_ts

        next_dnd_start_ts = self.next_dnd_start_ts

        ok = self.ok

        snooze_enabled = self.snooze_enabled

        snooze_endtime = self.snooze_endtime

        snooze_remaining = self.snooze_remaining


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "dnd_enabled": dnd_enabled,
            "next_dnd_end_ts": next_dnd_end_ts,
            "next_dnd_start_ts": next_dnd_start_ts,
            "ok": ok,
        })
        if snooze_enabled is not UNSET:
            field_dict["snooze_enabled"] = snooze_enabled
        if snooze_endtime is not UNSET:
            field_dict["snooze_endtime"] = snooze_endtime
        if snooze_remaining is not UNSET:
            field_dict["snooze_remaining"] = snooze_remaining

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dnd_enabled = d.pop("dnd_enabled")

        next_dnd_end_ts = d.pop("next_dnd_end_ts")

        next_dnd_start_ts = d.pop("next_dnd_start_ts")

        ok = d.pop("ok")

        snooze_enabled = d.pop("snooze_enabled", UNSET)

        snooze_endtime = d.pop("snooze_endtime", UNSET)

        snooze_remaining = d.pop("snooze_remaining", UNSET)

        dnd_info_dnd_info_schema = cls(
            dnd_enabled=dnd_enabled,
            next_dnd_end_ts=next_dnd_end_ts,
            next_dnd_start_ts=next_dnd_start_ts,
            ok=ok,
            snooze_enabled=snooze_enabled,
            snooze_endtime=snooze_endtime,
            snooze_remaining=snooze_remaining,
        )

        return dnd_info_dnd_info_schema

