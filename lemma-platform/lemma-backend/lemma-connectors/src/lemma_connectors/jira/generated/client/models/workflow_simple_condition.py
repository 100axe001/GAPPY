from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_simple_condition_configuration import WorkflowSimpleConditionConfiguration





T = TypeVar("T", bound="WorkflowSimpleCondition")



@_attrs_define
class WorkflowSimpleCondition:
    """ A workflow transition rule condition. This object returns `nodeType` as `simple`.

        Attributes:
            node_type (str):
            type_ (str): The type of the transition rule.
            configuration (WorkflowSimpleConditionConfiguration | Unset): EXPERIMENTAL. The configuration of the transition
                rule.
     """

    node_type: str
    type_: str
    configuration: WorkflowSimpleConditionConfiguration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_simple_condition_configuration import WorkflowSimpleConditionConfiguration
        node_type = self.node_type

        type_ = self.type_

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "nodeType": node_type,
            "type": type_,
        })
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_simple_condition_configuration import WorkflowSimpleConditionConfiguration
        d = dict(src_dict)
        node_type = d.pop("nodeType")

        type_ = d.pop("type")

        _configuration = d.pop("configuration", UNSET)
        configuration: WorkflowSimpleConditionConfiguration | Unset
        if isinstance(_configuration,  Unset):
            configuration = UNSET
        else:
            configuration = WorkflowSimpleConditionConfiguration.from_dict(_configuration)




        workflow_simple_condition = cls(
            node_type=node_type,
            type_=type_,
            configuration=configuration,
        )


        workflow_simple_condition.additional_properties = d
        return workflow_simple_condition

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
