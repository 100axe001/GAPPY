from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_footer_request_type import CreateFooterRequestType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.location import Location





T = TypeVar("T", bound="CreateFooterRequest")



@_attrs_define
class CreateFooterRequest:
    """ Creates a Footer. The new footer is applied to the SectionStyle at the location of the SectionBreak if specified,
    otherwise it is applied to the DocumentStyle. If a footer of the specified type already exists, a 400 bad request
    error is returned.

        Attributes:
            section_break_location (Location | Unset): A particular location in the document.
            type_ (CreateFooterRequestType | Unset): The type of footer to create.
     """

    section_break_location: Location | Unset = UNSET
    type_: CreateFooterRequestType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.location import Location
        section_break_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.section_break_location, Unset):
            section_break_location = self.section_break_location.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if section_break_location is not UNSET:
            field_dict["sectionBreakLocation"] = section_break_location
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location import Location
        d = dict(src_dict)
        _section_break_location = d.pop("sectionBreakLocation", UNSET)
        section_break_location: Location | Unset
        if isinstance(_section_break_location,  Unset):
            section_break_location = UNSET
        else:
            section_break_location = Location.from_dict(_section_break_location)




        _type_ = d.pop("type", UNSET)
        type_: CreateFooterRequestType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = CreateFooterRequestType(_type_)




        create_footer_request = cls(
            section_break_location=section_break_location,
            type_=type_,
        )


        create_footer_request.additional_properties = d
        return create_footer_request

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
