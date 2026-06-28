from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.usergroup_object_prefs import UsergroupObjectPrefs





T = TypeVar("T", bound="UsergroupObject")



@_attrs_define
class UsergroupObject:
    """ 
        Attributes:
            auto_provision (bool):
            auto_type (Any):
            created_by (str):
            date_create (int):
            date_delete (int):
            date_update (int):
            deleted_by (Any):
            description (str):
            enterprise_subteam_id (str):
            handle (str):
            id (str):
            is_external (bool):
            is_subteam (bool):
            is_usergroup (bool):
            name (str):
            prefs (UsergroupObjectPrefs):
            team_id (str):
            updated_by (str):
            channel_count (int | Unset):
            user_count (int | Unset):
            users (list[str] | Unset):
     """

    auto_provision: bool
    auto_type: Any
    created_by: str
    date_create: int
    date_delete: int
    date_update: int
    deleted_by: Any
    description: str
    enterprise_subteam_id: str
    handle: str
    id: str
    is_external: bool
    is_subteam: bool
    is_usergroup: bool
    name: str
    prefs: UsergroupObjectPrefs
    team_id: str
    updated_by: str
    channel_count: int | Unset = UNSET
    user_count: int | Unset = UNSET
    users: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.usergroup_object_prefs import UsergroupObjectPrefs
        auto_provision = self.auto_provision

        auto_type = self.auto_type

        created_by = self.created_by

        date_create = self.date_create

        date_delete = self.date_delete

        date_update = self.date_update

        deleted_by = self.deleted_by

        description = self.description

        enterprise_subteam_id = self.enterprise_subteam_id

        handle = self.handle

        id = self.id

        is_external = self.is_external

        is_subteam = self.is_subteam

        is_usergroup = self.is_usergroup

        name = self.name

        prefs = self.prefs.to_dict()

        team_id = self.team_id

        updated_by = self.updated_by

        channel_count = self.channel_count

        user_count = self.user_count

        users: list[str] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "auto_provision": auto_provision,
            "auto_type": auto_type,
            "created_by": created_by,
            "date_create": date_create,
            "date_delete": date_delete,
            "date_update": date_update,
            "deleted_by": deleted_by,
            "description": description,
            "enterprise_subteam_id": enterprise_subteam_id,
            "handle": handle,
            "id": id,
            "is_external": is_external,
            "is_subteam": is_subteam,
            "is_usergroup": is_usergroup,
            "name": name,
            "prefs": prefs,
            "team_id": team_id,
            "updated_by": updated_by,
        })
        if channel_count is not UNSET:
            field_dict["channel_count"] = channel_count
        if user_count is not UNSET:
            field_dict["user_count"] = user_count
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usergroup_object_prefs import UsergroupObjectPrefs
        d = dict(src_dict)
        auto_provision = d.pop("auto_provision")

        auto_type = d.pop("auto_type")

        created_by = d.pop("created_by")

        date_create = d.pop("date_create")

        date_delete = d.pop("date_delete")

        date_update = d.pop("date_update")

        deleted_by = d.pop("deleted_by")

        description = d.pop("description")

        enterprise_subteam_id = d.pop("enterprise_subteam_id")

        handle = d.pop("handle")

        id = d.pop("id")

        is_external = d.pop("is_external")

        is_subteam = d.pop("is_subteam")

        is_usergroup = d.pop("is_usergroup")

        name = d.pop("name")

        prefs = UsergroupObjectPrefs.from_dict(d.pop("prefs"))




        team_id = d.pop("team_id")

        updated_by = d.pop("updated_by")

        channel_count = d.pop("channel_count", UNSET)

        user_count = d.pop("user_count", UNSET)

        users = cast(list[str], d.pop("users", UNSET))


        usergroup_object = cls(
            auto_provision=auto_provision,
            auto_type=auto_type,
            created_by=created_by,
            date_create=date_create,
            date_delete=date_delete,
            date_update=date_update,
            deleted_by=deleted_by,
            description=description,
            enterprise_subteam_id=enterprise_subteam_id,
            handle=handle,
            id=id,
            is_external=is_external,
            is_subteam=is_subteam,
            is_usergroup=is_usergroup,
            name=name,
            prefs=prefs,
            team_id=team_id,
            updated_by=updated_by,
            channel_count=channel_count,
            user_count=user_count,
            users=users,
        )

        return usergroup_object

