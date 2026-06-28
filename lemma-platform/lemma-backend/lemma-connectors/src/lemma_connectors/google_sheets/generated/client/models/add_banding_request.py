from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.banded_range import BandedRange





T = TypeVar("T", bound="AddBandingRequest")



@_attrs_define
class AddBandingRequest:
    """ Adds a new banded range to the spreadsheet.

        Attributes:
            banded_range (BandedRange | Unset): A banded (alternating colors) range in a sheet.
     """

    banded_range: BandedRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.banded_range import BandedRange
        banded_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.banded_range, Unset):
            banded_range = self.banded_range.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if banded_range is not UNSET:
            field_dict["bandedRange"] = banded_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.banded_range import BandedRange
        d = dict(src_dict)
        _banded_range = d.pop("bandedRange", UNSET)
        banded_range: BandedRange | Unset
        if isinstance(_banded_range,  Unset):
            banded_range = UNSET
        else:
            banded_range = BandedRange.from_dict(_banded_range)




        add_banding_request = cls(
            banded_range=banded_range,
        )


        add_banding_request.additional_properties = d
        return add_banding_request

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
