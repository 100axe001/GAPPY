from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.project_details import ProjectDetails
  from ..models.published_workflow_id import PublishedWorkflowId
  from ..models.transition import Transition
  from ..models.workflow_operations import WorkflowOperations
  from ..models.workflow_scheme_id_name import WorkflowSchemeIdName
  from ..models.workflow_status import WorkflowStatus





T = TypeVar("T", bound="Workflow")



@_attrs_define
class Workflow:
    """ Details about a workflow.

        Attributes:
            description (str): The description of the workflow.
            id (PublishedWorkflowId): Properties that identify a published workflow.
            created (datetime.datetime | Unset): The creation date of the workflow.
            has_draft_workflow (bool | Unset): Whether the workflow has a draft version.
            is_default (bool | Unset): Whether this is the default workflow.
            operations (WorkflowOperations | Unset): Operations allowed on a workflow
            projects (list[ProjectDetails] | Unset): The projects the workflow is assigned to, through workflow schemes.
            schemes (list[WorkflowSchemeIdName] | Unset): The workflow schemes the workflow is assigned to.
            statuses (list[WorkflowStatus] | Unset): The statuses of the workflow.
            transitions (list[Transition] | Unset): The transitions of the workflow.
            updated (datetime.datetime | Unset): The last edited date of the workflow.
     """

    description: str
    id: PublishedWorkflowId
    created: datetime.datetime | Unset = UNSET
    has_draft_workflow: bool | Unset = UNSET
    is_default: bool | Unset = UNSET
    operations: WorkflowOperations | Unset = UNSET
    projects: list[ProjectDetails] | Unset = UNSET
    schemes: list[WorkflowSchemeIdName] | Unset = UNSET
    statuses: list[WorkflowStatus] | Unset = UNSET
    transitions: list[Transition] | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_details import ProjectDetails
        from ..models.published_workflow_id import PublishedWorkflowId
        from ..models.transition import Transition
        from ..models.workflow_operations import WorkflowOperations
        from ..models.workflow_scheme_id_name import WorkflowSchemeIdName
        from ..models.workflow_status import WorkflowStatus
        description = self.description

        id = self.id.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        has_draft_workflow = self.has_draft_workflow

        is_default = self.is_default

        operations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = self.operations.to_dict()

        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)



        schemes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schemes, Unset):
            schemes = []
            for schemes_item_data in self.schemes:
                schemes_item = schemes_item_data.to_dict()
                schemes.append(schemes_item)



        statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()
                statuses.append(statuses_item)



        transitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transitions, Unset):
            transitions = []
            for transitions_item_data in self.transitions:
                transitions_item = transitions_item_data.to_dict()
                transitions.append(transitions_item)



        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "description": description,
            "id": id,
        })
        if created is not UNSET:
            field_dict["created"] = created
        if has_draft_workflow is not UNSET:
            field_dict["hasDraftWorkflow"] = has_draft_workflow
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if operations is not UNSET:
            field_dict["operations"] = operations
        if projects is not UNSET:
            field_dict["projects"] = projects
        if schemes is not UNSET:
            field_dict["schemes"] = schemes
        if statuses is not UNSET:
            field_dict["statuses"] = statuses
        if transitions is not UNSET:
            field_dict["transitions"] = transitions
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_details import ProjectDetails
        from ..models.published_workflow_id import PublishedWorkflowId
        from ..models.transition import Transition
        from ..models.workflow_operations import WorkflowOperations
        from ..models.workflow_scheme_id_name import WorkflowSchemeIdName
        from ..models.workflow_status import WorkflowStatus
        d = dict(src_dict)
        description = d.pop("description")

        id = PublishedWorkflowId.from_dict(d.pop("id"))




        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        has_draft_workflow = d.pop("hasDraftWorkflow", UNSET)

        is_default = d.pop("isDefault", UNSET)

        _operations = d.pop("operations", UNSET)
        operations: WorkflowOperations | Unset
        if isinstance(_operations,  Unset):
            operations = UNSET
        else:
            operations = WorkflowOperations.from_dict(_operations)




        _projects = d.pop("projects", UNSET)
        projects: list[ProjectDetails] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = ProjectDetails.from_dict(projects_item_data)



                projects.append(projects_item)


        _schemes = d.pop("schemes", UNSET)
        schemes: list[WorkflowSchemeIdName] | Unset = UNSET
        if _schemes is not UNSET:
            schemes = []
            for schemes_item_data in _schemes:
                schemes_item = WorkflowSchemeIdName.from_dict(schemes_item_data)



                schemes.append(schemes_item)


        _statuses = d.pop("statuses", UNSET)
        statuses: list[WorkflowStatus] | Unset = UNSET
        if _statuses is not UNSET:
            statuses = []
            for statuses_item_data in _statuses:
                statuses_item = WorkflowStatus.from_dict(statuses_item_data)



                statuses.append(statuses_item)


        _transitions = d.pop("transitions", UNSET)
        transitions: list[Transition] | Unset = UNSET
        if _transitions is not UNSET:
            transitions = []
            for transitions_item_data in _transitions:
                transitions_item = Transition.from_dict(transitions_item_data)



                transitions.append(transitions_item)


        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated,  Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)




        workflow = cls(
            description=description,
            id=id,
            created=created,
            has_draft_workflow=has_draft_workflow,
            is_default=is_default,
            operations=operations,
            projects=projects,
            schemes=schemes,
            statuses=statuses,
            transitions=transitions,
            updated=updated,
        )

        return workflow

