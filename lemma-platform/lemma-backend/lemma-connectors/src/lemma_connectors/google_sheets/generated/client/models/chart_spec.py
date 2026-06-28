from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.chart_spec_hidden_dimension_strategy import ChartSpecHiddenDimensionStrategy
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.basic_chart_spec import BasicChartSpec
  from ..models.bubble_chart_spec import BubbleChartSpec
  from ..models.candlestick_chart_spec import CandlestickChartSpec
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.data_source_chart_properties import DataSourceChartProperties
  from ..models.filter_spec import FilterSpec
  from ..models.histogram_chart_spec import HistogramChartSpec
  from ..models.org_chart_spec import OrgChartSpec
  from ..models.pie_chart_spec import PieChartSpec
  from ..models.scorecard_chart_spec import ScorecardChartSpec
  from ..models.sort_spec import SortSpec
  from ..models.text_format import TextFormat
  from ..models.text_position import TextPosition
  from ..models.treemap_chart_spec import TreemapChartSpec
  from ..models.waterfall_chart_spec import WaterfallChartSpec





T = TypeVar("T", bound="ChartSpec")



@_attrs_define
class ChartSpec:
    """ The specifications of a chart.

        Attributes:
            alt_text (str | Unset): The alternative text that describes the chart. This is often used for accessibility.
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
            basic_chart (BasicChartSpec | Unset): The specification for a basic chart. See BasicChartType for the list of
                charts this supports.
            bubble_chart (BubbleChartSpec | Unset): A bubble chart.
            candlestick_chart (CandlestickChartSpec | Unset): A candlestick chart.
            data_source_chart_properties (DataSourceChartProperties | Unset): Properties of a data source chart.
            filter_specs (list[FilterSpec] | Unset): The filters applied to the source data of the chart. Only supported for
                data source charts.
            font_name (str | Unset): The name of the font to use by default for all chart text (e.g. title, axis labels,
                legend). If a font is specified for a specific part of the chart it will override this font name.
            hidden_dimension_strategy (ChartSpecHiddenDimensionStrategy | Unset): Determines how the charts will use hidden
                rows or columns.
            histogram_chart (HistogramChartSpec | Unset): A histogram chart. A histogram chart groups data items into bins,
                displaying each bin as a column of stacked items. Histograms are used to display the distribution of a dataset.
                Each column of items represents a range into which those items fall. The number of bins can be chosen
                automatically or specified explicitly.
            maximized (bool | Unset): True to make a chart fill the entire space in which it's rendered with minimum
                padding. False to use the default padding. (Not applicable to Geo and Org charts.)
            org_chart (OrgChartSpec | Unset): An org chart. Org charts require a unique set of labels in labels and may
                optionally include parent_labels and tooltips. parent_labels contain, for each node, the label identifying the
                parent node. tooltips contain, for each node, an optional tooltip. For example, to describe an OrgChart with
                Alice as the CEO, Bob as the President (reporting to Alice) and Cathy as VP of Sales (also reporting to Alice),
                have labels contain "Alice", "Bob", "Cathy", parent_labels contain "", "Alice", "Alice" and tooltips contain
                "CEO", "President", "VP Sales".
            pie_chart (PieChartSpec | Unset): A pie chart.
            scorecard_chart (ScorecardChartSpec | Unset): A scorecard chart. Scorecard charts are used to highlight key
                performance indicators, known as KPIs, on the spreadsheet. A scorecard chart can represent things like total
                sales, average cost, or a top selling item. You can specify a single data value, or aggregate over a range of
                data. Percentage or absolute difference from a baseline value can be highlighted, like changes over time.
            sort_specs (list[SortSpec] | Unset): The order to sort the chart data by. Only a single sort spec is supported.
                Only supported for data source charts.
            subtitle (str | Unset): The subtitle of the chart.
            subtitle_text_format (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that
                the field isn't specified.
            subtitle_text_position (TextPosition | Unset): Position settings for text.
            title (str | Unset): The title of the chart.
            title_text_format (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the
                field isn't specified.
            title_text_position (TextPosition | Unset): Position settings for text.
            treemap_chart (TreemapChartSpec | Unset): A Treemap chart.
            waterfall_chart (WaterfallChartSpec | Unset): A waterfall chart.
     """

    alt_text: str | Unset = UNSET
    background_color: Color | Unset = UNSET
    background_color_style: ColorStyle | Unset = UNSET
    basic_chart: BasicChartSpec | Unset = UNSET
    bubble_chart: BubbleChartSpec | Unset = UNSET
    candlestick_chart: CandlestickChartSpec | Unset = UNSET
    data_source_chart_properties: DataSourceChartProperties | Unset = UNSET
    filter_specs: list[FilterSpec] | Unset = UNSET
    font_name: str | Unset = UNSET
    hidden_dimension_strategy: ChartSpecHiddenDimensionStrategy | Unset = UNSET
    histogram_chart: HistogramChartSpec | Unset = UNSET
    maximized: bool | Unset = UNSET
    org_chart: OrgChartSpec | Unset = UNSET
    pie_chart: PieChartSpec | Unset = UNSET
    scorecard_chart: ScorecardChartSpec | Unset = UNSET
    sort_specs: list[SortSpec] | Unset = UNSET
    subtitle: str | Unset = UNSET
    subtitle_text_format: TextFormat | Unset = UNSET
    subtitle_text_position: TextPosition | Unset = UNSET
    title: str | Unset = UNSET
    title_text_format: TextFormat | Unset = UNSET
    title_text_position: TextPosition | Unset = UNSET
    treemap_chart: TreemapChartSpec | Unset = UNSET
    waterfall_chart: WaterfallChartSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.basic_chart_spec import BasicChartSpec
        from ..models.bubble_chart_spec import BubbleChartSpec
        from ..models.candlestick_chart_spec import CandlestickChartSpec
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.data_source_chart_properties import DataSourceChartProperties
        from ..models.filter_spec import FilterSpec
        from ..models.histogram_chart_spec import HistogramChartSpec
        from ..models.org_chart_spec import OrgChartSpec
        from ..models.pie_chart_spec import PieChartSpec
        from ..models.scorecard_chart_spec import ScorecardChartSpec
        from ..models.sort_spec import SortSpec
        from ..models.text_format import TextFormat
        from ..models.text_position import TextPosition
        from ..models.treemap_chart_spec import TreemapChartSpec
        from ..models.waterfall_chart_spec import WaterfallChartSpec
        alt_text = self.alt_text

        background_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.to_dict()

        background_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color_style, Unset):
            background_color_style = self.background_color_style.to_dict()

        basic_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_chart, Unset):
            basic_chart = self.basic_chart.to_dict()

        bubble_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bubble_chart, Unset):
            bubble_chart = self.bubble_chart.to_dict()

        candlestick_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.candlestick_chart, Unset):
            candlestick_chart = self.candlestick_chart.to_dict()

        data_source_chart_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_chart_properties, Unset):
            data_source_chart_properties = self.data_source_chart_properties.to_dict()

        filter_specs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_specs, Unset):
            filter_specs = []
            for filter_specs_item_data in self.filter_specs:
                filter_specs_item = filter_specs_item_data.to_dict()
                filter_specs.append(filter_specs_item)



        font_name = self.font_name

        hidden_dimension_strategy: str | Unset = UNSET
        if not isinstance(self.hidden_dimension_strategy, Unset):
            hidden_dimension_strategy = self.hidden_dimension_strategy.value


        histogram_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.histogram_chart, Unset):
            histogram_chart = self.histogram_chart.to_dict()

        maximized = self.maximized

        org_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.org_chart, Unset):
            org_chart = self.org_chart.to_dict()

        pie_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pie_chart, Unset):
            pie_chart = self.pie_chart.to_dict()

        scorecard_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scorecard_chart, Unset):
            scorecard_chart = self.scorecard_chart.to_dict()

        sort_specs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sort_specs, Unset):
            sort_specs = []
            for sort_specs_item_data in self.sort_specs:
                sort_specs_item = sort_specs_item_data.to_dict()
                sort_specs.append(sort_specs_item)



        subtitle = self.subtitle

        subtitle_text_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subtitle_text_format, Unset):
            subtitle_text_format = self.subtitle_text_format.to_dict()

        subtitle_text_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subtitle_text_position, Unset):
            subtitle_text_position = self.subtitle_text_position.to_dict()

        title = self.title

        title_text_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title_text_format, Unset):
            title_text_format = self.title_text_format.to_dict()

        title_text_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title_text_position, Unset):
            title_text_position = self.title_text_position.to_dict()

        treemap_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.treemap_chart, Unset):
            treemap_chart = self.treemap_chart.to_dict()

        waterfall_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.waterfall_chart, Unset):
            waterfall_chart = self.waterfall_chart.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if alt_text is not UNSET:
            field_dict["altText"] = alt_text
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if background_color_style is not UNSET:
            field_dict["backgroundColorStyle"] = background_color_style
        if basic_chart is not UNSET:
            field_dict["basicChart"] = basic_chart
        if bubble_chart is not UNSET:
            field_dict["bubbleChart"] = bubble_chart
        if candlestick_chart is not UNSET:
            field_dict["candlestickChart"] = candlestick_chart
        if data_source_chart_properties is not UNSET:
            field_dict["dataSourceChartProperties"] = data_source_chart_properties
        if filter_specs is not UNSET:
            field_dict["filterSpecs"] = filter_specs
        if font_name is not UNSET:
            field_dict["fontName"] = font_name
        if hidden_dimension_strategy is not UNSET:
            field_dict["hiddenDimensionStrategy"] = hidden_dimension_strategy
        if histogram_chart is not UNSET:
            field_dict["histogramChart"] = histogram_chart
        if maximized is not UNSET:
            field_dict["maximized"] = maximized
        if org_chart is not UNSET:
            field_dict["orgChart"] = org_chart
        if pie_chart is not UNSET:
            field_dict["pieChart"] = pie_chart
        if scorecard_chart is not UNSET:
            field_dict["scorecardChart"] = scorecard_chart
        if sort_specs is not UNSET:
            field_dict["sortSpecs"] = sort_specs
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if subtitle_text_format is not UNSET:
            field_dict["subtitleTextFormat"] = subtitle_text_format
        if subtitle_text_position is not UNSET:
            field_dict["subtitleTextPosition"] = subtitle_text_position
        if title is not UNSET:
            field_dict["title"] = title
        if title_text_format is not UNSET:
            field_dict["titleTextFormat"] = title_text_format
        if title_text_position is not UNSET:
            field_dict["titleTextPosition"] = title_text_position
        if treemap_chart is not UNSET:
            field_dict["treemapChart"] = treemap_chart
        if waterfall_chart is not UNSET:
            field_dict["waterfallChart"] = waterfall_chart

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_chart_spec import BasicChartSpec
        from ..models.bubble_chart_spec import BubbleChartSpec
        from ..models.candlestick_chart_spec import CandlestickChartSpec
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.data_source_chart_properties import DataSourceChartProperties
        from ..models.filter_spec import FilterSpec
        from ..models.histogram_chart_spec import HistogramChartSpec
        from ..models.org_chart_spec import OrgChartSpec
        from ..models.pie_chart_spec import PieChartSpec
        from ..models.scorecard_chart_spec import ScorecardChartSpec
        from ..models.sort_spec import SortSpec
        from ..models.text_format import TextFormat
        from ..models.text_position import TextPosition
        from ..models.treemap_chart_spec import TreemapChartSpec
        from ..models.waterfall_chart_spec import WaterfallChartSpec
        d = dict(src_dict)
        alt_text = d.pop("altText", UNSET)

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




        _basic_chart = d.pop("basicChart", UNSET)
        basic_chart: BasicChartSpec | Unset
        if isinstance(_basic_chart,  Unset):
            basic_chart = UNSET
        else:
            basic_chart = BasicChartSpec.from_dict(_basic_chart)




        _bubble_chart = d.pop("bubbleChart", UNSET)
        bubble_chart: BubbleChartSpec | Unset
        if isinstance(_bubble_chart,  Unset):
            bubble_chart = UNSET
        else:
            bubble_chart = BubbleChartSpec.from_dict(_bubble_chart)




        _candlestick_chart = d.pop("candlestickChart", UNSET)
        candlestick_chart: CandlestickChartSpec | Unset
        if isinstance(_candlestick_chart,  Unset):
            candlestick_chart = UNSET
        else:
            candlestick_chart = CandlestickChartSpec.from_dict(_candlestick_chart)




        _data_source_chart_properties = d.pop("dataSourceChartProperties", UNSET)
        data_source_chart_properties: DataSourceChartProperties | Unset
        if isinstance(_data_source_chart_properties,  Unset):
            data_source_chart_properties = UNSET
        else:
            data_source_chart_properties = DataSourceChartProperties.from_dict(_data_source_chart_properties)




        _filter_specs = d.pop("filterSpecs", UNSET)
        filter_specs: list[FilterSpec] | Unset = UNSET
        if _filter_specs is not UNSET:
            filter_specs = []
            for filter_specs_item_data in _filter_specs:
                filter_specs_item = FilterSpec.from_dict(filter_specs_item_data)



                filter_specs.append(filter_specs_item)


        font_name = d.pop("fontName", UNSET)

        _hidden_dimension_strategy = d.pop("hiddenDimensionStrategy", UNSET)
        hidden_dimension_strategy: ChartSpecHiddenDimensionStrategy | Unset
        if isinstance(_hidden_dimension_strategy,  Unset):
            hidden_dimension_strategy = UNSET
        else:
            hidden_dimension_strategy = ChartSpecHiddenDimensionStrategy(_hidden_dimension_strategy)




        _histogram_chart = d.pop("histogramChart", UNSET)
        histogram_chart: HistogramChartSpec | Unset
        if isinstance(_histogram_chart,  Unset):
            histogram_chart = UNSET
        else:
            histogram_chart = HistogramChartSpec.from_dict(_histogram_chart)




        maximized = d.pop("maximized", UNSET)

        _org_chart = d.pop("orgChart", UNSET)
        org_chart: OrgChartSpec | Unset
        if isinstance(_org_chart,  Unset):
            org_chart = UNSET
        else:
            org_chart = OrgChartSpec.from_dict(_org_chart)




        _pie_chart = d.pop("pieChart", UNSET)
        pie_chart: PieChartSpec | Unset
        if isinstance(_pie_chart,  Unset):
            pie_chart = UNSET
        else:
            pie_chart = PieChartSpec.from_dict(_pie_chart)




        _scorecard_chart = d.pop("scorecardChart", UNSET)
        scorecard_chart: ScorecardChartSpec | Unset
        if isinstance(_scorecard_chart,  Unset):
            scorecard_chart = UNSET
        else:
            scorecard_chart = ScorecardChartSpec.from_dict(_scorecard_chart)




        _sort_specs = d.pop("sortSpecs", UNSET)
        sort_specs: list[SortSpec] | Unset = UNSET
        if _sort_specs is not UNSET:
            sort_specs = []
            for sort_specs_item_data in _sort_specs:
                sort_specs_item = SortSpec.from_dict(sort_specs_item_data)



                sort_specs.append(sort_specs_item)


        subtitle = d.pop("subtitle", UNSET)

        _subtitle_text_format = d.pop("subtitleTextFormat", UNSET)
        subtitle_text_format: TextFormat | Unset
        if isinstance(_subtitle_text_format,  Unset):
            subtitle_text_format = UNSET
        else:
            subtitle_text_format = TextFormat.from_dict(_subtitle_text_format)




        _subtitle_text_position = d.pop("subtitleTextPosition", UNSET)
        subtitle_text_position: TextPosition | Unset
        if isinstance(_subtitle_text_position,  Unset):
            subtitle_text_position = UNSET
        else:
            subtitle_text_position = TextPosition.from_dict(_subtitle_text_position)




        title = d.pop("title", UNSET)

        _title_text_format = d.pop("titleTextFormat", UNSET)
        title_text_format: TextFormat | Unset
        if isinstance(_title_text_format,  Unset):
            title_text_format = UNSET
        else:
            title_text_format = TextFormat.from_dict(_title_text_format)




        _title_text_position = d.pop("titleTextPosition", UNSET)
        title_text_position: TextPosition | Unset
        if isinstance(_title_text_position,  Unset):
            title_text_position = UNSET
        else:
            title_text_position = TextPosition.from_dict(_title_text_position)




        _treemap_chart = d.pop("treemapChart", UNSET)
        treemap_chart: TreemapChartSpec | Unset
        if isinstance(_treemap_chart,  Unset):
            treemap_chart = UNSET
        else:
            treemap_chart = TreemapChartSpec.from_dict(_treemap_chart)




        _waterfall_chart = d.pop("waterfallChart", UNSET)
        waterfall_chart: WaterfallChartSpec | Unset
        if isinstance(_waterfall_chart,  Unset):
            waterfall_chart = UNSET
        else:
            waterfall_chart = WaterfallChartSpec.from_dict(_waterfall_chart)




        chart_spec = cls(
            alt_text=alt_text,
            background_color=background_color,
            background_color_style=background_color_style,
            basic_chart=basic_chart,
            bubble_chart=bubble_chart,
            candlestick_chart=candlestick_chart,
            data_source_chart_properties=data_source_chart_properties,
            filter_specs=filter_specs,
            font_name=font_name,
            hidden_dimension_strategy=hidden_dimension_strategy,
            histogram_chart=histogram_chart,
            maximized=maximized,
            org_chart=org_chart,
            pie_chart=pie_chart,
            scorecard_chart=scorecard_chart,
            sort_specs=sort_specs,
            subtitle=subtitle,
            subtitle_text_format=subtitle_text_format,
            subtitle_text_position=subtitle_text_position,
            title=title,
            title_text_format=title_text_format,
            title_text_position=title_text_position,
            treemap_chart=treemap_chart,
            waterfall_chart=waterfall_chart,
        )


        chart_spec.additional_properties = d
        return chart_spec

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
