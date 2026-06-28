from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.event_reminder import EventReminder





T = TypeVar("T", bound="EventReminders")



@_attrs_define
class EventReminders:
    """ Information about the event's reminders for the authenticated user.

        Attributes:
            overrides (list[EventReminder] | Unset): If the event doesn't use the default reminders, this lists the
                reminders specific to the event, or, if not set, indicates that no reminders are set for this event. The maximum
                number of override reminders is 5.
            use_default (bool | Unset): Whether the default reminders of the calendar apply to the event.
     """

    overrides: list[EventReminder] | Unset = UNSET
    use_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.event_reminder import EventReminder
        overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = []
            for overrides_item_data in self.overrides:
                overrides_item = overrides_item_data.to_dict()
                overrides.append(overrides_item)



        use_default = self.use_default


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if use_default is not UNSET:
            field_dict["useDefault"] = use_default

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_reminder import EventReminder
        d = dict(src_dict)
        _overrides = d.pop("overrides", UNSET)
        overrides: list[EventReminder] | Unset = UNSET
        if _overrides is not UNSET:
            overrides = []
            for overrides_item_data in _overrides:
                overrides_item = EventReminder.from_dict(overrides_item_data)



                overrides.append(overrides_item)


        use_default = d.pop("useDefault", UNSET)

        event_reminders = cls(
            overrides=overrides,
            use_default=use_default,
        )


        event_reminders.additional_properties = d
        return event_reminders

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
