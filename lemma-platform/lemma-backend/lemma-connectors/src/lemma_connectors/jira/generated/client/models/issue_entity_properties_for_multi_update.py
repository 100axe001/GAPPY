from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_entity_properties_for_multi_update_properties import IssueEntityPropertiesForMultiUpdateProperties





T = TypeVar("T", bound="IssueEntityPropertiesForMultiUpdate")



@_attrs_define
class IssueEntityPropertiesForMultiUpdate:
    """ An issue ID with entity property values. See [Entity
    properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/) for more information.

        Attributes:
            issue_id (int | Unset): The ID of the issue.
            properties (IssueEntityPropertiesForMultiUpdateProperties | Unset): Entity properties to set on the issue. The
                maximum length of an issue property value is 32768 characters.
     """

    issue_id: int | Unset = UNSET
    properties: IssueEntityPropertiesForMultiUpdateProperties | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_entity_properties_for_multi_update_properties import IssueEntityPropertiesForMultiUpdateProperties
        issue_id = self.issue_id

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issue_id is not UNSET:
            field_dict["issueID"] = issue_id
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_entity_properties_for_multi_update_properties import IssueEntityPropertiesForMultiUpdateProperties
        d = dict(src_dict)
        issue_id = d.pop("issueID", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: IssueEntityPropertiesForMultiUpdateProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = IssueEntityPropertiesForMultiUpdateProperties.from_dict(_properties)




        issue_entity_properties_for_multi_update = cls(
            issue_id=issue_id,
            properties=properties,
        )

        return issue_entity_properties_for_multi_update

