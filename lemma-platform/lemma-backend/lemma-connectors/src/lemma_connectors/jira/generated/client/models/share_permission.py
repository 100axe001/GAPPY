from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.share_permission_type import SharePermissionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.group_name import GroupName
  from ..models.project import Project
  from ..models.project_role import ProjectRole
  from ..models.user_bean import UserBean





T = TypeVar("T", bound="SharePermission")



@_attrs_define
class SharePermission:
    """ Details of a share permission for the filter.

        Attributes:
            type_ (SharePermissionType): The type of share permission:

                 *  `user` Shared with a user.
                 *  `group` Shared with a group. If set in a request, then specify `sharePermission.group` as well.
                 *  `project` Shared with a project. If set in a request, then specify `sharePermission.project` as well.
                 *  `projectRole` Share with a project role in a project. This value is not returned in responses. It is used in
                requests, where it needs to be specify with `projectId` and `projectRoleId`.
                 *  `global` Shared globally. If set in a request, no other `sharePermission` properties need to be specified.
                 *  `loggedin` Shared with all logged-in users. Note: This value is set in a request by specifying
                `authenticated` as the `type`.
                 *  `project-unknown` Shared with a project that the user does not have access to. Cannot be set in a request.
            group (GroupName | Unset): Details about a group.
            id (int | Unset): The unique identifier of the share permission.
            project (Project | Unset): Details about a project.
            role (ProjectRole | Unset): Details about the roles in a project.
            user (UserBean | Unset):
     """

    type_: SharePermissionType
    group: GroupName | Unset = UNSET
    id: int | Unset = UNSET
    project: Project | Unset = UNSET
    role: ProjectRole | Unset = UNSET
    user: UserBean | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.group_name import GroupName
        from ..models.project import Project
        from ..models.project_role import ProjectRole
        from ..models.user_bean import UserBean
        type_ = self.type_.value

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        id = self.id

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if project is not UNSET:
            field_dict["project"] = project
        if role is not UNSET:
            field_dict["role"] = role
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_name import GroupName
        from ..models.project import Project
        from ..models.project_role import ProjectRole
        from ..models.user_bean import UserBean
        d = dict(src_dict)
        type_ = SharePermissionType(d.pop("type"))




        _group = d.pop("group", UNSET)
        group: GroupName | Unset
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = GroupName.from_dict(_group)




        id = d.pop("id", UNSET)

        _project = d.pop("project", UNSET)
        project: Project | Unset
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)




        _role = d.pop("role", UNSET)
        role: ProjectRole | Unset
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = ProjectRole.from_dict(_role)




        _user = d.pop("user", UNSET)
        user: UserBean | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = UserBean.from_dict(_user)




        share_permission = cls(
            type_=type_,
            group=group,
            id=id,
            project=project,
            role=role,
            user=user,
        )

        return share_permission

