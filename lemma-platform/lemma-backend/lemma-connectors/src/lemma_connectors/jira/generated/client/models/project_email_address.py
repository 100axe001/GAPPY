from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProjectEmailAddress")



@_attrs_define
class ProjectEmailAddress:
    """ A project's sender email address.

        Attributes:
            email_address (str | Unset): The email address.
            email_address_status (list[str] | Unset): When using a custom domain, the status of the email address.
     """

    email_address: str | Unset = UNSET
    email_address_status: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        email_address_status: list[str] | Unset = UNSET
        if not isinstance(self.email_address_status, Unset):
            email_address_status = self.email_address_status




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if email_address_status is not UNSET:
            field_dict["emailAddressStatus"] = email_address_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_address = d.pop("emailAddress", UNSET)

        email_address_status = cast(list[str], d.pop("emailAddressStatus", UNSET))


        project_email_address = cls(
            email_address=email_address,
            email_address_status=email_address_status,
        )

        return project_email_address

