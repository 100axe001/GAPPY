from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scope import Scope





T = TypeVar("T", bound="ProjectRoleDetails")



@_attrs_define
class ProjectRoleDetails:
    """ Details about a project role.

        Attributes:
            admin (bool | Unset): Whether this role is the admin role for the project.
            default (bool | Unset): Whether this role is the default role for the project.
            description (str | Unset): The description of the project role.
            id (int | Unset): The ID of the project role.
            name (str | Unset): The name of the project role.
            role_configurable (bool | Unset): Whether the roles are configurable for this project.
            scope (Scope | Unset): The projects the item is associated with. Indicated for items associated with [next-gen
                projects](https://confluence.atlassian.com/x/loMyO).
            self_ (str | Unset): The URL the project role details.
            translated_name (str | Unset): The translated name of the project role.
     """

    admin: bool | Unset = UNSET
    default: bool | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    role_configurable: bool | Unset = UNSET
    scope: Scope | Unset = UNSET
    self_: str | Unset = UNSET
    translated_name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.scope import Scope
        admin = self.admin

        default = self.default

        description = self.description

        id = self.id

        name = self.name

        role_configurable = self.role_configurable

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        self_ = self.self_

        translated_name = self.translated_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if admin is not UNSET:
            field_dict["admin"] = admin
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if role_configurable is not UNSET:
            field_dict["roleConfigurable"] = role_configurable
        if scope is not UNSET:
            field_dict["scope"] = scope
        if self_ is not UNSET:
            field_dict["self"] = self_
        if translated_name is not UNSET:
            field_dict["translatedName"] = translated_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scope import Scope
        d = dict(src_dict)
        admin = d.pop("admin", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        role_configurable = d.pop("roleConfigurable", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = Scope.from_dict(_scope)




        self_ = d.pop("self", UNSET)

        translated_name = d.pop("translatedName", UNSET)

        project_role_details = cls(
            admin=admin,
            default=default,
            description=description,
            id=id,
            name=name,
            role_configurable=role_configurable,
            scope=scope,
            self_=self_,
            translated_name=translated_name,
        )

        return project_role_details

