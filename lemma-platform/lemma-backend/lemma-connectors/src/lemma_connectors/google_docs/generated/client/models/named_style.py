from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.named_style_named_style_type import NamedStyleNamedStyleType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.paragraph_style import ParagraphStyle
  from ..models.text_style import TextStyle





T = TypeVar("T", bound="NamedStyle")



@_attrs_define
class NamedStyle:
    """ A named style. Paragraphs in the document can inherit their TextStyle and ParagraphStyle from this named style when
    they have the same named style type.

        Attributes:
            named_style_type (NamedStyleNamedStyleType | Unset): The type of this named style.
            paragraph_style (ParagraphStyle | Unset): Styles that apply to a whole paragraph. Inherited paragraph styles are
                represented as unset fields in this message. A paragraph style's parent depends on where the paragraph style is
                defined: * The ParagraphStyle on a Paragraph inherits from the paragraph's corresponding named style type. * The
                ParagraphStyle on a named style inherits from the normal text named style. * The ParagraphStyle of the normal
                text named style inherits from the default paragraph style in the Docs editor. * The ParagraphStyle on a
                Paragraph element that's contained in a table may inherit its paragraph style from the table style. If the
                paragraph style does not inherit from a parent, unsetting fields will revert the style to a value matching the
                defaults in the Docs editor.
            text_style (TextStyle | Unset): Represents the styling that can be applied to text. Inherited text styles are
                represented as unset fields in this message. A text style's parent depends on where the text style is defined: *
                The TextStyle of text in a Paragraph inherits from the paragraph's corresponding named style type. * The
                TextStyle on a named style inherits from the normal text named style. * The TextStyle of the normal text named
                style inherits from the default text style in the Docs editor. * The TextStyle on a Paragraph element that's
                contained in a table may inherit its text style from the table style. If the text style does not inherit from a
                parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.
     """

    named_style_type: NamedStyleNamedStyleType | Unset = UNSET
    paragraph_style: ParagraphStyle | Unset = UNSET
    text_style: TextStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.paragraph_style import ParagraphStyle
        from ..models.text_style import TextStyle
        named_style_type: str | Unset = UNSET
        if not isinstance(self.named_style_type, Unset):
            named_style_type = self.named_style_type.value


        paragraph_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paragraph_style, Unset):
            paragraph_style = self.paragraph_style.to_dict()

        text_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style, Unset):
            text_style = self.text_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if named_style_type is not UNSET:
            field_dict["namedStyleType"] = named_style_type
        if paragraph_style is not UNSET:
            field_dict["paragraphStyle"] = paragraph_style
        if text_style is not UNSET:
            field_dict["textStyle"] = text_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paragraph_style import ParagraphStyle
        from ..models.text_style import TextStyle
        d = dict(src_dict)
        _named_style_type = d.pop("namedStyleType", UNSET)
        named_style_type: NamedStyleNamedStyleType | Unset
        if isinstance(_named_style_type,  Unset):
            named_style_type = UNSET
        else:
            named_style_type = NamedStyleNamedStyleType(_named_style_type)




        _paragraph_style = d.pop("paragraphStyle", UNSET)
        paragraph_style: ParagraphStyle | Unset
        if isinstance(_paragraph_style,  Unset):
            paragraph_style = UNSET
        else:
            paragraph_style = ParagraphStyle.from_dict(_paragraph_style)




        _text_style = d.pop("textStyle", UNSET)
        text_style: TextStyle | Unset
        if isinstance(_text_style,  Unset):
            text_style = UNSET
        else:
            text_style = TextStyle.from_dict(_text_style)




        named_style = cls(
            named_style_type=named_style_type,
            paragraph_style=paragraph_style,
            text_style=text_style,
        )


        named_style.additional_properties = d
        return named_style

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
