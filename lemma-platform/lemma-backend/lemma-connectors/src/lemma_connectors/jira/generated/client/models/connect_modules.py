from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.connect_module import ConnectModule





T = TypeVar("T", bound="ConnectModules")



@_attrs_define
class ConnectModules:
    """ 
        Example:
            {'jiraEntityProperties': [{'entityType': 'issue', 'key': 'dynamic-attachment-entity-property',
                'keyConfigurations': [{'extractions': [{'alias': 'attachmentExtension', 'objectName': 'extension', 'type':
                'text'}], 'propertyKey': 'attachment'}], 'name': {'value': 'Attachment Index Document'}}], 'jiraIssueFields':
                [{'description': {'value': 'A dynamically added single-select field'}, 'extractions': [{'name': 'categoryName',
                'path': 'category', 'type': 'text'}], 'key': 'dynamic-select-field', 'name': {'value': 'Dynamic single select'},
                'type': 'single_select'}]}

        Attributes:
            modules (list[ConnectModule]): A list of app modules in the same format as the `modules` property in the
                [app descriptor](https://developer.atlassian.com/cloud/jira/platform/app-descriptor/).
     """

    modules: list[ConnectModule]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.connect_module import ConnectModule
        modules = []
        for modules_item_data in self.modules:
            modules_item = modules_item_data.to_dict()
            modules.append(modules_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "modules": modules,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connect_module import ConnectModule
        d = dict(src_dict)
        modules = []
        _modules = d.pop("modules")
        for modules_item_data in (_modules):
            modules_item = ConnectModule.from_dict(modules_item_data)



            modules.append(modules_item)


        connect_modules = cls(
            modules=modules,
        )


        connect_modules.additional_properties = d
        return connect_modules

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
