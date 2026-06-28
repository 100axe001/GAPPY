from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.surface_channel_route_response import SurfaceChannelRouteResponse
    from ..models.surface_identity_config_response import SurfaceIdentityConfigResponse


T = TypeVar("T", bound="SurfaceConfigResponse")


@_attrs_define
class SurfaceConfigResponse:
    """Mirrors SurfaceBehaviorConfigInput: what you send is what you get back.

    Attributes:
        channels (list[SurfaceChannelRouteResponse] | Unset):
        dm_conversation_reset_after_hours (int | Unset):  Default: 24.
        identity (SurfaceIdentityConfigResponse | Unset):
    """

    channels: list[SurfaceChannelRouteResponse] | Unset = UNSET
    dm_conversation_reset_after_hours: int | Unset = 24
    identity: SurfaceIdentityConfigResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        dm_conversation_reset_after_hours = self.dm_conversation_reset_after_hours

        identity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identity, Unset):
            identity = self.identity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if dm_conversation_reset_after_hours is not UNSET:
            field_dict["dm_conversation_reset_after_hours"] = (
                dm_conversation_reset_after_hours
            )
        if identity is not UNSET:
            field_dict["identity"] = identity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.surface_channel_route_response import SurfaceChannelRouteResponse
        from ..models.surface_identity_config_response import (
            SurfaceIdentityConfigResponse,
        )

        d = dict(src_dict)
        _channels = d.pop("channels", UNSET)
        channels: list[SurfaceChannelRouteResponse] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = SurfaceChannelRouteResponse.from_dict(
                    channels_item_data
                )

                channels.append(channels_item)

        dm_conversation_reset_after_hours = d.pop(
            "dm_conversation_reset_after_hours", UNSET
        )

        _identity = d.pop("identity", UNSET)
        identity: SurfaceIdentityConfigResponse | Unset
        if isinstance(_identity, Unset):
            identity = UNSET
        else:
            identity = SurfaceIdentityConfigResponse.from_dict(_identity)

        surface_config_response = cls(
            channels=channels,
            dm_conversation_reset_after_hours=dm_conversation_reset_after_hours,
            identity=identity,
        )

        surface_config_response.additional_properties = d
        return surface_config_response

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
