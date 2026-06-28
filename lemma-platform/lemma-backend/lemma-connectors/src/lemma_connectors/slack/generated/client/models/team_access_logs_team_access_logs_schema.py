from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.paging_object import PagingObject
  from ..models.team_access_logs_team_access_logs_schema_logins_item import TeamAccessLogsTeamAccessLogsSchemaLoginsItem





T = TypeVar("T", bound="TeamAccessLogsTeamAccessLogsSchema")



@_attrs_define
class TeamAccessLogsTeamAccessLogsSchema:
    """ Schema for successful response from team.accessLogs method

        Attributes:
            logins (list[TeamAccessLogsTeamAccessLogsSchemaLoginsItem]):
            ok (bool):
            paging (PagingObject):
     """

    logins: list[TeamAccessLogsTeamAccessLogsSchemaLoginsItem]
    ok: bool
    paging: PagingObject





    def to_dict(self) -> dict[str, Any]:
        from ..models.paging_object import PagingObject
        from ..models.team_access_logs_team_access_logs_schema_logins_item import TeamAccessLogsTeamAccessLogsSchemaLoginsItem
        logins = []
        for logins_item_data in self.logins:
            logins_item = logins_item_data.to_dict()
            logins.append(logins_item)



        ok = self.ok

        paging = self.paging.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "logins": logins,
            "ok": ok,
            "paging": paging,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paging_object import PagingObject
        from ..models.team_access_logs_team_access_logs_schema_logins_item import TeamAccessLogsTeamAccessLogsSchemaLoginsItem
        d = dict(src_dict)
        logins = []
        _logins = d.pop("logins")
        for logins_item_data in (_logins):
            logins_item = TeamAccessLogsTeamAccessLogsSchemaLoginsItem.from_dict(logins_item_data)



            logins.append(logins_item)


        ok = d.pop("ok")

        paging = PagingObject.from_dict(d.pop("paging"))




        team_access_logs_team_access_logs_schema = cls(
            logins=logins,
            ok=ok,
            paging=paging,
        )

        return team_access_logs_team_access_logs_schema

