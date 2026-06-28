from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cell_format_horizontal_alignment import CellFormatHorizontalAlignment
from ..models.cell_format_hyperlink_display_type import CellFormatHyperlinkDisplayType
from ..models.cell_format_text_direction import CellFormatTextDirection
from ..models.cell_format_vertical_alignment import CellFormatVerticalAlignment
from ..models.cell_format_wrap_strategy import CellFormatWrapStrategy
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.borders import Borders
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.number_format import NumberFormat
  from ..models.padding import Padding
  from ..models.text_format import TextFormat
  from ..models.text_rotation import TextRotation





T = TypeVar("T", bound="CellFormat")



@_attrs_define
class CellFormat:
    """ The format of a cell.

        Attributes:
            background_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed
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
            background_color_style (ColorStyle | Unset): A color value.
            borders (Borders | Unset): The borders of the cell.
            horizontal_alignment (CellFormatHorizontalAlignment | Unset): The horizontal alignment of the value in the cell.
            hyperlink_display_type (CellFormatHyperlinkDisplayType | Unset): If one exists, how a hyperlink should be
                displayed in the cell.
            number_format (NumberFormat | Unset): The number format of a cell.
            padding (Padding | Unset): The amount of padding around the cell, in pixels. When updating padding, every field
                must be specified.
            text_direction (CellFormatTextDirection | Unset): The direction of the text in the cell.
            text_format (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the field
                isn't specified.
            text_rotation (TextRotation | Unset): The rotation applied to text in a cell.
            vertical_alignment (CellFormatVerticalAlignment | Unset): The vertical alignment of the value in the cell.
            wrap_strategy (CellFormatWrapStrategy | Unset): The wrap strategy for the value in the cell.
     """

    background_color: Color | Unset = UNSET
    background_color_style: ColorStyle | Unset = UNSET
    borders: Borders | Unset = UNSET
    horizontal_alignment: CellFormatHorizontalAlignment | Unset = UNSET
    hyperlink_display_type: CellFormatHyperlinkDisplayType | Unset = UNSET
    number_format: NumberFormat | Unset = UNSET
    padding: Padding | Unset = UNSET
    text_direction: CellFormatTextDirection | Unset = UNSET
    text_format: TextFormat | Unset = UNSET
    text_rotation: TextRotation | Unset = UNSET
    vertical_alignment: CellFormatVerticalAlignment | Unset = UNSET
    wrap_strategy: CellFormatWrapStrategy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.borders import Borders
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.number_format import NumberFormat
        from ..models.padding import Padding
        from ..models.text_format import TextFormat
        from ..models.text_rotation import TextRotation
        background_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.to_dict()

        background_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color_style, Unset):
            background_color_style = self.background_color_style.to_dict()

        borders: dict[str, Any] | Unset = UNSET
        if not isinstance(self.borders, Unset):
            borders = self.borders.to_dict()

        horizontal_alignment: str | Unset = UNSET
        if not isinstance(self.horizontal_alignment, Unset):
            horizontal_alignment = self.horizontal_alignment.value


        hyperlink_display_type: str | Unset = UNSET
        if not isinstance(self.hyperlink_display_type, Unset):
            hyperlink_display_type = self.hyperlink_display_type.value


        number_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.number_format, Unset):
            number_format = self.number_format.to_dict()

        padding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.padding, Unset):
            padding = self.padding.to_dict()

        text_direction: str | Unset = UNSET
        if not isinstance(self.text_direction, Unset):
            text_direction = self.text_direction.value


        text_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_format, Unset):
            text_format = self.text_format.to_dict()

        text_rotation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_rotation, Unset):
            text_rotation = self.text_rotation.to_dict()

        vertical_alignment: str | Unset = UNSET
        if not isinstance(self.vertical_alignment, Unset):
            vertical_alignment = self.vertical_alignment.value


        wrap_strategy: str | Unset = UNSET
        if not isinstance(self.wrap_strategy, Unset):
            wrap_strategy = self.wrap_strategy.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if background_color_style is not UNSET:
            field_dict["backgroundColorStyle"] = background_color_style
        if borders is not UNSET:
            field_dict["borders"] = borders
        if horizontal_alignment is not UNSET:
            field_dict["horizontalAlignment"] = horizontal_alignment
        if hyperlink_display_type is not UNSET:
            field_dict["hyperlinkDisplayType"] = hyperlink_display_type
        if number_format is not UNSET:
            field_dict["numberFormat"] = number_format
        if padding is not UNSET:
            field_dict["padding"] = padding
        if text_direction is not UNSET:
            field_dict["textDirection"] = text_direction
        if text_format is not UNSET:
            field_dict["textFormat"] = text_format
        if text_rotation is not UNSET:
            field_dict["textRotation"] = text_rotation
        if vertical_alignment is not UNSET:
            field_dict["verticalAlignment"] = vertical_alignment
        if wrap_strategy is not UNSET:
            field_dict["wrapStrategy"] = wrap_strategy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.borders import Borders
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.number_format import NumberFormat
        from ..models.padding import Padding
        from ..models.text_format import TextFormat
        from ..models.text_rotation import TextRotation
        d = dict(src_dict)
        _background_color = d.pop("backgroundColor", UNSET)
        background_color: Color | Unset
        if isinstance(_background_color,  Unset):
            background_color = UNSET
        else:
            background_color = Color.from_dict(_background_color)




        _background_color_style = d.pop("backgroundColorStyle", UNSET)
        background_color_style: ColorStyle | Unset
        if isinstance(_background_color_style,  Unset):
            background_color_style = UNSET
        else:
            background_color_style = ColorStyle.from_dict(_background_color_style)




        _borders = d.pop("borders", UNSET)
        borders: Borders | Unset
        if isinstance(_borders,  Unset):
            borders = UNSET
        else:
            borders = Borders.from_dict(_borders)




        _horizontal_alignment = d.pop("horizontalAlignment", UNSET)
        horizontal_alignment: CellFormatHorizontalAlignment | Unset
        if isinstance(_horizontal_alignment,  Unset):
            horizontal_alignment = UNSET
        else:
            horizontal_alignment = CellFormatHorizontalAlignment(_horizontal_alignment)




        _hyperlink_display_type = d.pop("hyperlinkDisplayType", UNSET)
        hyperlink_display_type: CellFormatHyperlinkDisplayType | Unset
        if isinstance(_hyperlink_display_type,  Unset):
            hyperlink_display_type = UNSET
        else:
            hyperlink_display_type = CellFormatHyperlinkDisplayType(_hyperlink_display_type)




        _number_format = d.pop("numberFormat", UNSET)
        number_format: NumberFormat | Unset
        if isinstance(_number_format,  Unset):
            number_format = UNSET
        else:
            number_format = NumberFormat.from_dict(_number_format)




        _padding = d.pop("padding", UNSET)
        padding: Padding | Unset
        if isinstance(_padding,  Unset):
            padding = UNSET
        else:
            padding = Padding.from_dict(_padding)




        _text_direction = d.pop("textDirection", UNSET)
        text_direction: CellFormatTextDirection | Unset
        if isinstance(_text_direction,  Unset):
            text_direction = UNSET
        else:
            text_direction = CellFormatTextDirection(_text_direction)




        _text_format = d.pop("textFormat", UNSET)
        text_format: TextFormat | Unset
        if isinstance(_text_format,  Unset):
            text_format = UNSET
        else:
            text_format = TextFormat.from_dict(_text_format)




        _text_rotation = d.pop("textRotation", UNSET)
        text_rotation: TextRotation | Unset
        if isinstance(_text_rotation,  Unset):
            text_rotation = UNSET
        else:
            text_rotation = TextRotation.from_dict(_text_rotation)




        _vertical_alignment = d.pop("verticalAlignment", UNSET)
        vertical_alignment: CellFormatVerticalAlignment | Unset
        if isinstance(_vertical_alignment,  Unset):
            vertical_alignment = UNSET
        else:
            vertical_alignment = CellFormatVerticalAlignment(_vertical_alignment)




        _wrap_strategy = d.pop("wrapStrategy", UNSET)
        wrap_strategy: CellFormatWrapStrategy | Unset
        if isinstance(_wrap_strategy,  Unset):
            wrap_strategy = UNSET
        else:
            wrap_strategy = CellFormatWrapStrategy(_wrap_strategy)




        cell_format = cls(
            background_color=background_color,
            background_color_style=background_color_style,
            borders=borders,
            horizontal_alignment=horizontal_alignment,
            hyperlink_display_type=hyperlink_display_type,
            number_format=number_format,
            padding=padding,
            text_direction=text_direction,
            text_format=text_format,
            text_rotation=text_rotation,
            vertical_alignment=vertical_alignment,
            wrap_strategy=wrap_strategy,
        )


        cell_format.additional_properties = d
        return cell_format

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
