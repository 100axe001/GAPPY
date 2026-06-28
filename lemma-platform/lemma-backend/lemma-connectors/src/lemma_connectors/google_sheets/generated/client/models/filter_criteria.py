from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.boolean_condition import BooleanCondition
  from ..models.color import Color
  from ..models.color_style import ColorStyle





T = TypeVar("T", bound="FilterCriteria")



@_attrs_define
class FilterCriteria:
    """ Criteria for showing/hiding rows in a filter or filter view.

        Attributes:
            condition (BooleanCondition | Unset): A condition that can evaluate to true or false. BooleanConditions are used
                by conditional formatting, data validation, and the criteria in filters.
            hidden_values (list[str] | Unset): Values that should be hidden.
            visible_background_color (Color | Unset): Represents a color in the RGBA color space. This representation is
                designed for simplicity of conversion to/from color representations in various languages over compactness. For
                example, the fields of this representation can be trivially provided to the constructor of `java.awt.Color` in
                Java; it can also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with
                just a little work, it can be easily formatted into a CSS `rgba()` string in JavaScript. This reference page
                doesn't carry information about the absolute color space that should be used to interpret the RGB value (e.g.
                sRGB, Adobe RGB, DCI-P3, BT.2020, etc.). By default, applications should assume the sRGB color space. When color
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
            visible_background_color_style (ColorStyle | Unset): A color value.
            visible_foreground_color (Color | Unset): Represents a color in the RGBA color space. This representation is
                designed for simplicity of conversion to/from color representations in various languages over compactness. For
                example, the fields of this representation can be trivially provided to the constructor of `java.awt.Color` in
                Java; it can also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with
                just a little work, it can be easily formatted into a CSS `rgba()` string in JavaScript. This reference page
                doesn't carry information about the absolute color space that should be used to interpret the RGB value (e.g.
                sRGB, Adobe RGB, DCI-P3, BT.2020, etc.). By default, applications should assume the sRGB color space. When color
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
            visible_foreground_color_style (ColorStyle | Unset): A color value.
     """

    condition: BooleanCondition | Unset = UNSET
    hidden_values: list[str] | Unset = UNSET
    visible_background_color: Color | Unset = UNSET
    visible_background_color_style: ColorStyle | Unset = UNSET
    visible_foreground_color: Color | Unset = UNSET
    visible_foreground_color_style: ColorStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_condition import BooleanCondition
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        hidden_values: list[str] | Unset = UNSET
        if not isinstance(self.hidden_values, Unset):
            hidden_values = self.hidden_values



        visible_background_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visible_background_color, Unset):
            visible_background_color = self.visible_background_color.to_dict()

        visible_background_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visible_background_color_style, Unset):
            visible_background_color_style = self.visible_background_color_style.to_dict()

        visible_foreground_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visible_foreground_color, Unset):
            visible_foreground_color = self.visible_foreground_color.to_dict()

        visible_foreground_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visible_foreground_color_style, Unset):
            visible_foreground_color_style = self.visible_foreground_color_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if condition is not UNSET:
            field_dict["condition"] = condition
        if hidden_values is not UNSET:
            field_dict["hiddenValues"] = hidden_values
        if visible_background_color is not UNSET:
            field_dict["visibleBackgroundColor"] = visible_background_color
        if visible_background_color_style is not UNSET:
            field_dict["visibleBackgroundColorStyle"] = visible_background_color_style
        if visible_foreground_color is not UNSET:
            field_dict["visibleForegroundColor"] = visible_foreground_color
        if visible_foreground_color_style is not UNSET:
            field_dict["visibleForegroundColorStyle"] = visible_foreground_color_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_condition import BooleanCondition
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        d = dict(src_dict)
        _condition = d.pop("condition", UNSET)
        condition: BooleanCondition | Unset
        if isinstance(_condition,  Unset):
            condition = UNSET
        else:
            condition = BooleanCondition.from_dict(_condition)




        hidden_values = cast(list[str], d.pop("hiddenValues", UNSET))


        _visible_background_color = d.pop("visibleBackgroundColor", UNSET)
        visible_background_color: Color | Unset
        if isinstance(_visible_background_color,  Unset):
            visible_background_color = UNSET
        else:
            visible_background_color = Color.from_dict(_visible_background_color)




        _visible_background_color_style = d.pop("visibleBackgroundColorStyle", UNSET)
        visible_background_color_style: ColorStyle | Unset
        if isinstance(_visible_background_color_style,  Unset):
            visible_background_color_style = UNSET
        else:
            visible_background_color_style = ColorStyle.from_dict(_visible_background_color_style)




        _visible_foreground_color = d.pop("visibleForegroundColor", UNSET)
        visible_foreground_color: Color | Unset
        if isinstance(_visible_foreground_color,  Unset):
            visible_foreground_color = UNSET
        else:
            visible_foreground_color = Color.from_dict(_visible_foreground_color)




        _visible_foreground_color_style = d.pop("visibleForegroundColorStyle", UNSET)
        visible_foreground_color_style: ColorStyle | Unset
        if isinstance(_visible_foreground_color_style,  Unset):
            visible_foreground_color_style = UNSET
        else:
            visible_foreground_color_style = ColorStyle.from_dict(_visible_foreground_color_style)




        filter_criteria = cls(
            condition=condition,
            hidden_values=hidden_values,
            visible_background_color=visible_background_color,
            visible_background_color_style=visible_background_color_style,
            visible_foreground_color=visible_foreground_color,
            visible_foreground_color_style=visible_foreground_color_style,
        )


        filter_criteria.additional_properties = d
        return filter_criteria

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
