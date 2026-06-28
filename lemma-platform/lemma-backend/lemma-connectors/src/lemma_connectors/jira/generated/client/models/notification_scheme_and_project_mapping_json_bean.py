from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="NotificationSchemeAndProjectMappingJsonBean")



@_attrs_define
class NotificationSchemeAndProjectMappingJsonBean:
    """ 
        Attributes:
            notification_scheme_id (str | Unset):
            project_id (str | Unset):
     """

    notification_scheme_id: str | Unset = UNSET
    project_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        notification_scheme_id = self.notification_scheme_id

        project_id = self.project_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if notification_scheme_id is not UNSET:
            field_dict["notificationSchemeId"] = notification_scheme_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        notification_scheme_id = d.pop("notificationSchemeId", UNSET)

        project_id = d.pop("projectId", UNSET)

        notification_scheme_and_project_mapping_json_bean = cls(
            notification_scheme_id=notification_scheme_id,
            project_id=project_id,
        )

        return notification_scheme_and_project_mapping_json_bean

