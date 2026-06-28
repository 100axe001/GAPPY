from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.paragraph_style import ParagraphStyle
  from ..models.range_ import Range





T = TypeVar("T", bound="UpdateParagraphStyleRequest")



@_attrs_define
class UpdateParagraphStyleRequest:
    """ Update the styling of all paragraphs that overlap with the given range.

        Attributes:
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `paragraph_style` is implied and should not be specified. A single `"*"` can be used as short-hand for listing
                every field. For example, to update the paragraph style's alignment property, set `fields` to `"alignment"`. To
                reset a property to its default value, include its field name in the field mask but leave the field itself
                unset.
            paragraph_style (ParagraphStyle | Unset): Styles that apply to a whole paragraph. Inherited paragraph styles are
                represented as unset fields in this message. A paragraph style's parent depends on where the paragraph style is
                defined: * The ParagraphStyle on a Paragraph inherits from the paragraph's corresponding named style type. * The
                ParagraphStyle on a named style inherits from the normal text named style. * The ParagraphStyle of the normal
                text named style inherits from the default paragraph style in the Docs editor. * The ParagraphStyle on a
                Paragraph element that's contained in a table may inherit its paragraph style from the table style. If the
                paragraph style does not inherit from a parent, unsetting fields will revert the style to a value matching the
                defaults in the Docs editor.
            range_ (Range | Unset): Specifies a contiguous range of text.
     """

    fields: str | Unset = UNSET
    paragraph_style: ParagraphStyle | Unset = UNSET
    range_: Range | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.paragraph_style import ParagraphStyle
        from ..models.range_ import Range
        fields = self.fields

        paragraph_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paragraph_style, Unset):
            paragraph_style = self.paragraph_style.to_dict()

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if paragraph_style is not UNSET:
            field_dict["paragraphStyle"] = paragraph_style
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paragraph_style import ParagraphStyle
        from ..models.range_ import Range
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _paragraph_style = d.pop("paragraphStyle", UNSET)
        paragraph_style: ParagraphStyle | Unset
        if isinstance(_paragraph_style,  Unset):
            paragraph_style = UNSET
        else:
            paragraph_style = ParagraphStyle.from_dict(_paragraph_style)




        _range_ = d.pop("range", UNSET)
        range_: Range | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)




        update_paragraph_style_request = cls(
            fields=fields,
            paragraph_style=paragraph_style,
            range_=range_,
        )


        update_paragraph_style_request.additional_properties = d
        return update_paragraph_style_request

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
