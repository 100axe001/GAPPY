from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.json_node import JsonNode





T = TypeVar("T", bound="IssueEntityPropertiesForMultiUpdateProperties")



@_attrs_define
class IssueEntityPropertiesForMultiUpdateProperties:
    """ Entity properties to set on the issue. The maximum length of an issue property value is 32768 characters.

     """

    additional_properties: dict[str, JsonNode] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.json_node import JsonNode
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_node import JsonNode
        d = dict(src_dict)
        issue_entity_properties_for_multi_update_properties = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = JsonNode.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        issue_entity_properties_for_multi_update_properties.additional_properties = additional_properties
        return issue_entity_properties_for_multi_update_properties

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> JsonNode:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: JsonNode) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
