from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.request import Request
  from ..models.write_control import WriteControl





T = TypeVar("T", bound="BatchUpdateDocumentRequest")



@_attrs_define
class BatchUpdateDocumentRequest:
    """ Request message for BatchUpdateDocument.

        Attributes:
            requests (list[Request] | Unset): A list of updates to apply to the document.
            write_control (WriteControl | Unset): Provides control over how write requests are executed.
     """

    requests: list[Request] | Unset = UNSET
    write_control: WriteControl | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.request import Request
        from ..models.write_control import WriteControl
        requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requests, Unset):
            requests = []
            for requests_item_data in self.requests:
                requests_item = requests_item_data.to_dict()
                requests.append(requests_item)



        write_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.write_control, Unset):
            write_control = self.write_control.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if requests is not UNSET:
            field_dict["requests"] = requests
        if write_control is not UNSET:
            field_dict["writeControl"] = write_control

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request import Request
        from ..models.write_control import WriteControl
        d = dict(src_dict)
        _requests = d.pop("requests", UNSET)
        requests: list[Request] | Unset = UNSET
        if _requests is not UNSET:
            requests = []
            for requests_item_data in _requests:
                requests_item = Request.from_dict(requests_item_data)



                requests.append(requests_item)


        _write_control = d.pop("writeControl", UNSET)
        write_control: WriteControl | Unset
        if isinstance(_write_control,  Unset):
            write_control = UNSET
        else:
            write_control = WriteControl.from_dict(_write_control)




        batch_update_document_request = cls(
            requests=requests,
            write_control=write_control,
        )


        batch_update_document_request.additional_properties = d
        return batch_update_document_request

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
