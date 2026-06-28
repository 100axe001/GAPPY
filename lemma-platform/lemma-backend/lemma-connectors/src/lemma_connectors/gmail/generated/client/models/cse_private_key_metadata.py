from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.kacls_key_metadata import KaclsKeyMetadata





T = TypeVar("T", bound="CsePrivateKeyMetadata")



@_attrs_define
class CsePrivateKeyMetadata:
    """ Metadata for a private key instance.

        Attributes:
            kacls_key_metadata (KaclsKeyMetadata | Unset): Metadata for private keys managed by an external key access
                control list service. For details about managing key access, see [Google Workspace CSE API
                Reference](https://developers.google.com/workspace/cse/reference).
            private_key_metadata_id (str | Unset): Output only. The immutable ID for the private key metadata instance.
     """

    kacls_key_metadata: KaclsKeyMetadata | Unset = UNSET
    private_key_metadata_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.kacls_key_metadata import KaclsKeyMetadata
        kacls_key_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kacls_key_metadata, Unset):
            kacls_key_metadata = self.kacls_key_metadata.to_dict()

        private_key_metadata_id = self.private_key_metadata_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kacls_key_metadata is not UNSET:
            field_dict["kaclsKeyMetadata"] = kacls_key_metadata
        if private_key_metadata_id is not UNSET:
            field_dict["privateKeyMetadataId"] = private_key_metadata_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kacls_key_metadata import KaclsKeyMetadata
        d = dict(src_dict)
        _kacls_key_metadata = d.pop("kaclsKeyMetadata", UNSET)
        kacls_key_metadata: KaclsKeyMetadata | Unset
        if isinstance(_kacls_key_metadata,  Unset):
            kacls_key_metadata = UNSET
        else:
            kacls_key_metadata = KaclsKeyMetadata.from_dict(_kacls_key_metadata)




        private_key_metadata_id = d.pop("privateKeyMetadataId", UNSET)

        cse_private_key_metadata = cls(
            kacls_key_metadata=kacls_key_metadata,
            private_key_metadata_id=private_key_metadata_id,
        )


        cse_private_key_metadata.additional_properties = d
        return cse_private_key_metadata

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
