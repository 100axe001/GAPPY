from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_workflow_status_details import CreateWorkflowStatusDetails
  from ..models.create_workflow_transition_details import CreateWorkflowTransitionDetails





T = TypeVar("T", bound="CreateWorkflowDetails")



@_attrs_define
class CreateWorkflowDetails:
    """ The details of a workflow.

        Attributes:
            name (str): The name of the workflow. The name must be unique. The maximum length is 255 characters. Characters
                can be separated by a whitespace but the name cannot start or end with a whitespace.
            statuses (list[CreateWorkflowStatusDetails]): The statuses of the workflow. Any status that does not include a
                transition is added to the workflow without a transition.
            transitions (list[CreateWorkflowTransitionDetails]): The transitions of the workflow. For the request to be
                valid, these transitions must:

                 *  include one *initial* transition.
                 *  not use the same name for a *global* and *directed* transition.
                 *  have a unique name for each *global* transition.
                 *  have a unique 'to' status for each *global* transition.
                 *  have unique names for each transition from a status.
                 *  not have a 'from' status on *initial* and *global* transitions.
                 *  have a 'from' status on *directed* transitions.

                All the transition statuses must be included in `statuses`.
            description (str | Unset): The description of the workflow. The maximum length is 1000 characters.
     """

    name: str
    statuses: list[CreateWorkflowStatusDetails]
    transitions: list[CreateWorkflowTransitionDetails]
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workflow_status_details import CreateWorkflowStatusDetails
        from ..models.create_workflow_transition_details import CreateWorkflowTransitionDetails
        name = self.name

        statuses = []
        for statuses_item_data in self.statuses:
            statuses_item = statuses_item_data.to_dict()
            statuses.append(statuses_item)



        transitions = []
        for transitions_item_data in self.transitions:
            transitions_item = transitions_item_data.to_dict()
            transitions.append(transitions_item)



        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "statuses": statuses,
            "transitions": transitions,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_workflow_status_details import CreateWorkflowStatusDetails
        from ..models.create_workflow_transition_details import CreateWorkflowTransitionDetails
        d = dict(src_dict)
        name = d.pop("name")

        statuses = []
        _statuses = d.pop("statuses")
        for statuses_item_data in (_statuses):
            statuses_item = CreateWorkflowStatusDetails.from_dict(statuses_item_data)



            statuses.append(statuses_item)


        transitions = []
        _transitions = d.pop("transitions")
        for transitions_item_data in (_transitions):
            transitions_item = CreateWorkflowTransitionDetails.from_dict(transitions_item_data)



            transitions.append(transitions_item)


        description = d.pop("description", UNSET)

        create_workflow_details = cls(
            name=name,
            statuses=statuses,
            transitions=transitions,
            description=description,
        )

        return create_workflow_details

