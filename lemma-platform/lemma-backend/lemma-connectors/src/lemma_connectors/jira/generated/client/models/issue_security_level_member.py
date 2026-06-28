from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.permission_holder import PermissionHolder





T = TypeVar("T", bound="IssueSecurityLevelMember")



@_attrs_define
class IssueSecurityLevelMember:
    """ Issue security level member.

        Attributes:
            holder (PermissionHolder): Details of a user, group, field, or project role that holds a permission. See [Holder
                object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more information.
            id (int): The ID of the issue security level member.
            issue_security_level_id (int): The ID of the issue security level.
     """

    holder: PermissionHolder
    id: int
    issue_security_level_id: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_holder import PermissionHolder
        holder = self.holder.to_dict()

        id = self.id

        issue_security_level_id = self.issue_security_level_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "holder": holder,
            "id": id,
            "issueSecurityLevelId": issue_security_level_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_holder import PermissionHolder
        d = dict(src_dict)
        holder = PermissionHolder.from_dict(d.pop("holder"))




        id = d.pop("id")

        issue_security_level_id = d.pop("issueSecurityLevelId")

        issue_security_level_member = cls(
            holder=holder,
            id=id,
            issue_security_level_id=issue_security_level_id,
        )

        return issue_security_level_member

