from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.users_get_presence_users_counts_error_schema_additional_property import UsersGetPresenceUsersCountsErrorSchemaAdditionalProperty





T = TypeVar("T", bound="UsersGetPresenceUsersCountsErrorSchema")



@_attrs_define
class UsersGetPresenceUsersCountsErrorSchema:
    """ Schema for error response users.getPresence method

        Attributes:
            error (str):
            ok (bool):
     """

    error: str
    ok: bool
    additional_properties: dict[str, UsersGetPresenceUsersCountsErrorSchemaAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.users_get_presence_users_counts_error_schema_additional_property import UsersGetPresenceUsersCountsErrorSchemaAdditionalProperty
        error = self.error

        ok = self.ok


        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({
            "error": error,
            "ok": ok,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.users_get_presence_users_counts_error_schema_additional_property import UsersGetPresenceUsersCountsErrorSchemaAdditionalProperty
        d = dict(src_dict)
        error = d.pop("error")

        ok = d.pop("ok")

        users_get_presence_users_counts_error_schema = cls(
            error=error,
            ok=ok,
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = UsersGetPresenceUsersCountsErrorSchemaAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        users_get_presence_users_counts_error_schema.additional_properties = additional_properties
        return users_get_presence_users_counts_error_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> UsersGetPresenceUsersCountsErrorSchemaAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: UsersGetPresenceUsersCountsErrorSchemaAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
