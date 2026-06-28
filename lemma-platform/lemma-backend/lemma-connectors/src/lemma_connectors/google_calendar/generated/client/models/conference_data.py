from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conference_parameters import ConferenceParameters
  from ..models.conference_solution import ConferenceSolution
  from ..models.create_conference_request import CreateConferenceRequest
  from ..models.entry_point import EntryPoint





T = TypeVar("T", bound="ConferenceData")



@_attrs_define
class ConferenceData:
    """ 
        Attributes:
            conference_id (str | Unset): The ID of the conference.
                Can be used by developers to keep track of conferences, should not be displayed to users.
                The ID value is formed differently for each conference solution type:
                - eventHangout: ID is not set. (This conference type is deprecated.)
                - eventNamedHangout: ID is the name of the Hangout. (This conference type is deprecated.)
                - hangoutsMeet: ID is the 10-letter meeting code, for example aaa-bbbb-ccc.
                - addOn: ID is defined by the third-party provider.  Optional.
            conference_solution (ConferenceSolution | Unset):
            create_request (CreateConferenceRequest | Unset):
            entry_points (list[EntryPoint] | Unset): Information about individual conference entry points, such as URLs or
                phone numbers.
                All of them must belong to the same conference.
                Either conferenceSolution and at least one entryPoint, or createRequest is required.
            notes (str | Unset): Additional notes (such as instructions from the domain administrator, legal notices) to
                display to the user. Can contain HTML. The maximum length is 2048 characters. Optional.
            parameters (ConferenceParameters | Unset):
            signature (str | Unset): The signature of the conference data.
                Generated on server side.
                Unset for a conference with a failed create request.
                Optional for a conference with a pending create request.
     """

    conference_id: str | Unset = UNSET
    conference_solution: ConferenceSolution | Unset = UNSET
    create_request: CreateConferenceRequest | Unset = UNSET
    entry_points: list[EntryPoint] | Unset = UNSET
    notes: str | Unset = UNSET
    parameters: ConferenceParameters | Unset = UNSET
    signature: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conference_parameters import ConferenceParameters
        from ..models.conference_solution import ConferenceSolution
        from ..models.create_conference_request import CreateConferenceRequest
        from ..models.entry_point import EntryPoint
        conference_id = self.conference_id

        conference_solution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conference_solution, Unset):
            conference_solution = self.conference_solution.to_dict()

        create_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_request, Unset):
            create_request = self.create_request.to_dict()

        entry_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entry_points, Unset):
            entry_points = []
            for entry_points_item_data in self.entry_points:
                entry_points_item = entry_points_item_data.to_dict()
                entry_points.append(entry_points_item)



        notes = self.notes

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        signature = self.signature


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if conference_solution is not UNSET:
            field_dict["conferenceSolution"] = conference_solution
        if create_request is not UNSET:
            field_dict["createRequest"] = create_request
        if entry_points is not UNSET:
            field_dict["entryPoints"] = entry_points
        if notes is not UNSET:
            field_dict["notes"] = notes
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conference_parameters import ConferenceParameters
        from ..models.conference_solution import ConferenceSolution
        from ..models.create_conference_request import CreateConferenceRequest
        from ..models.entry_point import EntryPoint
        d = dict(src_dict)
        conference_id = d.pop("conferenceId", UNSET)

        _conference_solution = d.pop("conferenceSolution", UNSET)
        conference_solution: ConferenceSolution | Unset
        if isinstance(_conference_solution,  Unset):
            conference_solution = UNSET
        else:
            conference_solution = ConferenceSolution.from_dict(_conference_solution)




        _create_request = d.pop("createRequest", UNSET)
        create_request: CreateConferenceRequest | Unset
        if isinstance(_create_request,  Unset):
            create_request = UNSET
        else:
            create_request = CreateConferenceRequest.from_dict(_create_request)




        _entry_points = d.pop("entryPoints", UNSET)
        entry_points: list[EntryPoint] | Unset = UNSET
        if _entry_points is not UNSET:
            entry_points = []
            for entry_points_item_data in _entry_points:
                entry_points_item = EntryPoint.from_dict(entry_points_item_data)



                entry_points.append(entry_points_item)


        notes = d.pop("notes", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: ConferenceParameters | Unset
        if isinstance(_parameters,  Unset):
            parameters = UNSET
        else:
            parameters = ConferenceParameters.from_dict(_parameters)




        signature = d.pop("signature", UNSET)

        conference_data = cls(
            conference_id=conference_id,
            conference_solution=conference_solution,
            create_request=create_request,
            entry_points=entry_points,
            notes=notes,
            parameters=parameters,
            signature=signature,
        )


        conference_data.additional_properties = d
        return conference_data

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
