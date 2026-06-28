from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UserKey")



@_attrs_define
class UserKey:
    """ List of user account IDs.

        Attributes:
            account_id (str | Unset): The account ID of the user, which uniquely identifies the user across all Atlassian
                products. For example, *5b10ac8d82e05b22cc7d4ef5*. Returns *unknown* if the record is deleted and corrupted, for
                example, as the result of a server import.
            key (str | Unset): This property is no longer available and will be removed from the documentation soon. See the
                [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
                migration-guide/) for details.
     """

    account_id: str | Unset = UNSET
    key: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        key = self.key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        key = d.pop("key", UNSET)

        user_key = cls(
            account_id=account_id,
            key=key,
        )

        return user_key

