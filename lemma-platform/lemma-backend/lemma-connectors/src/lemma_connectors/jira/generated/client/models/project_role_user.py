from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProjectRoleUser")



@_attrs_define
class ProjectRoleUser:
    """ Details of the user associated with the role.

        Attributes:
            account_id (str | Unset): The account ID of the user, which uniquely identifies the user across all Atlassian
                products. For example, *5b10ac8d82e05b22cc7d4ef5*. Returns *unknown* if the record is deleted and corrupted, for
                example, as the result of a server import.
     """

    account_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        project_role_user = cls(
            account_id=account_id,
        )

        return project_role_user

