from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_role_actors_update_bean_categorised_actors import ProjectRoleActorsUpdateBeanCategorisedActors





T = TypeVar("T", bound="ProjectRoleActorsUpdateBean")



@_attrs_define
class ProjectRoleActorsUpdateBean:
    """ 
        Attributes:
            categorised_actors (ProjectRoleActorsUpdateBeanCategorisedActors | Unset): The actors to add to the project
                role.

                Add groups using:

                 *  `atlassian-group-role-actor` and a list of group names.
                 *  `atlassian-group-role-actor-id` and a list of group IDs.

                As a group's name can change, use of `atlassian-group-role-actor-id` is recommended. For example, `"atlassian-
                group-role-actor-id":["eef79f81-0b89-4fca-a736-4be531a10869","77f6ab39-e755-4570-a6ae-2d7a8df0bcb8"]`.

                Add users using `atlassian-user-role-actor` and a list of account IDs. For example, `"atlassian-user-role-
                actor":["12345678-9abc-def1-2345-6789abcdef12", "abcdef12-3456-789a-bcde-f123456789ab"]`.
            id (int | Unset): The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a
                list of project role IDs.
     """

    categorised_actors: ProjectRoleActorsUpdateBeanCategorisedActors | Unset = UNSET
    id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_role_actors_update_bean_categorised_actors import ProjectRoleActorsUpdateBeanCategorisedActors
        categorised_actors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.categorised_actors, Unset):
            categorised_actors = self.categorised_actors.to_dict()

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if categorised_actors is not UNSET:
            field_dict["categorisedActors"] = categorised_actors
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_role_actors_update_bean_categorised_actors import ProjectRoleActorsUpdateBeanCategorisedActors
        d = dict(src_dict)
        _categorised_actors = d.pop("categorisedActors", UNSET)
        categorised_actors: ProjectRoleActorsUpdateBeanCategorisedActors | Unset
        if isinstance(_categorised_actors,  Unset):
            categorised_actors = UNSET
        else:
            categorised_actors = ProjectRoleActorsUpdateBeanCategorisedActors.from_dict(_categorised_actors)




        id = d.pop("id", UNSET)

        project_role_actors_update_bean = cls(
            categorised_actors=categorised_actors,
            id=id,
        )

        return project_role_actors_update_bean

