from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WatchResponse")



@_attrs_define
class WatchResponse:
    """ Push notification watch response.

        Attributes:
            expiration (str | Unset): When Gmail will stop sending notifications for mailbox updates (epoch millis). Call
                `watch` again before this time to renew the watch.
            history_id (str | Unset): The ID of the mailbox's current history record.
     """

    expiration: str | Unset = UNSET
    history_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        expiration = self.expiration

        history_id = self.history_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if history_id is not UNSET:
            field_dict["historyId"] = history_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expiration = d.pop("expiration", UNSET)

        history_id = d.pop("historyId", UNSET)

        watch_response = cls(
            expiration=expiration,
            history_id=history_id,
        )


        watch_response.additional_properties = d
        return watch_response

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
