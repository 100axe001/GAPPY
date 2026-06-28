from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IdBean")



@_attrs_define
class IdBean:
    """ 
        Attributes:
            id (int): The ID of the permission scheme to associate with the project. Use the [Get all permission
                schemes](#api-rest-api-3-permissionscheme-get) resource to get a list of permission scheme IDs.
     """

    id: int





    def to_dict(self) -> dict[str, Any]:
        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        id_bean = cls(
            id=id,
        )

        return id_bean

