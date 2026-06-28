from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.notification_scheme_event_type_id import NotificationSchemeEventTypeId
  from ..models.notification_scheme_notification_details import NotificationSchemeNotificationDetails





T = TypeVar("T", bound="NotificationSchemeEventDetails")



@_attrs_define
class NotificationSchemeEventDetails:
    """ Details of a notification scheme event.

        Attributes:
            event (NotificationSchemeEventTypeId): The ID of an event that is being mapped to notifications.
            notifications (list[NotificationSchemeNotificationDetails]): The list of notifications mapped to a specified
                event.
     """

    event: NotificationSchemeEventTypeId
    notifications: list[NotificationSchemeNotificationDetails]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_scheme_event_type_id import NotificationSchemeEventTypeId
        from ..models.notification_scheme_notification_details import NotificationSchemeNotificationDetails
        event = self.event.to_dict()

        notifications = []
        for notifications_item_data in self.notifications:
            notifications_item = notifications_item_data.to_dict()
            notifications.append(notifications_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "event": event,
            "notifications": notifications,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_scheme_event_type_id import NotificationSchemeEventTypeId
        from ..models.notification_scheme_notification_details import NotificationSchemeNotificationDetails
        d = dict(src_dict)
        event = NotificationSchemeEventTypeId.from_dict(d.pop("event"))




        notifications = []
        _notifications = d.pop("notifications")
        for notifications_item_data in (_notifications):
            notifications_item = NotificationSchemeNotificationDetails.from_dict(notifications_item_data)



            notifications.append(notifications_item)


        notification_scheme_event_details = cls(
            event=event,
            notifications=notifications,
        )


        notification_scheme_event_details.additional_properties = d
        return notification_scheme_event_details

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
