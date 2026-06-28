from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueTypeWorkflowMapping")



@_attrs_define
class IssueTypeWorkflowMapping:
    """ Details about the mapping between an issue type and a workflow.

        Attributes:
            issue_type (str | Unset): The ID of the issue type. Not required if updating the issue type-workflow mapping.
            update_draft_if_needed (bool | Unset): Set to true to create or update the draft of a workflow scheme and update
                the mapping in the draft, when the workflow scheme cannot be edited. Defaults to `false`. Only applicable when
                updating the workflow-issue types mapping.
            workflow (str | Unset): The name of the workflow.
     """

    issue_type: str | Unset = UNSET
    update_draft_if_needed: bool | Unset = UNSET
    workflow: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        issue_type = self.issue_type

        update_draft_if_needed = self.update_draft_if_needed

        workflow = self.workflow


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issue_type is not UNSET:
            field_dict["issueType"] = issue_type
        if update_draft_if_needed is not UNSET:
            field_dict["updateDraftIfNeeded"] = update_draft_if_needed
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type = d.pop("issueType", UNSET)

        update_draft_if_needed = d.pop("updateDraftIfNeeded", UNSET)

        workflow = d.pop("workflow", UNSET)

        issue_type_workflow_mapping = cls(
            issue_type=issue_type,
            update_draft_if_needed=update_draft_if_needed,
            workflow=workflow,
        )

        return issue_type_workflow_mapping

