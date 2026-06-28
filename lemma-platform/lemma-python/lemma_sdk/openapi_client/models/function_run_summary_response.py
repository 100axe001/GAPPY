from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.function_run_status import FunctionRunStatus

T = TypeVar("T", bound="FunctionRunSummaryResponse")


@_attrs_define
class FunctionRunSummaryResponse:
    """Function run summary for list responses.

    Attributes:
        completed_at (Any):
        created_at (Any):
        function_id (UUID):
        id (UUID):
        started_at (Any):
        status (FunctionRunStatus): Status of a function run.
        user_id (UUID):
    """

    completed_at: Any
    created_at: Any
    function_id: UUID
    id: UUID
    started_at: Any
    status: FunctionRunStatus
    user_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed_at = self.completed_at

        created_at = self.created_at

        function_id = str(self.function_id)

        id = str(self.id)

        started_at = self.started_at

        status = self.status.value

        user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completed_at": completed_at,
                "created_at": created_at,
                "function_id": function_id,
                "id": id,
                "started_at": started_at,
                "status": status,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completed_at = d.pop("completed_at")

        created_at = d.pop("created_at")

        function_id = UUID(d.pop("function_id"))

        id = UUID(d.pop("id"))

        started_at = d.pop("started_at")

        status = FunctionRunStatus(d.pop("status"))

        user_id = UUID(d.pop("user_id"))

        function_run_summary_response = cls(
            completed_at=completed_at,
            created_at=created_at,
            function_id=function_id,
            id=id,
            started_at=started_at,
            status=status,
            user_id=user_id,
        )

        function_run_summary_response.additional_properties = d
        return function_run_summary_response

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
