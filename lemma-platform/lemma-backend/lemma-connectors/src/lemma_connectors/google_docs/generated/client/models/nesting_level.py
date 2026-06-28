from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.nesting_level_bullet_alignment import NestingLevelBulletAlignment
from ..models.nesting_level_glyph_type import NestingLevelGlyphType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension
  from ..models.text_style import TextStyle





T = TypeVar("T", bound="NestingLevel")



@_attrs_define
class NestingLevel:
    """ Contains properties describing the look and feel of a list bullet at a given level of nesting.

        Attributes:
            bullet_alignment (NestingLevelBulletAlignment | Unset): The alignment of the bullet within the space allotted
                for rendering the bullet.
            glyph_format (str | Unset): The format string used by bullets at this level of nesting. The glyph format
                contains one or more placeholders, and these placeholders are replaced with the appropriate values depending on
                the glyph_type or glyph_symbol. The placeholders follow the pattern `%[nesting_level]`. Furthermore,
                placeholders can have prefixes and suffixes. Thus, the glyph format follows the pattern `%[nesting_level]`. Note
                that the prefix and suffix are optional and can be arbitrary strings. For example, the glyph format `%0.`
                indicates that the rendered glyph will replace the placeholder with the corresponding glyph for nesting level 0
                followed by a period as the suffix. So a list with a glyph type of UPPER_ALPHA and glyph format `%0.` at nesting
                level 0 will result in a list with rendered glyphs `A.` `B.` `C.` The glyph format can contain placeholders for
                the current nesting level as well as placeholders for parent nesting levels. For example, a list can have a
                glyph format of `%0.` at nesting level 0 and a glyph format of `%0.%1.` at nesting level 1. Assuming both
                nesting levels have DECIMAL glyph types, this would result in a list with rendered glyphs `1.` `2.` ` 2.1.` `
                2.2.` `3.` For nesting levels that are ordered, the string that replaces a placeholder in the glyph format for a
                particular paragraph depends on the paragraph's order within the list.
            glyph_symbol (str | Unset): A custom glyph symbol used by bullets when paragraphs at this level of nesting are
                unordered. The glyph symbol replaces placeholders within the glyph_format. For example, if the glyph_symbol is
                the solid circle corresponding to Unicode U+25cf code point and the glyph_format is `%0`, the rendered glyph
                would be the solid circle.
            glyph_type (NestingLevelGlyphType | Unset): The type of glyph used by bullets when paragraphs at this level of
                nesting are ordered. The glyph type determines the type of glyph used to replace placeholders within the
                glyph_format when paragraphs at this level of nesting are ordered. For example, if the nesting level is 0, the
                glyph_format is `%0.` and the glyph type is DECIMAL, then the rendered glyph would replace the placeholder `%0`
                in the glyph format with a number corresponding to list item's order within the list.
            indent_first_line (Dimension | Unset): A magnitude in a single direction in the specified units.
            indent_start (Dimension | Unset): A magnitude in a single direction in the specified units.
            start_number (int | Unset): The number of the first list item at this nesting level. A value of 0 is treated as
                a value of 1 for lettered lists and Roman numeral lists. For values of both 0 and 1, lettered and Roman numeral
                lists will begin at `a` and `i` respectively. This value is ignored for nesting levels with unordered glyphs.
            text_style (TextStyle | Unset): Represents the styling that can be applied to text. Inherited text styles are
                represented as unset fields in this message. A text style's parent depends on where the text style is defined: *
                The TextStyle of text in a Paragraph inherits from the paragraph's corresponding named style type. * The
                TextStyle on a named style inherits from the normal text named style. * The TextStyle of the normal text named
                style inherits from the default text style in the Docs editor. * The TextStyle on a Paragraph element that's
                contained in a table may inherit its text style from the table style. If the text style does not inherit from a
                parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.
     """

    bullet_alignment: NestingLevelBulletAlignment | Unset = UNSET
    glyph_format: str | Unset = UNSET
    glyph_symbol: str | Unset = UNSET
    glyph_type: NestingLevelGlyphType | Unset = UNSET
    indent_first_line: Dimension | Unset = UNSET
    indent_start: Dimension | Unset = UNSET
    start_number: int | Unset = UNSET
    text_style: TextStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        from ..models.text_style import TextStyle
        bullet_alignment: str | Unset = UNSET
        if not isinstance(self.bullet_alignment, Unset):
            bullet_alignment = self.bullet_alignment.value


        glyph_format = self.glyph_format

        glyph_symbol = self.glyph_symbol

        glyph_type: str | Unset = UNSET
        if not isinstance(self.glyph_type, Unset):
            glyph_type = self.glyph_type.value


        indent_first_line: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indent_first_line, Unset):
            indent_first_line = self.indent_first_line.to_dict()

        indent_start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indent_start, Unset):
            indent_start = self.indent_start.to_dict()

        start_number = self.start_number

        text_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style, Unset):
            text_style = self.text_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bullet_alignment is not UNSET:
            field_dict["bulletAlignment"] = bullet_alignment
        if glyph_format is not UNSET:
            field_dict["glyphFormat"] = glyph_format
        if glyph_symbol is not UNSET:
            field_dict["glyphSymbol"] = glyph_symbol
        if glyph_type is not UNSET:
            field_dict["glyphType"] = glyph_type
        if indent_first_line is not UNSET:
            field_dict["indentFirstLine"] = indent_first_line
        if indent_start is not UNSET:
            field_dict["indentStart"] = indent_start
        if start_number is not UNSET:
            field_dict["startNumber"] = start_number
        if text_style is not UNSET:
            field_dict["textStyle"] = text_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        from ..models.text_style import TextStyle
        d = dict(src_dict)
        _bullet_alignment = d.pop("bulletAlignment", UNSET)
        bullet_alignment: NestingLevelBulletAlignment | Unset
        if isinstance(_bullet_alignment,  Unset):
            bullet_alignment = UNSET
        else:
            bullet_alignment = NestingLevelBulletAlignment(_bullet_alignment)




        glyph_format = d.pop("glyphFormat", UNSET)

        glyph_symbol = d.pop("glyphSymbol", UNSET)

        _glyph_type = d.pop("glyphType", UNSET)
        glyph_type: NestingLevelGlyphType | Unset
        if isinstance(_glyph_type,  Unset):
            glyph_type = UNSET
        else:
            glyph_type = NestingLevelGlyphType(_glyph_type)




        _indent_first_line = d.pop("indentFirstLine", UNSET)
        indent_first_line: Dimension | Unset
        if isinstance(_indent_first_line,  Unset):
            indent_first_line = UNSET
        else:
            indent_first_line = Dimension.from_dict(_indent_first_line)




        _indent_start = d.pop("indentStart", UNSET)
        indent_start: Dimension | Unset
        if isinstance(_indent_start,  Unset):
            indent_start = UNSET
        else:
            indent_start = Dimension.from_dict(_indent_start)




        start_number = d.pop("startNumber", UNSET)

        _text_style = d.pop("textStyle", UNSET)
        text_style: TextStyle | Unset
        if isinstance(_text_style,  Unset):
            text_style = UNSET
        else:
            text_style = TextStyle.from_dict(_text_style)




        nesting_level = cls(
            bullet_alignment=bullet_alignment,
            glyph_format=glyph_format,
            glyph_symbol=glyph_symbol,
            glyph_type=glyph_type,
            indent_first_line=indent_first_line,
            indent_start=indent_start,
            start_number=start_number,
            text_style=text_style,
        )


        nesting_level.additional_properties = d
        return nesting_level

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
