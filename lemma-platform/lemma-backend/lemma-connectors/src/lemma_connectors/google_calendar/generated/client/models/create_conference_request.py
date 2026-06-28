from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conference_request_status import ConferenceRequestStatus
  from ..models.conference_solution_key import ConferenceSolutionKey





T = TypeVar("T", bound="CreateConferenceRequest")



@_attrs_define
class CreateConferenceRequest:
    """ 
        Attributes:
            conference_solution_key (ConferenceSolutionKey | Unset):
            request_id (str | Unset): The client-generated unique ID for this request.
                Clients should regenerate this ID for every new request. If an ID provided is the same as for the previous
                request, the request is ignored.
            status (ConferenceRequestStatus | Unset):
     """

    conference_solution_key: ConferenceSolutionKey | Unset = UNSET
    request_id: str | Unset = UNSET
    status: ConferenceRequestStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conference_request_status import ConferenceRequestStatus
        from ..models.conference_solution_key import ConferenceSolutionKey
        conference_solution_key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conference_solution_key, Unset):
            conference_solution_key = self.conference_solution_key.to_dict()

        request_id = self.request_id

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if conference_solution_key is not UNSET:
            field_dict["conferenceSolutionKey"] = conference_solution_key
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conference_request_status import ConferenceRequestStatus
        from ..models.conference_solution_key import ConferenceSolutionKey
        d = dict(src_dict)
        _conference_solution_key = d.pop("conferenceSolutionKey", UNSET)
        conference_solution_key: ConferenceSolutionKey | Unset
        if isinstance(_conference_solution_key,  Unset):
            conference_solution_key = UNSET
        else:
            conference_solution_key = ConferenceSolutionKey.from_dict(_conference_solution_key)




        request_id = d.pop("requestId", UNSET)

        _status = d.pop("status", UNSET)
        status: ConferenceRequestStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ConferenceRequestStatus.from_dict(_status)




        create_conference_request = cls(
            conference_solution_key=conference_solution_key,
            request_id=request_id,
            status=status,
        )


        create_conference_request.additional_properties = d
        return create_conference_request

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
