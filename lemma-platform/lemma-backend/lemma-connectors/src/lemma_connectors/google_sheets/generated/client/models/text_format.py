from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.link import Link





T = TypeVar("T", bound="TextFormat")



@_attrs_define
class TextFormat:
    """ The format of a run of text in a cell. Absent values indicate that the field isn't specified.

        Attributes:
            bold (bool | Unset): True if the text is bold.
            font_family (str | Unset): The font family.
            font_size (int | Unset): The size of the font.
            foreground_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed
                for simplicity of conversion to/from color representations in various languages over compactness. For example,
                the fields of this representation can be trivially provided to the constructor of `java.awt.Color` in Java; it
                can also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with just a
                little work, it can be easily formatted into a CSS `rgba()` string in JavaScript. This reference page doesn't
                carry information about the absolute color space that should be used to interpret the RGB value (e.g. sRGB,
                Adobe RGB, DCI-P3, BT.2020, etc.). By default, applications should assume the sRGB color space. When color
                equality needs to be decided, implementations, unless documented otherwise, treat two colors as equal if all
                their red, green, blue, and alpha values each differ by at most 1e-5. Example (Java): import
                com.google.type.Color; // ... public static java.awt.Color fromProto(Color protocolor) { float alpha =
                protocolor.hasAlpha() ? protocolor.getAlpha().getValue() : 1.0; return new java.awt.Color( protocolor.getRed(),
                protocolor.getGreen(), protocolor.getBlue(), alpha); } public static Color toProto(java.awt.Color color) { float
                red = (float) color.getRed(); float green = (float) color.getGreen(); float blue = (float) color.getBlue();
                float denominator = 255.0; Color.Builder resultBuilder = Color .newBuilder() .setRed(red / denominator)
                .setGreen(green / denominator) .setBlue(blue / denominator); int alpha = color.getAlpha(); if (alpha != 255) {
                result.setAlpha( FloatValue .newBuilder() .setValue(((float) alpha) / denominator) .build()); } return
                resultBuilder.build(); } // ... Example (iOS / Obj-C): // ... static UIColor* fromProto(Color* protocolor) {
                float red = [protocolor red]; float green = [protocolor green]; float blue = [protocolor blue]; FloatValue*
                alpha_wrapper = [protocolor alpha]; float alpha = 1.0; if (alpha_wrapper != nil) { alpha = [alpha_wrapper
                value]; } return [UIColor colorWithRed:red green:green blue:blue alpha:alpha]; } static Color* toProto(UIColor*
                color) { CGFloat red, green, blue, alpha; if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                return nil; } Color* result = [[Color alloc] init]; [result setRed:red]; [result setGreen:green]; [result
                setBlue:blue]; if (alpha <= 0.9999) { [result setAlpha:floatWrapperWithValue(alpha)]; } [result autorelease];
                return result; } // ... Example (JavaScript): // ... var protoToCssColor = function(rgb_color) { var redFrac =
                rgb_color.red || 0.0; var greenFrac = rgb_color.green || 0.0; var blueFrac = rgb_color.blue || 0.0; var red =
                Math.floor(redFrac * 255); var green = Math.floor(greenFrac * 255); var blue = Math.floor(blueFrac * 255); if
                (!('alpha' in rgb_color)) { return rgbToCssColor(red, green, blue); } var alphaFrac = rgb_color.alpha.value ||
                0.0; var rgbParams = [red, green, blue].join(','); return ['rgba(', rgbParams, ',', alphaFrac, ')'].join(''); };
                var rgbToCssColor = function(red, green, blue) { var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                var hexString = rgbNumber.toString(16); var missingZeros = 6 - hexString.length; var resultBuilder = ['#']; for
                (var i = 0; i < missingZeros; i++) { resultBuilder.push('0'); } resultBuilder.push(hexString); return
                resultBuilder.join(''); }; // ...
            foreground_color_style (ColorStyle | Unset): A color value.
            italic (bool | Unset): True if the text is italicized.
            link (Link | Unset): An external or local reference.
            strikethrough (bool | Unset): True if the text has a strikethrough.
            underline (bool | Unset): True if the text is underlined.
     """

    bold: bool | Unset = UNSET
    font_family: str | Unset = UNSET
    font_size: int | Unset = UNSET
    foreground_color: Color | Unset = UNSET
    foreground_color_style: ColorStyle | Unset = UNSET
    italic: bool | Unset = UNSET
    link: Link | Unset = UNSET
    strikethrough: bool | Unset = UNSET
    underline: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.link import Link
        bold = self.bold

        font_family = self.font_family

        font_size = self.font_size

        foreground_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.foreground_color, Unset):
            foreground_color = self.foreground_color.to_dict()

        foreground_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.foreground_color_style, Unset):
            foreground_color_style = self.foreground_color_style.to_dict()

        italic = self.italic

        link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        strikethrough = self.strikethrough

        underline = self.underline


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bold is not UNSET:
            field_dict["bold"] = bold
        if font_family is not UNSET:
            field_dict["fontFamily"] = font_family
        if font_size is not UNSET:
            field_dict["fontSize"] = font_size
        if foreground_color is not UNSET:
            field_dict["foregroundColor"] = foreground_color
        if foreground_color_style is not UNSET:
            field_dict["foregroundColorStyle"] = foreground_color_style
        if italic is not UNSET:
            field_dict["italic"] = italic
        if link is not UNSET:
            field_dict["link"] = link
        if strikethrough is not UNSET:
            field_dict["strikethrough"] = strikethrough
        if underline is not UNSET:
            field_dict["underline"] = underline

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.link import Link
        d = dict(src_dict)
        bold = d.pop("bold", UNSET)

        font_family = d.pop("fontFamily", UNSET)

        font_size = d.pop("fontSize", UNSET)

        _foreground_color = d.pop("foregroundColor", UNSET)
        foreground_color: Color | Unset
        if isinstance(_foreground_color,  Unset):
            foreground_color = UNSET
        else:
            foreground_color = Color.from_dict(_foreground_color)




        _foreground_color_style = d.pop("foregroundColorStyle", UNSET)
        foreground_color_style: ColorStyle | Unset
        if isinstance(_foreground_color_style,  Unset):
            foreground_color_style = UNSET
        else:
            foreground_color_style = ColorStyle.from_dict(_foreground_color_style)




        italic = d.pop("italic", UNSET)

        _link = d.pop("link", UNSET)
        link: Link | Unset
        if isinstance(_link,  Unset):
            link = UNSET
        else:
            link = Link.from_dict(_link)




        strikethrough = d.pop("strikethrough", UNSET)

        underline = d.pop("underline", UNSET)

        text_format = cls(
            bold=bold,
            font_family=font_family,
            font_size=font_size,
            foreground_color=foreground_color,
            foreground_color_style=foreground_color_style,
            italic=italic,
            link=link,
            strikethrough=strikethrough,
            underline=underline,
        )


        text_format.additional_properties = d
        return text_format

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
