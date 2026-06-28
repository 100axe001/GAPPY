from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sheet_properties_sheet_type import SheetPropertiesSheetType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.data_source_sheet_properties import DataSourceSheetProperties
  from ..models.grid_properties import GridProperties





T = TypeVar("T", bound="SheetProperties")



@_attrs_define
class SheetProperties:
    """ Properties of a sheet.

        Attributes:
            data_source_sheet_properties (DataSourceSheetProperties | Unset): Additional properties of a DATA_SOURCE sheet.
            grid_properties (GridProperties | Unset): Properties of a grid.
            hidden (bool | Unset): True if the sheet is hidden in the UI, false if it's visible.
            index (int | Unset): The index of the sheet within the spreadsheet. When adding or updating sheet properties, if
                this field is excluded then the sheet is added or moved to the end of the sheet list. When updating sheet
                indices or inserting sheets, movement is considered in "before the move" indexes. For example, if there were 3
                sheets (S1, S2, S3) in order to move S1 ahead of S2 the index would have to be set to 2. A sheet index update
                request is ignored if the requested index is identical to the sheets current index or if the requested new index
                is equal to the current sheet index + 1.
            right_to_left (bool | Unset): True if the sheet is an RTL sheet instead of an LTR sheet.
            sheet_id (int | Unset): The ID of the sheet. Must be non-negative. This field cannot be changed once set.
            sheet_type (SheetPropertiesSheetType | Unset): The type of sheet. Defaults to GRID. This field cannot be changed
                once set.
            tab_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
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
            tab_color_style (ColorStyle | Unset): A color value.
            title (str | Unset): The name of the sheet.
     """

    data_source_sheet_properties: DataSourceSheetProperties | Unset = UNSET
    grid_properties: GridProperties | Unset = UNSET
    hidden: bool | Unset = UNSET
    index: int | Unset = UNSET
    right_to_left: bool | Unset = UNSET
    sheet_id: int | Unset = UNSET
    sheet_type: SheetPropertiesSheetType | Unset = UNSET
    tab_color: Color | Unset = UNSET
    tab_color_style: ColorStyle | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.data_source_sheet_properties import DataSourceSheetProperties
        from ..models.grid_properties import GridProperties
        data_source_sheet_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_sheet_properties, Unset):
            data_source_sheet_properties = self.data_source_sheet_properties.to_dict()

        grid_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grid_properties, Unset):
            grid_properties = self.grid_properties.to_dict()

        hidden = self.hidden

        index = self.index

        right_to_left = self.right_to_left

        sheet_id = self.sheet_id

        sheet_type: str | Unset = UNSET
        if not isinstance(self.sheet_type, Unset):
            sheet_type = self.sheet_type.value


        tab_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tab_color, Unset):
            tab_color = self.tab_color.to_dict()

        tab_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tab_color_style, Unset):
            tab_color_style = self.tab_color_style.to_dict()

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_source_sheet_properties is not UNSET:
            field_dict["dataSourceSheetProperties"] = data_source_sheet_properties
        if grid_properties is not UNSET:
            field_dict["gridProperties"] = grid_properties
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if index is not UNSET:
            field_dict["index"] = index
        if right_to_left is not UNSET:
            field_dict["rightToLeft"] = right_to_left
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id
        if sheet_type is not UNSET:
            field_dict["sheetType"] = sheet_type
        if tab_color is not UNSET:
            field_dict["tabColor"] = tab_color
        if tab_color_style is not UNSET:
            field_dict["tabColorStyle"] = tab_color_style
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.data_source_sheet_properties import DataSourceSheetProperties
        from ..models.grid_properties import GridProperties
        d = dict(src_dict)
        _data_source_sheet_properties = d.pop("dataSourceSheetProperties", UNSET)
        data_source_sheet_properties: DataSourceSheetProperties | Unset
        if isinstance(_data_source_sheet_properties,  Unset):
            data_source_sheet_properties = UNSET
        else:
            data_source_sheet_properties = DataSourceSheetProperties.from_dict(_data_source_sheet_properties)




        _grid_properties = d.pop("gridProperties", UNSET)
        grid_properties: GridProperties | Unset
        if isinstance(_grid_properties,  Unset):
            grid_properties = UNSET
        else:
            grid_properties = GridProperties.from_dict(_grid_properties)




        hidden = d.pop("hidden", UNSET)

        index = d.pop("index", UNSET)

        right_to_left = d.pop("rightToLeft", UNSET)

        sheet_id = d.pop("sheetId", UNSET)

        _sheet_type = d.pop("sheetType", UNSET)
        sheet_type: SheetPropertiesSheetType | Unset
        if isinstance(_sheet_type,  Unset):
            sheet_type = UNSET
        else:
            sheet_type = SheetPropertiesSheetType(_sheet_type)




        _tab_color = d.pop("tabColor", UNSET)
        tab_color: Color | Unset
        if isinstance(_tab_color,  Unset):
            tab_color = UNSET
        else:
            tab_color = Color.from_dict(_tab_color)




        _tab_color_style = d.pop("tabColorStyle", UNSET)
        tab_color_style: ColorStyle | Unset
        if isinstance(_tab_color_style,  Unset):
            tab_color_style = UNSET
        else:
            tab_color_style = ColorStyle.from_dict(_tab_color_style)




        title = d.pop("title", UNSET)

        sheet_properties = cls(
            data_source_sheet_properties=data_source_sheet_properties,
            grid_properties=grid_properties,
            hidden=hidden,
            index=index,
            right_to_left=right_to_left,
            sheet_id=sheet_id,
            sheet_type=sheet_type,
            tab_color=tab_color,
            tab_color_style=tab_color_style,
            title=title,
        )


        sheet_properties.additional_properties = d
        return sheet_properties

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
