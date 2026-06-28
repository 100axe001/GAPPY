from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TeamIntegrationLogsTeamIntegrationLogsSchemaLogsItem")



@_attrs_define
class TeamIntegrationLogsTeamIntegrationLogsSchemaLogsItem:
    """ 
        Attributes:
            app_id (str):
            app_type (str):
            change_type (str):
            date (str):
            scope (str):
            user_id (str):
            user_name (str):
            admin_app_id (str | Unset):
            channel (str | Unset):
            service_id (str | Unset):
            service_type (str | Unset):
     """

    app_id: str
    app_type: str
    change_type: str
    date: str
    scope: str
    user_id: str
    user_name: str
    admin_app_id: str | Unset = UNSET
    channel: str | Unset = UNSET
    service_id: str | Unset = UNSET
    service_type: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_type = self.app_type

        change_type = self.change_type

        date = self.date

        scope = self.scope

        user_id = self.user_id

        user_name = self.user_name

        admin_app_id = self.admin_app_id

        channel = self.channel

        service_id = self.service_id

        service_type = self.service_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "app_id": app_id,
            "app_type": app_type,
            "change_type": change_type,
            "date": date,
            "scope": scope,
            "user_id": user_id,
            "user_name": user_name,
        })
        if admin_app_id is not UNSET:
            field_dict["admin_app_id"] = admin_app_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if service_type is not UNSET:
            field_dict["service_type"] = service_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("app_id")

        app_type = d.pop("app_type")

        change_type = d.pop("change_type")

        date = d.pop("date")

        scope = d.pop("scope")

        user_id = d.pop("user_id")

        user_name = d.pop("user_name")

        admin_app_id = d.pop("admin_app_id", UNSET)

        channel = d.pop("channel", UNSET)

        service_id = d.pop("service_id", UNSET)

        service_type = d.pop("service_type", UNSET)

        team_integration_logs_team_integration_logs_schema_logs_item = cls(
            app_id=app_id,
            app_type=app_type,
            change_type=change_type,
            date=date,
            scope=scope,
            user_id=user_id,
            user_name=user_name,
            admin_app_id=admin_app_id,
            channel=channel,
            service_id=service_id,
            service_type=service_type,
        )

        return team_integration_logs_team_integration_logs_schema_logs_item

