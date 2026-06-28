from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.notification_scheme_event_details import NotificationSchemeEventDetails





T = TypeVar("T", bound="AddNotificationsDetails")



@_attrs_define
class AddNotificationsDetails:
    """ Details of notifications which should be added to the notification scheme.

        Attributes:
            notification_scheme_events (list[NotificationSchemeEventDetails]): The list of notifications which should be
                added to the notification scheme.
     """

    notification_scheme_events: list[NotificationSchemeEventDetails]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_scheme_event_details import NotificationSchemeEventDetails
        notification_scheme_events = []
        for notification_scheme_events_item_data in self.notification_scheme_events:
            notification_scheme_events_item = notification_scheme_events_item_data.to_dict()
            notification_scheme_events.append(notification_scheme_events_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "notificationSchemeEvents": notification_scheme_events,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_scheme_event_details import NotificationSchemeEventDetails
        d = dict(src_dict)
        notification_scheme_events = []
        _notification_scheme_events = d.pop("notificationSchemeEvents")
        for notification_scheme_events_item_data in (_notification_scheme_events):
            notification_scheme_events_item = NotificationSchemeEventDetails.from_dict(notification_scheme_events_item_data)



            notification_scheme_events.append(notification_scheme_events_item)


        add_notifications_details = cls(
            notification_scheme_events=notification_scheme_events,
        )


        add_notifications_details.additional_properties = d
        return add_notifications_details

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
