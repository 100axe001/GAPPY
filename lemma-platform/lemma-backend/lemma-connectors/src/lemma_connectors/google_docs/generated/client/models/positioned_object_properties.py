from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.embedded_object import EmbeddedObject
  from ..models.positioned_object_positioning import PositionedObjectPositioning





T = TypeVar("T", bound="PositionedObjectProperties")



@_attrs_define
class PositionedObjectProperties:
    """ Properties of a PositionedObject.

        Attributes:
            embedded_object (EmbeddedObject | Unset): An embedded object in the document.
            positioning (PositionedObjectPositioning | Unset): The positioning of a PositionedObject. The positioned object
                is positioned relative to the beginning of the Paragraph it's tethered to.
     """

    embedded_object: EmbeddedObject | Unset = UNSET
    positioning: PositionedObjectPositioning | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_object import EmbeddedObject
        from ..models.positioned_object_positioning import PositionedObjectPositioning
        embedded_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embedded_object, Unset):
            embedded_object = self.embedded_object.to_dict()

        positioning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positioning, Unset):
            positioning = self.positioning.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if embedded_object is not UNSET:
            field_dict["embeddedObject"] = embedded_object
        if positioning is not UNSET:
            field_dict["positioning"] = positioning

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_object import EmbeddedObject
        from ..models.positioned_object_positioning import PositionedObjectPositioning
        d = dict(src_dict)
        _embedded_object = d.pop("embeddedObject", UNSET)
        embedded_object: EmbeddedObject | Unset
        if isinstance(_embedded_object,  Unset):
            embedded_object = UNSET
        else:
            embedded_object = EmbeddedObject.from_dict(_embedded_object)




        _positioning = d.pop("positioning", UNSET)
        positioning: PositionedObjectPositioning | Unset
        if isinstance(_positioning,  Unset):
            positioning = UNSET
        else:
            positioning = PositionedObjectPositioning.from_dict(_positioning)




        positioned_object_properties = cls(
            embedded_object=embedded_object,
            positioning=positioning,
        )


        positioned_object_properties.additional_properties = d
        return positioned_object_properties

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
