from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.event_gadget_preferences import EventGadgetPreferences





T = TypeVar("T", bound="EventGadget")



@_attrs_define
class EventGadget:
    """ A gadget that extends this event. Gadgets are deprecated; this structure is instead only used for returning birthday
    calendar metadata.

        Attributes:
            display (str | Unset): The gadget's display mode. Deprecated. Possible values are:
                - "icon" - The gadget displays next to the event's title in the calendar view.
                - "chip" - The gadget displays when the event is clicked.
            height (int | Unset): The gadget's height in pixels. The height must be an integer greater than 0. Optional.
                Deprecated.
            icon_link (str | Unset): The gadget's icon URL. The URL scheme must be HTTPS. Deprecated.
            link (str | Unset): The gadget's URL. The URL scheme must be HTTPS. Deprecated.
            preferences (EventGadgetPreferences | Unset): Preferences.
            title (str | Unset): The gadget's title. Deprecated.
            type_ (str | Unset): The gadget's type. Deprecated.
            width (int | Unset): The gadget's width in pixels. The width must be an integer greater than 0. Optional.
                Deprecated.
     """

    display: str | Unset = UNSET
    height: int | Unset = UNSET
    icon_link: str | Unset = UNSET
    link: str | Unset = UNSET
    preferences: EventGadgetPreferences | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.event_gadget_preferences import EventGadgetPreferences
        display = self.display

        height = self.height

        icon_link = self.icon_link

        link = self.link

        preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = self.preferences.to_dict()

        title = self.title

        type_ = self.type_

        width = self.width


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display is not UNSET:
            field_dict["display"] = display
        if height is not UNSET:
            field_dict["height"] = height
        if icon_link is not UNSET:
            field_dict["iconLink"] = icon_link
        if link is not UNSET:
            field_dict["link"] = link
        if preferences is not UNSET:
            field_dict["preferences"] = preferences
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_gadget_preferences import EventGadgetPreferences
        d = dict(src_dict)
        display = d.pop("display", UNSET)

        height = d.pop("height", UNSET)

        icon_link = d.pop("iconLink", UNSET)

        link = d.pop("link", UNSET)

        _preferences = d.pop("preferences", UNSET)
        preferences: EventGadgetPreferences | Unset
        if isinstance(_preferences,  Unset):
            preferences = UNSET
        else:
            preferences = EventGadgetPreferences.from_dict(_preferences)




        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        width = d.pop("width", UNSET)

        event_gadget = cls(
            display=display,
            height=height,
            icon_link=icon_link,
            link=link,
            preferences=preferences,
            title=title,
            type_=type_,
            width=width,
        )


        event_gadget.additional_properties = d
        return event_gadget

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
