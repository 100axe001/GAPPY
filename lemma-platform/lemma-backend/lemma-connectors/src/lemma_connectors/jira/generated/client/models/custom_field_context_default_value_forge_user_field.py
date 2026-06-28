from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.user_filter import UserFilter





T = TypeVar("T", bound="CustomFieldContextDefaultValueForgeUserField")



@_attrs_define
class CustomFieldContextDefaultValueForgeUserField:
    """ Defaults for a Forge user custom field.

        Attributes:
            account_id (str): The ID of the default user.
            context_id (str): The ID of the context.
            type_ (str):
            user_filter (UserFilter): Filter for a User Picker (single) custom field.
     """

    account_id: str
    context_id: str
    type_: str
    user_filter: UserFilter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_filter import UserFilter
        account_id = self.account_id

        context_id = self.context_id

        type_ = self.type_

        user_filter = self.user_filter.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "accountId": account_id,
            "contextId": context_id,
            "type": type_,
            "userFilter": user_filter,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_filter import UserFilter
        d = dict(src_dict)
        account_id = d.pop("accountId")

        context_id = d.pop("contextId")

        type_ = d.pop("type")

        user_filter = UserFilter.from_dict(d.pop("userFilter"))




        custom_field_context_default_value_forge_user_field = cls(
            account_id=account_id,
            context_id=context_id,
            type_=type_,
            user_filter=user_filter,
        )


        custom_field_context_default_value_forge_user_field.additional_properties = d
        return custom_field_context_default_value_forge_user_field

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
