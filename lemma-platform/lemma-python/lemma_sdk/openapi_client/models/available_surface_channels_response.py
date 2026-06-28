from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.available_surface_channel_response import (
        AvailableSurfaceChannelResponse,
    )


T = TypeVar("T", bound="AvailableSurfaceChannelsResponse")


@_attrs_define
class AvailableSurfaceChannelsResponse:
    """
    Attributes:
        channels (list[AvailableSurfaceChannelResponse] | Unset):
    """

    channels: list[AvailableSurfaceChannelResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.available_surface_channel_response import (
            AvailableSurfaceChannelResponse,
        )

        d = dict(src_dict)
        _channels = d.pop("channels", UNSET)
        channels: list[AvailableSurfaceChannelResponse] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = AvailableSurfaceChannelResponse.from_dict(
                    channels_item_data
                )

                channels.append(channels_item)

        available_surface_channels_response = cls(
            channels=channels,
        )

        available_surface_channels_response.additional_properties = d
        return available_surface_channels_response

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
