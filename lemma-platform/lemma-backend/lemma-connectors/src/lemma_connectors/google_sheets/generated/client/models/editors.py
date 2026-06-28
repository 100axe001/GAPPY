from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Editors")



@_attrs_define
class Editors:
    """ The editors of a protected range.

        Attributes:
            domain_users_can_edit (bool | Unset): True if anyone in the document's domain has edit access to the protected
                range. Domain protection is only supported on documents within a domain.
            groups (list[str] | Unset): The email addresses of groups with edit access to the protected range.
            users (list[str] | Unset): The email addresses of users with edit access to the protected range.
     """

    domain_users_can_edit: bool | Unset = UNSET
    groups: list[str] | Unset = UNSET
    users: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        domain_users_can_edit = self.domain_users_can_edit

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups



        users: list[str] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if domain_users_can_edit is not UNSET:
            field_dict["domainUsersCanEdit"] = domain_users_can_edit
        if groups is not UNSET:
            field_dict["groups"] = groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_users_can_edit = d.pop("domainUsersCanEdit", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))


        users = cast(list[str], d.pop("users", UNSET))


        editors = cls(
            domain_users_can_edit=domain_users_can_edit,
            groups=groups,
            users=users,
        )


        editors.additional_properties = d
        return editors

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
