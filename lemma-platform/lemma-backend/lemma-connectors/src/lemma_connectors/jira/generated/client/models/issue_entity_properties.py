from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_entity_properties_properties import IssueEntityPropertiesProperties





T = TypeVar("T", bound="IssueEntityProperties")



@_attrs_define
class IssueEntityProperties:
    """ Lists of issues and entity properties. See [Entity
    properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/) for more information.

        Attributes:
            entities_ids (list[int] | Unset): A list of entity property IDs.
            properties (IssueEntityPropertiesProperties | Unset): A list of entity property keys and values.
     """

    entities_ids: list[int] | Unset = UNSET
    properties: IssueEntityPropertiesProperties | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_entity_properties_properties import IssueEntityPropertiesProperties
        entities_ids: list[int] | Unset = UNSET
        if not isinstance(self.entities_ids, Unset):
            entities_ids = self.entities_ids



        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entities_ids is not UNSET:
            field_dict["entitiesIds"] = entities_ids
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_entity_properties_properties import IssueEntityPropertiesProperties
        d = dict(src_dict)
        entities_ids = cast(list[int], d.pop("entitiesIds", UNSET))


        _properties = d.pop("properties", UNSET)
        properties: IssueEntityPropertiesProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = IssueEntityPropertiesProperties.from_dict(_properties)




        issue_entity_properties = cls(
            entities_ids=entities_ids,
            properties=properties,
        )

        return issue_entity_properties

