from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_compound_condition import WorkflowCompoundCondition
  from ..models.workflow_simple_condition import WorkflowSimpleCondition
  from ..models.workflow_transition_rule import WorkflowTransitionRule





T = TypeVar("T", bound="WorkflowRules")



@_attrs_define
class WorkflowRules:
    """ A collection of transition rules.

        Attributes:
            conditions_tree (Unset | WorkflowCompoundCondition | WorkflowSimpleCondition): The workflow transition rule
                conditions tree.
            post_functions (list[WorkflowTransitionRule] | Unset): The workflow post functions.
            validators (list[WorkflowTransitionRule] | Unset): The workflow validators.
     """

    conditions_tree: Unset | WorkflowCompoundCondition | WorkflowSimpleCondition = UNSET
    post_functions: list[WorkflowTransitionRule] | Unset = UNSET
    validators: list[WorkflowTransitionRule] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_compound_condition import WorkflowCompoundCondition
        from ..models.workflow_simple_condition import WorkflowSimpleCondition
        from ..models.workflow_transition_rule import WorkflowTransitionRule
        conditions_tree: dict[str, Any] | Unset
        if isinstance(self.conditions_tree, Unset):
            conditions_tree = UNSET
        elif isinstance(self.conditions_tree, WorkflowSimpleCondition):
            conditions_tree = self.conditions_tree.to_dict()
        else:
            conditions_tree = self.conditions_tree.to_dict()


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
        })
        if conditions_tree is not UNSET:
            field_dict["conditionsTree"] = conditions_tree
        if post_functions is not UNSET:
            field_dict["postFunctions"] = post_functions
        if validators is not UNSET:
            field_dict["validators"] = validators

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_compound_condition import WorkflowCompoundCondition
        from ..models.workflow_simple_condition import WorkflowSimpleCondition
        from ..models.workflow_transition_rule import WorkflowTransitionRule
        d = dict(src_dict)
        def _parse_conditions_tree(data: object) -> Unset | WorkflowCompoundCondition | WorkflowSimpleCondition:
            if isinstance(data, Unset):
                return data
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

        conditions_tree = _parse_conditions_tree(d.pop("conditionsTree", UNSET))


        _post_functions = d.pop("postFunctions", UNSET)
        post_functions: list[WorkflowTransitionRule] | Unset = UNSET
        if _post_functions is not UNSET:
            post_functions = []
            for post_functions_item_data in _post_functions:
                post_functions_item = WorkflowTransitionRule.from_dict(post_functions_item_data)



                post_functions.append(post_functions_item)


        _validators = d.pop("validators", UNSET)
        validators: list[WorkflowTransitionRule] | Unset = UNSET
        if _validators is not UNSET:
            validators = []
            for validators_item_data in _validators:
                validators_item = WorkflowTransitionRule.from_dict(validators_item_data)



                validators.append(validators_item)


        workflow_rules = cls(
            conditions_tree=conditions_tree,
            post_functions=post_functions,
            validators=validators,
        )

        return workflow_rules

