from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.history import History





T = TypeVar("T", bound="ListHistoryResponse")



@_attrs_define
class ListHistoryResponse:
    """ 
        Attributes:
            history (list[History] | Unset): List of history records. Any `messages` contained in the response will
                typically only have `id` and `threadId` fields populated.
            history_id (str | Unset): The ID of the mailbox's current history record.
            next_page_token (str | Unset): Page token to retrieve the next page of results in the list.
     """

    history: list[History] | Unset = UNSET
    history_id: str | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.history import History
        history: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)



        history_id = self.history_id

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if history is not UNSET:
            field_dict["history"] = history
        if history_id is not UNSET:
            field_dict["historyId"] = history_id
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.history import History
        d = dict(src_dict)
        _history = d.pop("history", UNSET)
        history: list[History] | Unset = UNSET
        if _history is not UNSET:
            history = []
            for history_item_data in _history:
                history_item = History.from_dict(history_item_data)



                history.append(history_item)


        history_id = d.pop("historyId", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_history_response = cls(
            history=history,
            history_id=history_id,
            next_page_token=next_page_token,
        )


        list_history_response.additional_properties = d
        return list_history_response

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
