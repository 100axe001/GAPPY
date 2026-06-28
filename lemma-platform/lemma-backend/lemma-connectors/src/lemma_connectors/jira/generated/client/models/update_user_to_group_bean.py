from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateUserToGroupBean")



@_attrs_define
class UpdateUserToGroupBean:
    """ 
        Attributes:
            account_id (str | Unset): The account ID of the user, which uniquely identifies the user across all Atlassian
                products. For example, *5b10ac8d82e05b22cc7d4ef5*.
            name (str | Unset): This property is no longer available. See the [deprecation
                notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-
                guide/) for details.
     """

    account_id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        name = d.pop("name", UNSET)

        update_user_to_group_bean = cls(
            account_id=account_id,
            name=name,
        )


        update_user_to_group_bean.additional_properties = d
        return update_user_to_group_bean

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
