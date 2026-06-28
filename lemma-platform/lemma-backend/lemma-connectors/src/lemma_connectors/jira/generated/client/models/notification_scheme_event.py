from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.event_notification import EventNotification
  from ..models.notification_event import NotificationEvent





T = TypeVar("T", bound="NotificationSchemeEvent")



@_attrs_define
class NotificationSchemeEvent:
    """ Details about a notification scheme event.

        Attributes:
            event (NotificationEvent | Unset): Details about a notification event.
            notifications (list[EventNotification] | Unset):
     """

    event: NotificationEvent | Unset = UNSET
    notifications: list[EventNotification] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.event_notification import EventNotification
        from ..models.notification_event import NotificationEvent
        event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        notifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for notifications_item_data in self.notifications:
                notifications_item = notifications_item_data.to_dict()
                notifications.append(notifications_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if event is not UNSET:
            field_dict["event"] = event
        if notifications is not UNSET:
            field_dict["notifications"] = notifications

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_notification import EventNotification
        from ..models.notification_event import NotificationEvent
        d = dict(src_dict)
        _event = d.pop("event", UNSET)
        event: NotificationEvent | Unset
        if isinstance(_event,  Unset):
            event = UNSET
        else:
            event = NotificationEvent.from_dict(_event)




        _notifications = d.pop("notifications", UNSET)
        notifications: list[EventNotification] | Unset = UNSET
        if _notifications is not UNSET:
            notifications = []
            for notifications_item_data in _notifications:
                notifications_item = EventNotification.from_dict(notifications_item_data)



                notifications.append(notifications_item)


        notification_scheme_event = cls(
            event=event,
            notifications=notifications,
        )

        return notification_scheme_event

