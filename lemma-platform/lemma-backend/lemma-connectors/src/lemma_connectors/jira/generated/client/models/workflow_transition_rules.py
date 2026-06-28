from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.connect_workflow_transition_rule import ConnectWorkflowTransitionRule
  from ..models.workflow_id import WorkflowId





T = TypeVar("T", bound="WorkflowTransitionRules")



@_attrs_define
class WorkflowTransitionRules:
    """ A workflow with transition rules.

        Attributes:
            workflow_id (WorkflowId): Properties that identify a workflow.
            conditions (list[ConnectWorkflowTransitionRule] | Unset): The list of conditions within the workflow.
            post_functions (list[ConnectWorkflowTransitionRule] | Unset): The list of post functions within the workflow.
            validators (list[ConnectWorkflowTransitionRule] | Unset): The list of validators within the workflow.
     """

    workflow_id: WorkflowId
    conditions: list[ConnectWorkflowTransitionRule] | Unset = UNSET
    post_functions: list[ConnectWorkflowTransitionRule] | Unset = UNSET
    validators: list[ConnectWorkflowTransitionRule] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.connect_workflow_transition_rule import ConnectWorkflowTransitionRule
        from ..models.workflow_id import WorkflowId
        workflow_id = self.workflow_id.to_dict()

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)



        post_functions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.post_functions, Unset):
            post_functions = []
            for post_functions_item_data in self.post_functions:
                post_functions_item = post_functions_item_data.to_dict()
                post_functions.append(post_functions_item)



        validators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.validators, Unset):
            validators = []
            for validators_item_data in self.validators:
                validators_item = validators_item_data.to_dict()
                validators.append(validators_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "workflowId": workflow_id,
        })
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if post_functions is not UNSET:
            field_dict["postFunctions"] = post_functions
        if validators is not UNSET:
            field_dict["validators"] = validators

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connect_workflow_transition_rule import ConnectWorkflowTransitionRule
        from ..models.workflow_id import WorkflowId
        d = dict(src_dict)
        workflow_id = WorkflowId.from_dict(d.pop("workflowId"))




        _conditions = d.pop("conditions", UNSET)
        conditions: list[ConnectWorkflowTransitionRule] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ConnectWorkflowTransitionRule.from_dict(conditions_item_data)



                conditions.append(conditions_item)


        _post_functions = d.pop("postFunctions", UNSET)
        post_functions: list[ConnectWorkflowTransitionRule] | Unset = UNSET
        if _post_functions is not UNSET:
            post_functions = []
            for post_functions_item_data in _post_functions:
                post_functions_item = ConnectWorkflowTransitionRule.from_dict(post_functions_item_data)



                post_functions.append(post_functions_item)


        _validators = d.pop("validators", UNSET)
        validators: list[ConnectWorkflowTransitionRule] | Unset = UNSET
        if _validators is not UNSET:
            validators = []
            for validators_item_data in _validators:
                validators_item = ConnectWorkflowTransitionRule.from_dict(validators_item_data)



                validators.append(validators_item)


        workflow_transition_rules = cls(
            workflow_id=workflow_id,
            conditions=conditions,
            post_functions=post_functions,
            validators=validators,
        )

        return workflow_transition_rules

