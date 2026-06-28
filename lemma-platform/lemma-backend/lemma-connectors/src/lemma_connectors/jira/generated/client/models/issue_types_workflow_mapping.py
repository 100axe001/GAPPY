from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IssueTypesWorkflowMapping")



@_attrs_define
class IssueTypesWorkflowMapping:
    """ Details about the mapping between issue types and a workflow.

        Attributes:
            default_mapping (bool | Unset): Whether the workflow is the default workflow for the workflow scheme.
            issue_types (list[str] | Unset): The list of issue type IDs.
            update_draft_if_needed (bool | Unset): Whether a draft workflow scheme is created or updated when updating an
                active workflow scheme. The draft is updated with the new workflow-issue types mapping. Defaults to `false`.
            workflow (str | Unset): The name of the workflow. Optional if updating the workflow-issue types mapping.
     """

    default_mapping: bool | Unset = UNSET
    issue_types: list[str] | Unset = UNSET
    update_draft_if_needed: bool | Unset = UNSET
    workflow: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        default_mapping = self.default_mapping

        issue_types: list[str] | Unset = UNSET
        if not isinstance(self.issue_types, Unset):
            issue_types = self.issue_types



        update_draft_if_needed = self.update_draft_if_needed

        workflow = self.workflow


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if default_mapping is not UNSET:
            field_dict["defaultMapping"] = default_mapping
        if issue_types is not UNSET:
            field_dict["issueTypes"] = issue_types
        if update_draft_if_needed is not UNSET:
            field_dict["updateDraftIfNeeded"] = update_draft_if_needed
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_mapping = d.pop("defaultMapping", UNSET)

        issue_types = cast(list[str], d.pop("issueTypes", UNSET))


        update_draft_if_needed = d.pop("updateDraftIfNeeded", UNSET)

        workflow = d.pop("workflow", UNSET)

        issue_types_workflow_mapping = cls(
            default_mapping=default_mapping,
            issue_types=issue_types,
            update_draft_if_needed=update_draft_if_needed,
            workflow=workflow,
        )

        return issue_types_workflow_mapping

