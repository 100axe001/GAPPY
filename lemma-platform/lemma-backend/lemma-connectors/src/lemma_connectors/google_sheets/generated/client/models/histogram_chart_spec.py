from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.histogram_chart_spec_legend_position import HistogramChartSpecLegendPosition
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.histogram_series import HistogramSeries





T = TypeVar("T", bound="HistogramChartSpec")



@_attrs_define
class HistogramChartSpec:
    """ A histogram chart. A histogram chart groups data items into bins, displaying each bin as a column of stacked items.
    Histograms are used to display the distribution of a dataset. Each column of items represents a range into which
    those items fall. The number of bins can be chosen automatically or specified explicitly.

        Attributes:
            bucket_size (float | Unset): By default the bucket size (the range of values stacked in a single column) is
                chosen automatically, but it may be overridden here. E.g., A bucket size of 1.5 results in buckets from 0 - 1.5,
                1.5 - 3.0, etc. Cannot be negative. This field is optional.
            legend_position (HistogramChartSpecLegendPosition | Unset): The position of the chart legend.
            outlier_percentile (float | Unset): The outlier percentile is used to ensure that outliers do not adversely
                affect the calculation of bucket sizes. For example, setting an outlier percentile of 0.05 indicates that the
                top and bottom 5% of values when calculating buckets. The values are still included in the chart, they will be
                added to the first or last buckets instead of their own buckets. Must be between 0.0 and 0.5.
            series (list[HistogramSeries] | Unset): The series for a histogram may be either a single series of values to be
                bucketed or multiple series, each of the same length, containing the name of the series followed by the values
                to be bucketed for that series.
            show_item_dividers (bool | Unset): Whether horizontal divider lines should be displayed between items in each
                column.
     """

    bucket_size: float | Unset = UNSET
    legend_position: HistogramChartSpecLegendPosition | Unset = UNSET
    outlier_percentile: float | Unset = UNSET
    series: list[HistogramSeries] | Unset = UNSET
    show_item_dividers: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.histogram_series import HistogramSeries
        bucket_size = self.bucket_size

        legend_position: str | Unset = UNSET
        if not isinstance(self.legend_position, Unset):
            legend_position = self.legend_position.value


        outlier_percentile = self.outlier_percentile

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)



        show_item_dividers = self.show_item_dividers


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bucket_size is not UNSET:
            field_dict["bucketSize"] = bucket_size
        if legend_position is not UNSET:
            field_dict["legendPosition"] = legend_position
        if outlier_percentile is not UNSET:
            field_dict["outlierPercentile"] = outlier_percentile
        if series is not UNSET:
            field_dict["series"] = series
        if show_item_dividers is not UNSET:
            field_dict["showItemDividers"] = show_item_dividers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.histogram_series import HistogramSeries
        d = dict(src_dict)
        bucket_size = d.pop("bucketSize", UNSET)

        _legend_position = d.pop("legendPosition", UNSET)
        legend_position: HistogramChartSpecLegendPosition | Unset
        if isinstance(_legend_position,  Unset):
            legend_position = UNSET
        else:
            legend_position = HistogramChartSpecLegendPosition(_legend_position)




        outlier_percentile = d.pop("outlierPercentile", UNSET)

        _series = d.pop("series", UNSET)
        series: list[HistogramSeries] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = HistogramSeries.from_dict(series_item_data)



                series.append(series_item)


        show_item_dividers = d.pop("showItemDividers", UNSET)

        histogram_chart_spec = cls(
            bucket_size=bucket_size,
            legend_position=legend_position,
            outlier_percentile=outlier_percentile,
            series=series,
            show_item_dividers=show_item_dividers,
        )


        histogram_chart_spec.additional_properties = d
        return histogram_chart_spec

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
