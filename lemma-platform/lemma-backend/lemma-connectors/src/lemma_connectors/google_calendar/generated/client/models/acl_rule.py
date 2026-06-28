from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.acl_rule_scope import AclRuleScope





T = TypeVar("T", bound="AclRule")



@_attrs_define
class AclRule:
    """ 
        Attributes:
            etag (str | Unset): ETag of the resource.
            id (str | Unset): Identifier of the Access Control List (ACL) rule. See Sharing calendars.
            kind (str | Unset): Type of the resource ("calendar#aclRule"). Default: 'calendar#aclRule'.
            role (str | Unset): The role assigned to the scope. Possible values are:
                - "none" - Provides no access.
                - "freeBusyReader" - Provides read access to free/busy information.
                - "reader" - Provides read access to the calendar. Private events will appear to users with reader access, but
                event details will be hidden.
                - "writer" - Provides read and write access to the calendar. Private events will appear to users with writer
                access, and event details will be visible.
                - "owner" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the
                additional ability to see and manipulate ACLs.
            scope (AclRuleScope | Unset): The extent to which calendar access is granted by this ACL rule.
     """

    etag: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'calendar#aclRule'
    role: str | Unset = UNSET
    scope: AclRuleScope | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.acl_rule_scope import AclRuleScope
        etag = self.etag

        id = self.id

        kind = self.kind

        role = self.role

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if role is not UNSET:
            field_dict["role"] = role
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acl_rule_scope import AclRuleScope
        d = dict(src_dict)
        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        role = d.pop("role", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: AclRuleScope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = AclRuleScope.from_dict(_scope)




        acl_rule = cls(
            etag=etag,
            id=id,
            kind=kind,
            role=role,
            scope=scope,
        )


        acl_rule.additional_properties = d
        return acl_rule

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
