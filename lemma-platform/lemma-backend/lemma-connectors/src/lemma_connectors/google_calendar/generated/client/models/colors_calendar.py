from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.color_definition import ColorDefinition





T = TypeVar("T", bound="ColorsCalendar")



@_attrs_define
class ColorsCalendar:
    """ A global palette of calendar colors, mapping from the color ID to its definition. A calendarListEntry resource
    refers to one of these color IDs in its colorId field. Read-only.

     """

    additional_properties: dict[str, ColorDefinition] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.color_definition import ColorDefinition
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color_definition import ColorDefinition
        d = dict(src_dict)
        colors_calendar = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ColorDefinition.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        colors_calendar.additional_properties = additional_properties
        return colors_calendar

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ColorDefinition:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ColorDefinition) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
