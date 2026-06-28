from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UserMigrationBean")



@_attrs_define
class UserMigrationBean:
    """ 
        Attributes:
            account_id (str | Unset):
            key (str | Unset):
            username (str | Unset):
     """

    account_id: str | Unset = UNSET
    key: str | Unset = UNSET
    username: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        key = self.key

        username = self.username


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if key is not UNSET:
            field_dict["key"] = key
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        key = d.pop("key", UNSET)

        username = d.pop("username", UNSET)

        user_migration_bean = cls(
            account_id=account_id,
            key=key,
            username=username,
        )

        return user_migration_bean

