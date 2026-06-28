from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.status_mapping import StatusMapping





T = TypeVar("T", bound="PublishDraftWorkflowScheme")



@_attrs_define
class PublishDraftWorkflowScheme:
    """ Details about the status mappings for publishing a draft workflow scheme.

        Attributes:
            status_mappings (list[StatusMapping] | Unset): Mappings of statuses to new statuses for issue types.
     """

    status_mappings: list[StatusMapping] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_mapping import StatusMapping
        status_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.status_mappings, Unset):
            status_mappings = []
            for status_mappings_item_data in self.status_mappings:
                status_mappings_item = status_mappings_item_data.to_dict()
                status_mappings.append(status_mappings_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if status_mappings is not UNSET:
            field_dict["statusMappings"] = status_mappings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_mapping import StatusMapping
        d = dict(src_dict)
        _status_mappings = d.pop("statusMappings", UNSET)
        status_mappings: list[StatusMapping] | Unset = UNSET
        if _status_mappings is not UNSET:
            status_mappings = []
            for status_mappings_item_data in _status_mappings:
                status_mappings_item = StatusMapping.from_dict(status_mappings_item_data)



                status_mappings.append(status_mappings_item)


        publish_draft_workflow_scheme = cls(
            status_mappings=status_mappings,
        )

        return publish_draft_workflow_scheme

