from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.surface_channel_route_input import SurfaceChannelRouteInput
    from ..models.surface_identity_config_input import SurfaceIdentityConfigInput


T = TypeVar("T", bound="SurfaceBehaviorConfigInput")


@_attrs_define
class SurfaceBehaviorConfigInput:
    """
    Attributes:
        channels (list[SurfaceChannelRouteInput] | Unset):
        dm_conversation_reset_after_hours (int | Unset):  Default: 24.
        identity (SurfaceIdentityConfigInput | Unset):
    """

    channels: list[SurfaceChannelRouteInput] | Unset = UNSET
    dm_conversation_reset_after_hours: int | Unset = 24
    identity: SurfaceIdentityConfigInput | Unset = UNSET

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
        from ..models.surface_channel_route_input import SurfaceChannelRouteInput
        from ..models.surface_identity_config_input import SurfaceIdentityConfigInput

        d = dict(src_dict)
        _channels = d.pop("channels", UNSET)
        channels: list[SurfaceChannelRouteInput] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = SurfaceChannelRouteInput.from_dict(channels_item_data)

                channels.append(channels_item)

        dm_conversation_reset_after_hours = d.pop(
            "dm_conversation_reset_after_hours", UNSET
        )

        _identity = d.pop("identity", UNSET)
        identity: SurfaceIdentityConfigInput | Unset
        if isinstance(_identity, Unset):
            identity = UNSET
        else:
            identity = SurfaceIdentityConfigInput.from_dict(_identity)

        surface_behavior_config_input = cls(
            channels=channels,
            dm_conversation_reset_after_hours=dm_conversation_reset_after_hours,
            identity=identity,
        )

        return surface_behavior_config_input
