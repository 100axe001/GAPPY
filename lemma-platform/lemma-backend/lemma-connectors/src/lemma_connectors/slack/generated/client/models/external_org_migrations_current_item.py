from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ExternalOrgMigrationsCurrentItem")



@_attrs_define
class ExternalOrgMigrationsCurrentItem:
    """ 
        Attributes:
            date_started (int):
            team_id (str):
     """

    date_started: int
    team_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date_started = self.date_started

        team_id = self.team_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "date_started": date_started,
            "team_id": team_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date_started = d.pop("date_started")

        team_id = d.pop("team_id")

        external_org_migrations_current_item = cls(
            date_started=date_started,
            team_id=team_id,
        )


        external_org_migrations_current_item.additional_properties = d
        return external_org_migrations_current_item

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
