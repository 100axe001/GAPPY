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





T = TypeVar("T", bound="UpdateEmbeddedObjectPositionResponse")



@_attrs_define
class UpdateEmbeddedObjectPositionResponse:
    """ The result of updating an embedded object's position.

        Attributes:
            position (EmbeddedObjectPosition | Unset): The position of an embedded object such as a chart.
     """

    position: EmbeddedObjectPosition | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_object_position import EmbeddedObjectPosition
        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_object_position import EmbeddedObjectPosition
        d = dict(src_dict)
        _position = d.pop("position", UNSET)
        position: EmbeddedObjectPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = EmbeddedObjectPosition.from_dict(_position)




        update_embedded_object_position_response = cls(
            position=position,
        )


        update_embedded_object_position_response.additional_properties = d
        return update_embedded_object_position_response

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
