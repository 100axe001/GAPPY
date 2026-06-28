from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ProjectRoleActorsUpdateBeanCategorisedActors")



@_attrs_define
class ProjectRoleActorsUpdateBeanCategorisedActors:
    """ The actors to add to the project role.

    Add groups using:

     *  `atlassian-group-role-actor` and a list of group names.
     *  `atlassian-group-role-actor-id` and a list of group IDs.

    As a group's name can change, use of `atlassian-group-role-actor-id` is recommended. For example, `"atlassian-group-
    role-actor-id":["eef79f81-0b89-4fca-a736-4be531a10869","77f6ab39-e755-4570-a6ae-2d7a8df0bcb8"]`.

    Add users using `atlassian-user-role-actor` and a list of account IDs. For example, `"atlassian-user-role-
    actor":["12345678-9abc-def1-2345-6789abcdef12", "abcdef12-3456-789a-bcde-f123456789ab"]`.

     """

    additional_properties: dict[str, list[str]] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop




        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_role_actors_update_bean_categorised_actors = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(list[str], prop_dict)

            additional_properties[prop_name] = additional_property

        project_role_actors_update_bean_categorised_actors.additional_properties = additional_properties
        return project_role_actors_update_bean_categorised_actors

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
