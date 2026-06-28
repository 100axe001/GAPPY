from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.workflow_compound_condition_operator import WorkflowCompoundConditionOperator
from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_simple_condition import WorkflowSimpleCondition





T = TypeVar("T", bound="WorkflowCompoundCondition")



@_attrs_define
class WorkflowCompoundCondition:
    """ A compound workflow transition rule condition. This object returns `nodeType` as `compound`.

        Attributes:
            conditions (list[WorkflowCompoundCondition | WorkflowSimpleCondition]): The list of workflow conditions.
            node_type (str):
            operator (WorkflowCompoundConditionOperator): The compound condition operator.
     """

    conditions: list[WorkflowCompoundCondition | WorkflowSimpleCondition]
    node_type: str
    operator: WorkflowCompoundConditionOperator
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_simple_condition import WorkflowSimpleCondition
        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item: dict[str, Any]
            if isinstance(conditions_item_data, WorkflowSimpleCondition):
                conditions_item = conditions_item_data.to_dict()
            else:
                conditions_item = conditions_item_data.to_dict()

            conditions.append(conditions_item)



        node_type = self.node_type

        operator = self.operator.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "conditions": conditions,
            "nodeType": node_type,
            "operator": operator,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_simple_condition import WorkflowSimpleCondition
        d = dict(src_dict)
        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in (_conditions):
            def _parse_conditions_item(data: object) -> WorkflowCompoundCondition | WorkflowSimpleCondition:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_workflow_condition_type_0 = WorkflowSimpleCondition.from_dict(data)



                    return componentsschemas_workflow_condition_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_condition_type_1 = WorkflowCompoundCondition.from_dict(data)



                return componentsschemas_workflow_condition_type_1

            conditions_item = _parse_conditions_item(conditions_item_data)

            conditions.append(conditions_item)


        node_type = d.pop("nodeType")

        operator = WorkflowCompoundConditionOperator(d.pop("operator"))




        workflow_compound_condition = cls(
            conditions=conditions,
            node_type=node_type,
            operator=operator,
        )


        workflow_compound_condition.additional_properties = d
        return workflow_compound_condition

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
