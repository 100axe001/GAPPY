from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.interpolation_point import InterpolationPoint





T = TypeVar("T", bound="GradientRule")



@_attrs_define
class GradientRule:
    """ A rule that applies a gradient color scale format, based on the interpolation points listed. The format of a cell
    will vary based on its contents as compared to the values of the interpolation points.

        Attributes:
            maxpoint (InterpolationPoint | Unset): A single interpolation point on a gradient conditional format. These pin
                the gradient color scale according to the color, type and value chosen.
            midpoint (InterpolationPoint | Unset): A single interpolation point on a gradient conditional format. These pin
                the gradient color scale according to the color, type and value chosen.
            minpoint (InterpolationPoint | Unset): A single interpolation point on a gradient conditional format. These pin
                the gradient color scale according to the color, type and value chosen.
     """

    maxpoint: InterpolationPoint | Unset = UNSET
    midpoint: InterpolationPoint | Unset = UNSET
    minpoint: InterpolationPoint | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.interpolation_point import InterpolationPoint
        maxpoint: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maxpoint, Unset):
            maxpoint = self.maxpoint.to_dict()

        midpoint: dict[str, Any] | Unset = UNSET
        if not isinstance(self.midpoint, Unset):
            midpoint = self.midpoint.to_dict()

        minpoint: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minpoint, Unset):
            minpoint = self.minpoint.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if maxpoint is not UNSET:
            field_dict["maxpoint"] = maxpoint
        if midpoint is not UNSET:
            field_dict["midpoint"] = midpoint
        if minpoint is not UNSET:
            field_dict["minpoint"] = minpoint

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interpolation_point import InterpolationPoint
        d = dict(src_dict)
        _maxpoint = d.pop("maxpoint", UNSET)
        maxpoint: InterpolationPoint | Unset
        if isinstance(_maxpoint,  Unset):
            maxpoint = UNSET
        else:
            maxpoint = InterpolationPoint.from_dict(_maxpoint)




        _midpoint = d.pop("midpoint", UNSET)
        midpoint: InterpolationPoint | Unset
        if isinstance(_midpoint,  Unset):
            midpoint = UNSET
        else:
            midpoint = InterpolationPoint.from_dict(_midpoint)




        _minpoint = d.pop("minpoint", UNSET)
        minpoint: InterpolationPoint | Unset
        if isinstance(_minpoint,  Unset):
            minpoint = UNSET
        else:
            minpoint = InterpolationPoint.from_dict(_minpoint)




        gradient_rule = cls(
            maxpoint=maxpoint,
            midpoint=midpoint,
            minpoint=minpoint,
        )


        gradient_rule.additional_properties = d
        return gradient_rule

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
