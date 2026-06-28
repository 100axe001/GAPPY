from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.status_category import StatusCategory





T = TypeVar("T", bound="StatusDetails")



@_attrs_define
class StatusDetails:
    """ A status.

        Attributes:
            description (str | Unset): The description of the status.
            icon_url (str | Unset): The URL of the icon used to represent the status.
            id (str | Unset): The ID of the status.
            name (str | Unset): The name of the status.
            self_ (str | Unset): The URL of the status.
            status_category (StatusCategory | Unset): A status category.
     """

    description: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET
    status_category: StatusCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_category import StatusCategory
        description = self.description

        icon_url = self.icon_url

        id = self.id

        name = self.name

        self_ = self.self_

        status_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_category, Unset):
            status_category = self.status_category.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_category import StatusCategory
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        _status_category = d.pop("statusCategory", UNSET)
        status_category: StatusCategory | Unset
        if isinstance(_status_category,  Unset):
            status_category = UNSET
        else:
            status_category = StatusCategory.from_dict(_status_category)




        status_details = cls(
            description=description,
            icon_url=icon_url,
            id=id,
            name=name,
            self_=self_,
            status_category=status_category,
        )


        status_details.additional_properties = d
        return status_details

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
