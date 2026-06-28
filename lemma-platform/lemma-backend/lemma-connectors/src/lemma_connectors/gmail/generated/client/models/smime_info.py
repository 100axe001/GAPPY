from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SmimeInfo")



@_attrs_define
class SmimeInfo:
    """ An S/MIME email config.

        Attributes:
            encrypted_key_password (str | Unset): Encrypted key password, when key is encrypted.
            expiration (str | Unset): When the certificate expires (in milliseconds since epoch).
            id (str | Unset): The immutable ID for the SmimeInfo.
            is_default (bool | Unset): Whether this SmimeInfo is the default one for this user's send-as address.
            issuer_cn (str | Unset): The S/MIME certificate issuer's common name.
            pem (str | Unset): PEM formatted X509 concatenated certificate string (standard base64 encoding). Format used
                for returning key, which includes public key as well as certificate chain (not private key).
            pkcs12 (str | Unset): PKCS#12 format containing a single private/public key pair and certificate chain. This
                format is only accepted from client for creating a new SmimeInfo and is never returned, because the private key
                is not intended to be exported. PKCS#12 may be encrypted, in which case encryptedKeyPassword should be set
                appropriately.
     """

    encrypted_key_password: str | Unset = UNSET
    expiration: str | Unset = UNSET
    id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    issuer_cn: str | Unset = UNSET
    pem: str | Unset = UNSET
    pkcs12: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        encrypted_key_password = self.encrypted_key_password

        expiration = self.expiration

        id = self.id

        is_default = self.is_default

        issuer_cn = self.issuer_cn

        pem = self.pem

        pkcs12 = self.pkcs12


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if encrypted_key_password is not UNSET:
            field_dict["encryptedKeyPassword"] = encrypted_key_password
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if issuer_cn is not UNSET:
            field_dict["issuerCn"] = issuer_cn
        if pem is not UNSET:
            field_dict["pem"] = pem
        if pkcs12 is not UNSET:
            field_dict["pkcs12"] = pkcs12

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encrypted_key_password = d.pop("encryptedKeyPassword", UNSET)

        expiration = d.pop("expiration", UNSET)

        id = d.pop("id", UNSET)

        is_default = d.pop("isDefault", UNSET)

        issuer_cn = d.pop("issuerCn", UNSET)

        pem = d.pop("pem", UNSET)

        pkcs12 = d.pop("pkcs12", UNSET)

        smime_info = cls(
            encrypted_key_password=encrypted_key_password,
            expiration=expiration,
            id=id,
            is_default=is_default,
            issuer_cn=issuer_cn,
            pem=pem,
            pkcs12=pkcs12,
        )


        smime_info.additional_properties = d
        return smime_info

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
