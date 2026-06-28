from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.team_profile_get_team_profile_get_success_schema_profile import TeamProfileGetTeamProfileGetSuccessSchemaProfile





T = TypeVar("T", bound="TeamProfileGetTeamProfileGetSuccessSchema")



@_attrs_define
class TeamProfileGetTeamProfileGetSuccessSchema:
    """ Schema for successful response from team.profile.get method

        Attributes:
            ok (bool):
            profile (TeamProfileGetTeamProfileGetSuccessSchemaProfile):
     """

    ok: bool
    profile: TeamProfileGetTeamProfileGetSuccessSchemaProfile





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_profile_get_team_profile_get_success_schema_profile import TeamProfileGetTeamProfileGetSuccessSchemaProfile
        ok = self.ok

        profile = self.profile.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "profile": profile,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_profile_get_team_profile_get_success_schema_profile import TeamProfileGetTeamProfileGetSuccessSchemaProfile
        d = dict(src_dict)
        ok = d.pop("ok")

        profile = TeamProfileGetTeamProfileGetSuccessSchemaProfile.from_dict(d.pop("profile"))




        team_profile_get_team_profile_get_success_schema = cls(
            ok=ok,
            profile=profile,
        )

        return team_profile_get_team_profile_get_success_schema

