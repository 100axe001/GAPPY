from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.bots_info_bots_info_schema_bot import BotsInfoBotsInfoSchemaBot





T = TypeVar("T", bound="BotsInfoBotsInfoSchema")



@_attrs_define
class BotsInfoBotsInfoSchema:
    """ Schema for successful response from bots.info method

        Attributes:
            bot (BotsInfoBotsInfoSchemaBot):
            ok (bool):
     """

    bot: BotsInfoBotsInfoSchemaBot
    ok: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.bots_info_bots_info_schema_bot import BotsInfoBotsInfoSchemaBot
        bot = self.bot.to_dict()

        ok = self.ok


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "bot": bot,
            "ok": ok,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bots_info_bots_info_schema_bot import BotsInfoBotsInfoSchemaBot
        d = dict(src_dict)
        bot = BotsInfoBotsInfoSchemaBot.from_dict(d.pop("bot"))




        ok = d.pop("ok")

        bots_info_bots_info_schema = cls(
            bot=bot,
            ok=ok,
        )

        return bots_info_bots_info_schema

