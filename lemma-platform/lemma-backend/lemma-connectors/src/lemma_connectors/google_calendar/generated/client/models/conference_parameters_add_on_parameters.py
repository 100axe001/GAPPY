from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conference_parameters_add_on_parameters_parameters import ConferenceParametersAddOnParametersParameters





T = TypeVar("T", bound="ConferenceParametersAddOnParameters")



@_attrs_define
class ConferenceParametersAddOnParameters:
    """ 
        Attributes:
            parameters (ConferenceParametersAddOnParametersParameters | Unset):
     """

    parameters: ConferenceParametersAddOnParametersParameters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conference_parameters_add_on_parameters_parameters import ConferenceParametersAddOnParametersParameters
        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conference_parameters_add_on_parameters_parameters import ConferenceParametersAddOnParametersParameters
        d = dict(src_dict)
        _parameters = d.pop("parameters", UNSET)
        parameters: ConferenceParametersAddOnParametersParameters | Unset
        if isinstance(_parameters,  Unset):
            parameters = UNSET
        else:
            parameters = ConferenceParametersAddOnParametersParameters.from_dict(_parameters)




        conference_parameters_add_on_parameters = cls(
            parameters=parameters,
        )


        conference_parameters_add_on_parameters.additional_properties = d
        return conference_parameters_add_on_parameters

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
