from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TimeTrackingDetails")



@_attrs_define
class TimeTrackingDetails:
    """ Time tracking details.

        Attributes:
            original_estimate (str | Unset): The original estimate of time needed for this issue in readable format.
            original_estimate_seconds (int | Unset): The original estimate of time needed for this issue in seconds.
            remaining_estimate (str | Unset): The remaining estimate of time needed for this issue in readable format.
            remaining_estimate_seconds (int | Unset): The remaining estimate of time needed for this issue in seconds.
            time_spent (str | Unset): Time worked on this issue in readable format.
            time_spent_seconds (int | Unset): Time worked on this issue in seconds.
     """

    original_estimate: str | Unset = UNSET
    original_estimate_seconds: int | Unset = UNSET
    remaining_estimate: str | Unset = UNSET
    remaining_estimate_seconds: int | Unset = UNSET
    time_spent: str | Unset = UNSET
    time_spent_seconds: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        original_estimate = self.original_estimate

        original_estimate_seconds = self.original_estimate_seconds

        remaining_estimate = self.remaining_estimate

        remaining_estimate_seconds = self.remaining_estimate_seconds

        time_spent = self.time_spent

        time_spent_seconds = self.time_spent_seconds


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if original_estimate is not UNSET:
            field_dict["originalEstimate"] = original_estimate
        if original_estimate_seconds is not UNSET:
            field_dict["originalEstimateSeconds"] = original_estimate_seconds
        if remaining_estimate is not UNSET:
            field_dict["remainingEstimate"] = remaining_estimate
        if remaining_estimate_seconds is not UNSET:
            field_dict["remainingEstimateSeconds"] = remaining_estimate_seconds
        if time_spent is not UNSET:
            field_dict["timeSpent"] = time_spent
        if time_spent_seconds is not UNSET:
            field_dict["timeSpentSeconds"] = time_spent_seconds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        original_estimate = d.pop("originalEstimate", UNSET)

        original_estimate_seconds = d.pop("originalEstimateSeconds", UNSET)

        remaining_estimate = d.pop("remainingEstimate", UNSET)

        remaining_estimate_seconds = d.pop("remainingEstimateSeconds", UNSET)

        time_spent = d.pop("timeSpent", UNSET)

        time_spent_seconds = d.pop("timeSpentSeconds", UNSET)

        time_tracking_details = cls(
            original_estimate=original_estimate,
            original_estimate_seconds=original_estimate_seconds,
            remaining_estimate=remaining_estimate,
            remaining_estimate_seconds=remaining_estimate_seconds,
            time_spent=time_spent,
            time_spent_seconds=time_spent_seconds,
        )

        return time_tracking_details

