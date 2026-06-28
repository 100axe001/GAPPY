from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.protected_range import ProtectedRange





T = TypeVar("T", bound="AddProtectedRangeRequest")



@_attrs_define
class AddProtectedRangeRequest:
    """ Adds a new protected range.

        Attributes:
            protected_range (ProtectedRange | Unset): A protected range.
     """

    protected_range: ProtectedRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.protected_range import ProtectedRange
        protected_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protected_range, Unset):
            protected_range = self.protected_range.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if protected_range is not UNSET:
            field_dict["protectedRange"] = protected_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protected_range import ProtectedRange
        d = dict(src_dict)
        _protected_range = d.pop("protectedRange", UNSET)
        protected_range: ProtectedRange | Unset
        if isinstance(_protected_range,  Unset):
            protected_range = UNSET
        else:
            protected_range = ProtectedRange.from_dict(_protected_range)




        add_protected_range_request = cls(
            protected_range=protected_range,
        )


        add_protected_range_request.additional_properties = d
        return add_protected_range_request

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
