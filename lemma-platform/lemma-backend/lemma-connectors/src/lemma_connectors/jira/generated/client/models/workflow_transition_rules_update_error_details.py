from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_id import WorkflowId
  from ..models.workflow_transition_rules_update_error_details_rule_update_errors import WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors





T = TypeVar("T", bound="WorkflowTransitionRulesUpdateErrorDetails")



@_attrs_define
class WorkflowTransitionRulesUpdateErrorDetails:
    """ Details of any errors encountered while updating workflow transition rules for a workflow.

        Attributes:
            rule_update_errors (WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors): A list of transition rule update
                errors, indexed by the transition rule ID. Any transition rule that appears here wasn't updated.
            update_errors (list[str]): The list of errors that specify why the workflow update failed. The workflow was not
                updated if the list contains any entries.
            workflow_id (WorkflowId): Properties that identify a workflow.
     """

    rule_update_errors: WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors
    update_errors: list[str]
    workflow_id: WorkflowId





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_id import WorkflowId
        from ..models.workflow_transition_rules_update_error_details_rule_update_errors import WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors
        rule_update_errors = self.rule_update_errors.to_dict()

        update_errors = self.update_errors



        workflow_id = self.workflow_id.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ruleUpdateErrors": rule_update_errors,
            "updateErrors": update_errors,
            "workflowId": workflow_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_id import WorkflowId
        from ..models.workflow_transition_rules_update_error_details_rule_update_errors import WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors
        d = dict(src_dict)
        rule_update_errors = WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors.from_dict(d.pop("ruleUpdateErrors"))




        update_errors = cast(list[str], d.pop("updateErrors"))


        workflow_id = WorkflowId.from_dict(d.pop("workflowId"))




        workflow_transition_rules_update_error_details = cls(
            rule_update_errors=rule_update_errors,
            update_errors=update_errors,
            workflow_id=workflow_id,
        )

        return workflow_transition_rules_update_error_details

