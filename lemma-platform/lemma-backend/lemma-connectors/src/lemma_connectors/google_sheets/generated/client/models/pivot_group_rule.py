from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.date_time_rule import DateTimeRule
  from ..models.histogram_rule import HistogramRule
  from ..models.manual_rule import ManualRule





T = TypeVar("T", bound="PivotGroupRule")



@_attrs_define
class PivotGroupRule:
    """ An optional setting on a PivotGroup that defines buckets for the values in the source data column rather than
    breaking out each individual value. Only one PivotGroup with a group rule may be added for each column in the source
    data, though on any given column you may add both a PivotGroup that has a rule and a PivotGroup that does not.

        Attributes:
            date_time_rule (DateTimeRule | Unset): Allows you to organize the date-time values in a source data column into
                buckets based on selected parts of their date or time values. For example, consider a pivot table showing sales
                transactions by date: +----------+--------------+ | Date | SUM of Sales | +----------+--------------+ | 1/1/2017
                | $621.14 | | 2/3/2017 | $708.84 | | 5/8/2017 | $326.84 | ... +----------+--------------+ Applying a date-time
                group rule with a DateTimeRuleType of YEAR_MONTH results in the following pivot table.
                +--------------+--------------+ | Grouped Date | SUM of Sales | +--------------+--------------+ | 2017-Jan |
                $53,731.78 | | 2017-Feb | $83,475.32 | | 2017-Mar | $94,385.05 | ... +--------------+--------------+
            histogram_rule (HistogramRule | Unset): Allows you to organize the numeric values in a source data column into
                buckets of a constant size. All values from HistogramRule.start to HistogramRule.end are placed into groups of
                size HistogramRule.interval. In addition, all values below HistogramRule.start are placed in one group, and all
                values above HistogramRule.end are placed in another. Only HistogramRule.interval is required, though if
                HistogramRule.start and HistogramRule.end are both provided, HistogramRule.start must be less than
                HistogramRule.end. For example, a pivot table showing average purchase amount by age that has 50+ rows:
                +-----+-------------------+ | Age | AVERAGE of Amount | +-----+-------------------+ | 16 | $27.13 | | 17 | $5.24
                | | 18 | $20.15 | ... +-----+-------------------+ could be turned into a pivot table that looks like the one
                below by applying a histogram group rule with a HistogramRule.start of 25, an HistogramRule.interval of 20, and
                an HistogramRule.end of 65. +-------------+-------------------+ | Grouped Age | AVERAGE of Amount |
                +-------------+-------------------+ | < 25 | $19.34 | | 25-45 | $31.43 | | 45-65 | $35.87 | | > 65 | $27.55 |
                +-------------+-------------------+ | Grand Total | $29.12 | +-------------+-------------------+
            manual_rule (ManualRule | Unset): Allows you to manually organize the values in a source data column into
                buckets with names of your choosing. For example, a pivot table that aggregates population by state:
                +-------+-------------------+ | State | SUM of Population | +-------+-------------------+ | AK | 0.7 | | AL |
                4.8 | | AR | 2.9 | ... +-------+-------------------+ could be turned into a pivot table that aggregates
                population by time zone by providing a list of groups (for example, groupName = 'Central', items = ['AL', 'AR',
                'IA', ...]) to a manual group rule. Note that a similar effect could be achieved by adding a time zone column to
                the source data and adjusting the pivot table. +-----------+-------------------+ | Time Zone | SUM of Population
                | +-----------+-------------------+ | Central | 106.3 | | Eastern | 151.9 | | Mountain | 17.4 | ...
                +-----------+-------------------+
     """

    date_time_rule: DateTimeRule | Unset = UNSET
    histogram_rule: HistogramRule | Unset = UNSET
    manual_rule: ManualRule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.date_time_rule import DateTimeRule
        from ..models.histogram_rule import HistogramRule
        from ..models.manual_rule import ManualRule
        date_time_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_time_rule, Unset):
            date_time_rule = self.date_time_rule.to_dict()

        histogram_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.histogram_rule, Unset):
            histogram_rule = self.histogram_rule.to_dict()

        manual_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manual_rule, Unset):
            manual_rule = self.manual_rule.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date_time_rule is not UNSET:
            field_dict["dateTimeRule"] = date_time_rule
        if histogram_rule is not UNSET:
            field_dict["histogramRule"] = histogram_rule
        if manual_rule is not UNSET:
            field_dict["manualRule"] = manual_rule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_time_rule import DateTimeRule
        from ..models.histogram_rule import HistogramRule
        from ..models.manual_rule import ManualRule
        d = dict(src_dict)
        _date_time_rule = d.pop("dateTimeRule", UNSET)
        date_time_rule: DateTimeRule | Unset
        if isinstance(_date_time_rule,  Unset):
            date_time_rule = UNSET
        else:
            date_time_rule = DateTimeRule.from_dict(_date_time_rule)




        _histogram_rule = d.pop("histogramRule", UNSET)
        histogram_rule: HistogramRule | Unset
        if isinstance(_histogram_rule,  Unset):
            histogram_rule = UNSET
        else:
            histogram_rule = HistogramRule.from_dict(_histogram_rule)




        _manual_rule = d.pop("manualRule", UNSET)
        manual_rule: ManualRule | Unset
        if isinstance(_manual_rule,  Unset):
            manual_rule = UNSET
        else:
            manual_rule = ManualRule.from_dict(_manual_rule)




        pivot_group_rule = cls(
            date_time_rule=date_time_rule,
            histogram_rule=histogram_rule,
            manual_rule=manual_rule,
        )


        pivot_group_rule.additional_properties = d
        return pivot_group_rule

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
