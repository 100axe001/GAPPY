from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ContainerForWebhookIDs")



@_attrs_define
class ContainerForWebhookIDs:
    """ Container for a list of webhook IDs.

        Attributes:
            webhook_ids (list[int]): A list of webhook IDs.
     """

    webhook_ids: list[int]





    def to_dict(self) -> dict[str, Any]:
        webhook_ids = self.webhook_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "webhookIds": webhook_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_ids = cast(list[int], d.pop("webhookIds"))


        container_for_webhook_i_ds = cls(
            webhook_ids=webhook_ids,
        )

        return container_for_webhook_i_ds

