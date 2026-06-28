from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.embedded_object_border import EmbeddedObjectBorder





T = TypeVar("T", bound="UpdateEmbeddedObjectBorderRequest")



@_attrs_define
class UpdateEmbeddedObjectBorderRequest:
    """ Updates an embedded object's border property.

        Attributes:
            border (EmbeddedObjectBorder | Unset): A border along an embedded object.
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root `border`
                is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.
            object_id (int | Unset): The ID of the embedded object to update.
     """

    border: EmbeddedObjectBorder | Unset = UNSET
    fields: str | Unset = UNSET
    object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_object_border import EmbeddedObjectBorder
        border: dict[str, Any] | Unset = UNSET
        if not isinstance(self.border, Unset):
            border = self.border.to_dict()

        fields = self.fields

        object_id = self.object_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if border is not UNSET:
            field_dict["border"] = border
        if fields is not UNSET:
            field_dict["fields"] = fields
        if object_id is not UNSET:
            field_dict["objectId"] = object_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_object_border import EmbeddedObjectBorder
        d = dict(src_dict)
        _border = d.pop("border", UNSET)
        border: EmbeddedObjectBorder | Unset
        if isinstance(_border,  Unset):
            border = UNSET
        else:
            border = EmbeddedObjectBorder.from_dict(_border)




        fields = d.pop("fields", UNSET)

        object_id = d.pop("objectId", UNSET)

        update_embedded_object_border_request = cls(
            border=border,
            fields=fields,
            object_id=object_id,
        )


        update_embedded_object_border_request.additional_properties = d
        return update_embedded_object_border_request

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
