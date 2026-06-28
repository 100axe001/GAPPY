from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.smime_info import SmimeInfo





T = TypeVar("T", bound="ListSmimeInfoResponse")



@_attrs_define
class ListSmimeInfoResponse:
    """ 
        Attributes:
            smime_info (list[SmimeInfo] | Unset): List of SmimeInfo.
     """

    smime_info: list[SmimeInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.smime_info import SmimeInfo
        smime_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.smime_info, Unset):
            smime_info = []
            for smime_info_item_data in self.smime_info:
                smime_info_item = smime_info_item_data.to_dict()
                smime_info.append(smime_info_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if smime_info is not UNSET:
            field_dict["smimeInfo"] = smime_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.smime_info import SmimeInfo
        d = dict(src_dict)
        _smime_info = d.pop("smimeInfo", UNSET)
        smime_info: list[SmimeInfo] | Unset = UNSET
        if _smime_info is not UNSET:
            smime_info = []
            for smime_info_item_data in _smime_info:
                smime_info_item = SmimeInfo.from_dict(smime_info_item_data)



                smime_info.append(smime_info_item)


        list_smime_info_response = cls(
            smime_info=smime_info,
        )


        list_smime_info_response.additional_properties = d
        return list_smime_info_response

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
