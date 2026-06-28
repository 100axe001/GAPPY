from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_stats_bucket_response import UsageStatsBucketResponse


T = TypeVar("T", bound="UsageStatsResponse")


@_attrs_define
class UsageStatsResponse:
    """
    Attributes:
        end_date (datetime.datetime):
        granularity (str):
        items (list[UsageStatsBucketResponse]):
        start_date (datetime.datetime):
        total (int):
        group_by (None | str | Unset):
    """

    end_date: datetime.datetime
    granularity: str
    items: list[UsageStatsBucketResponse]
    start_date: datetime.datetime
    total: int
    group_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date.isoformat()

        granularity = self.granularity

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        start_date = self.start_date.isoformat()

        total = self.total

        group_by: None | str | Unset
        if isinstance(self.group_by, Unset):
            group_by = UNSET
        else:
            group_by = self.group_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_date": end_date,
                "granularity": granularity,
                "items": items,
                "start_date": start_date,
                "total": total,
            }
        )
        if group_by is not UNSET:
            field_dict["group_by"] = group_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_stats_bucket_response import UsageStatsBucketResponse

        d = dict(src_dict)
        end_date = isoparse(d.pop("end_date"))

        granularity = d.pop("granularity")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = UsageStatsBucketResponse.from_dict(items_item_data)

            items.append(items_item)

        start_date = isoparse(d.pop("start_date"))

        total = d.pop("total")

        def _parse_group_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_by = _parse_group_by(d.pop("group_by", UNSET))

        usage_stats_response = cls(
            end_date=end_date,
            granularity=granularity,
            items=items,
            start_date=start_date,
            total=total,
            group_by=group_by,
        )

        usage_stats_response.additional_properties = d
        return usage_stats_response

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
