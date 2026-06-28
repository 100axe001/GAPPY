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
  from ..models.write_control import WriteControl





T = TypeVar("T", bound="BatchUpdateDocumentResponse")



@_attrs_define
class BatchUpdateDocumentResponse:
    """ Response message from a BatchUpdateDocument request.

        Attributes:
            document_id (str | Unset): The ID of the document to which the updates were applied to.
            replies (list[Response] | Unset): The reply of the updates. This maps 1:1 with the updates, although replies to
                some requests may be empty.
            write_control (WriteControl | Unset): Provides control over how write requests are executed.
     """

    document_id: str | Unset = UNSET
    replies: list[Response] | Unset = UNSET
    write_control: WriteControl | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.response import Response
        from ..models.write_control import WriteControl
        document_id = self.document_id

        replies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replies, Unset):
            replies = []
            for replies_item_data in self.replies:
                replies_item = replies_item_data.to_dict()
                replies.append(replies_item)



        write_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.write_control, Unset):
            write_control = self.write_control.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if replies is not UNSET:
            field_dict["replies"] = replies
        if write_control is not UNSET:
            field_dict["writeControl"] = write_control

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response import Response
        from ..models.write_control import WriteControl
        d = dict(src_dict)
        document_id = d.pop("documentId", UNSET)

        _replies = d.pop("replies", UNSET)
        replies: list[Response] | Unset = UNSET
        if _replies is not UNSET:
            replies = []
            for replies_item_data in _replies:
                replies_item = Response.from_dict(replies_item_data)



                replies.append(replies_item)


        _write_control = d.pop("writeControl", UNSET)
        write_control: WriteControl | Unset
        if isinstance(_write_control,  Unset):
            write_control = UNSET
        else:
            write_control = WriteControl.from_dict(_write_control)




        batch_update_document_response = cls(
            document_id=document_id,
            replies=replies,
            write_control=write_control,
        )


        batch_update_document_response.additional_properties = d
        return batch_update_document_response

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
