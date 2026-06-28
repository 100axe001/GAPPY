from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.workflow_transition_rules import WorkflowTransitionRules





T = TypeVar("T", bound="WorkflowRulesSearchDetails")



@_attrs_define
class WorkflowRulesSearchDetails:
    """ Details of workflow transition rules.

        Attributes:
            invalid_rules (list[UUID] | Unset): List of workflow rule IDs that do not belong to the workflow or can not be
                found.
            valid_rules (list[WorkflowTransitionRules] | Unset): List of valid workflow transition rules.
            workflow_entity_id (UUID | Unset): The workflow ID. Example: a498d711-685d-428d-8c3e-bc03bb450ea7.
     """

    invalid_rules: list[UUID] | Unset = UNSET
    valid_rules: list[WorkflowTransitionRules] | Unset = UNSET
    workflow_entity_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_transition_rules import WorkflowTransitionRules
        invalid_rules: list[str] | Unset = UNSET
        if not isinstance(self.invalid_rules, Unset):
            invalid_rules = []
            for invalid_rules_item_data in self.invalid_rules:
                invalid_rules_item = str(invalid_rules_item_data)
                invalid_rules.append(invalid_rules_item)



        valid_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.valid_rules, Unset):
            valid_rules = []
            for valid_rules_item_data in self.valid_rules:
                valid_rules_item = valid_rules_item_data.to_dict()
                valid_rules.append(valid_rules_item)



        workflow_entity_id: str | Unset = UNSET
        if not isinstance(self.workflow_entity_id, Unset):
            workflow_entity_id = str(self.workflow_entity_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if invalid_rules is not UNSET:
            field_dict["invalidRules"] = invalid_rules
        if valid_rules is not UNSET:
            field_dict["validRules"] = valid_rules
        if workflow_entity_id is not UNSET:
            field_dict["workflowEntityId"] = workflow_entity_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_transition_rules import WorkflowTransitionRules
        d = dict(src_dict)
        _invalid_rules = d.pop("invalidRules", UNSET)
        invalid_rules: list[UUID] | Unset = UNSET
        if _invalid_rules is not UNSET:
            invalid_rules = []
            for invalid_rules_item_data in _invalid_rules:
                invalid_rules_item = UUID(invalid_rules_item_data)



                invalid_rules.append(invalid_rules_item)


        _valid_rules = d.pop("validRules", UNSET)
        valid_rules: list[WorkflowTransitionRules] | Unset = UNSET
        if _valid_rules is not UNSET:
            valid_rules = []
            for valid_rules_item_data in _valid_rules:
                valid_rules_item = WorkflowTransitionRules.from_dict(valid_rules_item_data)



                valid_rules.append(valid_rules_item)


        _workflow_entity_id = d.pop("workflowEntityId", UNSET)
        workflow_entity_id: UUID | Unset
        if isinstance(_workflow_entity_id,  Unset):
            workflow_entity_id = UNSET
        else:
            workflow_entity_id = UUID(_workflow_entity_id)




        workflow_rules_search_details = cls(
            invalid_rules=invalid_rules,
            valid_rules=valid_rules,
            workflow_entity_id=workflow_entity_id,
        )


        workflow_rules_search_details.additional_properties = d
        return workflow_rules_search_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
