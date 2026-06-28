from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_summary import OperationSummary


T = TypeVar("T", bound="OperationDiscoverResponse")


@_attrs_define
class OperationDiscoverResponse:
    """Structured result for operation discovery within one connector.

    Attributes:
        connector_id (str): Connector identifier.
        items (list[OperationSummary]): Matching operations with compact descriptions.
        returned_count (int): Number of operations returned in this response.
        total_operations (int): Total operations available for the connector.
        query (None | str | Unset): Optional discovery query used to rank or filter operations.
    """

    connector_id: str
    items: list[OperationSummary]
    returned_count: int
    total_operations: int
    query: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_id = self.connector_id

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        returned_count = self.returned_count

        total_operations = self.total_operations

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connector_id": connector_id,
                "items": items,
                "returned_count": returned_count,
                "total_operations": total_operations,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.operation_summary import OperationSummary

        d = dict(src_dict)
        connector_id = d.pop("connector_id")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OperationSummary.from_dict(items_item_data)

            items.append(items_item)

        returned_count = d.pop("returned_count")

        total_operations = d.pop("total_operations")

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        operation_discover_response = cls(
            connector_id=connector_id,
            items=items,
            returned_count=returned_count,
            total_operations=total_operations,
            query=query,
        )

        operation_discover_response.additional_properties = d
        return operation_discover_response

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
