from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Setting")



@_attrs_define
class Setting:
    """ 
        Attributes:
            etag (str | Unset): ETag of the resource.
            id (str | Unset): The id of the user setting.
            kind (str | Unset): Type of the resource ("calendar#setting"). Default: 'calendar#setting'.
            value (str | Unset): Value of the user setting. The format of the value depends on the ID of the setting. It
                must always be a UTF-8 string of length up to 1024 characters.
     """

    etag: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'calendar#setting'
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        etag = self.etag

        id = self.id

        kind = self.kind

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        value = d.pop("value", UNSET)

        setting = cls(
            etag=etag,
            id=id,
            kind=kind,
            value=value,
        )


        setting.additional_properties = d
        return setting

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
