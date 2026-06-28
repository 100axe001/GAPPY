from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.notification_scheme_event_details import NotificationSchemeEventDetails





T = TypeVar("T", bound="CreateNotificationSchemeDetails")



@_attrs_define
class CreateNotificationSchemeDetails:
    """ Details of an notification scheme.

        Attributes:
            name (str): The name of the notification scheme. Must be unique (case-insensitive).
            description (str | Unset): The description of the notification scheme.
            notification_scheme_events (list[NotificationSchemeEventDetails] | Unset): The list of notifications which
                should be added to the notification scheme.
     """

    name: str
    description: str | Unset = UNSET
    notification_scheme_events: list[NotificationSchemeEventDetails] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_scheme_event_details import NotificationSchemeEventDetails
        name = self.name

        description = self.description

        notification_scheme_events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notification_scheme_events, Unset):
            notification_scheme_events = []
            for notification_scheme_events_item_data in self.notification_scheme_events:
                notification_scheme_events_item = notification_scheme_events_item_data.to_dict()
                notification_scheme_events.append(notification_scheme_events_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if notification_scheme_events is not UNSET:
            field_dict["notificationSchemeEvents"] = notification_scheme_events

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_scheme_event_details import NotificationSchemeEventDetails
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _notification_scheme_events = d.pop("notificationSchemeEvents", UNSET)
        notification_scheme_events: list[NotificationSchemeEventDetails] | Unset = UNSET
        if _notification_scheme_events is not UNSET:
            notification_scheme_events = []
            for notification_scheme_events_item_data in _notification_scheme_events:
                notification_scheme_events_item = NotificationSchemeEventDetails.from_dict(notification_scheme_events_item_data)



                notification_scheme_events.append(notification_scheme_events_item)


        create_notification_scheme_details = cls(
            name=name,
            description=description,
            notification_scheme_events=notification_scheme_events,
        )


        create_notification_scheme_details.additional_properties = d
        return create_notification_scheme_details

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
