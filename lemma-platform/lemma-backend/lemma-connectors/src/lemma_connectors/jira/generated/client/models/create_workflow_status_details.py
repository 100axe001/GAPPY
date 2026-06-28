from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_workflow_status_details_properties import CreateWorkflowStatusDetailsProperties





T = TypeVar("T", bound="CreateWorkflowStatusDetails")



@_attrs_define
class CreateWorkflowStatusDetails:
    """ The details of a transition status.

        Attributes:
            id (str): The ID of the status.
            properties (CreateWorkflowStatusDetailsProperties | Unset): The properties of the status.
     """

    id: str
    properties: CreateWorkflowStatusDetailsProperties | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workflow_status_details_properties import CreateWorkflowStatusDetailsProperties
        id = self.id

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_workflow_status_details_properties import CreateWorkflowStatusDetailsProperties
        d = dict(src_dict)
        id = d.pop("id")

        _properties = d.pop("properties", UNSET)
        properties: CreateWorkflowStatusDetailsProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = CreateWorkflowStatusDetailsProperties.from_dict(_properties)




        create_workflow_status_details = cls(
            id=id,
            properties=properties,
        )

        return create_workflow_status_details

