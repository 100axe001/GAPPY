from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.channel_params import ChannelParams





T = TypeVar("T", bound="Channel")



@_attrs_define
class Channel:
    """ 
        Attributes:
            address (str | Unset): The address where notifications are delivered for this channel.
            expiration (str | Unset): Date and time of notification channel expiration, expressed as a Unix timestamp, in
                milliseconds. Optional.
            id (str | Unset): A UUID or similar unique string that identifies this channel.
            kind (str | Unset): Identifies this as a notification channel used to watch for changes to a resource, which is
                "api#channel". Default: 'api#channel'.
            params (ChannelParams | Unset): Additional parameters controlling delivery channel behavior. Optional.
            payload (bool | Unset): A Boolean value to indicate whether payload is wanted. Optional.
            resource_id (str | Unset): An opaque ID that identifies the resource being watched on this channel. Stable
                across different API versions.
            resource_uri (str | Unset): A version-specific identifier for the watched resource.
            token (str | Unset): An arbitrary string delivered to the target address with each notification delivered over
                this channel. Optional.
            type_ (str | Unset): The type of delivery mechanism used for this channel. Valid values are "web_hook" (or
                "webhook"). Both values refer to a channel where Http requests are used to deliver messages.
     """

    address: str | Unset = UNSET
    expiration: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'api#channel'
    params: ChannelParams | Unset = UNSET
    payload: bool | Unset = UNSET
    resource_id: str | Unset = UNSET
    resource_uri: str | Unset = UNSET
    token: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.channel_params import ChannelParams
        address = self.address

        expiration = self.expiration

        id = self.id

        kind = self.kind

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        payload = self.payload

        resource_id = self.resource_id

        resource_uri = self.resource_uri

        token = self.token

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if params is not UNSET:
            field_dict["params"] = params
        if payload is not UNSET:
            field_dict["payload"] = payload
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if token is not UNSET:
            field_dict["token"] = token
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_params import ChannelParams
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        expiration = d.pop("expiration", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        _params = d.pop("params", UNSET)
        params: ChannelParams | Unset
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = ChannelParams.from_dict(_params)




        payload = d.pop("payload", UNSET)

        resource_id = d.pop("resourceId", UNSET)

        resource_uri = d.pop("resourceUri", UNSET)

        token = d.pop("token", UNSET)

        type_ = d.pop("type", UNSET)

        channel = cls(
            address=address,
            expiration=expiration,
            id=id,
            kind=kind,
            params=params,
            payload=payload,
            resource_id=resource_id,
            resource_uri=resource_uri,
            token=token,
            type_=type_,
        )


        channel.additional_properties = d
        return channel

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
