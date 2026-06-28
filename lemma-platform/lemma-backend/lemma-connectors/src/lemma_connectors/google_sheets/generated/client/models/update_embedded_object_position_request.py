from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.embedded_object_position import EmbeddedObjectPosition





T = TypeVar("T", bound="UpdateEmbeddedObjectPositionRequest")



@_attrs_define
class UpdateEmbeddedObjectPositionRequest:
    """ Update an embedded object's position (such as a moving or resizing a chart or image).

        Attributes:
            fields (str | Unset): The fields of OverlayPosition that should be updated when setting a new position. Used
                only if newPosition.overlayPosition is set, in which case at least one field must be specified. The root
                `newPosition.overlayPosition` is implied and should not be specified. A single `"*"` can be used as short-hand
                for listing every field.
            new_position (EmbeddedObjectPosition | Unset): The position of an embedded object such as a chart.
            object_id (int | Unset): The ID of the object to moved.
     """

    fields: str | Unset = UNSET
    new_position: EmbeddedObjectPosition | Unset = UNSET
    object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_object_position import EmbeddedObjectPosition
        fields = self.fields

        new_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_position, Unset):
            new_position = self.new_position.to_dict()

        object_id = self.object_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if new_position is not UNSET:
            field_dict["newPosition"] = new_position
        if object_id is not UNSET:
            field_dict["objectId"] = object_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_object_position import EmbeddedObjectPosition
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _new_position = d.pop("newPosition", UNSET)
        new_position: EmbeddedObjectPosition | Unset
        if isinstance(_new_position,  Unset):
            new_position = UNSET
        else:
            new_position = EmbeddedObjectPosition.from_dict(_new_position)




        object_id = d.pop("objectId", UNSET)

        update_embedded_object_position_request = cls(
            fields=fields,
            new_position=new_position,
            object_id=object_id,
        )


        update_embedded_object_position_request.additional_properties = d
        return update_embedded_object_position_request

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
