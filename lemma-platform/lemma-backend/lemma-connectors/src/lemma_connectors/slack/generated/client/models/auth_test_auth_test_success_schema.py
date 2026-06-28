from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AuthTestAuthTestSuccessSchema")



@_attrs_define
class AuthTestAuthTestSuccessSchema:
    """ Schema for successful response auth.test method

        Attributes:
            ok (bool):
            team (str):
            team_id (str):
            url (str):
            user (str):
            user_id (str):
            bot_id (str | Unset):
            is_enterprise_install (bool | Unset):
     """

    ok: bool
    team: str
    team_id: str
    url: str
    user: str
    user_id: str
    bot_id: str | Unset = UNSET
    is_enterprise_install: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        team = self.team

        team_id = self.team_id

        url = self.url

        user = self.user

        user_id = self.user_id

        bot_id = self.bot_id

        is_enterprise_install = self.is_enterprise_install


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "team": team,
            "team_id": team_id,
            "url": url,
            "user": user,
            "user_id": user_id,
        })
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if is_enterprise_install is not UNSET:
            field_dict["is_enterprise_install"] = is_enterprise_install

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        team = d.pop("team")

        team_id = d.pop("team_id")

        url = d.pop("url")

        user = d.pop("user")

        user_id = d.pop("user_id")

        bot_id = d.pop("bot_id", UNSET)

        is_enterprise_install = d.pop("is_enterprise_install", UNSET)

        auth_test_auth_test_success_schema = cls(
            ok=ok,
            team=team,
            team_id=team_id,
            url=url,
            user=user,
            user_id=user_id,
            bot_id=bot_id,
            is_enterprise_install=is_enterprise_install,
        )

        return auth_test_auth_test_success_schema

