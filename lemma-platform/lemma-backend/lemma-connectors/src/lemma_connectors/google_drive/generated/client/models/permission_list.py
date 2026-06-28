from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.permission import Permission





T = TypeVar("T", bound="PermissionList")



@_attrs_define
class PermissionList:
    """ A list of permissions for a file.

        Attributes:
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#permissionList".
                Default: 'drive#permissionList'.
            next_page_token (str | Unset): The page token for the next page of permissions. This field will be absent if the
                end of the permissions list has been reached. If the token is rejected for any reason, it should be discarded,
                and pagination should be restarted from the first page of results.
            permissions (list[Permission] | Unset): The list of permissions. If nextPageToken is populated, then this list
                may be incomplete and an additional page of results should be fetched.
     """

    kind: str | Unset = 'drive#permissionList'
    next_page_token: str | Unset = UNSET
    permissions: list[Permission] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission import Permission
        kind = self.kind

        next_page_token = self.next_page_token

        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission import Permission
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: list[Permission] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = Permission.from_dict(permissions_item_data)



                permissions.append(permissions_item)


        permission_list = cls(
            kind=kind,
            next_page_token=next_page_token,
            permissions=permissions,
        )


        permission_list.additional_properties = d
        return permission_list

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
