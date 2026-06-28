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





T = TypeVar("T", bound="BandingProperties")



@_attrs_define
class BandingProperties:
    """ Properties referring a single dimension (either row or column). If both BandedRange.row_properties and
    BandedRange.column_properties are set, the fill colors are applied to cells according to the following rules: *
    header_color and footer_color take priority over band colors. * first_band_color takes priority over
    second_band_color. * row_properties takes priority over column_properties. For example, the first row color takes
    priority over the first column color, but the first column color takes priority over the second row color.
    Similarly, the row header takes priority over the column header in the top left cell, but the column header takes
    priority over the first row color if the row header is not set.

        Attributes:
            first_band_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed
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
            first_band_color_style (ColorStyle | Unset): A color value.
            footer_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
                simplicity of conversion to/from color representations in various languages over compactness. For example, the
                fields of this representation can be trivially provided to the constructor of `java.awt.Color` in Java; it can
                also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with just a little
                work, it can be easily formatted into a CSS `rgba()` string in JavaScript. This reference page doesn't carry
                information about the absolute color space that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                DCI-P3, BT.2020, etc.). By default, applications should assume the sRGB color space. When color equality needs
                to be decided, implementations, unless documented otherwise, treat two colors as equal if all their red, green,
                blue, and alpha values each differ by at most 1e-5. Example (Java): import com.google.type.Color; // ... public
                static java.awt.Color fromProto(Color protocolor) { float alpha = protocolor.hasAlpha() ?
                protocolor.getAlpha().getValue() : 1.0; return new java.awt.Color( protocolor.getRed(), protocolor.getGreen(),
                protocolor.getBlue(), alpha); } public static Color toProto(java.awt.Color color) { float red = (float)
                color.getRed(); float green = (float) color.getGreen(); float blue = (float) color.getBlue(); float denominator
                = 255.0; Color.Builder resultBuilder = Color .newBuilder() .setRed(red / denominator) .setGreen(green /
                denominator) .setBlue(blue / denominator); int alpha = color.getAlpha(); if (alpha != 255) { result.setAlpha(
                FloatValue .newBuilder() .setValue(((float) alpha) / denominator) .build()); } return resultBuilder.build(); }
                // ... Example (iOS / Obj-C): // ... static UIColor* fromProto(Color* protocolor) { float red = [protocolor
                red]; float green = [protocolor green]; float blue = [protocolor blue]; FloatValue* alpha_wrapper = [protocolor
                alpha]; float alpha = 1.0; if (alpha_wrapper != nil) { alpha = [alpha_wrapper value]; } return [UIColor
                colorWithRed:red green:green blue:blue alpha:alpha]; } static Color* toProto(UIColor* color) { CGFloat red,
                green, blue, alpha; if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) { return nil; } Color* result
                = [[Color alloc] init]; [result setRed:red]; [result setGreen:green]; [result setBlue:blue]; if (alpha <=
                0.9999) { [result setAlpha:floatWrapperWithValue(alpha)]; } [result autorelease]; return result; } // ...
                Example (JavaScript): // ... var protoToCssColor = function(rgb_color) { var redFrac = rgb_color.red || 0.0; var
                greenFrac = rgb_color.green || 0.0; var blueFrac = rgb_color.blue || 0.0; var red = Math.floor(redFrac * 255);
                var green = Math.floor(greenFrac * 255); var blue = Math.floor(blueFrac * 255); if (!('alpha' in rgb_color)) {
                return rgbToCssColor(red, green, blue); } var alphaFrac = rgb_color.alpha.value || 0.0; var rgbParams = [red,
                green, blue].join(','); return ['rgba(', rgbParams, ',', alphaFrac, ')'].join(''); }; var rgbToCssColor =
                function(red, green, blue) { var rgbNumber = new Number((red << 16) | (green << 8) | blue); var hexString =
                rgbNumber.toString(16); var missingZeros = 6 - hexString.length; var resultBuilder = ['#']; for (var i = 0; i <
                missingZeros; i++) { resultBuilder.push('0'); } resultBuilder.push(hexString); return resultBuilder.join(''); };
                // ...
            footer_color_style (ColorStyle | Unset): A color value.
            header_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
                simplicity of conversion to/from color representations in various languages over compactness. For example, the
                fields of this representation can be trivially provided to the constructor of `java.awt.Color` in Java; it can
                also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with just a little
                work, it can be easily formatted into a CSS `rgba()` string in JavaScript. This reference page doesn't carry
                information about the absolute color space that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                DCI-P3, BT.2020, etc.). By default, applications should assume the sRGB color space. When color equality needs
                to be decided, implementations, unless documented otherwise, treat two colors as equal if all their red, green,
                blue, and alpha values each differ by at most 1e-5. Example (Java): import com.google.type.Color; // ... public
                static java.awt.Color fromProto(Color protocolor) { float alpha = protocolor.hasAlpha() ?
                protocolor.getAlpha().getValue() : 1.0; return new java.awt.Color( protocolor.getRed(), protocolor.getGreen(),
                protocolor.getBlue(), alpha); } public static Color toProto(java.awt.Color color) { float red = (float)
                color.getRed(); float green = (float) color.getGreen(); float blue = (float) color.getBlue(); float denominator
                = 255.0; Color.Builder resultBuilder = Color .newBuilder() .setRed(red / denominator) .setGreen(green /
                denominator) .setBlue(blue / denominator); int alpha = color.getAlpha(); if (alpha != 255) { result.setAlpha(
                FloatValue .newBuilder() .setValue(((float) alpha) / denominator) .build()); } return resultBuilder.build(); }
                // ... Example (iOS / Obj-C): // ... static UIColor* fromProto(Color* protocolor) { float red = [protocolor
                red]; float green = [protocolor green]; float blue = [protocolor blue]; FloatValue* alpha_wrapper = [protocolor
                alpha]; float alpha = 1.0; if (alpha_wrapper != nil) { alpha = [alpha_wrapper value]; } return [UIColor
                colorWithRed:red green:green blue:blue alpha:alpha]; } static Color* toProto(UIColor* color) { CGFloat red,
                green, blue, alpha; if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) { return nil; } Color* result
                = [[Color alloc] init]; [result setRed:red]; [result setGreen:green]; [result setBlue:blue]; if (alpha <=
                0.9999) { [result setAlpha:floatWrapperWithValue(alpha)]; } [result autorelease]; return result; } // ...
                Example (JavaScript): // ... var protoToCssColor = function(rgb_color) { var redFrac = rgb_color.red || 0.0; var
                greenFrac = rgb_color.green || 0.0; var blueFrac = rgb_color.blue || 0.0; var red = Math.floor(redFrac * 255);
                var green = Math.floor(greenFrac * 255); var blue = Math.floor(blueFrac * 255); if (!('alpha' in rgb_color)) {
                return rgbToCssColor(red, green, blue); } var alphaFrac = rgb_color.alpha.value || 0.0; var rgbParams = [red,
                green, blue].join(','); return ['rgba(', rgbParams, ',', alphaFrac, ')'].join(''); }; var rgbToCssColor =
                function(red, green, blue) { var rgbNumber = new Number((red << 16) | (green << 8) | blue); var hexString =
                rgbNumber.toString(16); var missingZeros = 6 - hexString.length; var resultBuilder = ['#']; for (var i = 0; i <
                missingZeros; i++) { resultBuilder.push('0'); } resultBuilder.push(hexString); return resultBuilder.join(''); };
                // ...
            header_color_style (ColorStyle | Unset): A color value.
            second_band_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed
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
            second_band_color_style (ColorStyle | Unset): A color value.
     """

    first_band_color: Color | Unset = UNSET
    first_band_color_style: ColorStyle | Unset = UNSET
    footer_color: Color | Unset = UNSET
    footer_color_style: ColorStyle | Unset = UNSET
    header_color: Color | Unset = UNSET
    header_color_style: ColorStyle | Unset = UNSET
    second_band_color: Color | Unset = UNSET
    second_band_color_style: ColorStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        first_band_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_band_color, Unset):
            first_band_color = self.first_band_color.to_dict()

        first_band_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_band_color_style, Unset):
            first_band_color_style = self.first_band_color_style.to_dict()

        footer_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.footer_color, Unset):
            footer_color = self.footer_color.to_dict()

        footer_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.footer_color_style, Unset):
            footer_color_style = self.footer_color_style.to_dict()

        header_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header_color, Unset):
            header_color = self.header_color.to_dict()

        header_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header_color_style, Unset):
            header_color_style = self.header_color_style.to_dict()

        second_band_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.second_band_color, Unset):
            second_band_color = self.second_band_color.to_dict()

        second_band_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.second_band_color_style, Unset):
            second_band_color_style = self.second_band_color_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if first_band_color is not UNSET:
            field_dict["firstBandColor"] = first_band_color
        if first_band_color_style is not UNSET:
            field_dict["firstBandColorStyle"] = first_band_color_style
        if footer_color is not UNSET:
            field_dict["footerColor"] = footer_color
        if footer_color_style is not UNSET:
            field_dict["footerColorStyle"] = footer_color_style
        if header_color is not UNSET:
            field_dict["headerColor"] = header_color
        if header_color_style is not UNSET:
            field_dict["headerColorStyle"] = header_color_style
        if second_band_color is not UNSET:
            field_dict["secondBandColor"] = second_band_color
        if second_band_color_style is not UNSET:
            field_dict["secondBandColorStyle"] = second_band_color_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        d = dict(src_dict)
        _first_band_color = d.pop("firstBandColor", UNSET)
        first_band_color: Color | Unset
        if isinstance(_first_band_color,  Unset):
            first_band_color = UNSET
        else:
            first_band_color = Color.from_dict(_first_band_color)




        _first_band_color_style = d.pop("firstBandColorStyle", UNSET)
        first_band_color_style: ColorStyle | Unset
        if isinstance(_first_band_color_style,  Unset):
            first_band_color_style = UNSET
        else:
            first_band_color_style = ColorStyle.from_dict(_first_band_color_style)




        _footer_color = d.pop("footerColor", UNSET)
        footer_color: Color | Unset
        if isinstance(_footer_color,  Unset):
            footer_color = UNSET
        else:
            footer_color = Color.from_dict(_footer_color)




        _footer_color_style = d.pop("footerColorStyle", UNSET)
        footer_color_style: ColorStyle | Unset
        if isinstance(_footer_color_style,  Unset):
            footer_color_style = UNSET
        else:
            footer_color_style = ColorStyle.from_dict(_footer_color_style)




        _header_color = d.pop("headerColor", UNSET)
        header_color: Color | Unset
        if isinstance(_header_color,  Unset):
            header_color = UNSET
        else:
            header_color = Color.from_dict(_header_color)




        _header_color_style = d.pop("headerColorStyle", UNSET)
        header_color_style: ColorStyle | Unset
        if isinstance(_header_color_style,  Unset):
            header_color_style = UNSET
        else:
            header_color_style = ColorStyle.from_dict(_header_color_style)




        _second_band_color = d.pop("secondBandColor", UNSET)
        second_band_color: Color | Unset
        if isinstance(_second_band_color,  Unset):
            second_band_color = UNSET
        else:
            second_band_color = Color.from_dict(_second_band_color)




        _second_band_color_style = d.pop("secondBandColorStyle", UNSET)
        second_band_color_style: ColorStyle | Unset
        if isinstance(_second_band_color_style,  Unset):
            second_band_color_style = UNSET
        else:
            second_band_color_style = ColorStyle.from_dict(_second_band_color_style)




        banding_properties = cls(
            first_band_color=first_band_color,
            first_band_color_style=first_band_color_style,
            footer_color=footer_color,
            footer_color_style=footer_color_style,
            header_color=header_color,
            header_color_style=header_color_style,
            second_band_color=second_band_color,
            second_band_color_style=second_band_color_style,
        )


        banding_properties.additional_properties = d
        return banding_properties

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
