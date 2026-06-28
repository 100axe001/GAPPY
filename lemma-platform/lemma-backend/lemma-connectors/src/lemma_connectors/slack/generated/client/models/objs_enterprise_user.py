from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ObjsEnterpriseUser")



@_attrs_define
class ObjsEnterpriseUser:
    """ 
        Attributes:
            enterprise_id (str):
            enterprise_name (str):
            id (str):
            is_admin (bool):
            is_owner (bool):
            teams (list[str]):
     """

    enterprise_id: str
    enterprise_name: str
    id: str
    is_admin: bool
    is_owner: bool
    teams: list[str]





    def to_dict(self) -> dict[str, Any]:
        enterprise_id = self.enterprise_id

        enterprise_name = self.enterprise_name

        id = self.id

        is_admin = self.is_admin

        is_owner = self.is_owner

        teams = self.teams




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "enterprise_id": enterprise_id,
            "enterprise_name": enterprise_name,
            "id": id,
            "is_admin": is_admin,
            "is_owner": is_owner,
            "teams": teams,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enterprise_id = d.pop("enterprise_id")

        enterprise_name = d.pop("enterprise_name")

        id = d.pop("id")

        is_admin = d.pop("is_admin")

        is_owner = d.pop("is_owner")

        teams = cast(list[str], d.pop("teams"))


        objs_enterprise_user = cls(
            enterprise_id=enterprise_id,
            enterprise_name=enterprise_name,
            id=id,
            is_admin=is_admin,
            is_owner=is_owner,
            teams=teams,
        )

        return objs_enterprise_user

