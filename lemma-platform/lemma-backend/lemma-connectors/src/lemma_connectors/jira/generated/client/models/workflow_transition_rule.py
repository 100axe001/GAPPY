from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WorkflowTransitionRule")



@_attrs_define
class WorkflowTransitionRule:
    """ A workflow transition rule.

        Attributes:
            type_ (str): The type of the transition rule.
            configuration (Any | Unset): EXPERIMENTAL. The configuration of the transition rule.
     """

    type_: str
    configuration: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        configuration = self.configuration


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        configuration = d.pop("configuration", UNSET)

        workflow_transition_rule = cls(
            type_=type_,
            configuration=configuration,
        )

        return workflow_transition_rule

