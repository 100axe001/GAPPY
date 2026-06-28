from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AclRuleScope")



@_attrs_define
class AclRuleScope:
    """ The extent to which calendar access is granted by this ACL rule.

        Attributes:
            type_ (str | Unset): The type of the scope. Possible values are:
                - "default" - The public scope. This is the default value.
                - "user" - Limits the scope to a single user.
                - "group" - Limits the scope to a group.
                - "domain" - Limits the scope to a domain.  Note: The permissions granted to the "default", or public, scope
                apply to any user, authenticated or not.
            value (str | Unset): The email address of a user or group, or the name of a domain, depending on the scope type.
                Omitted for type "default".
     """

    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        acl_rule_scope = cls(
            type_=type_,
            value=value,
        )


        acl_rule_scope.additional_properties = d
        return acl_rule_scope

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
