from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.candlestick_series import CandlestickSeries





T = TypeVar("T", bound="CandlestickData")



@_attrs_define
class CandlestickData:
    """ The Candlestick chart data, each containing the low, open, close, and high values for a series.

        Attributes:
            close_series (CandlestickSeries | Unset): The series of a CandlestickData.
            high_series (CandlestickSeries | Unset): The series of a CandlestickData.
            low_series (CandlestickSeries | Unset): The series of a CandlestickData.
            open_series (CandlestickSeries | Unset): The series of a CandlestickData.
     """

    close_series: CandlestickSeries | Unset = UNSET
    high_series: CandlestickSeries | Unset = UNSET
    low_series: CandlestickSeries | Unset = UNSET
    open_series: CandlestickSeries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.candlestick_series import CandlestickSeries
        close_series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.close_series, Unset):
            close_series = self.close_series.to_dict()

        high_series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.high_series, Unset):
            high_series = self.high_series.to_dict()

        low_series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.low_series, Unset):
            low_series = self.low_series.to_dict()

        open_series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.open_series, Unset):
            open_series = self.open_series.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if close_series is not UNSET:
            field_dict["closeSeries"] = close_series
        if high_series is not UNSET:
            field_dict["highSeries"] = high_series
        if low_series is not UNSET:
            field_dict["lowSeries"] = low_series
        if open_series is not UNSET:
            field_dict["openSeries"] = open_series

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candlestick_series import CandlestickSeries
        d = dict(src_dict)
        _close_series = d.pop("closeSeries", UNSET)
        close_series: CandlestickSeries | Unset
        if isinstance(_close_series,  Unset):
            close_series = UNSET
        else:
            close_series = CandlestickSeries.from_dict(_close_series)




        _high_series = d.pop("highSeries", UNSET)
        high_series: CandlestickSeries | Unset
        if isinstance(_high_series,  Unset):
            high_series = UNSET
        else:
            high_series = CandlestickSeries.from_dict(_high_series)




        _low_series = d.pop("lowSeries", UNSET)
        low_series: CandlestickSeries | Unset
        if isinstance(_low_series,  Unset):
            low_series = UNSET
        else:
            low_series = CandlestickSeries.from_dict(_low_series)




        _open_series = d.pop("openSeries", UNSET)
        open_series: CandlestickSeries | Unset
        if isinstance(_open_series,  Unset):
            open_series = UNSET
        else:
            open_series = CandlestickSeries.from_dict(_open_series)




        candlestick_data = cls(
            close_series=close_series,
            high_series=high_series,
            low_series=low_series,
            open_series=open_series,
        )


        candlestick_data.additional_properties = d
        return candlestick_data

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
