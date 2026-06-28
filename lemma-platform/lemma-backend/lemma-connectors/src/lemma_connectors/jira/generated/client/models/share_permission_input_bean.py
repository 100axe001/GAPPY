from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.share_permission_input_bean_type import SharePermissionInputBeanType
from ..types import UNSET, Unset






T = TypeVar("T", bound="SharePermissionInputBean")



@_attrs_define
class SharePermissionInputBean:
    """ 
        Attributes:
            type_ (SharePermissionInputBeanType): The type of the share permission.Specify the type as follows:

                 *  `user` Share with a user.
                 *  `group` Share with a group. Specify `groupname` as well.
                 *  `project` Share with a project. Specify `projectId` as well.
                 *  `projectRole` Share with a project role in a project. Specify `projectId` and `projectRoleId` as well.
                 *  `global` Share globally, including anonymous users. If set, this type overrides all existing share
                permissions and must be deleted before any non-global share permissions is set.
                 *  `authenticated` Share with all logged-in users. This shows as `loggedin` in the response. If set, this type
                overrides all existing share permissions and must be deleted before any non-global share permissions is set.
            account_id (str | Unset): The user account ID that the filter is shared with. For a request, specify the
                `accountId` property for the user.
            group_id (str | Unset): The ID of the group, which uniquely identifies the group across all Atlassian
                products.For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*. Cannot be provided with `groupname`.
            groupname (str | Unset): The name of the group to share the filter with. Set `type` to `group`. Please note that
                the name of a group is mutable, to reliably identify a group use `groupId`.
            project_id (str | Unset): The ID of the project to share the filter with. Set `type` to `project`.
            project_role_id (str | Unset): The ID of the project role to share the filter with. Set `type` to `projectRole`
                and the `projectId` for the project that the role is in.
            rights (int | Unset): The rights for the share permission.
     """

    type_: SharePermissionInputBeanType
    account_id: str | Unset = UNSET
    group_id: str | Unset = UNSET
    groupname: str | Unset = UNSET
    project_id: str | Unset = UNSET
    project_role_id: str | Unset = UNSET
    rights: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        account_id = self.account_id

        group_id = self.group_id

        groupname = self.groupname

        project_id = self.project_id

        project_role_id = self.project_role_id

        rights = self.rights


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if groupname is not UNSET:
            field_dict["groupname"] = groupname
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_role_id is not UNSET:
            field_dict["projectRoleId"] = project_role_id
        if rights is not UNSET:
            field_dict["rights"] = rights

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SharePermissionInputBeanType(d.pop("type"))




        account_id = d.pop("accountId", UNSET)

        group_id = d.pop("groupId", UNSET)

        groupname = d.pop("groupname", UNSET)

        project_id = d.pop("projectId", UNSET)

        project_role_id = d.pop("projectRoleId", UNSET)

        rights = d.pop("rights", UNSET)

        share_permission_input_bean = cls(
            type_=type_,
            account_id=account_id,
            group_id=group_id,
            groupname=groupname,
            project_id=project_id,
            project_role_id=project_role_id,
            rights=rights,
        )

        return share_permission_input_bean

