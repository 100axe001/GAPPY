from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_run_form_submit_request_inputs import (
        WorkflowRunFormSubmitRequestInputs,
    )


T = TypeVar("T", bound="WorkflowRunFormSubmitRequest")


@_attrs_define
class WorkflowRunFormSubmitRequest:
    """Canonical form submission payload — identical across web, SDKs, CLI.

    Attributes:
        node_id (str): Id of the FORM node being submitted. Must match the run's active wait; mismatches return 422.
        inputs (WorkflowRunFormSubmitRequestInputs | Unset): Form field values keyed by field name.
    """

    node_id: str
    inputs: WorkflowRunFormSubmitRequestInputs | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "node_id": node_id,
            }
        )
        if inputs is not UNSET:
            field_dict["inputs"] = inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_run_form_submit_request_inputs import (
            WorkflowRunFormSubmitRequestInputs,
        )

        d = dict(src_dict)
        node_id = d.pop("node_id")

        _inputs = d.pop("inputs", UNSET)
        inputs: WorkflowRunFormSubmitRequestInputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = WorkflowRunFormSubmitRequestInputs.from_dict(_inputs)

        workflow_run_form_submit_request = cls(
            node_id=node_id,
            inputs=inputs,
        )

        return workflow_run_form_submit_request
