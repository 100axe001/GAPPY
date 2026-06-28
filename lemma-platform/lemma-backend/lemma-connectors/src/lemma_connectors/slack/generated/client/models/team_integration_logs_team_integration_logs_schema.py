from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.paging_object import PagingObject
  from ..models.team_integration_logs_team_integration_logs_schema_logs_item import TeamIntegrationLogsTeamIntegrationLogsSchemaLogsItem





T = TypeVar("T", bound="TeamIntegrationLogsTeamIntegrationLogsSchema")



@_attrs_define
class TeamIntegrationLogsTeamIntegrationLogsSchema:
    """ Schema for successful response from team.integrationLogs method

        Attributes:
            logs (list[TeamIntegrationLogsTeamIntegrationLogsSchemaLogsItem]):
            ok (bool):
            paging (PagingObject):
     """

    logs: list[TeamIntegrationLogsTeamIntegrationLogsSchemaLogsItem]
    ok: bool
    paging: PagingObject





    def to_dict(self) -> dict[str, Any]:
        from ..models.paging_object import PagingObject
        from ..models.team_integration_logs_team_integration_logs_schema_logs_item import TeamIntegrationLogsTeamIntegrationLogsSchemaLogsItem
        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)



        ok = self.ok

        paging = self.paging.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "logs": logs,
            "ok": ok,
            "paging": paging,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paging_object import PagingObject
        from ..models.team_integration_logs_team_integration_logs_schema_logs_item import TeamIntegrationLogsTeamIntegrationLogsSchemaLogsItem
        d = dict(src_dict)
        logs = []
        _logs = d.pop("logs")
        for logs_item_data in (_logs):
            logs_item = TeamIntegrationLogsTeamIntegrationLogsSchemaLogsItem.from_dict(logs_item_data)



            logs.append(logs_item)


        ok = d.pop("ok")

        paging = PagingObject.from_dict(d.pop("paging"))




        team_integration_logs_team_integration_logs_schema = cls(
            logs=logs,
            ok=ok,
            paging=paging,
        )

        return team_integration_logs_team_integration_logs_schema

