from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bots_info_bots_info_schema_bot_icons import BotsInfoBotsInfoSchemaBotIcons





T = TypeVar("T", bound="BotsInfoBotsInfoSchemaBot")



@_attrs_define
class BotsInfoBotsInfoSchemaBot:
    """ 
        Attributes:
            app_id (str):
            deleted (bool):
            icons (BotsInfoBotsInfoSchemaBotIcons):
            id (str):
            name (str):
            updated (int):
            user_id (str | Unset):
     """

    app_id: str
    deleted: bool
    icons: BotsInfoBotsInfoSchemaBotIcons
    id: str
    name: str
    updated: int
    user_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.bots_info_bots_info_schema_bot_icons import BotsInfoBotsInfoSchemaBotIcons
        app_id = self.app_id

        deleted = self.deleted

        icons = self.icons.to_dict()

        id = self.id

        name = self.name

        updated = self.updated

        user_id = self.user_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "app_id": app_id,
            "deleted": deleted,
            "icons": icons,
            "id": id,
            "name": name,
            "updated": updated,
        })
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bots_info_bots_info_schema_bot_icons import BotsInfoBotsInfoSchemaBotIcons
        d = dict(src_dict)
        app_id = d.pop("app_id")

        deleted = d.pop("deleted")

        icons = BotsInfoBotsInfoSchemaBotIcons.from_dict(d.pop("icons"))




        id = d.pop("id")

        name = d.pop("name")

        updated = d.pop("updated")

        user_id = d.pop("user_id", UNSET)

        bots_info_bots_info_schema_bot = cls(
            app_id=app_id,
            deleted=deleted,
            icons=icons,
            id=id,
            name=name,
            updated=updated,
            user_id=user_id,
        )

        return bots_info_bots_info_schema_bot

