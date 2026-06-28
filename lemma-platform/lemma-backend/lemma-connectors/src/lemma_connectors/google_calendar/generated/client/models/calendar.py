from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conference_properties import ConferenceProperties





T = TypeVar("T", bound="Calendar")



@_attrs_define
class Calendar:
    """ 
        Attributes:
            conference_properties (ConferenceProperties | Unset):
            description (str | Unset): Description of the calendar. Optional.
            etag (str | Unset): ETag of the resource.
            id (str | Unset): Identifier of the calendar. To retrieve IDs call the calendarList.list() method.
            kind (str | Unset): Type of the resource ("calendar#calendar"). Default: 'calendar#calendar'.
            location (str | Unset): Geographic location of the calendar as free-form text. Optional.
            summary (str | Unset): Title of the calendar.
            time_zone (str | Unset): The time zone of the calendar. (Formatted as an IANA Time Zone Database name, e.g.
                "Europe/Zurich".) Optional.
     """

    conference_properties: ConferenceProperties | Unset = UNSET
    description: str | Unset = UNSET
    etag: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'calendar#calendar'
    location: str | Unset = UNSET
    summary: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conference_properties import ConferenceProperties
        conference_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conference_properties, Unset):
            conference_properties = self.conference_properties.to_dict()

        description = self.description

        etag = self.etag

        id = self.id

        kind = self.kind

        location = self.location

        summary = self.summary

        time_zone = self.time_zone


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if conference_properties is not UNSET:
            field_dict["conferenceProperties"] = conference_properties
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if location is not UNSET:
            field_dict["location"] = location
        if summary is not UNSET:
            field_dict["summary"] = summary
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conference_properties import ConferenceProperties
        d = dict(src_dict)
        _conference_properties = d.pop("conferenceProperties", UNSET)
        conference_properties: ConferenceProperties | Unset
        if isinstance(_conference_properties,  Unset):
            conference_properties = UNSET
        else:
            conference_properties = ConferenceProperties.from_dict(_conference_properties)




        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        location = d.pop("location", UNSET)

        summary = d.pop("summary", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        calendar = cls(
            conference_properties=conference_properties,
            description=description,
            etag=etag,
            id=id,
            kind=kind,
            location=location,
            summary=summary,
            time_zone=time_zone,
        )


        calendar.additional_properties = d
        return calendar

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
