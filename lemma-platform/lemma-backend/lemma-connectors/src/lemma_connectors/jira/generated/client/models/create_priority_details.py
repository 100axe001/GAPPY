from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_priority_details_icon_url import CreatePriorityDetailsIconUrl
from ..types import UNSET, Unset






T = TypeVar("T", bound="CreatePriorityDetails")



@_attrs_define
class CreatePriorityDetails:
    """ Details of an issue priority.

        Attributes:
            name (str): The name of the priority. Must be unique.
            status_color (str): The status color of the priority in 3-digit or 6-digit hexadecimal format.
            description (str | Unset): The description of the priority.
            icon_url (CreatePriorityDetailsIconUrl | Unset): The URL of an icon for the priority. Accepted protocols are
                HTTP and HTTPS. Built in icons can also be used.
     """

    name: str
    status_color: str
    description: str | Unset = UNSET
    icon_url: CreatePriorityDetailsIconUrl | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status_color = self.status_color

        description = self.description

        icon_url: str | Unset = UNSET
        if not isinstance(self.icon_url, Unset):
            icon_url = self.icon_url.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "statusColor": status_color,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        status_color = d.pop("statusColor")

        description = d.pop("description", UNSET)

        _icon_url = d.pop("iconUrl", UNSET)
        icon_url: CreatePriorityDetailsIconUrl | Unset
        if isinstance(_icon_url,  Unset):
            icon_url = UNSET
        else:
            icon_url = CreatePriorityDetailsIconUrl(_icon_url)




        create_priority_details = cls(
            name=name,
            status_color=status_color,
            description=description,
            icon_url=icon_url,
        )


        create_priority_details.additional_properties = d
        return create_priority_details

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
