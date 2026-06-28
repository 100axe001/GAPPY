from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.team_object import TeamObject





T = TypeVar("T", bound="TeamInfoTeamInfoSchema")



@_attrs_define
class TeamInfoTeamInfoSchema:
    """ Schema for successful response from team.info method

        Attributes:
            ok (bool):
            team (TeamObject):
     """

    ok: bool
    team: TeamObject





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_object import TeamObject
        ok = self.ok

        team = self.team.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "team": team,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_object import TeamObject
        d = dict(src_dict)
        ok = d.pop("ok")

        team = TeamObject.from_dict(d.pop("team"))




        team_info_team_info_schema = cls(
            ok=ok,
            team=team,
        )

        return team_info_team_info_schema

