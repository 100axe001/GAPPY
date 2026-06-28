from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_scheme_associations import WorkflowSchemeAssociations





T = TypeVar("T", bound="ContainerOfWorkflowSchemeAssociations")



@_attrs_define
class ContainerOfWorkflowSchemeAssociations:
    """ A container for a list of workflow schemes together with the projects they are associated with.

        Attributes:
            values (list[WorkflowSchemeAssociations]): A list of workflow schemes together with projects they are associated
                with.
     """

    values: list[WorkflowSchemeAssociations]





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_scheme_associations import WorkflowSchemeAssociations
        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "values": values,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_scheme_associations import WorkflowSchemeAssociations
        d = dict(src_dict)
        values = []
        _values = d.pop("values")
        for values_item_data in (_values):
            values_item = WorkflowSchemeAssociations.from_dict(values_item_data)



            values.append(values_item)


        container_of_workflow_scheme_associations = cls(
            values=values,
        )

        return container_of_workflow_scheme_associations

