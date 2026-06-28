from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_transition_rules import WorkflowTransitionRules





T = TypeVar("T", bound="WorkflowTransitionRulesUpdate")



@_attrs_define
class WorkflowTransitionRulesUpdate:
    """ Details about a workflow configuration update request.

        Attributes:
            workflows (list[WorkflowTransitionRules]): The list of workflows with transition rules to update.
     """

    workflows: list[WorkflowTransitionRules]





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_transition_rules import WorkflowTransitionRules
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
        from ..models.workflow_transition_rules import WorkflowTransitionRules
        d = dict(src_dict)
        workflows = []
        _workflows = d.pop("workflows")
        for workflows_item_data in (_workflows):
            workflows_item = WorkflowTransitionRules.from_dict(workflows_item_data)



            workflows.append(workflows_item)


        workflow_transition_rules_update = cls(
            workflows=workflows,
        )

        return workflow_transition_rules_update

