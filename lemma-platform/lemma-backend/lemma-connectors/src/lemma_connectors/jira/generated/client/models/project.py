from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.project_assignee_type import ProjectAssigneeType
from ..models.project_project_type_key import ProjectProjectTypeKey
from ..models.project_style import ProjectStyle
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.avatar_urls_bean import AvatarUrlsBean
  from ..models.hierarchy import Hierarchy
  from ..models.issue_type_details import IssueTypeDetails
  from ..models.project_category import ProjectCategory
  from ..models.project_component import ProjectComponent
  from ..models.project_insight import ProjectInsight
  from ..models.project_landing_page_info import ProjectLandingPageInfo
  from ..models.project_permissions import ProjectPermissions
  from ..models.project_properties import ProjectProperties
  from ..models.project_roles import ProjectRoles
  from ..models.user import User
  from ..models.version import Version





T = TypeVar("T", bound="Project")



@_attrs_define
class Project:
    """ Details about a project.

        Attributes:
            archived (bool | Unset): Whether the project is archived.
            archived_by (User | Unset): A user with details as permitted by the user's Atlassian Account privacy settings.
                However, be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            archived_date (datetime.datetime | Unset): The date when the project was archived.
            assignee_type (ProjectAssigneeType | Unset): The default assignee when creating issues for this project.
            avatar_urls (AvatarUrlsBean | Unset):
            components (list[ProjectComponent] | Unset): List of the components contained in the project.
            deleted (bool | Unset): Whether the project is marked as deleted.
            deleted_by (User | Unset): A user with details as permitted by the user's Atlassian Account privacy settings.
                However, be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            deleted_date (datetime.datetime | Unset): The date when the project was marked as deleted.
            description (str | Unset): A brief description of the project.
            email (str | Unset): An email address associated with the project.
            expand (str | Unset): Expand options that include additional project details in the response.
            favourite (bool | Unset): Whether the project is selected as a favorite.
            id (str | Unset): The ID of the project.
            insight (ProjectInsight | Unset): Additional details about a project.
            is_private (bool | Unset): Whether the project is private.
            issue_type_hierarchy (Hierarchy | Unset): The project issue type hierarchy.
            issue_types (list[IssueTypeDetails] | Unset): List of the issue types available in the project.
            key (str | Unset): The key of the project.
            landing_page_info (ProjectLandingPageInfo | Unset):
            lead (User | Unset): A user with details as permitted by the user's Atlassian Account privacy settings. However,
                be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            name (str | Unset): The name of the project.
            permissions (ProjectPermissions | Unset): Permissions which a user has on a project.
            project_category (ProjectCategory | Unset): A project category.
            project_type_key (ProjectProjectTypeKey | Unset): The [project
                type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes) of the
                project.
            properties (ProjectProperties | Unset): Map of project properties
            retention_till_date (datetime.datetime | Unset): The date when the project is deleted permanently.
            roles (ProjectRoles | Unset): The name and self URL for each role defined in the project. For more information,
                see [Create project role](#api-rest-api-3-role-post).
            self_ (str | Unset): The URL of the project details.
            simplified (bool | Unset): Whether the project is simplified.
            style (ProjectStyle | Unset): The type of the project.
            url (str | Unset): A link to information about this project, such as project documentation.
            uuid (UUID | Unset): Unique ID for next-gen projects.
            versions (list[Version] | Unset): The versions defined in the project. For more information, see [Create
                version](#api-rest-api-3-version-post).
     """

    archived: bool | Unset = UNSET
    archived_by: User | Unset = UNSET
    archived_date: datetime.datetime | Unset = UNSET
    assignee_type: ProjectAssigneeType | Unset = UNSET
    avatar_urls: AvatarUrlsBean | Unset = UNSET
    components: list[ProjectComponent] | Unset = UNSET
    deleted: bool | Unset = UNSET
    deleted_by: User | Unset = UNSET
    deleted_date: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    email: str | Unset = UNSET
    expand: str | Unset = UNSET
    favourite: bool | Unset = UNSET
    id: str | Unset = UNSET
    insight: ProjectInsight | Unset = UNSET
    is_private: bool | Unset = UNSET
    issue_type_hierarchy: Hierarchy | Unset = UNSET
    issue_types: list[IssueTypeDetails] | Unset = UNSET
    key: str | Unset = UNSET
    landing_page_info: ProjectLandingPageInfo | Unset = UNSET
    lead: User | Unset = UNSET
    name: str | Unset = UNSET
    permissions: ProjectPermissions | Unset = UNSET
    project_category: ProjectCategory | Unset = UNSET
    project_type_key: ProjectProjectTypeKey | Unset = UNSET
    properties: ProjectProperties | Unset = UNSET
    retention_till_date: datetime.datetime | Unset = UNSET
    roles: ProjectRoles | Unset = UNSET
    self_: str | Unset = UNSET
    simplified: bool | Unset = UNSET
    style: ProjectStyle | Unset = UNSET
    url: str | Unset = UNSET
    uuid: UUID | Unset = UNSET
    versions: list[Version] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.avatar_urls_bean import AvatarUrlsBean
        from ..models.hierarchy import Hierarchy
        from ..models.issue_type_details import IssueTypeDetails
        from ..models.project_category import ProjectCategory
        from ..models.project_component import ProjectComponent
        from ..models.project_insight import ProjectInsight
        from ..models.project_landing_page_info import ProjectLandingPageInfo
        from ..models.project_permissions import ProjectPermissions
        from ..models.project_properties import ProjectProperties
        from ..models.project_roles import ProjectRoles
        from ..models.user import User
        from ..models.version import Version
        archived = self.archived

        archived_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.archived_by, Unset):
            archived_by = self.archived_by.to_dict()

        archived_date: str | Unset = UNSET
        if not isinstance(self.archived_date, Unset):
            archived_date = self.archived_date.isoformat()

        assignee_type: str | Unset = UNSET
        if not isinstance(self.assignee_type, Unset):
            assignee_type = self.assignee_type.value


        avatar_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar_urls, Unset):
            avatar_urls = self.avatar_urls.to_dict()

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)



        deleted = self.deleted

        deleted_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_by, Unset):
            deleted_by = self.deleted_by.to_dict()

        deleted_date: str | Unset = UNSET
        if not isinstance(self.deleted_date, Unset):
            deleted_date = self.deleted_date.isoformat()

        description = self.description

        email = self.email

        expand = self.expand

        favourite = self.favourite

        id = self.id

        insight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insight, Unset):
            insight = self.insight.to_dict()

        is_private = self.is_private

        issue_type_hierarchy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_type_hierarchy, Unset):
            issue_type_hierarchy = self.issue_type_hierarchy.to_dict()

        issue_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issue_types, Unset):
            issue_types = []
            for issue_types_item_data in self.issue_types:
                issue_types_item = issue_types_item_data.to_dict()
                issue_types.append(issue_types_item)



        key = self.key

        landing_page_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.landing_page_info, Unset):
            landing_page_info = self.landing_page_info.to_dict()

        lead: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lead, Unset):
            lead = self.lead.to_dict()

        name = self.name

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        project_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_category, Unset):
            project_category = self.project_category.to_dict()

        project_type_key: str | Unset = UNSET
        if not isinstance(self.project_type_key, Unset):
            project_type_key = self.project_type_key.value


        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        retention_till_date: str | Unset = UNSET
        if not isinstance(self.retention_till_date, Unset):
            retention_till_date = self.retention_till_date.isoformat()

        roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles.to_dict()

        self_ = self.self_

        simplified = self.simplified

        style: str | Unset = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value


        url = self.url

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archived_by is not UNSET:
            field_dict["archivedBy"] = archived_by
        if archived_date is not UNSET:
            field_dict["archivedDate"] = archived_date
        if assignee_type is not UNSET:
            field_dict["assigneeType"] = assignee_type
        if avatar_urls is not UNSET:
            field_dict["avatarUrls"] = avatar_urls
        if components is not UNSET:
            field_dict["components"] = components
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if deleted_by is not UNSET:
            field_dict["deletedBy"] = deleted_by
        if deleted_date is not UNSET:
            field_dict["deletedDate"] = deleted_date
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if expand is not UNSET:
            field_dict["expand"] = expand
        if favourite is not UNSET:
            field_dict["favourite"] = favourite
        if id is not UNSET:
            field_dict["id"] = id
        if insight is not UNSET:
            field_dict["insight"] = insight
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if issue_type_hierarchy is not UNSET:
            field_dict["issueTypeHierarchy"] = issue_type_hierarchy
        if issue_types is not UNSET:
            field_dict["issueTypes"] = issue_types
        if key is not UNSET:
            field_dict["key"] = key
        if landing_page_info is not UNSET:
            field_dict["landingPageInfo"] = landing_page_info
        if lead is not UNSET:
            field_dict["lead"] = lead
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if project_category is not UNSET:
            field_dict["projectCategory"] = project_category
        if project_type_key is not UNSET:
            field_dict["projectTypeKey"] = project_type_key
        if properties is not UNSET:
            field_dict["properties"] = properties
        if retention_till_date is not UNSET:
            field_dict["retentionTillDate"] = retention_till_date
        if roles is not UNSET:
            field_dict["roles"] = roles
        if self_ is not UNSET:
            field_dict["self"] = self_
        if simplified is not UNSET:
            field_dict["simplified"] = simplified
        if style is not UNSET:
            field_dict["style"] = style
        if url is not UNSET:
            field_dict["url"] = url
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar_urls_bean import AvatarUrlsBean
        from ..models.hierarchy import Hierarchy
        from ..models.issue_type_details import IssueTypeDetails
        from ..models.project_category import ProjectCategory
        from ..models.project_component import ProjectComponent
        from ..models.project_insight import ProjectInsight
        from ..models.project_landing_page_info import ProjectLandingPageInfo
        from ..models.project_permissions import ProjectPermissions
        from ..models.project_properties import ProjectProperties
        from ..models.project_roles import ProjectRoles
        from ..models.user import User
        from ..models.version import Version
        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        _archived_by = d.pop("archivedBy", UNSET)
        archived_by: User | Unset
        if isinstance(_archived_by,  Unset):
            archived_by = UNSET
        else:
            archived_by = User.from_dict(_archived_by)




        _archived_date = d.pop("archivedDate", UNSET)
        archived_date: datetime.datetime | Unset
        if isinstance(_archived_date,  Unset):
            archived_date = UNSET
        else:
            archived_date = isoparse(_archived_date)




        _assignee_type = d.pop("assigneeType", UNSET)
        assignee_type: ProjectAssigneeType | Unset
        if isinstance(_assignee_type,  Unset):
            assignee_type = UNSET
        else:
            assignee_type = ProjectAssigneeType(_assignee_type)




        _avatar_urls = d.pop("avatarUrls", UNSET)
        avatar_urls: AvatarUrlsBean | Unset
        if isinstance(_avatar_urls,  Unset):
            avatar_urls = UNSET
        else:
            avatar_urls = AvatarUrlsBean.from_dict(_avatar_urls)




        _components = d.pop("components", UNSET)
        components: list[ProjectComponent] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = ProjectComponent.from_dict(components_item_data)



                components.append(components_item)


        deleted = d.pop("deleted", UNSET)

        _deleted_by = d.pop("deletedBy", UNSET)
        deleted_by: User | Unset
        if isinstance(_deleted_by,  Unset):
            deleted_by = UNSET
        else:
            deleted_by = User.from_dict(_deleted_by)




        _deleted_date = d.pop("deletedDate", UNSET)
        deleted_date: datetime.datetime | Unset
        if isinstance(_deleted_date,  Unset):
            deleted_date = UNSET
        else:
            deleted_date = isoparse(_deleted_date)




        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        expand = d.pop("expand", UNSET)

        favourite = d.pop("favourite", UNSET)

        id = d.pop("id", UNSET)

        _insight = d.pop("insight", UNSET)
        insight: ProjectInsight | Unset
        if isinstance(_insight,  Unset):
            insight = UNSET
        else:
            insight = ProjectInsight.from_dict(_insight)




        is_private = d.pop("isPrivate", UNSET)

        _issue_type_hierarchy = d.pop("issueTypeHierarchy", UNSET)
        issue_type_hierarchy: Hierarchy | Unset
        if isinstance(_issue_type_hierarchy,  Unset):
            issue_type_hierarchy = UNSET
        else:
            issue_type_hierarchy = Hierarchy.from_dict(_issue_type_hierarchy)




        _issue_types = d.pop("issueTypes", UNSET)
        issue_types: list[IssueTypeDetails] | Unset = UNSET
        if _issue_types is not UNSET:
            issue_types = []
            for issue_types_item_data in _issue_types:
                issue_types_item = IssueTypeDetails.from_dict(issue_types_item_data)



                issue_types.append(issue_types_item)


        key = d.pop("key", UNSET)

        _landing_page_info = d.pop("landingPageInfo", UNSET)
        landing_page_info: ProjectLandingPageInfo | Unset
        if isinstance(_landing_page_info,  Unset):
            landing_page_info = UNSET
        else:
            landing_page_info = ProjectLandingPageInfo.from_dict(_landing_page_info)




        _lead = d.pop("lead", UNSET)
        lead: User | Unset
        if isinstance(_lead,  Unset):
            lead = UNSET
        else:
            lead = User.from_dict(_lead)




        name = d.pop("name", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: ProjectPermissions | Unset
        if isinstance(_permissions,  Unset):
            permissions = UNSET
        else:
            permissions = ProjectPermissions.from_dict(_permissions)




        _project_category = d.pop("projectCategory", UNSET)
        project_category: ProjectCategory | Unset
        if isinstance(_project_category,  Unset):
            project_category = UNSET
        else:
            project_category = ProjectCategory.from_dict(_project_category)




        _project_type_key = d.pop("projectTypeKey", UNSET)
        project_type_key: ProjectProjectTypeKey | Unset
        if isinstance(_project_type_key,  Unset):
            project_type_key = UNSET
        else:
            project_type_key = ProjectProjectTypeKey(_project_type_key)




        _properties = d.pop("properties", UNSET)
        properties: ProjectProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = ProjectProperties.from_dict(_properties)




        _retention_till_date = d.pop("retentionTillDate", UNSET)
        retention_till_date: datetime.datetime | Unset
        if isinstance(_retention_till_date,  Unset):
            retention_till_date = UNSET
        else:
            retention_till_date = isoparse(_retention_till_date)




        _roles = d.pop("roles", UNSET)
        roles: ProjectRoles | Unset
        if isinstance(_roles,  Unset):
            roles = UNSET
        else:
            roles = ProjectRoles.from_dict(_roles)




        self_ = d.pop("self", UNSET)

        simplified = d.pop("simplified", UNSET)

        _style = d.pop("style", UNSET)
        style: ProjectStyle | Unset
        if isinstance(_style,  Unset):
            style = UNSET
        else:
            style = ProjectStyle(_style)




        url = d.pop("url", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid,  Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)




        _versions = d.pop("versions", UNSET)
        versions: list[Version] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = Version.from_dict(versions_item_data)



                versions.append(versions_item)


        project = cls(
            archived=archived,
            archived_by=archived_by,
            archived_date=archived_date,
            assignee_type=assignee_type,
            avatar_urls=avatar_urls,
            components=components,
            deleted=deleted,
            deleted_by=deleted_by,
            deleted_date=deleted_date,
            description=description,
            email=email,
            expand=expand,
            favourite=favourite,
            id=id,
            insight=insight,
            is_private=is_private,
            issue_type_hierarchy=issue_type_hierarchy,
            issue_types=issue_types,
            key=key,
            landing_page_info=landing_page_info,
            lead=lead,
            name=name,
            permissions=permissions,
            project_category=project_category,
            project_type_key=project_type_key,
            properties=properties,
            retention_till_date=retention_till_date,
            roles=roles,
            self_=self_,
            simplified=simplified,
            style=style,
            url=url,
            uuid=uuid,
            versions=versions,
        )

        return project

