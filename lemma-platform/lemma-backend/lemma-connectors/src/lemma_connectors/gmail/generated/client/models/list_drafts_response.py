from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.draft import Draft





T = TypeVar("T", bound="ListDraftsResponse")



@_attrs_define
class ListDraftsResponse:
    """ 
        Attributes:
            drafts (list[Draft] | Unset): List of drafts. Note that the `Message` property in each `Draft` resource only
                contains an `id` and a `threadId`. The messages.get method can fetch additional message details.
            next_page_token (str | Unset): Token to retrieve the next page of results in the list.
            result_size_estimate (int | Unset): Estimated total number of results.
     """

    drafts: list[Draft] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    result_size_estimate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.draft import Draft
        drafts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.drafts, Unset):
            drafts = []
            for drafts_item_data in self.drafts:
                drafts_item = drafts_item_data.to_dict()
                drafts.append(drafts_item)



        next_page_token = self.next_page_token

        result_size_estimate = self.result_size_estimate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if drafts is not UNSET:
            field_dict["drafts"] = drafts
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if result_size_estimate is not UNSET:
            field_dict["resultSizeEstimate"] = result_size_estimate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.draft import Draft
        d = dict(src_dict)
        _drafts = d.pop("drafts", UNSET)
        drafts: list[Draft] | Unset = UNSET
        if _drafts is not UNSET:
            drafts = []
            for drafts_item_data in _drafts:
                drafts_item = Draft.from_dict(drafts_item_data)



                drafts.append(drafts_item)


        next_page_token = d.pop("nextPageToken", UNSET)

        result_size_estimate = d.pop("resultSizeEstimate", UNSET)

        list_drafts_response = cls(
            drafts=drafts,
            next_page_token=next_page_token,
            result_size_estimate=result_size_estimate,
        )


        list_drafts_response.additional_properties = d
        return list_drafts_response

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
