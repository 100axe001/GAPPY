from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="EventWorkingLocationPropertiesOfficeLocation")



@_attrs_define
class EventWorkingLocationPropertiesOfficeLocation:
    """ If present, specifies that the user is working from an office.

        Attributes:
            building_id (str | Unset): An optional building identifier. This should reference a building ID in the
                organization's Resources database.
            desk_id (str | Unset): An optional arbitrary desk identifier.
            floor_id (str | Unset): An optional arbitrary floor identifier.
            floor_section_id (str | Unset): An optional arbitrary floor section identifier.
            label (str | Unset): An optional extra label for additional information.
     """

    building_id: str | Unset = UNSET
    desk_id: str | Unset = UNSET
    floor_id: str | Unset = UNSET
    floor_section_id: str | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        building_id = self.building_id

        desk_id = self.desk_id

        floor_id = self.floor_id

        floor_section_id = self.floor_section_id

        label = self.label


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if building_id is not UNSET:
            field_dict["buildingId"] = building_id
        if desk_id is not UNSET:
            field_dict["deskId"] = desk_id
        if floor_id is not UNSET:
            field_dict["floorId"] = floor_id
        if floor_section_id is not UNSET:
            field_dict["floorSectionId"] = floor_section_id
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        building_id = d.pop("buildingId", UNSET)

        desk_id = d.pop("deskId", UNSET)

        floor_id = d.pop("floorId", UNSET)

        floor_section_id = d.pop("floorSectionId", UNSET)

        label = d.pop("label", UNSET)

        event_working_location_properties_office_location = cls(
            building_id=building_id,
            desk_id=desk_id,
            floor_id=floor_id,
            floor_section_id=floor_section_id,
            label=label,
        )


        event_working_location_properties_office_location.additional_properties = d
        return event_working_location_properties_office_location

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
