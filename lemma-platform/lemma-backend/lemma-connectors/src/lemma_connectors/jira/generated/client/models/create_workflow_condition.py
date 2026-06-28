from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_workflow_condition_operator import CreateWorkflowConditionOperator
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_workflow_condition_configuration import CreateWorkflowConditionConfiguration





T = TypeVar("T", bound="CreateWorkflowCondition")



@_attrs_define
class CreateWorkflowCondition:
    """ A workflow transition condition.

        Attributes:
            conditions (list[CreateWorkflowCondition] | Unset): The list of workflow conditions.
            configuration (CreateWorkflowConditionConfiguration | Unset): EXPERIMENTAL. The configuration of the transition
                rule.
            operator (CreateWorkflowConditionOperator | Unset): The compound condition operator.
            type_ (str | Unset): The type of the transition rule.
     """

    conditions: list[CreateWorkflowCondition] | Unset = UNSET
    configuration: CreateWorkflowConditionConfiguration | Unset = UNSET
    operator: CreateWorkflowConditionOperator | Unset = UNSET
    type_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workflow_condition_configuration import CreateWorkflowConditionConfiguration
        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)



        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value


        type_ = self.type_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if operator is not UNSET:
            field_dict["operator"] = operator
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_workflow_condition_configuration import CreateWorkflowConditionConfiguration
        d = dict(src_dict)
        _conditions = d.pop("conditions", UNSET)
        conditions: list[CreateWorkflowCondition] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = CreateWorkflowCondition.from_dict(conditions_item_data)



                conditions.append(conditions_item)


        _configuration = d.pop("configuration", UNSET)
        configuration: CreateWorkflowConditionConfiguration | Unset
        if isinstance(_configuration,  Unset):
            configuration = UNSET
        else:
            configuration = CreateWorkflowConditionConfiguration.from_dict(_configuration)




        _operator = d.pop("operator", UNSET)
        operator: CreateWorkflowConditionOperator | Unset
        if isinstance(_operator,  Unset):
            operator = UNSET
        else:
            operator = CreateWorkflowConditionOperator(_operator)




        type_ = d.pop("type", UNSET)

        create_workflow_condition = cls(
            conditions=conditions,
            configuration=configuration,
            operator=operator,
            type_=type_,
        )

        return create_workflow_condition

