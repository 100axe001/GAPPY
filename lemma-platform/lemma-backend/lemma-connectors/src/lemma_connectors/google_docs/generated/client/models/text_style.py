from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_style_baseline_offset import TextStyleBaselineOffset
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension
  from ..models.link import Link
  from ..models.optional_color import OptionalColor
  from ..models.weighted_font_family import WeightedFontFamily





T = TypeVar("T", bound="TextStyle")



@_attrs_define
class TextStyle:
    """ Represents the styling that can be applied to text. Inherited text styles are represented as unset fields in this
    message. A text style's parent depends on where the text style is defined: * The TextStyle of text in a Paragraph
    inherits from the paragraph's corresponding named style type. * The TextStyle on a named style inherits from the
    normal text named style. * The TextStyle of the normal text named style inherits from the default text style in the
    Docs editor. * The TextStyle on a Paragraph element that's contained in a table may inherit its text style from the
    table style. If the text style does not inherit from a parent, unsetting fields will revert the style to a value
    matching the defaults in the Docs editor.

        Attributes:
            background_color (OptionalColor | Unset): A color that can either be fully opaque or fully transparent.
            baseline_offset (TextStyleBaselineOffset | Unset): The text's vertical offset from its normal position. Text
                with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically rendered in a smaller font size, computed
                based on the `font_size` field. Changes in this field don't affect the `font_size`.
            bold (bool | Unset): Whether or not the text is rendered as bold.
            font_size (Dimension | Unset): A magnitude in a single direction in the specified units.
            foreground_color (OptionalColor | Unset): A color that can either be fully opaque or fully transparent.
            italic (bool | Unset): Whether or not the text is italicized.
            link (Link | Unset): A reference to another portion of a document or an external URL resource.
            small_caps (bool | Unset): Whether or not the text is in small capital letters.
            strikethrough (bool | Unset): Whether or not the text is struck through.
            underline (bool | Unset): Whether or not the text is underlined.
            weighted_font_family (WeightedFontFamily | Unset): Represents a font family and weight of text.
     """

    background_color: OptionalColor | Unset = UNSET
    baseline_offset: TextStyleBaselineOffset | Unset = UNSET
    bold: bool | Unset = UNSET
    font_size: Dimension | Unset = UNSET
    foreground_color: OptionalColor | Unset = UNSET
    italic: bool | Unset = UNSET
    link: Link | Unset = UNSET
    small_caps: bool | Unset = UNSET
    strikethrough: bool | Unset = UNSET
    underline: bool | Unset = UNSET
    weighted_font_family: WeightedFontFamily | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        from ..models.link import Link
        from ..models.optional_color import OptionalColor
        from ..models.weighted_font_family import WeightedFontFamily
        background_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.to_dict()

        baseline_offset: str | Unset = UNSET
        if not isinstance(self.baseline_offset, Unset):
            baseline_offset = self.baseline_offset.value


        bold = self.bold

        font_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.font_size, Unset):
            font_size = self.font_size.to_dict()

        foreground_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.foreground_color, Unset):
            foreground_color = self.foreground_color.to_dict()

        italic = self.italic

        link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        small_caps = self.small_caps

        strikethrough = self.strikethrough

        underline = self.underline

        weighted_font_family: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weighted_font_family, Unset):
            weighted_font_family = self.weighted_font_family.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if baseline_offset is not UNSET:
            field_dict["baselineOffset"] = baseline_offset
        if bold is not UNSET:
            field_dict["bold"] = bold
        if font_size is not UNSET:
            field_dict["fontSize"] = font_size
        if foreground_color is not UNSET:
            field_dict["foregroundColor"] = foreground_color
        if italic is not UNSET:
            field_dict["italic"] = italic
        if link is not UNSET:
            field_dict["link"] = link
        if small_caps is not UNSET:
            field_dict["smallCaps"] = small_caps
        if strikethrough is not UNSET:
            field_dict["strikethrough"] = strikethrough
        if underline is not UNSET:
            field_dict["underline"] = underline
        if weighted_font_family is not UNSET:
            field_dict["weightedFontFamily"] = weighted_font_family

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        from ..models.link import Link
        from ..models.optional_color import OptionalColor
        from ..models.weighted_font_family import WeightedFontFamily
        d = dict(src_dict)
        _background_color = d.pop("backgroundColor", UNSET)
        background_color: OptionalColor | Unset
        if isinstance(_background_color,  Unset):
            background_color = UNSET
        else:
            background_color = OptionalColor.from_dict(_background_color)




        _baseline_offset = d.pop("baselineOffset", UNSET)
        baseline_offset: TextStyleBaselineOffset | Unset
        if isinstance(_baseline_offset,  Unset):
            baseline_offset = UNSET
        else:
            baseline_offset = TextStyleBaselineOffset(_baseline_offset)




        bold = d.pop("bold", UNSET)

        _font_size = d.pop("fontSize", UNSET)
        font_size: Dimension | Unset
        if isinstance(_font_size,  Unset):
            font_size = UNSET
        else:
            font_size = Dimension.from_dict(_font_size)




        _foreground_color = d.pop("foregroundColor", UNSET)
        foreground_color: OptionalColor | Unset
        if isinstance(_foreground_color,  Unset):
            foreground_color = UNSET
        else:
            foreground_color = OptionalColor.from_dict(_foreground_color)




        italic = d.pop("italic", UNSET)

        _link = d.pop("link", UNSET)
        link: Link | Unset
        if isinstance(_link,  Unset):
            link = UNSET
        else:
            link = Link.from_dict(_link)




        small_caps = d.pop("smallCaps", UNSET)

        strikethrough = d.pop("strikethrough", UNSET)

        underline = d.pop("underline", UNSET)

        _weighted_font_family = d.pop("weightedFontFamily", UNSET)
        weighted_font_family: WeightedFontFamily | Unset
        if isinstance(_weighted_font_family,  Unset):
            weighted_font_family = UNSET
        else:
            weighted_font_family = WeightedFontFamily.from_dict(_weighted_font_family)




        text_style = cls(
            background_color=background_color,
            baseline_offset=baseline_offset,
            bold=bold,
            font_size=font_size,
            foreground_color=foreground_color,
            italic=italic,
            link=link,
            small_caps=small_caps,
            strikethrough=strikethrough,
            underline=underline,
            weighted_font_family=weighted_font_family,
        )


        text_style.additional_properties = d
        return text_style

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
