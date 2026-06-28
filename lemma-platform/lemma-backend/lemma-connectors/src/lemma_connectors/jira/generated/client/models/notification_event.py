from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="NotificationEvent")



@_attrs_define
class NotificationEvent:
    """ Details about a notification event.

        Attributes:
            description (str | Unset): The description of the event.
            id (int | Unset): The ID of the event. The event can be a [Jira system
                event](https://confluence.atlassian.com/x/8YdKLg#Creatinganotificationscheme-eventsEvents) or a [custom
                event](https://confluence.atlassian.com/x/AIlKLg).
            name (str | Unset): The name of the event.
            template_event (NotificationEvent | Unset): Details about a notification event.
     """

    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    template_event: NotificationEvent | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        name = self.name

        template_event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_event, Unset):
            template_event = self.template_event.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if template_event is not UNSET:
            field_dict["templateEvent"] = template_event

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _template_event = d.pop("templateEvent", UNSET)
        template_event: NotificationEvent | Unset
        if isinstance(_template_event,  Unset):
            template_event = UNSET
        else:
            template_event = NotificationEvent.from_dict(_template_event)




        notification_event = cls(
            description=description,
            id=id,
            name=name,
            template_event=template_event,
        )

        return notification_event

