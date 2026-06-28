from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.response import Response
  from ..models.spreadsheet import Spreadsheet





T = TypeVar("T", bound="BatchUpdateSpreadsheetResponse")



@_attrs_define
class BatchUpdateSpreadsheetResponse:
    """ The reply for batch updating a spreadsheet.

        Attributes:
            replies (list[Response] | Unset): The reply of the updates. This maps 1:1 with the updates, although replies to
                some requests may be empty.
            spreadsheet_id (str | Unset): The spreadsheet the updates were applied to.
            updated_spreadsheet (Spreadsheet | Unset): Resource that represents a spreadsheet.
     """

    replies: list[Response] | Unset = UNSET
    spreadsheet_id: str | Unset = UNSET
    updated_spreadsheet: Spreadsheet | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.response import Response
        from ..models.spreadsheet import Spreadsheet
        replies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replies, Unset):
            replies = []
            for replies_item_data in self.replies:
                replies_item = replies_item_data.to_dict()
                replies.append(replies_item)



        spreadsheet_id = self.spreadsheet_id

        updated_spreadsheet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_spreadsheet, Unset):
            updated_spreadsheet = self.updated_spreadsheet.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if replies is not UNSET:
            field_dict["replies"] = replies
        if spreadsheet_id is not UNSET:
            field_dict["spreadsheetId"] = spreadsheet_id
        if updated_spreadsheet is not UNSET:
            field_dict["updatedSpreadsheet"] = updated_spreadsheet

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response import Response
        from ..models.spreadsheet import Spreadsheet
        d = dict(src_dict)
        _replies = d.pop("replies", UNSET)
        replies: list[Response] | Unset = UNSET
        if _replies is not UNSET:
            replies = []
            for replies_item_data in _replies:
                replies_item = Response.from_dict(replies_item_data)



                replies.append(replies_item)


        spreadsheet_id = d.pop("spreadsheetId", UNSET)

        _updated_spreadsheet = d.pop("updatedSpreadsheet", UNSET)
        updated_spreadsheet: Spreadsheet | Unset
        if isinstance(_updated_spreadsheet,  Unset):
            updated_spreadsheet = UNSET
        else:
            updated_spreadsheet = Spreadsheet.from_dict(_updated_spreadsheet)




        batch_update_spreadsheet_response = cls(
            replies=replies,
            spreadsheet_id=spreadsheet_id,
            updated_spreadsheet=updated_spreadsheet,
        )


        batch_update_spreadsheet_response.additional_properties = d
        return batch_update_spreadsheet_response

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
