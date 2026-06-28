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





T = TypeVar("T", bound="UpdateProtectedRangeRequest")



@_attrs_define
class UpdateProtectedRangeRequest:
    """ Updates an existing protected range with the specified protectedRangeId.

        Attributes:
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `protectedRange` is implied and should not be specified. A single `"*"` can be used as short-hand for listing
                every field.
            protected_range (ProtectedRange | Unset): A protected range.
     """

    fields: str | Unset = UNSET
    protected_range: ProtectedRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.protected_range import ProtectedRange
        fields = self.fields

        protected_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protected_range, Unset):
            protected_range = self.protected_range.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if protected_range is not UNSET:
            field_dict["protectedRange"] = protected_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protected_range import ProtectedRange
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _protected_range = d.pop("protectedRange", UNSET)
        protected_range: ProtectedRange | Unset
        if isinstance(_protected_range,  Unset):
            protected_range = UNSET
        else:
            protected_range = ProtectedRange.from_dict(_protected_range)




        update_protected_range_request = cls(
            fields=fields,
            protected_range=protected_range,
        )


        update_protected_range_request.additional_properties = d
        return update_protected_range_request

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
