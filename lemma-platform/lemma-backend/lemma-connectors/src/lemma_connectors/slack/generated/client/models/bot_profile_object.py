from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.bot_profile_object_icons import BotProfileObjectIcons





T = TypeVar("T", bound="BotProfileObject")



@_attrs_define
class BotProfileObject:
    """ 
        Attributes:
            app_id (str):
            deleted (bool):
            icons (BotProfileObjectIcons):
            id (str):
            name (str):
            team_id (str):
            updated (int):
     """

    app_id: str
    deleted: bool
    icons: BotProfileObjectIcons
    id: str
    name: str
    team_id: str
    updated: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_profile_object_icons import BotProfileObjectIcons
        app_id = self.app_id

        deleted = self.deleted

        icons = self.icons.to_dict()

        id = self.id

        name = self.name

        team_id = self.team_id

        updated = self.updated


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "app_id": app_id,
            "deleted": deleted,
            "icons": icons,
            "id": id,
            "name": name,
            "team_id": team_id,
            "updated": updated,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_profile_object_icons import BotProfileObjectIcons
        d = dict(src_dict)
        app_id = d.pop("app_id")

        deleted = d.pop("deleted")

        icons = BotProfileObjectIcons.from_dict(d.pop("icons"))




        id = d.pop("id")

        name = d.pop("name")

        team_id = d.pop("team_id")

        updated = d.pop("updated")

        bot_profile_object = cls(
            app_id=app_id,
            deleted=deleted,
            icons=icons,
            id=id,
            name=name,
            team_id=team_id,
            updated=updated,
        )

        return bot_profile_object

