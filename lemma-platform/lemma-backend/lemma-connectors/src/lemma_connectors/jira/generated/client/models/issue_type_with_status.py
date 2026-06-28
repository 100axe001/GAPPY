from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.status_details import StatusDetails





T = TypeVar("T", bound="IssueTypeWithStatus")



@_attrs_define
class IssueTypeWithStatus:
    """ Status details for an issue type.

        Attributes:
            id (str): The ID of the issue type.
            name (str): The name of the issue type.
            self_ (str): The URL of the issue type's status details.
            statuses (list[StatusDetails]): List of status details for the issue type.
            subtask (bool): Whether this issue type represents subtasks.
     """

    id: str
    name: str
    self_: str
    statuses: list[StatusDetails]
    subtask: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_details import StatusDetails
        id = self.id

        name = self.name

        self_ = self.self_

        statuses = []
        for statuses_item_data in self.statuses:
            statuses_item = statuses_item_data.to_dict()
            statuses.append(statuses_item)



        subtask = self.subtask


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "self": self_,
            "statuses": statuses,
            "subtask": subtask,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_details import StatusDetails
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        self_ = d.pop("self")

        statuses = []
        _statuses = d.pop("statuses")
        for statuses_item_data in (_statuses):
            statuses_item = StatusDetails.from_dict(statuses_item_data)



            statuses.append(statuses_item)


        subtask = d.pop("subtask")

        issue_type_with_status = cls(
            id=id,
            name=name,
            self_=self_,
            statuses=statuses,
            subtask=subtask,
        )

        return issue_type_with_status

