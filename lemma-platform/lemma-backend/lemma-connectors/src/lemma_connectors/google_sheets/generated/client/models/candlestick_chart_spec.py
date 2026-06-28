from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.candlestick_data import CandlestickData
  from ..models.candlestick_domain import CandlestickDomain





T = TypeVar("T", bound="CandlestickChartSpec")



@_attrs_define
class CandlestickChartSpec:
    """ A candlestick chart.

        Attributes:
            data (list[CandlestickData] | Unset): The Candlestick chart data. Only one CandlestickData is supported.
            domain (CandlestickDomain | Unset): The domain of a CandlestickChart.
     """

    data: list[CandlestickData] | Unset = UNSET
    domain: CandlestickDomain | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.candlestick_data import CandlestickData
        from ..models.candlestick_domain import CandlestickDomain
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        domain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain, Unset):
            domain = self.domain.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candlestick_data import CandlestickData
        from ..models.candlestick_domain import CandlestickDomain
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[CandlestickData] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = CandlestickData.from_dict(data_item_data)



                data.append(data_item)


        _domain = d.pop("domain", UNSET)
        domain: CandlestickDomain | Unset
        if isinstance(_domain,  Unset):
            domain = UNSET
        else:
            domain = CandlestickDomain.from_dict(_domain)




        candlestick_chart_spec = cls(
            data=data,
            domain=domain,
        )


        candlestick_chart_spec.additional_properties = d
        return candlestick_chart_spec

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
