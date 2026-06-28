from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FailedWebhook")



@_attrs_define
class FailedWebhook:
    """ Details about a failed webhook.

        Attributes:
            failure_time (int): The time the webhook was added to the list of failed webhooks (that is, the time of the last
                failed retry).
            id (str): The webhook ID, as sent in the `X-Atlassian-Webhook-Identifier` header with the webhook.
            url (str): The original webhook destination.
            body (str | Unset): The webhook body.
     """

    failure_time: int
    id: str
    url: str
    body: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        failure_time = self.failure_time

        id = self.id

        url = self.url

        body = self.body


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "failureTime": failure_time,
            "id": id,
            "url": url,
        })
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failure_time = d.pop("failureTime")

        id = d.pop("id")

        url = d.pop("url")

        body = d.pop("body", UNSET)

        failed_webhook = cls(
            failure_time=failure_time,
            id=id,
            url=url,
            body=body,
        )

        return failed_webhook

