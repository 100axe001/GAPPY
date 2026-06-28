from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.delegate import Delegate





T = TypeVar("T", bound="ListDelegatesResponse")



@_attrs_define
class ListDelegatesResponse:
    """ Response for the ListDelegates method.

        Attributes:
            delegates (list[Delegate] | Unset): List of the user's delegates (with any verification status). If an account
                doesn't have delegates, this field doesn't appear.
     """

    delegates: list[Delegate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.delegate import Delegate
        delegates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delegates, Unset):
            delegates = []
            for delegates_item_data in self.delegates:
                delegates_item = delegates_item_data.to_dict()
                delegates.append(delegates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if delegates is not UNSET:
            field_dict["delegates"] = delegates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delegate import Delegate
        d = dict(src_dict)
        _delegates = d.pop("delegates", UNSET)
        delegates: list[Delegate] | Unset = UNSET
        if _delegates is not UNSET:
            delegates = []
            for delegates_item_data in _delegates:
                delegates_item = Delegate.from_dict(delegates_item_data)



                delegates.append(delegates_item)


        list_delegates_response = cls(
            delegates=delegates,
        )


        list_delegates_response.additional_properties = d
        return list_delegates_response

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
