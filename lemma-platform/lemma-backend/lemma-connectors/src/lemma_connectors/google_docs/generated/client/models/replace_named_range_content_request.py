from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReplaceNamedRangeContentRequest")



@_attrs_define
class ReplaceNamedRangeContentRequest:
    """ Replaces the contents of the specified NamedRange or NamedRanges with the given replacement content. Note that an
    individual NamedRange may consist of multiple discontinuous ranges. In this case, only the content in the first
    range will be replaced. The other ranges and their content will be deleted. In cases where replacing or deleting any
    ranges would result in an invalid document structure, a 400 bad request error is returned.

        Attributes:
            named_range_id (str | Unset): The ID of the named range whose content will be replaced. If there is no named
                range with the given ID a 400 bad request error is returned.
            named_range_name (str | Unset): The name of the NamedRanges whose content will be replaced. If there are
                multiple named ranges with the given name, then the content of each one will be replaced. If there are no named
                ranges with the given name, then the request will be a no-op.
            text (str | Unset): Replaces the content of the specified named range(s) with the given text.
     """

    named_range_id: str | Unset = UNSET
    named_range_name: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        named_range_id = self.named_range_id

        named_range_name = self.named_range_name

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if named_range_id is not UNSET:
            field_dict["namedRangeId"] = named_range_id
        if named_range_name is not UNSET:
            field_dict["namedRangeName"] = named_range_name
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        named_range_id = d.pop("namedRangeId", UNSET)

        named_range_name = d.pop("namedRangeName", UNSET)

        text = d.pop("text", UNSET)

        replace_named_range_content_request = cls(
            named_range_id=named_range_id,
            named_range_name=named_range_name,
            text=text,
        )


        replace_named_range_content_request.additional_properties = d
        return replace_named_range_content_request

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
