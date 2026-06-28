from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_transition_rules_details import WorkflowTransitionRulesDetails





T = TypeVar("T", bound="WorkflowsWithTransitionRulesDetails")



@_attrs_define
class WorkflowsWithTransitionRulesDetails:
    """ Details of workflows and their transition rules to delete.

        Attributes:
            workflows (list[WorkflowTransitionRulesDetails]): The list of workflows with transition rules to delete.
     """

    workflows: list[WorkflowTransitionRulesDetails]





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_transition_rules_details import WorkflowTransitionRulesDetails
        workflows = []
        for workflows_item_data in self.workflows:
            workflows_item = workflows_item_data.to_dict()
            workflows.append(workflows_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "workflows": workflows,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_transition_rules_details import WorkflowTransitionRulesDetails
        d = dict(src_dict)
        workflows = []
        _workflows = d.pop("workflows")
        for workflows_item_data in (_workflows):
            workflows_item = WorkflowTransitionRulesDetails.from_dict(workflows_item_data)



            workflows.append(workflows_item)


        workflows_with_transition_rules_details = cls(
            workflows=workflows,
        )

        return workflows_with_transition_rules_details

