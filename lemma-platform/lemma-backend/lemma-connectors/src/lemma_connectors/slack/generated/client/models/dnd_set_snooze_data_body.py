from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DndSetSnoozeDataBody")



@_attrs_define
class DndSetSnoozeDataBody:
    """ 
        Attributes:
            token (str): Authentication token. Requires scope: `dnd:write`
            num_minutes (str): Number of minutes, from now, to snooze until.
     """

    token: str
    num_minutes: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        token = self.token

        num_minutes = self.num_minutes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "token": token,
            "num_minutes": num_minutes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        num_minutes = d.pop("num_minutes")

        dnd_set_snooze_data_body = cls(
            token=token,
            num_minutes=num_minutes,
        )


        dnd_set_snooze_data_body.additional_properties = d
        return dnd_set_snooze_data_body

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
