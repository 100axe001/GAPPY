from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.point_style_shape import PointStyleShape
from ..types import UNSET, Unset






T = TypeVar("T", bound="PointStyle")



@_attrs_define
class PointStyle:
    """ The style of a point on the chart.

        Attributes:
            shape (PointStyleShape | Unset): The point shape. If empty or unspecified, a default shape is used.
            size (float | Unset): The point size. If empty, a default size is used.
     """

    shape: PointStyleShape | Unset = UNSET
    size: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        shape: str | Unset = UNSET
        if not isinstance(self.shape, Unset):
            shape = self.shape.value


        size = self.size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if shape is not UNSET:
            field_dict["shape"] = shape
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _shape = d.pop("shape", UNSET)
        shape: PointStyleShape | Unset
        if isinstance(_shape,  Unset):
            shape = UNSET
        else:
            shape = PointStyleShape(_shape)




        size = d.pop("size", UNSET)

        point_style = cls(
            shape=shape,
            size=size,
        )


        point_style.additional_properties = d
        return point_style

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
