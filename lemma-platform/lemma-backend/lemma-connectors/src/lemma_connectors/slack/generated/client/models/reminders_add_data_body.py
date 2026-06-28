from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RemindersAddDataBody")



@_attrs_define
class RemindersAddDataBody:
    """ 
        Attributes:
            text (str): The content of the reminder
            time (str): When this reminder should happen: the Unix timestamp (up to five years from now), the number of
                seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes," or
                "every Thursday")
            user (str | Unset): The user who will receive the reminder. If no user is specified, the reminder will go to
                user who created it.
     """

    text: str
    time: str
    user: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        text = self.text

        time = self.time

        user = self.user


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "text": text,
            "time": time,
        })
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        time = d.pop("time")

        user = d.pop("user", UNSET)

        reminders_add_data_body = cls(
            text=text,
            time=time,
            user=user,
        )


        reminders_add_data_body.additional_properties = d
        return reminders_add_data_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
