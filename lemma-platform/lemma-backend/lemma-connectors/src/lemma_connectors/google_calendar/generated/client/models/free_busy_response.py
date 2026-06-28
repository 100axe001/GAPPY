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

if TYPE_CHECKING:
  from ..models.free_busy_response_calendars import FreeBusyResponseCalendars
  from ..models.free_busy_response_groups import FreeBusyResponseGroups





T = TypeVar("T", bound="FreeBusyResponse")



@_attrs_define
class FreeBusyResponse:
    """ 
        Attributes:
            calendars (FreeBusyResponseCalendars | Unset): List of free/busy information for calendars.
            groups (FreeBusyResponseGroups | Unset): Expansion of groups.
            kind (str | Unset): Type of the resource ("calendar#freeBusy"). Default: 'calendar#freeBusy'.
            time_max (datetime.datetime | Unset): The end of the interval.
            time_min (datetime.datetime | Unset): The start of the interval.
     """

    calendars: FreeBusyResponseCalendars | Unset = UNSET
    groups: FreeBusyResponseGroups | Unset = UNSET
    kind: str | Unset = 'calendar#freeBusy'
    time_max: datetime.datetime | Unset = UNSET
    time_min: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.free_busy_response_calendars import FreeBusyResponseCalendars
        from ..models.free_busy_response_groups import FreeBusyResponseGroups
        calendars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calendars, Unset):
            calendars = self.calendars.to_dict()

        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        kind = self.kind

        time_max: str | Unset = UNSET
        if not isinstance(self.time_max, Unset):
            time_max = self.time_max.isoformat()

        time_min: str | Unset = UNSET
        if not isinstance(self.time_min, Unset):
            time_min = self.time_min.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if calendars is not UNSET:
            field_dict["calendars"] = calendars
        if groups is not UNSET:
            field_dict["groups"] = groups
        if kind is not UNSET:
            field_dict["kind"] = kind
        if time_max is not UNSET:
            field_dict["timeMax"] = time_max
        if time_min is not UNSET:
            field_dict["timeMin"] = time_min

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.free_busy_response_calendars import FreeBusyResponseCalendars
        from ..models.free_busy_response_groups import FreeBusyResponseGroups
        d = dict(src_dict)
        _calendars = d.pop("calendars", UNSET)
        calendars: FreeBusyResponseCalendars | Unset
        if isinstance(_calendars,  Unset):
            calendars = UNSET
        else:
            calendars = FreeBusyResponseCalendars.from_dict(_calendars)




        _groups = d.pop("groups", UNSET)
        groups: FreeBusyResponseGroups | Unset
        if isinstance(_groups,  Unset):
            groups = UNSET
        else:
            groups = FreeBusyResponseGroups.from_dict(_groups)




        kind = d.pop("kind", UNSET)

        _time_max = d.pop("timeMax", UNSET)
        time_max: datetime.datetime | Unset
        if isinstance(_time_max,  Unset):
            time_max = UNSET
        else:
            time_max = isoparse(_time_max)




        _time_min = d.pop("timeMin", UNSET)
        time_min: datetime.datetime | Unset
        if isinstance(_time_min,  Unset):
            time_min = UNSET
        else:
            time_min = isoparse(_time_min)




        free_busy_response = cls(
            calendars=calendars,
            groups=groups,
            kind=kind,
            time_max=time_max,
            time_min=time_min,
        )


        free_busy_response.additional_properties = d
        return free_busy_response

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
