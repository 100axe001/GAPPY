from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.section_style import SectionStyle





T = TypeVar("T", bound="SectionBreak")



@_attrs_define
class SectionBreak:
    """ A StructuralElement representing a section break. A section is a range of content that has the same SectionStyle. A
    section break represents the start of a new section, and the section style applies to the section after the section
    break. The document body always begins with a section break.

        Attributes:
            section_style (SectionStyle | Unset): The styling that applies to a section.
            suggested_deletion_ids (list[str] | Unset): The suggested deletion IDs. If empty, then there are no suggested
                deletions of this content.
            suggested_insertion_ids (list[str] | Unset): The suggested insertion IDs. A SectionBreak may have multiple
                insertion IDs if it's a nested suggested change. If empty, then this is not a suggested insertion.
     """

    section_style: SectionStyle | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_insertion_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.section_style import SectionStyle
        section_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.section_style, Unset):
            section_style = self.section_style.to_dict()

        suggested_deletion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_deletion_ids, Unset):
            suggested_deletion_ids = self.suggested_deletion_ids



        suggested_insertion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_insertion_ids, Unset):
            suggested_insertion_ids = self.suggested_insertion_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if section_style is not UNSET:
            field_dict["sectionStyle"] = section_style
        if suggested_deletion_ids is not UNSET:
            field_dict["suggestedDeletionIds"] = suggested_deletion_ids
        if suggested_insertion_ids is not UNSET:
            field_dict["suggestedInsertionIds"] = suggested_insertion_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.section_style import SectionStyle
        d = dict(src_dict)
        _section_style = d.pop("sectionStyle", UNSET)
        section_style: SectionStyle | Unset
        if isinstance(_section_style,  Unset):
            section_style = UNSET
        else:
            section_style = SectionStyle.from_dict(_section_style)




        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        suggested_insertion_ids = cast(list[str], d.pop("suggestedInsertionIds", UNSET))


        section_break = cls(
            section_style=section_style,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_insertion_ids=suggested_insertion_ids,
        )


        section_break.additional_properties = d
        return section_break

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
