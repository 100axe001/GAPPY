from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.usergroup_object import UsergroupObject





T = TypeVar("T", bound="UsergroupsUpdateUsergroupsUpdateSchema")



@_attrs_define
class UsergroupsUpdateUsergroupsUpdateSchema:
    """ Schema for successful response from usergroups.update method

        Attributes:
            ok (bool):
            usergroup (UsergroupObject):
     """

    ok: bool
    usergroup: UsergroupObject





    def to_dict(self) -> dict[str, Any]:
        from ..models.usergroup_object import UsergroupObject
        ok = self.ok

        usergroup = self.usergroup.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "usergroup": usergroup,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usergroup_object import UsergroupObject
        d = dict(src_dict)
        ok = d.pop("ok")

        usergroup = UsergroupObject.from_dict(d.pop("usergroup"))




        usergroups_update_usergroups_update_schema = cls(
            ok=ok,
            usergroup=usergroup,
        )

        return usergroups_update_usergroups_update_schema

