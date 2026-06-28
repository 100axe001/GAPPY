from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_workflow_transition_details_type import CreateWorkflowTransitionDetailsType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_workflow_transition_details_properties import CreateWorkflowTransitionDetailsProperties
  from ..models.create_workflow_transition_rules_details import CreateWorkflowTransitionRulesDetails
  from ..models.create_workflow_transition_screen_details import CreateWorkflowTransitionScreenDetails





T = TypeVar("T", bound="CreateWorkflowTransitionDetails")



@_attrs_define
class CreateWorkflowTransitionDetails:
    """ The details of a workflow transition.

        Attributes:
            name (str): The name of the transition. The maximum length is 60 characters.
            to (str): The status the transition goes to.
            type_ (CreateWorkflowTransitionDetailsType): The type of the transition.
            description (str | Unset): The description of the transition. The maximum length is 1000 characters.
            from_ (list[str] | Unset): The statuses the transition can start from.
            properties (CreateWorkflowTransitionDetailsProperties | Unset): The properties of the transition.
            rules (CreateWorkflowTransitionRulesDetails | Unset): The details of a workflow transition rules.
            screen (CreateWorkflowTransitionScreenDetails | Unset): The details of a transition screen.
     """

    name: str
    to: str
    type_: CreateWorkflowTransitionDetailsType
    description: str | Unset = UNSET
    from_: list[str] | Unset = UNSET
    properties: CreateWorkflowTransitionDetailsProperties | Unset = UNSET
    rules: CreateWorkflowTransitionRulesDetails | Unset = UNSET
    screen: CreateWorkflowTransitionScreenDetails | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workflow_transition_details_properties import CreateWorkflowTransitionDetailsProperties
        from ..models.create_workflow_transition_rules_details import CreateWorkflowTransitionRulesDetails
        from ..models.create_workflow_transition_screen_details import CreateWorkflowTransitionScreenDetails
        name = self.name

        to = self.to

        type_ = self.type_.value

        description = self.description

        from_: list[str] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_



        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        screen: dict[str, Any] | Unset = UNSET
        if not isinstance(self.screen, Unset):
            screen = self.screen.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "to": to,
            "type": type_,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if from_ is not UNSET:
            field_dict["from"] = from_
        if properties is not UNSET:
            field_dict["properties"] = properties
        if rules is not UNSET:
            field_dict["rules"] = rules
        if screen is not UNSET:
            field_dict["screen"] = screen

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_workflow_transition_details_properties import CreateWorkflowTransitionDetailsProperties
        from ..models.create_workflow_transition_rules_details import CreateWorkflowTransitionRulesDetails
        from ..models.create_workflow_transition_screen_details import CreateWorkflowTransitionScreenDetails
        d = dict(src_dict)
        name = d.pop("name")

        to = d.pop("to")

        type_ = CreateWorkflowTransitionDetailsType(d.pop("type"))




        description = d.pop("description", UNSET)

        from_ = cast(list[str], d.pop("from", UNSET))


        _properties = d.pop("properties", UNSET)
        properties: CreateWorkflowTransitionDetailsProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = CreateWorkflowTransitionDetailsProperties.from_dict(_properties)




        _rules = d.pop("rules", UNSET)
        rules: CreateWorkflowTransitionRulesDetails | Unset
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = CreateWorkflowTransitionRulesDetails.from_dict(_rules)




        _screen = d.pop("screen", UNSET)
        screen: CreateWorkflowTransitionScreenDetails | Unset
        if isinstance(_screen,  Unset):
            screen = UNSET
        else:
            screen = CreateWorkflowTransitionScreenDetails.from_dict(_screen)




        create_workflow_transition_details = cls(
            name=name,
            to=to,
            type_=type_,
            description=description,
            from_=from_,
            properties=properties,
            rules=rules,
            screen=screen,
        )

        return create_workflow_transition_details

