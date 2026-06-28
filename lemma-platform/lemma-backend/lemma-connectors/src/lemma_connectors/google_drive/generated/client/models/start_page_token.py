from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="StartPageToken")



@_attrs_define
class StartPageToken:
    """ 
        Attributes:
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#startPageToken".
                Default: 'drive#startPageToken'.
            start_page_token (str | Unset): The starting page token for listing changes.
     """

    kind: str | Unset = 'drive#startPageToken'
    start_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        start_page_token = self.start_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if start_page_token is not UNSET:
            field_dict["startPageToken"] = start_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        start_page_token = d.pop("startPageToken", UNSET)

        start_page_token = cls(
            kind=kind,
            start_page_token=start_page_token,
        )


        start_page_token.additional_properties = d
        return start_page_token

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
