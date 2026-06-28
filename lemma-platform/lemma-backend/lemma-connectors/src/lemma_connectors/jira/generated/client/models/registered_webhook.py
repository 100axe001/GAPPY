from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RegisteredWebhook")



@_attrs_define
class RegisteredWebhook:
    """ ID of a registered webhook or error messages explaining why a webhook wasn't registered.

        Attributes:
            created_webhook_id (int | Unset): The ID of the webhook. Returned if the webhook is created.
            errors (list[str] | Unset): Error messages specifying why the webhook creation failed.
     """

    created_webhook_id: int | Unset = UNSET
    errors: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_webhook_id = self.created_webhook_id

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_webhook_id is not UNSET:
            field_dict["createdWebhookId"] = created_webhook_id
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_webhook_id = d.pop("createdWebhookId", UNSET)

        errors = cast(list[str], d.pop("errors", UNSET))


        registered_webhook = cls(
            created_webhook_id=created_webhook_id,
            errors=errors,
        )

        return registered_webhook

