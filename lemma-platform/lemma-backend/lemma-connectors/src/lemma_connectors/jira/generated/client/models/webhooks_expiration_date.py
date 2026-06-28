from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="WebhooksExpirationDate")



@_attrs_define
class WebhooksExpirationDate:
    """ The date the refreshed webhooks expire.

        Attributes:
            expiration_date (int): The expiration date of all the refreshed webhooks.
     """

    expiration_date: int





    def to_dict(self) -> dict[str, Any]:
        expiration_date = self.expiration_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expirationDate": expiration_date,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expiration_date = d.pop("expirationDate")

        webhooks_expiration_date = cls(
            expiration_date=expiration_date,
        )

        return webhooks_expiration_date

