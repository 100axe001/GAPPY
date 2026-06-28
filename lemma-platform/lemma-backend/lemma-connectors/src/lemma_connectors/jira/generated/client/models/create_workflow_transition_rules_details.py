from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_workflow_condition import CreateWorkflowCondition
  from ..models.create_workflow_transition_rule import CreateWorkflowTransitionRule





T = TypeVar("T", bound="CreateWorkflowTransitionRulesDetails")



@_attrs_define
class CreateWorkflowTransitionRulesDetails:
    """ The details of a workflow transition rules.

        Attributes:
            conditions (CreateWorkflowCondition | Unset): A workflow transition condition.
            post_functions (list[CreateWorkflowTransitionRule] | Unset): The workflow post functions.

                **Note:** The default post functions are always added to the *initial* transition, as in:

                    "postFunctions": [
                        {
                            "type": "IssueCreateFunction"
                        },
                        {
                            "type": "IssueReindexFunction"
                        },
                        {
                            "type": "FireIssueEventFunction",
                            "configuration": {
                                "event": {
                                    "id": "1",
                                    "name": "issue_created"
                                }
                            }
                        }
                    ]

                **Note:** The default post functions are always added to the *global* and *directed* transitions, as in:

                    "postFunctions": [
                        {
                            "type": "UpdateIssueStatusFunction"
                        },
                        {
                            "type": "CreateCommentFunction"
                        },
                        {
                            "type": "GenerateChangeHistoryFunction"
                        },
                        {
                            "type": "IssueReindexFunction"
                        },
                        {
                            "type": "FireIssueEventFunction",
                            "configuration": {
                                "event": {
                                    "id": "13",
                                    "name": "issue_generic"
                                }
                            }
                        }
                    ]
            validators (list[CreateWorkflowTransitionRule] | Unset): The workflow validators.

                **Note:** The default permission validator is always added to the *initial* transition, as in:

                    "validators": [
                        {
                            "type": "PermissionValidator",
                            "configuration": {
                                "permissionKey": "CREATE_ISSUES"
                            }
                        }
                    ]
     """

    conditions: CreateWorkflowCondition | Unset = UNSET
    post_functions: list[CreateWorkflowTransitionRule] | Unset = UNSET
    validators: list[CreateWorkflowTransitionRule] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workflow_condition import CreateWorkflowCondition
        from ..models.create_workflow_transition_rule import CreateWorkflowTransitionRule
        conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

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
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if post_functions is not UNSET:
            field_dict["postFunctions"] = post_functions
        if validators is not UNSET:
            field_dict["validators"] = validators

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_workflow_condition import CreateWorkflowCondition
        from ..models.create_workflow_transition_rule import CreateWorkflowTransitionRule
        d = dict(src_dict)
        _conditions = d.pop("conditions", UNSET)
        conditions: CreateWorkflowCondition | Unset
        if isinstance(_conditions,  Unset):
            conditions = UNSET
        else:
            conditions = CreateWorkflowCondition.from_dict(_conditions)




        _post_functions = d.pop("postFunctions", UNSET)
        post_functions: list[CreateWorkflowTransitionRule] | Unset = UNSET
        if _post_functions is not UNSET:
            post_functions = []
            for post_functions_item_data in _post_functions:
                post_functions_item = CreateWorkflowTransitionRule.from_dict(post_functions_item_data)



                post_functions.append(post_functions_item)


        _validators = d.pop("validators", UNSET)
        validators: list[CreateWorkflowTransitionRule] | Unset = UNSET
        if _validators is not UNSET:
            validators = []
            for validators_item_data in _validators:
                validators_item = CreateWorkflowTransitionRule.from_dict(validators_item_data)



                validators.append(validators_item)


        create_workflow_transition_rules_details = cls(
            conditions=conditions,
            post_functions=post_functions,
            validators=validators,
        )

        return create_workflow_transition_rules_details

