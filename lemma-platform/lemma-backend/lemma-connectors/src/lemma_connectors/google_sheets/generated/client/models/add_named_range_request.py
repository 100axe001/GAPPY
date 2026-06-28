from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.named_range import NamedRange





T = TypeVar("T", bound="AddNamedRangeRequest")



@_attrs_define
class AddNamedRangeRequest:
    """ Adds a named range to the spreadsheet.

        Attributes:
            named_range (NamedRange | Unset): A named range.
     """

    named_range: NamedRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.named_range import NamedRange
        named_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.named_range, Unset):
            named_range = self.named_range.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if named_range is not UNSET:
            field_dict["namedRange"] = named_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.named_range import NamedRange
        d = dict(src_dict)
        _named_range = d.pop("namedRange", UNSET)
        named_range: NamedRange | Unset
        if isinstance(_named_range,  Unset):
            named_range = UNSET
        else:
            named_range = NamedRange.from_dict(_named_range)




        add_named_range_request = cls(
            named_range=named_range,
        )


        add_named_range_request.additional_properties = d
        return add_named_range_request

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
