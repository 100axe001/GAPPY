from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageStatsBucketResponse")


@_attrs_define
class UsageStatsBucketResponse:
    """
    Attributes:
        bucket (datetime.datetime):
        input_tokens (int):
        output_tokens (int):
        system_cost_usd (float):
        total_tokens (int):
        units (float):
        group (None | str | Unset):
    """

    bucket: datetime.datetime
    input_tokens: int
    output_tokens: int
    system_cost_usd: float
    total_tokens: int
    units: float
    group: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket.isoformat()

        input_tokens = self.input_tokens

        output_tokens = self.output_tokens

        system_cost_usd = self.system_cost_usd

        total_tokens = self.total_tokens

        units = self.units

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "system_cost_usd": system_cost_usd,
                "total_tokens": total_tokens,
                "units": units,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = isoparse(d.pop("bucket"))

        input_tokens = d.pop("input_tokens")

        output_tokens = d.pop("output_tokens")

        system_cost_usd = d.pop("system_cost_usd")

        total_tokens = d.pop("total_tokens")

        units = d.pop("units")

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        usage_stats_bucket_response = cls(
            bucket=bucket,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            system_cost_usd=system_cost_usd,
            total_tokens=total_tokens,
            units=units,
            group=group,
        )

        usage_stats_bucket_response.additional_properties = d
        return usage_stats_bucket_response

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
