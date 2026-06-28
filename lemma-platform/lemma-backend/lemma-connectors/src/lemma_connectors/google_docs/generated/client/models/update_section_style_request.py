from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.range_ import Range
  from ..models.section_style import SectionStyle





T = TypeVar("T", bound="UpdateSectionStyleRequest")



@_attrs_define
class UpdateSectionStyleRequest:
    """ Updates the SectionStyle.

        Attributes:
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `section_style` is implied and must not be specified. A single `"*"` can be used as short-hand for listing every
                field. For example to update the left margin, set `fields` to `"margin_left"`.
            range_ (Range | Unset): Specifies a contiguous range of text.
            section_style (SectionStyle | Unset): The styling that applies to a section.
     """

    fields: str | Unset = UNSET
    range_: Range | Unset = UNSET
    section_style: SectionStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.range_ import Range
        from ..models.section_style import SectionStyle
        fields = self.fields

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        section_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.section_style, Unset):
            section_style = self.section_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if range_ is not UNSET:
            field_dict["range"] = range_
        if section_style is not UNSET:
            field_dict["sectionStyle"] = section_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.range_ import Range
        from ..models.section_style import SectionStyle
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: Range | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)




        _section_style = d.pop("sectionStyle", UNSET)
        section_style: SectionStyle | Unset
        if isinstance(_section_style,  Unset):
            section_style = UNSET
        else:
            section_style = SectionStyle.from_dict(_section_style)




        update_section_style_request = cls(
            fields=fields,
            range_=range_,
            section_style=section_style,
        )


        update_section_style_request.additional_properties = d
        return update_section_style_request

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
