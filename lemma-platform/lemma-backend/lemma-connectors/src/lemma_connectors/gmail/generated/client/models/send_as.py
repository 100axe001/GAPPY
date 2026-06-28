from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_as_verification_status import SendAsVerificationStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.smtp_msa import SmtpMsa





T = TypeVar("T", bound="SendAs")



@_attrs_define
class SendAs:
    """ Settings associated with a send-as alias, which can be either the primary login address associated with the account
    or a custom "from" address. Send-as aliases correspond to the "Send Mail As" feature in the web interface.

        Attributes:
            display_name (str | Unset): A name that appears in the "From:" header for mail sent using this alias. For custom
                "from" addresses, when this is empty, Gmail will populate the "From:" header with the name that is used for the
                primary address associated with the account. If the admin has disabled the ability for users to update their
                name format, requests to update this field for the primary login will silently fail.
            is_default (bool | Unset): Whether this address is selected as the default "From:" address in situations such as
                composing a new message or sending a vacation auto-reply. Every Gmail account has exactly one default send-as
                address, so the only legal value that clients may write to this field is `true`. Changing this from `false` to
                `true` for an address will result in this field becoming `false` for the other previous default address.
            is_primary (bool | Unset): Whether this address is the primary address used to login to the account. Every Gmail
                account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases. This
                field is read-only.
            reply_to_address (str | Unset): An optional email address that is included in a "Reply-To:" header for mail sent
                using this alias. If this is empty, Gmail will not generate a "Reply-To:" header.
            send_as_email (str | Unset): The email address that appears in the "From:" header for mail sent using this
                alias. This is read-only for all operations except create.
            signature (str | Unset): An optional HTML signature that is included in messages composed with this alias in the
                Gmail web UI. This signature is added to new emails only.
            smtp_msa (SmtpMsa | Unset): Configuration for communication with an SMTP service.
            treat_as_alias (bool | Unset): Whether Gmail should treat this address as an alias for the user's primary email
                address. This setting only applies to custom "from" aliases.
            verification_status (SendAsVerificationStatus | Unset): Indicates whether this address has been verified for use
                as a send-as alias. Read-only. This setting only applies to custom "from" aliases.
     """

    display_name: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    is_primary: bool | Unset = UNSET
    reply_to_address: str | Unset = UNSET
    send_as_email: str | Unset = UNSET
    signature: str | Unset = UNSET
    smtp_msa: SmtpMsa | Unset = UNSET
    treat_as_alias: bool | Unset = UNSET
    verification_status: SendAsVerificationStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.smtp_msa import SmtpMsa
        display_name = self.display_name

        is_default = self.is_default

        is_primary = self.is_primary

        reply_to_address = self.reply_to_address

        send_as_email = self.send_as_email

        signature = self.signature

        smtp_msa: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smtp_msa, Unset):
            smtp_msa = self.smtp_msa.to_dict()

        treat_as_alias = self.treat_as_alias

        verification_status: str | Unset = UNSET
        if not isinstance(self.verification_status, Unset):
            verification_status = self.verification_status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if reply_to_address is not UNSET:
            field_dict["replyToAddress"] = reply_to_address
        if send_as_email is not UNSET:
            field_dict["sendAsEmail"] = send_as_email
        if signature is not UNSET:
            field_dict["signature"] = signature
        if smtp_msa is not UNSET:
            field_dict["smtpMsa"] = smtp_msa
        if treat_as_alias is not UNSET:
            field_dict["treatAsAlias"] = treat_as_alias
        if verification_status is not UNSET:
            field_dict["verificationStatus"] = verification_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.smtp_msa import SmtpMsa
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        reply_to_address = d.pop("replyToAddress", UNSET)

        send_as_email = d.pop("sendAsEmail", UNSET)

        signature = d.pop("signature", UNSET)

        _smtp_msa = d.pop("smtpMsa", UNSET)
        smtp_msa: SmtpMsa | Unset
        if isinstance(_smtp_msa,  Unset):
            smtp_msa = UNSET
        else:
            smtp_msa = SmtpMsa.from_dict(_smtp_msa)




        treat_as_alias = d.pop("treatAsAlias", UNSET)

        _verification_status = d.pop("verificationStatus", UNSET)
        verification_status: SendAsVerificationStatus | Unset
        if isinstance(_verification_status,  Unset):
            verification_status = UNSET
        else:
            verification_status = SendAsVerificationStatus(_verification_status)




        send_as = cls(
            display_name=display_name,
            is_default=is_default,
            is_primary=is_primary,
            reply_to_address=reply_to_address,
            send_as_email=send_as_email,
            signature=signature,
            smtp_msa=smtp_msa,
            treat_as_alias=treat_as_alias,
            verification_status=verification_status,
        )


        send_as.additional_properties = d
        return send_as

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
