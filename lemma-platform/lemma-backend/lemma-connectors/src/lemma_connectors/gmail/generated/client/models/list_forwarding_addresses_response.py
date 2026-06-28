from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.forwarding_address import ForwardingAddress





T = TypeVar("T", bound="ListForwardingAddressesResponse")



@_attrs_define
class ListForwardingAddressesResponse:
    """ Response for the ListForwardingAddresses method.

        Attributes:
            forwarding_addresses (list[ForwardingAddress] | Unset): List of addresses that may be used for forwarding.
     """

    forwarding_addresses: list[ForwardingAddress] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.forwarding_address import ForwardingAddress
        forwarding_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.forwarding_addresses, Unset):
            forwarding_addresses = []
            for forwarding_addresses_item_data in self.forwarding_addresses:
                forwarding_addresses_item = forwarding_addresses_item_data.to_dict()
                forwarding_addresses.append(forwarding_addresses_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if forwarding_addresses is not UNSET:
            field_dict["forwardingAddresses"] = forwarding_addresses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.forwarding_address import ForwardingAddress
        d = dict(src_dict)
        _forwarding_addresses = d.pop("forwardingAddresses", UNSET)
        forwarding_addresses: list[ForwardingAddress] | Unset = UNSET
        if _forwarding_addresses is not UNSET:
            forwarding_addresses = []
            for forwarding_addresses_item_data in _forwarding_addresses:
                forwarding_addresses_item = ForwardingAddress.from_dict(forwarding_addresses_item_data)



                forwarding_addresses.append(forwarding_addresses_item)


        list_forwarding_addresses_response = cls(
            forwarding_addresses=forwarding_addresses,
        )


        list_forwarding_addresses_response.additional_properties = d
        return list_forwarding_addresses_response

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
