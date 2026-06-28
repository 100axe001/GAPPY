from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.notification_scheme_event import NotificationSchemeEvent
  from ..models.scope import Scope





T = TypeVar("T", bound="NotificationScheme")



@_attrs_define
class NotificationScheme:
    """ Details about a notification scheme.

        Attributes:
            description (str | Unset): The description of the notification scheme.
            expand (str | Unset): Expand options that include additional notification scheme details in the response.
            id (int | Unset): The ID of the notification scheme.
            name (str | Unset): The name of the notification scheme.
            notification_scheme_events (list[NotificationSchemeEvent] | Unset): The notification events and associated
                recipients.
            projects (list[int] | Unset): The list of project IDs associated with the notification scheme.
            scope (Scope | Unset): The projects the item is associated with. Indicated for items associated with [next-gen
                projects](https://confluence.atlassian.com/x/loMyO).
            self_ (str | Unset):
     """

    description: str | Unset = UNSET
    expand: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    notification_scheme_events: list[NotificationSchemeEvent] | Unset = UNSET
    projects: list[int] | Unset = UNSET
    scope: Scope | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_scheme_event import NotificationSchemeEvent
        from ..models.scope import Scope
        description = self.description

        expand = self.expand

        id = self.id

        name = self.name

        notification_scheme_events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notification_scheme_events, Unset):
            notification_scheme_events = []
            for notification_scheme_events_item_data in self.notification_scheme_events:
                notification_scheme_events_item = notification_scheme_events_item_data.to_dict()
                notification_scheme_events.append(notification_scheme_events_item)



        projects: list[int] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects



        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if expand is not UNSET:
            field_dict["expand"] = expand
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if notification_scheme_events is not UNSET:
            field_dict["notificationSchemeEvents"] = notification_scheme_events
        if projects is not UNSET:
            field_dict["projects"] = projects
        if scope is not UNSET:
            field_dict["scope"] = scope
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_scheme_event import NotificationSchemeEvent
        from ..models.scope import Scope
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        expand = d.pop("expand", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _notification_scheme_events = d.pop("notificationSchemeEvents", UNSET)
        notification_scheme_events: list[NotificationSchemeEvent] | Unset = UNSET
        if _notification_scheme_events is not UNSET:
            notification_scheme_events = []
            for notification_scheme_events_item_data in _notification_scheme_events:
                notification_scheme_events_item = NotificationSchemeEvent.from_dict(notification_scheme_events_item_data)



                notification_scheme_events.append(notification_scheme_events_item)


        projects = cast(list[int], d.pop("projects", UNSET))


        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = Scope.from_dict(_scope)




        self_ = d.pop("self", UNSET)

        notification_scheme = cls(
            description=description,
            expand=expand,
            id=id,
            name=name,
            notification_scheme_events=notification_scheme_events,
            projects=projects,
            scope=scope,
            self_=self_,
        )

        return notification_scheme

