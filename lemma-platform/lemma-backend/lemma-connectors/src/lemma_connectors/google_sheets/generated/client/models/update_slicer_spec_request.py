from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.slicer_spec import SlicerSpec





T = TypeVar("T", bound="UpdateSlicerSpecRequest")



@_attrs_define
class UpdateSlicerSpecRequest:
    """ Updates a slicer's specifications. (This does not move or resize a slicer. To move or resize a slicer use
    UpdateEmbeddedObjectPositionRequest.

        Attributes:
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `SlicerSpec` is implied and should not be specified. A single "*"` can be used as short-hand for listing every
                field.
            slicer_id (int | Unset): The id of the slicer to update.
            spec (SlicerSpec | Unset): The specifications of a slicer.
     """

    fields: str | Unset = UNSET
    slicer_id: int | Unset = UNSET
    spec: SlicerSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.slicer_spec import SlicerSpec
        fields = self.fields

        slicer_id = self.slicer_id

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if slicer_id is not UNSET:
            field_dict["slicerId"] = slicer_id
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slicer_spec import SlicerSpec
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        slicer_id = d.pop("slicerId", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: SlicerSpec | Unset
        if isinstance(_spec,  Unset):
            spec = UNSET
        else:
            spec = SlicerSpec.from_dict(_spec)




        update_slicer_spec_request = cls(
            fields=fields,
            slicer_id=slicer_id,
            spec=spec,
        )


        update_slicer_spec_request.additional_properties = d
        return update_slicer_spec_request

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
