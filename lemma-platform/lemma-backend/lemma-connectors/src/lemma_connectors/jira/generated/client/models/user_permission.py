from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_permission_type import UserPermissionType
from ..types import UNSET, Unset






T = TypeVar("T", bound="UserPermission")



@_attrs_define
class UserPermission:
    """ Details of a permission and its availability to a user.

        Attributes:
            deprecated_key (bool | Unset): Indicate whether the permission key is deprecated. Note that deprecated keys
                cannot be used in the `permissions parameter of Get my permissions. Deprecated keys are not returned by Get all
                permissions.`
            description (str | Unset): The description of the permission.
            have_permission (bool | Unset): Whether the permission is available to the user in the queried context.
            id (str | Unset): The ID of the permission. Either `id` or `key` must be specified. Use [Get all
                permissions](#api-rest-api-3-permissions-get) to get the list of permissions.
            key (str | Unset): The key of the permission. Either `id` or `key` must be specified. Use [Get all
                permissions](#api-rest-api-3-permissions-get) to get the list of permissions.
            name (str | Unset): The name of the permission.
            type_ (UserPermissionType | Unset): The type of the permission.
     """

    deprecated_key: bool | Unset = UNSET
    description: str | Unset = UNSET
    have_permission: bool | Unset = UNSET
    id: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: UserPermissionType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        deprecated_key = self.deprecated_key

        description = self.description

        have_permission = self.have_permission

        id = self.id

        key = self.key

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if deprecated_key is not UNSET:
            field_dict["deprecatedKey"] = deprecated_key
        if description is not UNSET:
            field_dict["description"] = description
        if have_permission is not UNSET:
            field_dict["havePermission"] = have_permission
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deprecated_key = d.pop("deprecatedKey", UNSET)

        description = d.pop("description", UNSET)

        have_permission = d.pop("havePermission", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: UserPermissionType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = UserPermissionType(_type_)




        user_permission = cls(
            deprecated_key=deprecated_key,
            description=description,
            have_permission=have_permission,
            id=id,
            key=key,
            name=name,
            type_=type_,
        )


        user_permission.additional_properties = d
        return user_permission

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
