from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.registered_webhook import RegisteredWebhook





T = TypeVar("T", bound="ContainerForRegisteredWebhooks")



@_attrs_define
class ContainerForRegisteredWebhooks:
    """ Container for a list of registered webhooks. Webhook details are returned in the same order as the request.

        Attributes:
            webhook_registration_result (list[RegisteredWebhook] | Unset): A list of registered webhooks.
     """

    webhook_registration_result: list[RegisteredWebhook] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.registered_webhook import RegisteredWebhook
        webhook_registration_result: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.webhook_registration_result, Unset):
            webhook_registration_result = []
            for webhook_registration_result_item_data in self.webhook_registration_result:
                webhook_registration_result_item = webhook_registration_result_item_data.to_dict()
                webhook_registration_result.append(webhook_registration_result_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if webhook_registration_result is not UNSET:
            field_dict["webhookRegistrationResult"] = webhook_registration_result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_webhook import RegisteredWebhook
        d = dict(src_dict)
        _webhook_registration_result = d.pop("webhookRegistrationResult", UNSET)
        webhook_registration_result: list[RegisteredWebhook] | Unset = UNSET
        if _webhook_registration_result is not UNSET:
            webhook_registration_result = []
            for webhook_registration_result_item_data in _webhook_registration_result:
                webhook_registration_result_item = RegisteredWebhook.from_dict(webhook_registration_result_item_data)



                webhook_registration_result.append(webhook_registration_result_item)


        container_for_registered_webhooks = cls(
            webhook_registration_result=webhook_registration_result,
        )

        return container_for_registered_webhooks

