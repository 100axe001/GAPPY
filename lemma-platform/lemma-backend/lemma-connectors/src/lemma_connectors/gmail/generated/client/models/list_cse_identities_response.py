from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cse_identity import CseIdentity





T = TypeVar("T", bound="ListCseIdentitiesResponse")



@_attrs_define
class ListCseIdentitiesResponse:
    """ 
        Attributes:
            cse_identities (list[CseIdentity] | Unset): One page of the list of CSE identities configured for the user.
            next_page_token (str | Unset): Pagination token to be passed to a subsequent ListCseIdentities call in order to
                retrieve the next page of identities. If this value is not returned or is the empty string, then no further
                pages remain.
     """

    cse_identities: list[CseIdentity] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cse_identity import CseIdentity
        cse_identities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cse_identities, Unset):
            cse_identities = []
            for cse_identities_item_data in self.cse_identities:
                cse_identities_item = cse_identities_item_data.to_dict()
                cse_identities.append(cse_identities_item)



        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cse_identities is not UNSET:
            field_dict["cseIdentities"] = cse_identities
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cse_identity import CseIdentity
        d = dict(src_dict)
        _cse_identities = d.pop("cseIdentities", UNSET)
        cse_identities: list[CseIdentity] | Unset = UNSET
        if _cse_identities is not UNSET:
            cse_identities = []
            for cse_identities_item_data in _cse_identities:
                cse_identities_item = CseIdentity.from_dict(cse_identities_item_data)



                cse_identities.append(cse_identities_item)


        next_page_token = d.pop("nextPageToken", UNSET)

        list_cse_identities_response = cls(
            cse_identities=cse_identities,
            next_page_token=next_page_token,
        )


        list_cse_identities_response.additional_properties = d
        return list_cse_identities_response

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
