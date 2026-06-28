from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_project_details_assignee_type import UpdateProjectDetailsAssigneeType
from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateProjectDetails")



@_attrs_define
class UpdateProjectDetails:
    """ Details about the project.

        Attributes:
            assignee_type (UpdateProjectDetailsAssigneeType | Unset): The default assignee when creating issues for this
                project.
            avatar_id (int | Unset): An integer value for the project's avatar.
            category_id (int | Unset): The ID of the project's category. A complete list of category IDs is found using the
                [Get all project categories](#api-rest-api-3-projectCategory-get) operation. To remove the project category from
                the project, set the value to `-1.`
            description (str | Unset): A brief description of the project.
            issue_security_scheme (int | Unset): The ID of the issue security scheme for the project, which enables you to
                control who can and cannot view issues. Use the [Get issue security schemes](#api-rest-
                api-3-issuesecurityschemes-get) resource to get all issue security scheme IDs.
            key (str | Unset): Project keys must be unique and start with an uppercase letter followed by one or more
                uppercase alphanumeric characters. The maximum length is 10 characters.
            lead (str | Unset): This parameter is deprecated because of privacy changes. Use `leadAccountId` instead. See
                the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
                migration-guide/) for details. The user name of the project lead. Cannot be provided with `leadAccountId`.
            lead_account_id (str | Unset): The account ID of the project lead. Cannot be provided with `lead`.
            name (str | Unset): The name of the project.
            notification_scheme (int | Unset): The ID of the notification scheme for the project. Use the [Get notification
                schemes](#api-rest-api-3-notificationscheme-get) resource to get a list of notification scheme IDs.
            permission_scheme (int | Unset): The ID of the permission scheme for the project. Use the [Get all permission
                schemes](#api-rest-api-3-permissionscheme-get) resource to see a list of all permission scheme IDs.
            url (str | Unset): A link to information about this project, such as project documentation
     """

    assignee_type: UpdateProjectDetailsAssigneeType | Unset = UNSET
    avatar_id: int | Unset = UNSET
    category_id: int | Unset = UNSET
    description: str | Unset = UNSET
    issue_security_scheme: int | Unset = UNSET
    key: str | Unset = UNSET
    lead: str | Unset = UNSET
    lead_account_id: str | Unset = UNSET
    name: str | Unset = UNSET
    notification_scheme: int | Unset = UNSET
    permission_scheme: int | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        assignee_type: str | Unset = UNSET
        if not isinstance(self.assignee_type, Unset):
            assignee_type = self.assignee_type.value


        avatar_id = self.avatar_id

        category_id = self.category_id

        description = self.description

        issue_security_scheme = self.issue_security_scheme

        key = self.key

        lead = self.lead

        lead_account_id = self.lead_account_id

        name = self.name

        notification_scheme = self.notification_scheme

        permission_scheme = self.permission_scheme

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignee_type is not UNSET:
            field_dict["assigneeType"] = assignee_type
        if avatar_id is not UNSET:
            field_dict["avatarId"] = avatar_id
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if description is not UNSET:
            field_dict["description"] = description
        if issue_security_scheme is not UNSET:
            field_dict["issueSecurityScheme"] = issue_security_scheme
        if key is not UNSET:
            field_dict["key"] = key
        if lead is not UNSET:
            field_dict["lead"] = lead
        if lead_account_id is not UNSET:
            field_dict["leadAccountId"] = lead_account_id
        if name is not UNSET:
            field_dict["name"] = name
        if notification_scheme is not UNSET:
            field_dict["notificationScheme"] = notification_scheme
        if permission_scheme is not UNSET:
            field_dict["permissionScheme"] = permission_scheme
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _assignee_type = d.pop("assigneeType", UNSET)
        assignee_type: UpdateProjectDetailsAssigneeType | Unset
        if isinstance(_assignee_type,  Unset):
            assignee_type = UNSET
        else:
            assignee_type = UpdateProjectDetailsAssigneeType(_assignee_type)




        avatar_id = d.pop("avatarId", UNSET)

        category_id = d.pop("categoryId", UNSET)

        description = d.pop("description", UNSET)

        issue_security_scheme = d.pop("issueSecurityScheme", UNSET)

        key = d.pop("key", UNSET)

        lead = d.pop("lead", UNSET)

        lead_account_id = d.pop("leadAccountId", UNSET)

        name = d.pop("name", UNSET)

        notification_scheme = d.pop("notificationScheme", UNSET)

        permission_scheme = d.pop("permissionScheme", UNSET)

        url = d.pop("url", UNSET)

        update_project_details = cls(
            assignee_type=assignee_type,
            avatar_id=avatar_id,
            category_id=category_id,
            description=description,
            issue_security_scheme=issue_security_scheme,
            key=key,
            lead=lead,
            lead_account_id=lead_account_id,
            name=name,
            notification_scheme=notification_scheme,
            permission_scheme=permission_scheme,
            url=url,
        )

        return update_project_details

