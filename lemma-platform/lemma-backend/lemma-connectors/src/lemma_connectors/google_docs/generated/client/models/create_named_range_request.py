from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.range_ import Range





T = TypeVar("T", bound="CreateNamedRangeRequest")



@_attrs_define
class CreateNamedRangeRequest:
    """ Creates a NamedRange referencing the given range.

        Attributes:
            name (str | Unset): The name of the NamedRange. Names do not need to be unique. Names must be at least 1
                character and no more than 256 characters, measured in UTF-16 code units.
            range_ (Range | Unset): Specifies a contiguous range of text.
     """

    name: str | Unset = UNSET
    range_: Range | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.range_ import Range
        name = self.name

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.range_ import Range
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: Range | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)




        create_named_range_request = cls(
            name=name,
            range_=range_,
        )


        create_named_range_request.additional_properties = d
        return create_named_range_request

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
