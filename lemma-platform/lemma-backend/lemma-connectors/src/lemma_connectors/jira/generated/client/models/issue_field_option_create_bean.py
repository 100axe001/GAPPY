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
  from ..models.issue_field_option_create_bean_properties import IssueFieldOptionCreateBeanProperties





T = TypeVar("T", bound="IssueFieldOptionCreateBean")



@_attrs_define
class IssueFieldOptionCreateBean:
    """ 
        Attributes:
            value (str): The option's name, which is displayed in Jira.
            config (IssueFieldOptionConfiguration | Unset): Details of the projects the option is available in.
            properties (IssueFieldOptionCreateBeanProperties | Unset): The properties of the option as arbitrary key-value
                pairs. These properties can be searched using JQL, if the extractions (see
                https://developer.atlassian.com/cloud/jira/platform/modules/issue-field-option-property-index/) are defined in
                the descriptor for the issue field module.
     """

    value: str
    config: IssueFieldOptionConfiguration | Unset = UNSET
    properties: IssueFieldOptionCreateBeanProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_field_option_configuration import IssueFieldOptionConfiguration
        from ..models.issue_field_option_create_bean_properties import IssueFieldOptionCreateBeanProperties
        value = self.value

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
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
        from ..models.issue_field_option_create_bean_properties import IssueFieldOptionCreateBeanProperties
        d = dict(src_dict)
        value = d.pop("value")

        _config = d.pop("config", UNSET)
        config: IssueFieldOptionConfiguration | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = IssueFieldOptionConfiguration.from_dict(_config)




        _properties = d.pop("properties", UNSET)
        properties: IssueFieldOptionCreateBeanProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = IssueFieldOptionCreateBeanProperties.from_dict(_properties)




        issue_field_option_create_bean = cls(
            value=value,
            config=config,
            properties=properties,
        )


        issue_field_option_create_bean.additional_properties = d
        return issue_field_option_create_bean

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
