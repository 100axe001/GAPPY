from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.entity_property import EntityProperty





T = TypeVar("T", bound="ChangedWorklog")



@_attrs_define
class ChangedWorklog:
    """ Details of a changed worklog.

        Attributes:
            properties (list[EntityProperty] | Unset): Details of properties associated with the change.
            updated_time (int | Unset): The datetime of the change.
            worklog_id (int | Unset): The ID of the worklog.
     """

    properties: list[EntityProperty] | Unset = UNSET
    updated_time: int | Unset = UNSET
    worklog_id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_property import EntityProperty
        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)



        updated_time = self.updated_time

        worklog_id = self.worklog_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if properties is not UNSET:
            field_dict["properties"] = properties
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time
        if worklog_id is not UNSET:
            field_dict["worklogId"] = worklog_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_property import EntityProperty
        d = dict(src_dict)
        _properties = d.pop("properties", UNSET)
        properties: list[EntityProperty] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = EntityProperty.from_dict(properties_item_data)



                properties.append(properties_item)


        updated_time = d.pop("updatedTime", UNSET)

        worklog_id = d.pop("worklogId", UNSET)

        changed_worklog = cls(
            properties=properties,
            updated_time=updated_time,
            worklog_id=worklog_id,
        )

        return changed_worklog

