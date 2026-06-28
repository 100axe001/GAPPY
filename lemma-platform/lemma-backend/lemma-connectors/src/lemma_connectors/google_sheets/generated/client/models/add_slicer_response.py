from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.slicer import Slicer





T = TypeVar("T", bound="AddSlicerResponse")



@_attrs_define
class AddSlicerResponse:
    """ The result of adding a slicer to a spreadsheet.

        Attributes:
            slicer (Slicer | Unset): A slicer in a sheet.
     """

    slicer: Slicer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.slicer import Slicer
        slicer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slicer, Unset):
            slicer = self.slicer.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if slicer is not UNSET:
            field_dict["slicer"] = slicer

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slicer import Slicer
        d = dict(src_dict)
        _slicer = d.pop("slicer", UNSET)
        slicer: Slicer | Unset
        if isinstance(_slicer,  Unset):
            slicer = UNSET
        else:
            slicer = Slicer.from_dict(_slicer)




        add_slicer_response = cls(
            slicer=slicer,
        )


        add_slicer_response.additional_properties = d
        return add_slicer_response

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
