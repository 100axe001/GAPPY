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
  from ..models.free_busy_request_item import FreeBusyRequestItem





T = TypeVar("T", bound="FreeBusyRequest")



@_attrs_define
class FreeBusyRequest:
    """ 
        Attributes:
            calendar_expansion_max (int | Unset): Maximal number of calendars for which FreeBusy information is to be
                provided. Optional. Maximum value is 50.
            group_expansion_max (int | Unset): Maximal number of calendar identifiers to be provided for a single group.
                Optional. An error is returned for a group with more members than this value. Maximum value is 100.
            items (list[FreeBusyRequestItem] | Unset): List of calendars and/or groups to query.
            time_max (datetime.datetime | Unset): The end of the interval for the query formatted as per RFC3339.
            time_min (datetime.datetime | Unset): The start of the interval for the query formatted as per RFC3339.
            time_zone (str | Unset): Time zone used in the response. Optional. The default is UTC. Default: 'UTC'.
     """

    calendar_expansion_max: int | Unset = UNSET
    group_expansion_max: int | Unset = UNSET
    items: list[FreeBusyRequestItem] | Unset = UNSET
    time_max: datetime.datetime | Unset = UNSET
    time_min: datetime.datetime | Unset = UNSET
    time_zone: str | Unset = 'UTC'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.free_busy_request_item import FreeBusyRequestItem
        calendar_expansion_max = self.calendar_expansion_max

        group_expansion_max = self.group_expansion_max

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        time_max: str | Unset = UNSET
        if not isinstance(self.time_max, Unset):
            time_max = self.time_max.isoformat()

        time_min: str | Unset = UNSET
        if not isinstance(self.time_min, Unset):
            time_min = self.time_min.isoformat()

        time_zone = self.time_zone


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if calendar_expansion_max is not UNSET:
            field_dict["calendarExpansionMax"] = calendar_expansion_max
        if group_expansion_max is not UNSET:
            field_dict["groupExpansionMax"] = group_expansion_max
        if items is not UNSET:
            field_dict["items"] = items
        if time_max is not UNSET:
            field_dict["timeMax"] = time_max
        if time_min is not UNSET:
            field_dict["timeMin"] = time_min
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.free_busy_request_item import FreeBusyRequestItem
        d = dict(src_dict)
        calendar_expansion_max = d.pop("calendarExpansionMax", UNSET)

        group_expansion_max = d.pop("groupExpansionMax", UNSET)

        _items = d.pop("items", UNSET)
        items: list[FreeBusyRequestItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = FreeBusyRequestItem.from_dict(items_item_data)



                items.append(items_item)


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




        time_zone = d.pop("timeZone", UNSET)

        free_busy_request = cls(
            calendar_expansion_max=calendar_expansion_max,
            group_expansion_max=group_expansion_max,
            items=items,
            time_max=time_max,
            time_min=time_min,
            time_zone=time_zone,
        )


        free_busy_request.additional_properties = d
        return free_busy_request

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
