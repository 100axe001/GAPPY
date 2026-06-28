from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user import User
  from ..models.workflow_scheme_issue_type_mappings import WorkflowSchemeIssueTypeMappings
  from ..models.workflow_scheme_issue_types import WorkflowSchemeIssueTypes
  from ..models.workflow_scheme_original_issue_type_mappings import WorkflowSchemeOriginalIssueTypeMappings





T = TypeVar("T", bound="WorkflowScheme")



@_attrs_define
class WorkflowScheme:
    """ Details about a workflow scheme.

        Attributes:
            default_workflow (str | Unset): The name of the default workflow for the workflow scheme. The default workflow
                has *All Unassigned Issue Types* assigned to it in Jira. If `defaultWorkflow` is not specified when creating a
                workflow scheme, it is set to *Jira Workflow (jira)*.
            description (str | Unset): The description of the workflow scheme.
            draft (bool | Unset): Whether the workflow scheme is a draft or not.
            id (int | Unset): The ID of the workflow scheme.
            issue_type_mappings (WorkflowSchemeIssueTypeMappings | Unset): The issue type to workflow mappings, where each
                mapping is an issue type ID and workflow name pair. Note that an issue type can only be mapped to one workflow
                in a workflow scheme.
            issue_types (WorkflowSchemeIssueTypes | Unset): The issue types available in Jira.
            last_modified (str | Unset): The date-time that the draft workflow scheme was last modified. A modification is a
                change to the issue type-project mappings only. This property does not apply to non-draft workflows.
            last_modified_user (User | Unset): A user with details as permitted by the user's Atlassian Account privacy
                settings. However, be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            name (str | Unset): The name of the workflow scheme. The name must be unique. The maximum length is 255
                characters. Required when creating a workflow scheme.
            original_default_workflow (str | Unset): For draft workflow schemes, this property is the name of the default
                workflow for the original workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it
                in Jira.
            original_issue_type_mappings (WorkflowSchemeOriginalIssueTypeMappings | Unset): For draft workflow schemes, this
                property is the issue type to workflow mappings for the original workflow scheme, where each mapping is an issue
                type ID and workflow name pair. Note that an issue type can only be mapped to one workflow in a workflow scheme.
            self_ (str | Unset):
            update_draft_if_needed (bool | Unset): Whether to create or update a draft workflow scheme when updating an
                active workflow scheme. An active workflow scheme is a workflow scheme that is used by at least one project. The
                following examples show how this property works:

                 *  Update an active workflow scheme with `updateDraftIfNeeded` set to `true`: If a draft workflow scheme
                exists, it is updated. Otherwise, a draft workflow scheme is created.
                 *  Update an active workflow scheme with `updateDraftIfNeeded` set to `false`: An error is returned, as active
                workflow schemes cannot be updated.
                 *  Update an inactive workflow scheme with `updateDraftIfNeeded` set to `true`: The workflow scheme is updated,
                as inactive workflow schemes do not require drafts to update.

                Defaults to `false`.
     """

    default_workflow: str | Unset = UNSET
    description: str | Unset = UNSET
    draft: bool | Unset = UNSET
    id: int | Unset = UNSET
    issue_type_mappings: WorkflowSchemeIssueTypeMappings | Unset = UNSET
    issue_types: WorkflowSchemeIssueTypes | Unset = UNSET
    last_modified: str | Unset = UNSET
    last_modified_user: User | Unset = UNSET
    name: str | Unset = UNSET
    original_default_workflow: str | Unset = UNSET
    original_issue_type_mappings: WorkflowSchemeOriginalIssueTypeMappings | Unset = UNSET
    self_: str | Unset = UNSET
    update_draft_if_needed: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User
        from ..models.workflow_scheme_issue_type_mappings import WorkflowSchemeIssueTypeMappings
        from ..models.workflow_scheme_issue_types import WorkflowSchemeIssueTypes
        from ..models.workflow_scheme_original_issue_type_mappings import WorkflowSchemeOriginalIssueTypeMappings
        default_workflow = self.default_workflow

        description = self.description

        draft = self.draft

        id = self.id

        issue_type_mappings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_type_mappings, Unset):
            issue_type_mappings = self.issue_type_mappings.to_dict()

        issue_types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_types, Unset):
            issue_types = self.issue_types.to_dict()

        last_modified = self.last_modified

        last_modified_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modified_user, Unset):
            last_modified_user = self.last_modified_user.to_dict()

        name = self.name

        original_default_workflow = self.original_default_workflow

        original_issue_type_mappings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_issue_type_mappings, Unset):
            original_issue_type_mappings = self.original_issue_type_mappings.to_dict()

        self_ = self.self_

        update_draft_if_needed = self.update_draft_if_needed


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if default_workflow is not UNSET:
            field_dict["defaultWorkflow"] = default_workflow
        if description is not UNSET:
            field_dict["description"] = description
        if draft is not UNSET:
            field_dict["draft"] = draft
        if id is not UNSET:
            field_dict["id"] = id
        if issue_type_mappings is not UNSET:
            field_dict["issueTypeMappings"] = issue_type_mappings
        if issue_types is not UNSET:
            field_dict["issueTypes"] = issue_types
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if last_modified_user is not UNSET:
            field_dict["lastModifiedUser"] = last_modified_user
        if name is not UNSET:
            field_dict["name"] = name
        if original_default_workflow is not UNSET:
            field_dict["originalDefaultWorkflow"] = original_default_workflow
        if original_issue_type_mappings is not UNSET:
            field_dict["originalIssueTypeMappings"] = original_issue_type_mappings
        if self_ is not UNSET:
            field_dict["self"] = self_
        if update_draft_if_needed is not UNSET:
            field_dict["updateDraftIfNeeded"] = update_draft_if_needed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        from ..models.workflow_scheme_issue_type_mappings import WorkflowSchemeIssueTypeMappings
        from ..models.workflow_scheme_issue_types import WorkflowSchemeIssueTypes
        from ..models.workflow_scheme_original_issue_type_mappings import WorkflowSchemeOriginalIssueTypeMappings
        d = dict(src_dict)
        default_workflow = d.pop("defaultWorkflow", UNSET)

        description = d.pop("description", UNSET)

        draft = d.pop("draft", UNSET)

        id = d.pop("id", UNSET)

        _issue_type_mappings = d.pop("issueTypeMappings", UNSET)
        issue_type_mappings: WorkflowSchemeIssueTypeMappings | Unset
        if isinstance(_issue_type_mappings,  Unset):
            issue_type_mappings = UNSET
        else:
            issue_type_mappings = WorkflowSchemeIssueTypeMappings.from_dict(_issue_type_mappings)




        _issue_types = d.pop("issueTypes", UNSET)
        issue_types: WorkflowSchemeIssueTypes | Unset
        if isinstance(_issue_types,  Unset):
            issue_types = UNSET
        else:
            issue_types = WorkflowSchemeIssueTypes.from_dict(_issue_types)




        last_modified = d.pop("lastModified", UNSET)

        _last_modified_user = d.pop("lastModifiedUser", UNSET)
        last_modified_user: User | Unset
        if isinstance(_last_modified_user,  Unset):
            last_modified_user = UNSET
        else:
            last_modified_user = User.from_dict(_last_modified_user)




        name = d.pop("name", UNSET)

        original_default_workflow = d.pop("originalDefaultWorkflow", UNSET)

        _original_issue_type_mappings = d.pop("originalIssueTypeMappings", UNSET)
        original_issue_type_mappings: WorkflowSchemeOriginalIssueTypeMappings | Unset
        if isinstance(_original_issue_type_mappings,  Unset):
            original_issue_type_mappings = UNSET
        else:
            original_issue_type_mappings = WorkflowSchemeOriginalIssueTypeMappings.from_dict(_original_issue_type_mappings)




        self_ = d.pop("self", UNSET)

        update_draft_if_needed = d.pop("updateDraftIfNeeded", UNSET)

        workflow_scheme = cls(
            default_workflow=default_workflow,
            description=description,
            draft=draft,
            id=id,
            issue_type_mappings=issue_type_mappings,
            issue_types=issue_types,
            last_modified=last_modified,
            last_modified_user=last_modified_user,
            name=name,
            original_default_workflow=original_default_workflow,
            original_issue_type_mappings=original_issue_type_mappings,
            self_=self_,
            update_draft_if_needed=update_draft_if_needed,
        )

        return workflow_scheme

