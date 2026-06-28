from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.rtm_connect_rtm_connect_schema_self import RtmConnectRtmConnectSchemaSelf
  from ..models.rtm_connect_rtm_connect_schema_team import RtmConnectRtmConnectSchemaTeam





T = TypeVar("T", bound="RtmConnectRtmConnectSchema")



@_attrs_define
class RtmConnectRtmConnectSchema:
    """ Schema for successful response from rtm.connect method

        Attributes:
            ok (bool):
            self_ (RtmConnectRtmConnectSchemaSelf):
            team (RtmConnectRtmConnectSchemaTeam):
            url (str):
     """

    ok: bool
    self_: RtmConnectRtmConnectSchemaSelf
    team: RtmConnectRtmConnectSchemaTeam
    url: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.rtm_connect_rtm_connect_schema_self import RtmConnectRtmConnectSchemaSelf
        from ..models.rtm_connect_rtm_connect_schema_team import RtmConnectRtmConnectSchemaTeam
        ok = self.ok

        self_ = self.self_.to_dict()

        team = self.team.to_dict()

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "self": self_,
            "team": team,
            "url": url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rtm_connect_rtm_connect_schema_self import RtmConnectRtmConnectSchemaSelf
        from ..models.rtm_connect_rtm_connect_schema_team import RtmConnectRtmConnectSchemaTeam
        d = dict(src_dict)
        ok = d.pop("ok")

        self_ = RtmConnectRtmConnectSchemaSelf.from_dict(d.pop("self"))




        team = RtmConnectRtmConnectSchemaTeam.from_dict(d.pop("team"))




        url = d.pop("url")

        rtm_connect_rtm_connect_schema = cls(
            ok=ok,
            self_=self_,
            team=team,
            url=url,
        )

        return rtm_connect_rtm_connect_schema

