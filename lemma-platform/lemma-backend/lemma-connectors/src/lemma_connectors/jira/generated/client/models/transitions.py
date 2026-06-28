from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_transition import IssueTransition





T = TypeVar("T", bound="Transitions")



@_attrs_define
class Transitions:
    """ List of issue transitions.

        Attributes:
            expand (str | Unset): Expand options that include additional transitions details in the response.
            transitions (list[IssueTransition] | Unset): List of issue transitions.
     """

    expand: str | Unset = UNSET
    transitions: list[IssueTransition] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_transition import IssueTransition
        expand = self.expand

        transitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transitions, Unset):
            transitions = []
            for transitions_item_data in self.transitions:
                transitions_item = transitions_item_data.to_dict()
                transitions.append(transitions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expand is not UNSET:
            field_dict["expand"] = expand
        if transitions is not UNSET:
            field_dict["transitions"] = transitions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_transition import IssueTransition
        d = dict(src_dict)
        expand = d.pop("expand", UNSET)

        _transitions = d.pop("transitions", UNSET)
        transitions: list[IssueTransition] | Unset = UNSET
        if _transitions is not UNSET:
            transitions = []
            for transitions_item_data in _transitions:
                transitions_item = IssueTransition.from_dict(transitions_item_data)



                transitions.append(transitions_item)


        transitions = cls(
            expand=expand,
            transitions=transitions,
        )

        return transitions

