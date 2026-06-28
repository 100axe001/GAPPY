from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WorkflowSchemeProjectAssociation")



@_attrs_define
class WorkflowSchemeProjectAssociation:
    """ An associated workflow scheme and project.

        Attributes:
            project_id (str): The ID of the project.
            workflow_scheme_id (str | Unset): The ID of the workflow scheme. If the workflow scheme ID is `null`, the
                operation assigns the default workflow scheme.
     """

    project_id: str
    workflow_scheme_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        workflow_scheme_id = self.workflow_scheme_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "projectId": project_id,
        })
        if workflow_scheme_id is not UNSET:
            field_dict["workflowSchemeId"] = workflow_scheme_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        workflow_scheme_id = d.pop("workflowSchemeId", UNSET)

        workflow_scheme_project_association = cls(
            project_id=project_id,
            workflow_scheme_id=workflow_scheme_id,
        )

        return workflow_scheme_project_association

