from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.webhook_details import WebhookDetails





T = TypeVar("T", bound="WebhookRegistrationDetails")



@_attrs_define
class WebhookRegistrationDetails:
    """ Details of webhooks to register.

        Attributes:
            url (str): The URL that specifies where to send the webhooks. This URL must use the same base URL as the Connect
                app. Only a single URL per app is allowed to be registered.
            webhooks (list[WebhookDetails]): A list of webhooks.
     """

    url: str
    webhooks: list[WebhookDetails]





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_details import WebhookDetails
        url = self.url

        webhooks = []
        for webhooks_item_data in self.webhooks:
            webhooks_item = webhooks_item_data.to_dict()
            webhooks.append(webhooks_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "url": url,
            "webhooks": webhooks,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_details import WebhookDetails
        d = dict(src_dict)
        url = d.pop("url")

        webhooks = []
        _webhooks = d.pop("webhooks")
        for webhooks_item_data in (_webhooks):
            webhooks_item = WebhookDetails.from_dict(webhooks_item_data)



            webhooks.append(webhooks_item)


        webhook_registration_details = cls(
            url=url,
            webhooks=webhooks,
        )

        return webhook_registration_details

