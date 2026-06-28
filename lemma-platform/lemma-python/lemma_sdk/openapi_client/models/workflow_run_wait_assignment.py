from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_run_summary_response import WorkflowRunSummaryResponse
    from ..models.workflow_run_wait_response import WorkflowRunWaitResponse


T = TypeVar("T", bound="WorkflowRunWaitAssignment")


@_attrs_define
class WorkflowRunWaitAssignment:
    """
    Attributes:
        run (WorkflowRunSummaryResponse):
        wait (WorkflowRunWaitResponse):
    """

    run: WorkflowRunSummaryResponse
    wait: WorkflowRunWaitResponse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run = self.run.to_dict()

        wait = self.wait.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run": run,
                "wait": wait,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_run_summary_response import WorkflowRunSummaryResponse
        from ..models.workflow_run_wait_response import WorkflowRunWaitResponse

        d = dict(src_dict)
        run = WorkflowRunSummaryResponse.from_dict(d.pop("run"))

        wait = WorkflowRunWaitResponse.from_dict(d.pop("wait"))

        workflow_run_wait_assignment = cls(
            run=run,
            wait=wait,
        )

        workflow_run_wait_assignment.additional_properties = d
        return workflow_run_wait_assignment

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
