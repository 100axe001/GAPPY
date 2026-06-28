from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_scheme import WorkflowScheme





T = TypeVar("T", bound="WorkflowSchemeAssociations")



@_attrs_define
class WorkflowSchemeAssociations:
    """ A workflow scheme along with a list of projects that use it.

        Attributes:
            project_ids (list[str]): The list of projects that use the workflow scheme.
            workflow_scheme (WorkflowScheme): Details about a workflow scheme.
     """

    project_ids: list[str]
    workflow_scheme: WorkflowScheme





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_scheme import WorkflowScheme
        project_ids = self.project_ids



        workflow_scheme = self.workflow_scheme.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "projectIds": project_ids,
            "workflowScheme": workflow_scheme,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_scheme import WorkflowScheme
        d = dict(src_dict)
        project_ids = cast(list[str], d.pop("projectIds"))


        workflow_scheme = WorkflowScheme.from_dict(d.pop("workflowScheme"))




        workflow_scheme_associations = cls(
            project_ids=project_ids,
            workflow_scheme=workflow_scheme,
        )

        return workflow_scheme_associations

