from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cse_key_pair import CseKeyPair





T = TypeVar("T", bound="ListCseKeyPairsResponse")



@_attrs_define
class ListCseKeyPairsResponse:
    """ 
        Attributes:
            cse_key_pairs (list[CseKeyPair] | Unset): One page of the list of CSE key pairs installed for the user.
            next_page_token (str | Unset): Pagination token to be passed to a subsequent ListCseKeyPairs call in order to
                retrieve the next page of key pairs. If this value is not returned, then no further pages remain.
     """

    cse_key_pairs: list[CseKeyPair] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cse_key_pair import CseKeyPair
        cse_key_pairs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cse_key_pairs, Unset):
            cse_key_pairs = []
            for cse_key_pairs_item_data in self.cse_key_pairs:
                cse_key_pairs_item = cse_key_pairs_item_data.to_dict()
                cse_key_pairs.append(cse_key_pairs_item)



        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cse_key_pairs is not UNSET:
            field_dict["cseKeyPairs"] = cse_key_pairs
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cse_key_pair import CseKeyPair
        d = dict(src_dict)
        _cse_key_pairs = d.pop("cseKeyPairs", UNSET)
        cse_key_pairs: list[CseKeyPair] | Unset = UNSET
        if _cse_key_pairs is not UNSET:
            cse_key_pairs = []
            for cse_key_pairs_item_data in _cse_key_pairs:
                cse_key_pairs_item = CseKeyPair.from_dict(cse_key_pairs_item_data)



                cse_key_pairs.append(cse_key_pairs_item)


        next_page_token = d.pop("nextPageToken", UNSET)

        list_cse_key_pairs_response = cls(
            cse_key_pairs=cse_key_pairs,
            next_page_token=next_page_token,
        )


        list_cse_key_pairs_response.additional_properties = d
        return list_cse_key_pairs_response

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
