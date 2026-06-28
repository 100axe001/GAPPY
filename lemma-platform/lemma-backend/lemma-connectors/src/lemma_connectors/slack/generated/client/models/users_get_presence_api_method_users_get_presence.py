from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UsersGetPresenceAPIMethodUsersGetPresence")



@_attrs_define
class UsersGetPresenceAPIMethodUsersGetPresence:
    """ Generated from users.getPresence with shasum e7251aec575d8863f9e0eb38663ae9dc26655f65

        Attributes:
            ok (bool):
            presence (str):
            auto_away (bool | Unset):
            connection_count (int | Unset):
            last_activity (int | Unset):
            manual_away (bool | Unset):
            online (bool | Unset):
     """

    ok: bool
    presence: str
    auto_away: bool | Unset = UNSET
    connection_count: int | Unset = UNSET
    last_activity: int | Unset = UNSET
    manual_away: bool | Unset = UNSET
    online: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        presence = self.presence

        auto_away = self.auto_away

        connection_count = self.connection_count

        last_activity = self.last_activity

        manual_away = self.manual_away

        online = self.online


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ok": ok,
            "presence": presence,
        })
        if auto_away is not UNSET:
            field_dict["auto_away"] = auto_away
        if connection_count is not UNSET:
            field_dict["connection_count"] = connection_count
        if last_activity is not UNSET:
            field_dict["last_activity"] = last_activity
        if manual_away is not UNSET:
            field_dict["manual_away"] = manual_away
        if online is not UNSET:
            field_dict["online"] = online

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        presence = d.pop("presence")

        auto_away = d.pop("auto_away", UNSET)

        connection_count = d.pop("connection_count", UNSET)

        last_activity = d.pop("last_activity", UNSET)

        manual_away = d.pop("manual_away", UNSET)

        online = d.pop("online", UNSET)

        users_get_presence_api_method_users_get_presence = cls(
            ok=ok,
            presence=presence,
            auto_away=auto_away,
            connection_count=connection_count,
            last_activity=last_activity,
            manual_away=manual_away,
            online=online,
        )


        users_get_presence_api_method_users_get_presence.additional_properties = d
        return users_get_presence_api_method_users_get_presence

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
