from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="EventDateTime")



@_attrs_define
class EventDateTime:
    """ 
        Attributes:
            date (datetime.date | Unset): The date, in the format "yyyy-mm-dd", if this is an all-day event.
            date_time (datetime.datetime | Unset): The time, as a combined date-time value (formatted according to RFC3339).
                A time zone offset is required unless a time zone is explicitly specified in timeZone.
            time_zone (str | Unset): The time zone in which the time is specified. (Formatted as an IANA Time Zone Database
                name, e.g. "Europe/Zurich".) For recurring events this field is required and specifies the time zone in which
                the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the
                event start/end.
     """

    date: datetime.date | Unset = UNSET
    date_time: datetime.datetime | Unset = UNSET
    time_zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        date_time: str | Unset = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

        time_zone = self.time_zone


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        _date_time = d.pop("dateTime", UNSET)
        date_time: datetime.datetime | Unset
        if isinstance(_date_time,  Unset):
            date_time = UNSET
        else:
            date_time = isoparse(_date_time)




        time_zone = d.pop("timeZone", UNSET)

        event_date_time = cls(
            date=date,
            date_time=date_time,
            time_zone=time_zone,
        )


        event_date_time.additional_properties = d
        return event_date_time

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
