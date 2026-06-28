from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.component_with_issue_count_assignee_type import ComponentWithIssueCountAssigneeType
from ..models.component_with_issue_count_real_assignee_type import ComponentWithIssueCountRealAssigneeType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user import User





T = TypeVar("T", bound="ComponentWithIssueCount")



@_attrs_define
class ComponentWithIssueCount:
    """ Details about a component with a count of the issues it contains.

        Attributes:
            assignee (User | Unset): A user with details as permitted by the user's Atlassian Account privacy settings.
                However, be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            assignee_type (ComponentWithIssueCountAssigneeType | Unset): The nominal user type used to determine the
                assignee for issues created with this component. See `realAssigneeType` for details on how the type of the user,
                and hence the user, assigned to issues is determined. Takes the following values:

                 *  `PROJECT_LEAD` the assignee to any issues created with this component is nominally the lead for the project
                the component is in.
                 *  `COMPONENT_LEAD` the assignee to any issues created with this component is nominally the lead for the
                component.
                 *  `UNASSIGNED` an assignee is not set for issues created with this component.
                 *  `PROJECT_DEFAULT` the assignee to any issues created with this component is nominally the default assignee
                for the project that the component is in.
            description (str | Unset): The description for the component.
            id (str | Unset): The unique identifier for the component.
            is_assignee_type_valid (bool | Unset): Whether a user is associated with `assigneeType`. For example, if the
                `assigneeType` is set to `COMPONENT_LEAD` but the component lead is not set, then `false` is returned.
            issue_count (int | Unset): Count of issues for the component.
            lead (User | Unset): A user with details as permitted by the user's Atlassian Account privacy settings. However,
                be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            name (str | Unset): The name for the component.
            project (str | Unset): The key of the project to which the component is assigned.
            project_id (int | Unset): Not used.
            real_assignee (User | Unset): A user with details as permitted by the user's Atlassian Account privacy settings.
                However, be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            real_assignee_type (ComponentWithIssueCountRealAssigneeType | Unset): The type of the assignee that is assigned
                to issues created with this component, when an assignee cannot be set from the `assigneeType`. For example,
                `assigneeType` is set to `COMPONENT_LEAD` but no component lead is set. This property is set to one of the
                following values:

                 *  `PROJECT_LEAD` when `assigneeType` is `PROJECT_LEAD` and the project lead has permission to be assigned
                issues in the project that the component is in.
                 *  `COMPONENT_LEAD` when `assignee`Type is `COMPONENT_LEAD` and the component lead has permission to be
                assigned issues in the project that the component is in.
                 *  `UNASSIGNED` when `assigneeType` is `UNASSIGNED` and Jira is configured to allow unassigned issues.
                 *  `PROJECT_DEFAULT` when none of the preceding cases are true.
            self_ (str | Unset): The URL for this count of the issues contained in the component.
     """

    assignee: User | Unset = UNSET
    assignee_type: ComponentWithIssueCountAssigneeType | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    is_assignee_type_valid: bool | Unset = UNSET
    issue_count: int | Unset = UNSET
    lead: User | Unset = UNSET
    name: str | Unset = UNSET
    project: str | Unset = UNSET
    project_id: int | Unset = UNSET
    real_assignee: User | Unset = UNSET
    real_assignee_type: ComponentWithIssueCountRealAssigneeType | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User
        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        assignee_type: str | Unset = UNSET
        if not isinstance(self.assignee_type, Unset):
            assignee_type = self.assignee_type.value


        description = self.description

        id = self.id

        is_assignee_type_valid = self.is_assignee_type_valid

        issue_count = self.issue_count

        lead: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lead, Unset):
            lead = self.lead.to_dict()

        name = self.name

        project = self.project

        project_id = self.project_id

        real_assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.real_assignee, Unset):
            real_assignee = self.real_assignee.to_dict()

        real_assignee_type: str | Unset = UNSET
        if not isinstance(self.real_assignee_type, Unset):
            real_assignee_type = self.real_assignee_type.value


        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if assignee_type is not UNSET:
            field_dict["assigneeType"] = assignee_type
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if is_assignee_type_valid is not UNSET:
            field_dict["isAssigneeTypeValid"] = is_assignee_type_valid
        if issue_count is not UNSET:
            field_dict["issueCount"] = issue_count
        if lead is not UNSET:
            field_dict["lead"] = lead
        if name is not UNSET:
            field_dict["name"] = name
        if project is not UNSET:
            field_dict["project"] = project
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if real_assignee is not UNSET:
            field_dict["realAssignee"] = real_assignee
        if real_assignee_type is not UNSET:
            field_dict["realAssigneeType"] = real_assignee_type
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: User | Unset
        if isinstance(_assignee,  Unset):
            assignee = UNSET
        else:
            assignee = User.from_dict(_assignee)




        _assignee_type = d.pop("assigneeType", UNSET)
        assignee_type: ComponentWithIssueCountAssigneeType | Unset
        if isinstance(_assignee_type,  Unset):
            assignee_type = UNSET
        else:
            assignee_type = ComponentWithIssueCountAssigneeType(_assignee_type)




        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        is_assignee_type_valid = d.pop("isAssigneeTypeValid", UNSET)

        issue_count = d.pop("issueCount", UNSET)

        _lead = d.pop("lead", UNSET)
        lead: User | Unset
        if isinstance(_lead,  Unset):
            lead = UNSET
        else:
            lead = User.from_dict(_lead)




        name = d.pop("name", UNSET)

        project = d.pop("project", UNSET)

        project_id = d.pop("projectId", UNSET)

        _real_assignee = d.pop("realAssignee", UNSET)
        real_assignee: User | Unset
        if isinstance(_real_assignee,  Unset):
            real_assignee = UNSET
        else:
            real_assignee = User.from_dict(_real_assignee)




        _real_assignee_type = d.pop("realAssigneeType", UNSET)
        real_assignee_type: ComponentWithIssueCountRealAssigneeType | Unset
        if isinstance(_real_assignee_type,  Unset):
            real_assignee_type = UNSET
        else:
            real_assignee_type = ComponentWithIssueCountRealAssigneeType(_real_assignee_type)




        self_ = d.pop("self", UNSET)

        component_with_issue_count = cls(
            assignee=assignee,
            assignee_type=assignee_type,
            description=description,
            id=id,
            is_assignee_type_valid=is_assignee_type_valid,
            issue_count=issue_count,
            lead=lead,
            name=name,
            project=project,
            project_id=project_id,
            real_assignee=real_assignee,
            real_assignee_type=real_assignee_type,
            self_=self_,
        )

        return component_with_issue_count

