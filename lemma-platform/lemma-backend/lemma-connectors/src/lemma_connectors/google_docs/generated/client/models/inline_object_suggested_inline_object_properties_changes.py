from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.suggested_inline_object_properties import SuggestedInlineObjectProperties





T = TypeVar("T", bound="InlineObjectSuggestedInlineObjectPropertiesChanges")



@_attrs_define
class InlineObjectSuggestedInlineObjectPropertiesChanges:
    """ The suggested changes to the inline object properties, keyed by suggestion ID.

     """

    additional_properties: dict[str, SuggestedInlineObjectProperties] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.suggested_inline_object_properties import SuggestedInlineObjectProperties
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suggested_inline_object_properties import SuggestedInlineObjectProperties
        d = dict(src_dict)
        inline_object_suggested_inline_object_properties_changes = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SuggestedInlineObjectProperties.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        inline_object_suggested_inline_object_properties_changes.additional_properties = additional_properties
        return inline_object_suggested_inline_object_properties_changes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> SuggestedInlineObjectProperties:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: SuggestedInlineObjectProperties) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
