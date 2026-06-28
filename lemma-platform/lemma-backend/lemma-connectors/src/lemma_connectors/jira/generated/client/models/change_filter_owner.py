from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ChangeFilterOwner")



@_attrs_define
class ChangeFilterOwner:
    """ The account ID of the new owner.

        Attributes:
            account_id (str): The account ID of the new owner.
     """

    account_id: str





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "accountId": account_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        change_filter_owner = cls(
            account_id=account_id,
        )

        return change_filter_owner

