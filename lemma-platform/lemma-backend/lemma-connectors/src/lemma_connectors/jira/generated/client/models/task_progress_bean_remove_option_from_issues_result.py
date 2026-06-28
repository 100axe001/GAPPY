from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.task_progress_bean_remove_option_from_issues_result_status import TaskProgressBeanRemoveOptionFromIssuesResultStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.remove_option_from_issues_result import RemoveOptionFromIssuesResult





T = TypeVar("T", bound="TaskProgressBeanRemoveOptionFromIssuesResult")



@_attrs_define
class TaskProgressBeanRemoveOptionFromIssuesResult:
    """ Details about a task.

        Attributes:
            elapsed_runtime (int): The execution time of the task, in milliseconds.
            id (str): The ID of the task.
            last_update (int): A timestamp recording when the task progress was last updated.
            progress (int): The progress of the task, as a percentage complete.
            self_ (str): The URL of the task.
            status (TaskProgressBeanRemoveOptionFromIssuesResultStatus): The status of the task.
            submitted (int): A timestamp recording when the task was submitted.
            submitted_by (int): The ID of the user who submitted the task.
            description (str | Unset): The description of the task.
            finished (int | Unset): A timestamp recording when the task was finished.
            message (str | Unset): Information about the progress of the task.
            result (RemoveOptionFromIssuesResult | Unset):
            started (int | Unset): A timestamp recording when the task was started.
     """

    elapsed_runtime: int
    id: str
    last_update: int
    progress: int
    self_: str
    status: TaskProgressBeanRemoveOptionFromIssuesResultStatus
    submitted: int
    submitted_by: int
    description: str | Unset = UNSET
    finished: int | Unset = UNSET
    message: str | Unset = UNSET
    result: RemoveOptionFromIssuesResult | Unset = UNSET
    started: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.remove_option_from_issues_result import RemoveOptionFromIssuesResult
        elapsed_runtime = self.elapsed_runtime

        id = self.id

        last_update = self.last_update

        progress = self.progress

        self_ = self.self_

        status = self.status.value

        submitted = self.submitted

        submitted_by = self.submitted_by

        description = self.description

        finished = self.finished

        message = self.message

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        started = self.started


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "elapsedRuntime": elapsed_runtime,
            "id": id,
            "lastUpdate": last_update,
            "progress": progress,
            "self": self_,
            "status": status,
            "submitted": submitted,
            "submittedBy": submitted_by,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if finished is not UNSET:
            field_dict["finished"] = finished
        if message is not UNSET:
            field_dict["message"] = message
        if result is not UNSET:
            field_dict["result"] = result
        if started is not UNSET:
            field_dict["started"] = started

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remove_option_from_issues_result import RemoveOptionFromIssuesResult
        d = dict(src_dict)
        elapsed_runtime = d.pop("elapsedRuntime")

        id = d.pop("id")

        last_update = d.pop("lastUpdate")

        progress = d.pop("progress")

        self_ = d.pop("self")

        status = TaskProgressBeanRemoveOptionFromIssuesResultStatus(d.pop("status"))




        submitted = d.pop("submitted")

        submitted_by = d.pop("submittedBy")

        description = d.pop("description", UNSET)

        finished = d.pop("finished", UNSET)

        message = d.pop("message", UNSET)

        _result = d.pop("result", UNSET)
        result: RemoveOptionFromIssuesResult | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = RemoveOptionFromIssuesResult.from_dict(_result)




        started = d.pop("started", UNSET)

        task_progress_bean_remove_option_from_issues_result = cls(
            elapsed_runtime=elapsed_runtime,
            id=id,
            last_update=last_update,
            progress=progress,
            self_=self_,
            status=status,
            submitted=submitted,
            submitted_by=submitted_by,
            description=description,
            finished=finished,
            message=message,
            result=result,
            started=started,
        )

        return task_progress_bean_remove_option_from_issues_result

