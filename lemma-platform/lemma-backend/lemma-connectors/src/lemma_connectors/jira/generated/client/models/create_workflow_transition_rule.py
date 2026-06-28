from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_workflow_transition_rule_configuration import CreateWorkflowTransitionRuleConfiguration





T = TypeVar("T", bound="CreateWorkflowTransitionRule")



@_attrs_define
class CreateWorkflowTransitionRule:
    """ A workflow transition rule.

        Attributes:
            type_ (str): The type of the transition rule.
            configuration (CreateWorkflowTransitionRuleConfiguration | Unset): EXPERIMENTAL. The configuration of the
                transition rule.
     """

    type_: str
    configuration: CreateWorkflowTransitionRuleConfiguration | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workflow_transition_rule_configuration import CreateWorkflowTransitionRuleConfiguration
        type_ = self.type_

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_workflow_transition_rule_configuration import CreateWorkflowTransitionRuleConfiguration
        d = dict(src_dict)
        type_ = d.pop("type")

        _configuration = d.pop("configuration", UNSET)
        configuration: CreateWorkflowTransitionRuleConfiguration | Unset
        if isinstance(_configuration,  Unset):
            configuration = UNSET
        else:
            configuration = CreateWorkflowTransitionRuleConfiguration.from_dict(_configuration)




        create_workflow_transition_rule = cls(
            type_=type_,
            configuration=configuration,
        )

        return create_workflow_transition_rule

