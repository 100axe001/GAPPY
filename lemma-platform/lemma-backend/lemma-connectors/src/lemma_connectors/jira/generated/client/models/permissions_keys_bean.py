from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PermissionsKeysBean")



@_attrs_define
class PermissionsKeysBean:
    """ 
        Attributes:
            permissions (list[str]): A list of permission keys.
     """

    permissions: list[str]





    def to_dict(self) -> dict[str, Any]:
        permissions = self.permissions




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "permissions": permissions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = cast(list[str], d.pop("permissions"))


        permissions_keys_bean = cls(
            permissions=permissions,
        )

        return permissions_keys_bean

