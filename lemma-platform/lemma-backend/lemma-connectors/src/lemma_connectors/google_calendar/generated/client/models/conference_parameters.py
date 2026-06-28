from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conference_parameters_add_on_parameters import ConferenceParametersAddOnParameters





T = TypeVar("T", bound="ConferenceParameters")



@_attrs_define
class ConferenceParameters:
    """ 
        Attributes:
            add_on_parameters (ConferenceParametersAddOnParameters | Unset):
     """

    add_on_parameters: ConferenceParametersAddOnParameters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conference_parameters_add_on_parameters import ConferenceParametersAddOnParameters
        add_on_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_on_parameters, Unset):
            add_on_parameters = self.add_on_parameters.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if add_on_parameters is not UNSET:
            field_dict["addOnParameters"] = add_on_parameters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conference_parameters_add_on_parameters import ConferenceParametersAddOnParameters
        d = dict(src_dict)
        _add_on_parameters = d.pop("addOnParameters", UNSET)
        add_on_parameters: ConferenceParametersAddOnParameters | Unset
        if isinstance(_add_on_parameters,  Unset):
            add_on_parameters = UNSET
        else:
            add_on_parameters = ConferenceParametersAddOnParameters.from_dict(_add_on_parameters)




        conference_parameters = cls(
            add_on_parameters=add_on_parameters,
        )


        conference_parameters.additional_properties = d
        return conference_parameters

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
