from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.smtp_msa_security_mode import SmtpMsaSecurityMode
from ..types import UNSET, Unset






T = TypeVar("T", bound="SmtpMsa")



@_attrs_define
class SmtpMsa:
    """ Configuration for communication with an SMTP service.

        Attributes:
            host (str | Unset): The hostname of the SMTP service. Required.
            password (str | Unset): The password that will be used for authentication with the SMTP service. This is a
                write-only field that can be specified in requests to create or update SendAs settings; it is never populated in
                responses.
            port (int | Unset): The port of the SMTP service. Required.
            security_mode (SmtpMsaSecurityMode | Unset): The protocol that will be used to secure communication with the
                SMTP service. Required.
            username (str | Unset): The username that will be used for authentication with the SMTP service. This is a
                write-only field that can be specified in requests to create or update SendAs settings; it is never populated in
                responses.
     """

    host: str | Unset = UNSET
    password: str | Unset = UNSET
    port: int | Unset = UNSET
    security_mode: SmtpMsaSecurityMode | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        host = self.host

        password = self.password

        port = self.port

        security_mode: str | Unset = UNSET
        if not isinstance(self.security_mode, Unset):
            security_mode = self.security_mode.value


        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if host is not UNSET:
            field_dict["host"] = host
        if password is not UNSET:
            field_dict["password"] = password
        if port is not UNSET:
            field_dict["port"] = port
        if security_mode is not UNSET:
            field_dict["securityMode"] = security_mode
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        password = d.pop("password", UNSET)

        port = d.pop("port", UNSET)

        _security_mode = d.pop("securityMode", UNSET)
        security_mode: SmtpMsaSecurityMode | Unset
        if isinstance(_security_mode,  Unset):
            security_mode = UNSET
        else:
            security_mode = SmtpMsaSecurityMode(_security_mode)




        username = d.pop("username", UNSET)

        smtp_msa = cls(
            host=host,
            password=password,
            port=port,
            security_mode=security_mode,
            username=username,
        )


        smtp_msa.additional_properties = d
        return smtp_msa

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
