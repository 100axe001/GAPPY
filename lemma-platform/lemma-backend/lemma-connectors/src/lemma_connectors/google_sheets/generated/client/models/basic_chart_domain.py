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





T = TypeVar("T", bound="BasicChartDomain")



@_attrs_define
class BasicChartDomain:
    """ The domain of a chart. For example, if charting stock prices over time, this would be the date.

        Attributes:
            domain (ChartData | Unset): The data included in a domain or series.
            reversed_ (bool | Unset): True to reverse the order of the domain values (horizontal axis).
     """

    domain: ChartData | Unset = UNSET
    reversed_: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_data import ChartData
        domain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain, Unset):
            domain = self.domain.to_dict()

        reversed_ = self.reversed_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if domain is not UNSET:
            field_dict["domain"] = domain
        if reversed_ is not UNSET:
            field_dict["reversed"] = reversed_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_data import ChartData
        d = dict(src_dict)
        _domain = d.pop("domain", UNSET)
        domain: ChartData | Unset
        if isinstance(_domain,  Unset):
            domain = UNSET
        else:
            domain = ChartData.from_dict(_domain)




        reversed_ = d.pop("reversed", UNSET)

        basic_chart_domain = cls(
            domain=domain,
            reversed_=reversed_,
        )


        basic_chart_domain.additional_properties = d
        return basic_chart_domain

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
