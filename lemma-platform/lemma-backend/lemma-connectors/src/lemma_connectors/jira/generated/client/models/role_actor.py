from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.role_actor_type import RoleActorType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_role_group import ProjectRoleGroup
  from ..models.project_role_user import ProjectRoleUser





T = TypeVar("T", bound="RoleActor")



@_attrs_define
class RoleActor:
    """ Details about a user assigned to a project role.

        Attributes:
            actor_group (ProjectRoleGroup | Unset): Details of the group associated with the role.
            actor_user (ProjectRoleUser | Unset): Details of the user associated with the role.
            avatar_url (str | Unset): The avatar of the role actor.
            display_name (str | Unset): The display name of the role actor. For users, depending on the user’s privacy
                setting, this may return an alternative value for the user's name.
            id (int | Unset): The ID of the role actor.
            name (str | Unset): This property is no longer available and will be removed from the documentation soon. See
                the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-
                api-migration-guide/) for details.
            type_ (RoleActorType | Unset): The type of role actor.
     """

    actor_group: ProjectRoleGroup | Unset = UNSET
    actor_user: ProjectRoleUser | Unset = UNSET
    avatar_url: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: RoleActorType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_role_group import ProjectRoleGroup
        from ..models.project_role_user import ProjectRoleUser
        actor_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actor_group, Unset):
            actor_group = self.actor_group.to_dict()

        actor_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actor_user, Unset):
            actor_user = self.actor_user.to_dict()

        avatar_url = self.avatar_url

        display_name = self.display_name

        id = self.id

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if actor_group is not UNSET:
            field_dict["actorGroup"] = actor_group
        if actor_user is not UNSET:
            field_dict["actorUser"] = actor_user
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_role_group import ProjectRoleGroup
        from ..models.project_role_user import ProjectRoleUser
        d = dict(src_dict)
        _actor_group = d.pop("actorGroup", UNSET)
        actor_group: ProjectRoleGroup | Unset
        if isinstance(_actor_group,  Unset):
            actor_group = UNSET
        else:
            actor_group = ProjectRoleGroup.from_dict(_actor_group)




        _actor_user = d.pop("actorUser", UNSET)
        actor_user: ProjectRoleUser | Unset
        if isinstance(_actor_user,  Unset):
            actor_user = UNSET
        else:
            actor_user = ProjectRoleUser.from_dict(_actor_user)




        avatar_url = d.pop("avatarUrl", UNSET)

        display_name = d.pop("displayName", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RoleActorType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RoleActorType(_type_)




        role_actor = cls(
            actor_group=actor_group,
            actor_user=actor_user,
            avatar_url=avatar_url,
            display_name=display_name,
            id=id,
            name=name,
            type_=type_,
        )

        return role_actor

