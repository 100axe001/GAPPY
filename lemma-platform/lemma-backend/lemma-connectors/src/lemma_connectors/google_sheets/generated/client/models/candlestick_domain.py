from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_data import ChartData





T = TypeVar("T", bound="CandlestickDomain")



@_attrs_define
class CandlestickDomain:
    """ The domain of a CandlestickChart.

        Attributes:
            data (ChartData | Unset): The data included in a domain or series.
            reversed_ (bool | Unset): True to reverse the order of the domain values (horizontal axis).
     """

    data: ChartData | Unset = UNSET
    reversed_: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_data import ChartData
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        reversed_ = self.reversed_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if reversed_ is not UNSET:
            field_dict["reversed"] = reversed_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_data import ChartData
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ChartData | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = ChartData.from_dict(_data)




        reversed_ = d.pop("reversed", UNSET)

        candlestick_domain = cls(
            data=data,
            reversed_=reversed_,
        )


        candlestick_domain.additional_properties = d
        return candlestick_domain

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
