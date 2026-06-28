from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="TeamAccessLogsTeamAccessLogsSchemaLoginsItem")



@_attrs_define
class TeamAccessLogsTeamAccessLogsSchemaLoginsItem:
    """ 
        Attributes:
            count (int):
            country (None | str):
            date_first (int):
            date_last (int):
            ip (None | str):
            isp (None | str):
            region (None | str):
            user_agent (str):
            user_id (str):
            username (str):
     """

    count: int
    country: None | str
    date_first: int
    date_last: int
    ip: None | str
    isp: None | str
    region: None | str
    user_agent: str
    user_id: str
    username: str





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        country: None | str
        country = self.country

        date_first = self.date_first

        date_last = self.date_last

        ip: None | str
        ip = self.ip

        isp: None | str
        isp = self.isp

        region: None | str
        region = self.region

        user_agent = self.user_agent

        user_id = self.user_id

        username = self.username


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "count": count,
            "country": country,
            "date_first": date_first,
            "date_last": date_last,
            "ip": ip,
            "isp": isp,
            "region": region,
            "user_agent": user_agent,
            "user_id": user_id,
            "username": username,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))


        date_first = d.pop("date_first")

        date_last = d.pop("date_last")

        def _parse_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip = _parse_ip(d.pop("ip"))


        def _parse_isp(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        isp = _parse_isp(d.pop("isp"))


        def _parse_region(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        region = _parse_region(d.pop("region"))


        user_agent = d.pop("user_agent")

        user_id = d.pop("user_id")

        username = d.pop("username")

        team_access_logs_team_access_logs_schema_logins_item = cls(
            count=count,
            country=country,
            date_first=date_first,
            date_last=date_last,
            ip=ip,
            isp=isp,
            region=region,
            user_agent=user_agent,
            user_id=user_id,
            username=username,
        )

        return team_access_logs_team_access_logs_schema_logins_item

