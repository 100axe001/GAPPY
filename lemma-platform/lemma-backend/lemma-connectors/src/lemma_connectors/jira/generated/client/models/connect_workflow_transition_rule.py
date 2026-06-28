from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rule_configuration import RuleConfiguration
  from ..models.workflow_transition import WorkflowTransition





T = TypeVar("T", bound="ConnectWorkflowTransitionRule")



@_attrs_define
class ConnectWorkflowTransitionRule:
    """ A workflow transition rule.

        Attributes:
            configuration (RuleConfiguration): A rule configuration.
            id (str): The ID of the transition rule.
            key (str): The key of the rule, as defined in the Connect app descriptor.
            transition (WorkflowTransition | Unset): A workflow transition.
     """

    configuration: RuleConfiguration
    id: str
    key: str
    transition: WorkflowTransition | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.rule_configuration import RuleConfiguration
        from ..models.workflow_transition import WorkflowTransition
        configuration = self.configuration.to_dict()

        id = self.id

        key = self.key

        transition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transition, Unset):
            transition = self.transition.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "configuration": configuration,
            "id": id,
            "key": key,
        })
        if transition is not UNSET:
            field_dict["transition"] = transition

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_configuration import RuleConfiguration
        from ..models.workflow_transition import WorkflowTransition
        d = dict(src_dict)
        configuration = RuleConfiguration.from_dict(d.pop("configuration"))




        id = d.pop("id")

        key = d.pop("key")

        _transition = d.pop("transition", UNSET)
        transition: WorkflowTransition | Unset
        if isinstance(_transition,  Unset):
            transition = UNSET
        else:
            transition = WorkflowTransition.from_dict(_transition)




        connect_workflow_transition_rule = cls(
            configuration=configuration,
            id=id,
            key=key,
            transition=transition,
        )

        return connect_workflow_transition_rule

