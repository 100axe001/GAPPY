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
  from ..models.colors_calendar import ColorsCalendar
  from ..models.colors_event import ColorsEvent





T = TypeVar("T", bound="Colors")



@_attrs_define
class Colors:
    """ 
        Attributes:
            calendar (ColorsCalendar | Unset): A global palette of calendar colors, mapping from the color ID to its
                definition. A calendarListEntry resource refers to one of these color IDs in its colorId field. Read-only.
            event (ColorsEvent | Unset): A global palette of event colors, mapping from the color ID to its definition. An
                event resource may refer to one of these color IDs in its colorId field. Read-only.
            kind (str | Unset): Type of the resource ("calendar#colors"). Default: 'calendar#colors'.
            updated (datetime.datetime | Unset): Last modification time of the color palette (as a RFC3339 timestamp). Read-
                only.
     """

    calendar: ColorsCalendar | Unset = UNSET
    event: ColorsEvent | Unset = UNSET
    kind: str | Unset = 'calendar#colors'
    updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.colors_calendar import ColorsCalendar
        from ..models.colors_event import ColorsEvent
        calendar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = self.calendar.to_dict()

        event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        kind = self.kind

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if calendar is not UNSET:
            field_dict["calendar"] = calendar
        if event is not UNSET:
            field_dict["event"] = event
        if kind is not UNSET:
            field_dict["kind"] = kind
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.colors_calendar import ColorsCalendar
        from ..models.colors_event import ColorsEvent
        d = dict(src_dict)
        _calendar = d.pop("calendar", UNSET)
        calendar: ColorsCalendar | Unset
        if isinstance(_calendar,  Unset):
            calendar = UNSET
        else:
            calendar = ColorsCalendar.from_dict(_calendar)




        _event = d.pop("event", UNSET)
        event: ColorsEvent | Unset
        if isinstance(_event,  Unset):
            event = UNSET
        else:
            event = ColorsEvent.from_dict(_event)




        kind = d.pop("kind", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated,  Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)




        colors = cls(
            calendar=calendar,
            event=event,
            kind=kind,
            updated=updated,
        )


        colors.additional_properties = d
        return colors

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
