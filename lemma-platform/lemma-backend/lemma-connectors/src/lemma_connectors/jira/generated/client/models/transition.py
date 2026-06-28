from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.transition_type import TransitionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.transition_properties import TransitionProperties
  from ..models.transition_screen_details import TransitionScreenDetails
  from ..models.workflow_rules import WorkflowRules





T = TypeVar("T", bound="Transition")



@_attrs_define
class Transition:
    """ Details of a workflow transition.

        Attributes:
            description (str): The description of the transition.
            from_ (list[str]): The statuses the transition can start from.
            id (str): The ID of the transition.
            name (str): The name of the transition.
            to (str): The status the transition goes to.
            type_ (TransitionType): The type of the transition.
            properties (TransitionProperties | Unset): The properties of the transition.
            rules (WorkflowRules | Unset): A collection of transition rules.
            screen (TransitionScreenDetails | Unset): The details of a transition screen.
     """

    description: str
    from_: list[str]
    id: str
    name: str
    to: str
    type_: TransitionType
    properties: TransitionProperties | Unset = UNSET
    rules: WorkflowRules | Unset = UNSET
    screen: TransitionScreenDetails | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.transition_properties import TransitionProperties
        from ..models.transition_screen_details import TransitionScreenDetails
        from ..models.workflow_rules import WorkflowRules
        description = self.description

        from_ = self.from_



        id = self.id

        name = self.name

        to = self.to

        type_ = self.type_.value

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
            "description": description,
            "from": from_,
            "id": id,
            "name": name,
            "to": to,
            "type": type_,
        })
        if properties is not UNSET:
            field_dict["properties"] = properties
        if rules is not UNSET:
            field_dict["rules"] = rules
        if screen is not UNSET:
            field_dict["screen"] = screen

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transition_properties import TransitionProperties
        from ..models.transition_screen_details import TransitionScreenDetails
        from ..models.workflow_rules import WorkflowRules
        d = dict(src_dict)
        description = d.pop("description")

        from_ = cast(list[str], d.pop("from"))


        id = d.pop("id")

        name = d.pop("name")

        to = d.pop("to")

        type_ = TransitionType(d.pop("type"))




        _properties = d.pop("properties", UNSET)
        properties: TransitionProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = TransitionProperties.from_dict(_properties)




        _rules = d.pop("rules", UNSET)
        rules: WorkflowRules | Unset
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = WorkflowRules.from_dict(_rules)




        _screen = d.pop("screen", UNSET)
        screen: TransitionScreenDetails | Unset
        if isinstance(_screen,  Unset):
            screen = UNSET
        else:
            screen = TransitionScreenDetails.from_dict(_screen)




        transition = cls(
            description=description,
            from_=from_,
            id=id,
            name=name,
            to=to,
            type_=type_,
            properties=properties,
            rules=rules,
            screen=screen,
        )

        return transition

