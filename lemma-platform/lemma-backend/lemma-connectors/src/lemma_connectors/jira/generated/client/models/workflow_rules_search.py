from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="WorkflowRulesSearch")



@_attrs_define
class WorkflowRulesSearch:
    """ Details of the workflow and its transition rules.

        Attributes:
            rule_ids (list[UUID]): The list of workflow rule IDs.
            workflow_entity_id (UUID): The workflow ID. Example: a498d711-685d-428d-8c3e-bc03bb450ea7.
            expand (str | Unset): Use expand to include additional information in the response. This parameter accepts
                `transition` which, for each rule, returns information about the transition the rule is assigned to. Example:
                transition.
     """

    rule_ids: list[UUID]
    workflow_entity_id: UUID
    expand: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rule_ids = []
        for rule_ids_item_data in self.rule_ids:
            rule_ids_item = str(rule_ids_item_data)
            rule_ids.append(rule_ids_item)



        workflow_entity_id = str(self.workflow_entity_id)

        expand = self.expand


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ruleIds": rule_ids,
            "workflowEntityId": workflow_entity_id,
        })
        if expand is not UNSET:
            field_dict["expand"] = expand

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_ids = []
        _rule_ids = d.pop("ruleIds")
        for rule_ids_item_data in (_rule_ids):
            rule_ids_item = UUID(rule_ids_item_data)



            rule_ids.append(rule_ids_item)


        workflow_entity_id = UUID(d.pop("workflowEntityId"))




        expand = d.pop("expand", UNSET)

        workflow_rules_search = cls(
            rule_ids=rule_ids,
            workflow_entity_id=workflow_entity_id,
            expand=expand,
        )


        workflow_rules_search.additional_properties = d
        return workflow_rules_search

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
