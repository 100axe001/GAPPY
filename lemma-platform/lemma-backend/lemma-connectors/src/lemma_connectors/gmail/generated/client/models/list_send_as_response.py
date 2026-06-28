from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.send_as import SendAs





T = TypeVar("T", bound="ListSendAsResponse")



@_attrs_define
class ListSendAsResponse:
    """ Response for the ListSendAs method.

        Attributes:
            send_as (list[SendAs] | Unset): List of send-as aliases.
     """

    send_as: list[SendAs] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.send_as import SendAs
        send_as: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.send_as, Unset):
            send_as = []
            for send_as_item_data in self.send_as:
                send_as_item = send_as_item_data.to_dict()
                send_as.append(send_as_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if send_as is not UNSET:
            field_dict["sendAs"] = send_as

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_as import SendAs
        d = dict(src_dict)
        _send_as = d.pop("sendAs", UNSET)
        send_as: list[SendAs] | Unset = UNSET
        if _send_as is not UNSET:
            send_as = []
            for send_as_item_data in _send_as:
                send_as_item = SendAs.from_dict(send_as_item_data)



                send_as.append(send_as_item)


        list_send_as_response = cls(
            send_as=send_as,
        )


        list_send_as_response.additional_properties = d
        return list_send_as_response

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
