from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sort_spec_sort_order import SortSpecSortOrder
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.data_source_column_reference import DataSourceColumnReference





T = TypeVar("T", bound="SortSpec")



@_attrs_define
class SortSpec:
    """ A sort order associated with a specific column or row.

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
            data_source_column_reference (DataSourceColumnReference | Unset): An unique identifier that references a data
                source column.
            dimension_index (int | Unset): The dimension the sort should be applied to.
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
            sort_order (SortSpecSortOrder | Unset): The order data should be sorted.
     """

    background_color: Color | Unset = UNSET
    background_color_style: ColorStyle | Unset = UNSET
    data_source_column_reference: DataSourceColumnReference | Unset = UNSET
    dimension_index: int | Unset = UNSET
    foreground_color: Color | Unset = UNSET
    foreground_color_style: ColorStyle | Unset = UNSET
    sort_order: SortSpecSortOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.data_source_column_reference import DataSourceColumnReference
        background_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.to_dict()

        background_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color_style, Unset):
            background_color_style = self.background_color_style.to_dict()

        data_source_column_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_column_reference, Unset):
            data_source_column_reference = self.data_source_column_reference.to_dict()

        dimension_index = self.dimension_index

        foreground_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.foreground_color, Unset):
            foreground_color = self.foreground_color.to_dict()

        foreground_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.foreground_color_style, Unset):
            foreground_color_style = self.foreground_color_style.to_dict()

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if background_color_style is not UNSET:
            field_dict["backgroundColorStyle"] = background_color_style
        if data_source_column_reference is not UNSET:
            field_dict["dataSourceColumnReference"] = data_source_column_reference
        if dimension_index is not UNSET:
            field_dict["dimensionIndex"] = dimension_index
        if foreground_color is not UNSET:
            field_dict["foregroundColor"] = foreground_color
        if foreground_color_style is not UNSET:
            field_dict["foregroundColorStyle"] = foreground_color_style
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.data_source_column_reference import DataSourceColumnReference
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




        _data_source_column_reference = d.pop("dataSourceColumnReference", UNSET)
        data_source_column_reference: DataSourceColumnReference | Unset
        if isinstance(_data_source_column_reference,  Unset):
            data_source_column_reference = UNSET
        else:
            data_source_column_reference = DataSourceColumnReference.from_dict(_data_source_column_reference)




        dimension_index = d.pop("dimensionIndex", UNSET)

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




        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: SortSpecSortOrder | Unset
        if isinstance(_sort_order,  Unset):
            sort_order = UNSET
        else:
            sort_order = SortSpecSortOrder(_sort_order)




        sort_spec = cls(
            background_color=background_color,
            background_color_style=background_color_style,
            data_source_column_reference=data_source_column_reference,
            dimension_index=dimension_index,
            foreground_color=foreground_color,
            foreground_color_style=foreground_color_style,
            sort_order=sort_order,
        )


        sort_spec.additional_properties = d
        return sort_spec

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
