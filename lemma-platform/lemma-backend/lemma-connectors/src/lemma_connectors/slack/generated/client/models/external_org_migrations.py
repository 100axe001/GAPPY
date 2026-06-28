from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.external_org_migrations_current_item import ExternalOrgMigrationsCurrentItem





T = TypeVar("T", bound="ExternalOrgMigrations")



@_attrs_define
class ExternalOrgMigrations:
    """ 
        Attributes:
            current (list[ExternalOrgMigrationsCurrentItem]):
            date_updated (int):
     """

    current: list[ExternalOrgMigrationsCurrentItem]
    date_updated: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.external_org_migrations_current_item import ExternalOrgMigrationsCurrentItem
        current = []
        for current_item_data in self.current:
            current_item = current_item_data.to_dict()
            current.append(current_item)



        date_updated = self.date_updated


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "current": current,
            "date_updated": date_updated,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_org_migrations_current_item import ExternalOrgMigrationsCurrentItem
        d = dict(src_dict)
        current = []
        _current = d.pop("current")
        for current_item_data in (_current):
            current_item = ExternalOrgMigrationsCurrentItem.from_dict(current_item_data)



            current.append(current_item)


        date_updated = d.pop("date_updated")

        external_org_migrations = cls(
            current=current,
            date_updated=date_updated,
        )


        external_org_migrations.additional_properties = d
        return external_org_migrations

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
