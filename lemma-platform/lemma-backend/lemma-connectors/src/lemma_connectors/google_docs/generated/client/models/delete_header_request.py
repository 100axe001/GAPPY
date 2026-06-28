from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteHeaderRequest")



@_attrs_define
class DeleteHeaderRequest:
    """ Deletes a Header from the document.

        Attributes:
            header_id (str | Unset): The id of the header to delete. If this header is defined on DocumentStyle, the
                reference to this header is removed, resulting in no header of that type for the first section of the document.
                If this header is defined on a SectionStyle, the reference to this header is removed and the header of that type
                is now continued from the previous section.
     """

    header_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        header_id = self.header_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if header_id is not UNSET:
            field_dict["headerId"] = header_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        header_id = d.pop("headerId", UNSET)

        delete_header_request = cls(
            header_id=header_id,
        )


        delete_header_request.additional_properties = d
        return delete_header_request

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
