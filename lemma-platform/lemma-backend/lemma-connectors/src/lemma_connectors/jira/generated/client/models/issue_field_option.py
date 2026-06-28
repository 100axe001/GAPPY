from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_field_option_configuration import IssueFieldOptionConfiguration
  from ..models.issue_field_option_properties import IssueFieldOptionProperties





T = TypeVar("T", bound="IssueFieldOption")



@_attrs_define
class IssueFieldOption:
    """ Details of the options for a select list issue field.

        Attributes:
            id (int): The unique identifier for the option. This is only unique within the select field's set of options.
            value (str): The option's name, which is displayed in Jira.
            config (IssueFieldOptionConfiguration | Unset): Details of the projects the option is available in.
            properties (IssueFieldOptionProperties | Unset): The properties of the object, as arbitrary key-value pairs.
                These properties can be searched using JQL, if the extractions (see [Issue Field Option Property
                Index](https://developer.atlassian.com/cloud/jira/platform/modules/issue-field-option-property-index/)) are
                defined in the descriptor for the issue field module.
     """

    id: int
    value: str
    config: IssueFieldOptionConfiguration | Unset = UNSET
    properties: IssueFieldOptionProperties | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_field_option_configuration import IssueFieldOptionConfiguration
        from ..models.issue_field_option_properties import IssueFieldOptionProperties
        id = self.id

        value = self.value

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "value": value,
        })
        if config is not UNSET:
            field_dict["config"] = config
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_field_option_configuration import IssueFieldOptionConfiguration
        from ..models.issue_field_option_properties import IssueFieldOptionProperties
        d = dict(src_dict)
        id = d.pop("id")

        value = d.pop("value")

        _config = d.pop("config", UNSET)
        config: IssueFieldOptionConfiguration | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = IssueFieldOptionConfiguration.from_dict(_config)




        _properties = d.pop("properties", UNSET)
        properties: IssueFieldOptionProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = IssueFieldOptionProperties.from_dict(_properties)




        issue_field_option = cls(
            id=id,
            value=value,
            config=config,
            properties=properties,
        )

        return issue_field_option

