from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ServiceManagementNavigationInfo")



@_attrs_define
class ServiceManagementNavigationInfo:
    """ 
        Attributes:
            queue_category (str | Unset):
            queue_id (int | Unset):
            queue_name (str | Unset):
     """

    queue_category: str | Unset = UNSET
    queue_id: int | Unset = UNSET
    queue_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        queue_category = self.queue_category

        queue_id = self.queue_id

        queue_name = self.queue_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if queue_category is not UNSET:
            field_dict["queueCategory"] = queue_category
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if queue_name is not UNSET:
            field_dict["queueName"] = queue_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        queue_category = d.pop("queueCategory", UNSET)

        queue_id = d.pop("queueId", UNSET)

        queue_name = d.pop("queueName", UNSET)

        service_management_navigation_info = cls(
            queue_category=queue_category,
            queue_id=queue_id,
            queue_name=queue_name,
        )


        service_management_navigation_info.additional_properties = d
        return service_management_navigation_info

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
