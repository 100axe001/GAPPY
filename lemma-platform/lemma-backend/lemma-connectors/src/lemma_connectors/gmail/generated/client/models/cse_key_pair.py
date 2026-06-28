from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cse_key_pair_enablement_state import CseKeyPairEnablementState
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cse_private_key_metadata import CsePrivateKeyMetadata





T = TypeVar("T", bound="CseKeyPair")



@_attrs_define
class CseKeyPair:
    """ A client-side encryption S/MIME key pair, which is comprised of a public key, its certificate chain, and metadata
    for its paired private key. Gmail uses the key pair to complete the following tasks: - Sign outgoing client-side
    encrypted messages. - Save and reopen drafts of client-side encrypted messages. - Save and reopen sent messages. -
    Decrypt incoming or archived S/MIME messages.

        Attributes:
            disable_time (str | Unset): Output only. If a key pair is set to `DISABLED`, the time that the key pair's state
                changed from `ENABLED` to `DISABLED`. This field is present only when the key pair is in state `DISABLED`.
            enablement_state (CseKeyPairEnablementState | Unset): Output only. The current state of the key pair.
            key_pair_id (str | Unset): Output only. The immutable ID for the client-side encryption S/MIME key pair.
            pem (str | Unset): Output only. The public key and its certificate chain, in
                [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format.
            pkcs7 (str | Unset): Input only. The public key and its certificate chain. The chain must be in
                [PKCS#7](https://en.wikipedia.org/wiki/PKCS_7) format and use PEM encoding and ASCII armor.
            private_key_metadata (list[CsePrivateKeyMetadata] | Unset): Metadata for instances of this key pair's private
                key.
            subject_email_addresses (list[str] | Unset): Output only. The email address identities that are specified on the
                leaf certificate.
     """

    disable_time: str | Unset = UNSET
    enablement_state: CseKeyPairEnablementState | Unset = UNSET
    key_pair_id: str | Unset = UNSET
    pem: str | Unset = UNSET
    pkcs7: str | Unset = UNSET
    private_key_metadata: list[CsePrivateKeyMetadata] | Unset = UNSET
    subject_email_addresses: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cse_private_key_metadata import CsePrivateKeyMetadata
        disable_time = self.disable_time

        enablement_state: str | Unset = UNSET
        if not isinstance(self.enablement_state, Unset):
            enablement_state = self.enablement_state.value


        key_pair_id = self.key_pair_id

        pem = self.pem

        pkcs7 = self.pkcs7

        private_key_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.private_key_metadata, Unset):
            private_key_metadata = []
            for private_key_metadata_item_data in self.private_key_metadata:
                private_key_metadata_item = private_key_metadata_item_data.to_dict()
                private_key_metadata.append(private_key_metadata_item)



        subject_email_addresses: list[str] | Unset = UNSET
        if not isinstance(self.subject_email_addresses, Unset):
            subject_email_addresses = self.subject_email_addresses




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if disable_time is not UNSET:
            field_dict["disableTime"] = disable_time
        if enablement_state is not UNSET:
            field_dict["enablementState"] = enablement_state
        if key_pair_id is not UNSET:
            field_dict["keyPairId"] = key_pair_id
        if pem is not UNSET:
            field_dict["pem"] = pem
        if pkcs7 is not UNSET:
            field_dict["pkcs7"] = pkcs7
        if private_key_metadata is not UNSET:
            field_dict["privateKeyMetadata"] = private_key_metadata
        if subject_email_addresses is not UNSET:
            field_dict["subjectEmailAddresses"] = subject_email_addresses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cse_private_key_metadata import CsePrivateKeyMetadata
        d = dict(src_dict)
        disable_time = d.pop("disableTime", UNSET)

        _enablement_state = d.pop("enablementState", UNSET)
        enablement_state: CseKeyPairEnablementState | Unset
        if isinstance(_enablement_state,  Unset):
            enablement_state = UNSET
        else:
            enablement_state = CseKeyPairEnablementState(_enablement_state)




        key_pair_id = d.pop("keyPairId", UNSET)

        pem = d.pop("pem", UNSET)

        pkcs7 = d.pop("pkcs7", UNSET)

        _private_key_metadata = d.pop("privateKeyMetadata", UNSET)
        private_key_metadata: list[CsePrivateKeyMetadata] | Unset = UNSET
        if _private_key_metadata is not UNSET:
            private_key_metadata = []
            for private_key_metadata_item_data in _private_key_metadata:
                private_key_metadata_item = CsePrivateKeyMetadata.from_dict(private_key_metadata_item_data)



                private_key_metadata.append(private_key_metadata_item)


        subject_email_addresses = cast(list[str], d.pop("subjectEmailAddresses", UNSET))


        cse_key_pair = cls(
            disable_time=disable_time,
            enablement_state=enablement_state,
            key_pair_id=key_pair_id,
            pem=pem,
            pkcs7=pkcs7,
            private_key_metadata=private_key_metadata,
            subject_email_addresses=subject_email_addresses,
        )


        cse_key_pair.additional_properties = d
        return cse_key_pair

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
