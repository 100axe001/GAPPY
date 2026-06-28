from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.event_working_location_properties_custom_location import EventWorkingLocationPropertiesCustomLocation
  from ..models.event_working_location_properties_office_location import EventWorkingLocationPropertiesOfficeLocation





T = TypeVar("T", bound="EventWorkingLocationProperties")



@_attrs_define
class EventWorkingLocationProperties:
    """ 
        Attributes:
            custom_location (EventWorkingLocationPropertiesCustomLocation | Unset): If present, specifies that the user is
                working from a custom location.
            home_office (Any | Unset): If present, specifies that the user is working at home.
            office_location (EventWorkingLocationPropertiesOfficeLocation | Unset): If present, specifies that the user is
                working from an office.
     """

    custom_location: EventWorkingLocationPropertiesCustomLocation | Unset = UNSET
    home_office: Any | Unset = UNSET
    office_location: EventWorkingLocationPropertiesOfficeLocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.event_working_location_properties_custom_location import EventWorkingLocationPropertiesCustomLocation
        from ..models.event_working_location_properties_office_location import EventWorkingLocationPropertiesOfficeLocation
        custom_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_location, Unset):
            custom_location = self.custom_location.to_dict()

        home_office = self.home_office

        office_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.office_location, Unset):
            office_location = self.office_location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if custom_location is not UNSET:
            field_dict["customLocation"] = custom_location
        if home_office is not UNSET:
            field_dict["homeOffice"] = home_office
        if office_location is not UNSET:
            field_dict["officeLocation"] = office_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_working_location_properties_custom_location import EventWorkingLocationPropertiesCustomLocation
        from ..models.event_working_location_properties_office_location import EventWorkingLocationPropertiesOfficeLocation
        d = dict(src_dict)
        _custom_location = d.pop("customLocation", UNSET)
        custom_location: EventWorkingLocationPropertiesCustomLocation | Unset
        if isinstance(_custom_location,  Unset):
            custom_location = UNSET
        else:
            custom_location = EventWorkingLocationPropertiesCustomLocation.from_dict(_custom_location)




        home_office = d.pop("homeOffice", UNSET)

        _office_location = d.pop("officeLocation", UNSET)
        office_location: EventWorkingLocationPropertiesOfficeLocation | Unset
        if isinstance(_office_location,  Unset):
            office_location = UNSET
        else:
            office_location = EventWorkingLocationPropertiesOfficeLocation.from_dict(_office_location)




        event_working_location_properties = cls(
            custom_location=custom_location,
            home_office=home_office,
            office_location=office_location,
        )


        event_working_location_properties.additional_properties = d
        return event_working_location_properties

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
