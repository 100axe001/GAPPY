from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_project_details_assignee_type import CreateProjectDetailsAssigneeType
from ..models.create_project_details_project_template_key import CreateProjectDetailsProjectTemplateKey
from ..models.create_project_details_project_type_key import CreateProjectDetailsProjectTypeKey
from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateProjectDetails")



@_attrs_define
class CreateProjectDetails:
    """ Details about the project.

        Attributes:
            key (str): Project keys must be unique and start with an uppercase letter followed by one or more uppercase
                alphanumeric characters. The maximum length is 10 characters.
            name (str): The name of the project.
            assignee_type (CreateProjectDetailsAssigneeType | Unset): The default assignee when creating issues for this
                project.
            avatar_id (int | Unset): An integer value for the project's avatar.
            category_id (int | Unset): The ID of the project's category. A complete list of category IDs is found using the
                [Get all project categories](#api-rest-api-3-projectCategory-get) operation.
            description (str | Unset): A brief description of the project.
            field_configuration_scheme (int | Unset): The ID of the field configuration scheme for the project. Use the [Get
                all field configuration schemes](#api-rest-api-3-fieldconfigurationscheme-get) operation to get a list of field
                configuration scheme IDs. If you specify the field configuration scheme you cannot specify the project template
                key.
            issue_security_scheme (int | Unset): The ID of the issue security scheme for the project, which enables you to
                control who can and cannot view issues. Use the [Get issue security schemes](#api-rest-
                api-3-issuesecurityschemes-get) resource to get all issue security scheme IDs.
            issue_type_scheme (int | Unset): The ID of the issue type scheme for the project. Use the [Get all issue type
                schemes](#api-rest-api-3-issuetypescheme-get) operation to get a list of issue type scheme IDs. If you specify
                the issue type scheme you cannot specify the project template key.
            issue_type_screen_scheme (int | Unset): The ID of the issue type screen scheme for the project. Use the [Get all
                issue type screen schemes](#api-rest-api-3-issuetypescreenscheme-get) operation to get a list of issue type
                screen scheme IDs. If you specify the issue type screen scheme you cannot specify the project template key.
            lead (str | Unset): This parameter is deprecated because of privacy changes. Use `leadAccountId` instead. See
                the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
                migration-guide/) for details. The user name of the project lead. Either `lead` or `leadAccountId` must be set
                when creating a project. Cannot be provided with `leadAccountId`.
            lead_account_id (str | Unset): The account ID of the project lead. Either `lead` or `leadAccountId` must be set
                when creating a project. Cannot be provided with `lead`.
            notification_scheme (int | Unset): The ID of the notification scheme for the project. Use the [Get notification
                schemes](#api-rest-api-3-notificationscheme-get) resource to get a list of notification scheme IDs.
            permission_scheme (int | Unset): The ID of the permission scheme for the project. Use the [Get all permission
                schemes](#api-rest-api-3-permissionscheme-get) resource to see a list of all permission scheme IDs.
            project_template_key (CreateProjectDetailsProjectTemplateKey | Unset): A predefined configuration for a project.
                The type of the `projectTemplateKey` must match with the type of the `projectTypeKey`.
            project_type_key (CreateProjectDetailsProjectTypeKey | Unset): The [project
                type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes), which
                defines the application-specific feature set. If you don't specify the project template you have to specify the
                project type.
            url (str | Unset): A link to information about this project, such as project documentation
            workflow_scheme (int | Unset): The ID of the workflow scheme for the project. Use the [Get all workflow
                schemes](#api-rest-api-3-workflowscheme-get) operation to get a list of workflow scheme IDs. If you specify the
                workflow scheme you cannot specify the project template key.
     """

    key: str
    name: str
    assignee_type: CreateProjectDetailsAssigneeType | Unset = UNSET
    avatar_id: int | Unset = UNSET
    category_id: int | Unset = UNSET
    description: str | Unset = UNSET
    field_configuration_scheme: int | Unset = UNSET
    issue_security_scheme: int | Unset = UNSET
    issue_type_scheme: int | Unset = UNSET
    issue_type_screen_scheme: int | Unset = UNSET
    lead: str | Unset = UNSET
    lead_account_id: str | Unset = UNSET
    notification_scheme: int | Unset = UNSET
    permission_scheme: int | Unset = UNSET
    project_template_key: CreateProjectDetailsProjectTemplateKey | Unset = UNSET
    project_type_key: CreateProjectDetailsProjectTypeKey | Unset = UNSET
    url: str | Unset = UNSET
    workflow_scheme: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        assignee_type: str | Unset = UNSET
        if not isinstance(self.assignee_type, Unset):
            assignee_type = self.assignee_type.value


        avatar_id = self.avatar_id

        category_id = self.category_id

        description = self.description

        field_configuration_scheme = self.field_configuration_scheme

        issue_security_scheme = self.issue_security_scheme

        issue_type_scheme = self.issue_type_scheme

        issue_type_screen_scheme = self.issue_type_screen_scheme

        lead = self.lead

        lead_account_id = self.lead_account_id

        notification_scheme = self.notification_scheme

        permission_scheme = self.permission_scheme

        project_template_key: str | Unset = UNSET
        if not isinstance(self.project_template_key, Unset):
            project_template_key = self.project_template_key.value


        project_type_key: str | Unset = UNSET
        if not isinstance(self.project_type_key, Unset):
            project_type_key = self.project_type_key.value


        url = self.url

        workflow_scheme = self.workflow_scheme


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "name": name,
        })
        if assignee_type is not UNSET:
            field_dict["assigneeType"] = assignee_type
        if avatar_id is not UNSET:
            field_dict["avatarId"] = avatar_id
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if description is not UNSET:
            field_dict["description"] = description
        if field_configuration_scheme is not UNSET:
            field_dict["fieldConfigurationScheme"] = field_configuration_scheme
        if issue_security_scheme is not UNSET:
            field_dict["issueSecurityScheme"] = issue_security_scheme
        if issue_type_scheme is not UNSET:
            field_dict["issueTypeScheme"] = issue_type_scheme
        if issue_type_screen_scheme is not UNSET:
            field_dict["issueTypeScreenScheme"] = issue_type_screen_scheme
        if lead is not UNSET:
            field_dict["lead"] = lead
        if lead_account_id is not UNSET:
            field_dict["leadAccountId"] = lead_account_id
        if notification_scheme is not UNSET:
            field_dict["notificationScheme"] = notification_scheme
        if permission_scheme is not UNSET:
            field_dict["permissionScheme"] = permission_scheme
        if project_template_key is not UNSET:
            field_dict["projectTemplateKey"] = project_template_key
        if project_type_key is not UNSET:
            field_dict["projectTypeKey"] = project_type_key
        if url is not UNSET:
            field_dict["url"] = url
        if workflow_scheme is not UNSET:
            field_dict["workflowScheme"] = workflow_scheme

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        _assignee_type = d.pop("assigneeType", UNSET)
        assignee_type: CreateProjectDetailsAssigneeType | Unset
        if isinstance(_assignee_type,  Unset):
            assignee_type = UNSET
        else:
            assignee_type = CreateProjectDetailsAssigneeType(_assignee_type)




        avatar_id = d.pop("avatarId", UNSET)

        category_id = d.pop("categoryId", UNSET)

        description = d.pop("description", UNSET)

        field_configuration_scheme = d.pop("fieldConfigurationScheme", UNSET)

        issue_security_scheme = d.pop("issueSecurityScheme", UNSET)

        issue_type_scheme = d.pop("issueTypeScheme", UNSET)

        issue_type_screen_scheme = d.pop("issueTypeScreenScheme", UNSET)

        lead = d.pop("lead", UNSET)

        lead_account_id = d.pop("leadAccountId", UNSET)

        notification_scheme = d.pop("notificationScheme", UNSET)

        permission_scheme = d.pop("permissionScheme", UNSET)

        _project_template_key = d.pop("projectTemplateKey", UNSET)
        project_template_key: CreateProjectDetailsProjectTemplateKey | Unset
        if isinstance(_project_template_key,  Unset):
            project_template_key = UNSET
        else:
            project_template_key = CreateProjectDetailsProjectTemplateKey(_project_template_key)




        _project_type_key = d.pop("projectTypeKey", UNSET)
        project_type_key: CreateProjectDetailsProjectTypeKey | Unset
        if isinstance(_project_type_key,  Unset):
            project_type_key = UNSET
        else:
            project_type_key = CreateProjectDetailsProjectTypeKey(_project_type_key)




        url = d.pop("url", UNSET)

        workflow_scheme = d.pop("workflowScheme", UNSET)

        create_project_details = cls(
            key=key,
            name=name,
            assignee_type=assignee_type,
            avatar_id=avatar_id,
            category_id=category_id,
            description=description,
            field_configuration_scheme=field_configuration_scheme,
            issue_security_scheme=issue_security_scheme,
            issue_type_scheme=issue_type_scheme,
            issue_type_screen_scheme=issue_type_screen_scheme,
            lead=lead,
            lead_account_id=lead_account_id,
            notification_scheme=notification_scheme,
            permission_scheme=permission_scheme,
            project_template_key=project_template_key,
            project_type_key=project_type_key,
            url=url,
            workflow_scheme=workflow_scheme,
        )

        return create_project_details

