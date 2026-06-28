from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.footer import Footer





T = TypeVar("T", bound="DocumentFooters")



@_attrs_define
class DocumentFooters:
    """ Output only. The footers in the document, keyed by footer ID.

     """

    additional_properties: dict[str, Footer] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.footer import Footer
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.footer import Footer
        d = dict(src_dict)
        document_footers = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Footer.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        document_footers.additional_properties = additional_properties
        return document_footers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Footer:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Footer) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
