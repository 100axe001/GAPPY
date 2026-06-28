from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ObjsReminder")



@_attrs_define
class ObjsReminder:
    """ 
        Attributes:
            creator (str):
            id (str):
            recurring (bool):
            text (str):
            user (str):
            complete_ts (int | Unset):
            time (int | Unset):
     """

    creator: str
    id: str
    recurring: bool
    text: str
    user: str
    complete_ts: int | Unset = UNSET
    time: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        creator = self.creator

        id = self.id

        recurring = self.recurring

        text = self.text

        user = self.user

        complete_ts = self.complete_ts

        time = self.time


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "creator": creator,
            "id": id,
            "recurring": recurring,
            "text": text,
            "user": user,
        })
        if complete_ts is not UNSET:
            field_dict["complete_ts"] = complete_ts
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator = d.pop("creator")

        id = d.pop("id")

        recurring = d.pop("recurring")

        text = d.pop("text")

        user = d.pop("user")

        complete_ts = d.pop("complete_ts", UNSET)

        time = d.pop("time", UNSET)

        objs_reminder = cls(
            creator=creator,
            id=id,
            recurring=recurring,
            text=text,
            user=user,
            complete_ts=complete_ts,
            time=time,
        )

        return objs_reminder

