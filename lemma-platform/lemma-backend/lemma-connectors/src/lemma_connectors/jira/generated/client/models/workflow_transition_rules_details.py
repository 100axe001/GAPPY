from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_id import WorkflowId





T = TypeVar("T", bound="WorkflowTransitionRulesDetails")



@_attrs_define
class WorkflowTransitionRulesDetails:
    """ Details about a workflow configuration update request.

        Attributes:
            workflow_id (WorkflowId): Properties that identify a workflow.
            workflow_rule_ids (list[str]): The list of connect workflow rule IDs.
     """

    workflow_id: WorkflowId
    workflow_rule_ids: list[str]





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_id import WorkflowId
        workflow_id = self.workflow_id.to_dict()

        workflow_rule_ids = self.workflow_rule_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "workflowId": workflow_id,
            "workflowRuleIds": workflow_rule_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_id import WorkflowId
        d = dict(src_dict)
        workflow_id = WorkflowId.from_dict(d.pop("workflowId"))




        workflow_rule_ids = cast(list[str], d.pop("workflowRuleIds"))


        workflow_transition_rules_details = cls(
            workflow_id=workflow_id,
            workflow_rule_ids=workflow_rule_ids,
        )

        return workflow_transition_rules_details

