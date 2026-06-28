from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_transition_rules_update_error_details import WorkflowTransitionRulesUpdateErrorDetails





T = TypeVar("T", bound="WorkflowTransitionRulesUpdateErrors")



@_attrs_define
class WorkflowTransitionRulesUpdateErrors:
    """ Details of any errors encountered while updating workflow transition rules.

        Attributes:
            update_results (list[WorkflowTransitionRulesUpdateErrorDetails]): A list of workflows.
     """

    update_results: list[WorkflowTransitionRulesUpdateErrorDetails]





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_transition_rules_update_error_details import WorkflowTransitionRulesUpdateErrorDetails
        update_results = []
        for update_results_item_data in self.update_results:
            update_results_item = update_results_item_data.to_dict()
            update_results.append(update_results_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "updateResults": update_results,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_transition_rules_update_error_details import WorkflowTransitionRulesUpdateErrorDetails
        d = dict(src_dict)
        update_results = []
        _update_results = d.pop("updateResults")
        for update_results_item_data in (_update_results):
            update_results_item = WorkflowTransitionRulesUpdateErrorDetails.from_dict(update_results_item_data)



            update_results.append(update_results_item)


        workflow_transition_rules_update_errors = cls(
            update_results=update_results,
        )

        return workflow_transition_rules_update_errors

