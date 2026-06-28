from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.slicer_spec_horizontal_alignment import SlicerSpecHorizontalAlignment
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.filter_criteria import FilterCriteria
  from ..models.grid_range import GridRange
  from ..models.text_format import TextFormat





T = TypeVar("T", bound="SlicerSpec")



@_attrs_define
class SlicerSpec:
    """ The specifications of a slicer.

        Attributes:
            apply_to_pivot_tables (bool | Unset): True if the filter should apply to pivot tables. If not set, default to
                `True`.
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
            column_index (int | Unset): The column index in the data table on which the filter is applied to.
            data_range (GridRange | Unset): A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the
                start index is inclusive and the end index is exclusive -- [start_index, end_index). Missing indexes indicate
                the range is unbounded on that side. For example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 ==
                sheet_id: 123456, start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index: 1`
                `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2, end_row_index: 4, start_column_index: 0,
                end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index: 0, end_column_index: 2` `Sheet1!A5:B
                == sheet_id: 123456, start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 == sheet_id:
                123456` The start index must always be less than or equal to the end index. If the start index equals the end
                index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as
                `#REF!`.
            filter_criteria (FilterCriteria | Unset): Criteria for showing/hiding rows in a filter or filter view.
            horizontal_alignment (SlicerSpecHorizontalAlignment | Unset): The horizontal alignment of title in the slicer.
                If unspecified, defaults to `LEFT`
            text_format (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the field
                isn't specified.
            title (str | Unset): The title of the slicer.
     """

    apply_to_pivot_tables: bool | Unset = UNSET
    background_color: Color | Unset = UNSET
    background_color_style: ColorStyle | Unset = UNSET
    column_index: int | Unset = UNSET
    data_range: GridRange | Unset = UNSET
    filter_criteria: FilterCriteria | Unset = UNSET
    horizontal_alignment: SlicerSpecHorizontalAlignment | Unset = UNSET
    text_format: TextFormat | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.filter_criteria import FilterCriteria
        from ..models.grid_range import GridRange
        from ..models.text_format import TextFormat
        apply_to_pivot_tables = self.apply_to_pivot_tables

        background_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.to_dict()

        background_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color_style, Unset):
            background_color_style = self.background_color_style.to_dict()

        column_index = self.column_index

        data_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_range, Unset):
            data_range = self.data_range.to_dict()

        filter_criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_criteria, Unset):
            filter_criteria = self.filter_criteria.to_dict()

        horizontal_alignment: str | Unset = UNSET
        if not isinstance(self.horizontal_alignment, Unset):
            horizontal_alignment = self.horizontal_alignment.value


        text_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_format, Unset):
            text_format = self.text_format.to_dict()

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if apply_to_pivot_tables is not UNSET:
            field_dict["applyToPivotTables"] = apply_to_pivot_tables
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if background_color_style is not UNSET:
            field_dict["backgroundColorStyle"] = background_color_style
        if column_index is not UNSET:
            field_dict["columnIndex"] = column_index
        if data_range is not UNSET:
            field_dict["dataRange"] = data_range
        if filter_criteria is not UNSET:
            field_dict["filterCriteria"] = filter_criteria
        if horizontal_alignment is not UNSET:
            field_dict["horizontalAlignment"] = horizontal_alignment
        if text_format is not UNSET:
            field_dict["textFormat"] = text_format
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.filter_criteria import FilterCriteria
        from ..models.grid_range import GridRange
        from ..models.text_format import TextFormat
        d = dict(src_dict)
        apply_to_pivot_tables = d.pop("applyToPivotTables", UNSET)

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




        column_index = d.pop("columnIndex", UNSET)

        _data_range = d.pop("dataRange", UNSET)
        data_range: GridRange | Unset
        if isinstance(_data_range,  Unset):
            data_range = UNSET
        else:
            data_range = GridRange.from_dict(_data_range)




        _filter_criteria = d.pop("filterCriteria", UNSET)
        filter_criteria: FilterCriteria | Unset
        if isinstance(_filter_criteria,  Unset):
            filter_criteria = UNSET
        else:
            filter_criteria = FilterCriteria.from_dict(_filter_criteria)




        _horizontal_alignment = d.pop("horizontalAlignment", UNSET)
        horizontal_alignment: SlicerSpecHorizontalAlignment | Unset
        if isinstance(_horizontal_alignment,  Unset):
            horizontal_alignment = UNSET
        else:
            horizontal_alignment = SlicerSpecHorizontalAlignment(_horizontal_alignment)




        _text_format = d.pop("textFormat", UNSET)
        text_format: TextFormat | Unset
        if isinstance(_text_format,  Unset):
            text_format = UNSET
        else:
            text_format = TextFormat.from_dict(_text_format)




        title = d.pop("title", UNSET)

        slicer_spec = cls(
            apply_to_pivot_tables=apply_to_pivot_tables,
            background_color=background_color,
            background_color_style=background_color_style,
            column_index=column_index,
            data_range=data_range,
            filter_criteria=filter_criteria,
            horizontal_alignment=horizontal_alignment,
            text_format=text_format,
            title=title,
        )


        slicer_spec.additional_properties = d
        return slicer_spec

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
