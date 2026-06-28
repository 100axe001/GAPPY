from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_status_properties import WorkflowStatusProperties





T = TypeVar("T", bound="WorkflowStatus")



@_attrs_define
class WorkflowStatus:
    """ Details of a workflow status.

        Attributes:
            id (str): The ID of the issue status.
            name (str): The name of the status in the workflow.
            properties (WorkflowStatusProperties | Unset): Additional properties that modify the behavior of issues in this
                status. Supports the properties `jira.issue.editable` and `issueEditable` (deprecated) that indicate whether
                issues are editable.
     """

    id: str
    name: str
    properties: WorkflowStatusProperties | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_status_properties import WorkflowStatusProperties
        id = self.id

        name = self.name

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
        })
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_status_properties import WorkflowStatusProperties
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        _properties = d.pop("properties", UNSET)
        properties: WorkflowStatusProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = WorkflowStatusProperties.from_dict(_properties)




        workflow_status = cls(
            id=id,
            name=name,
            properties=properties,
        )

        return workflow_status

