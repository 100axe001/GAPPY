from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KaclsKeyMetadata")



@_attrs_define
class KaclsKeyMetadata:
    """ Metadata for private keys managed by an external key access control list service. For details about managing key
    access, see [Google Workspace CSE API Reference](https://developers.google.com/workspace/cse/reference).

        Attributes:
            kacls_data (str | Unset): Opaque data generated and used by the key access control list service. Maximum size: 8
                KiB.
            kacls_uri (str | Unset): The URI of the key access control list service that manages the private key.
     """

    kacls_data: str | Unset = UNSET
    kacls_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kacls_data = self.kacls_data

        kacls_uri = self.kacls_uri


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kacls_data is not UNSET:
            field_dict["kaclsData"] = kacls_data
        if kacls_uri is not UNSET:
            field_dict["kaclsUri"] = kacls_uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kacls_data = d.pop("kaclsData", UNSET)

        kacls_uri = d.pop("kaclsUri", UNSET)

        kacls_key_metadata = cls(
            kacls_data=kacls_data,
            kacls_uri=kacls_uri,
        )


        kacls_key_metadata.additional_properties = d
        return kacls_key_metadata

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
