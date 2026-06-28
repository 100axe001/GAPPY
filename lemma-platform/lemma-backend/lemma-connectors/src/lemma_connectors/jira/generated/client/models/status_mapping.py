from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="StatusMapping")



@_attrs_define
class StatusMapping:
    """ Details about the mapping from a status to a new status for an issue type.

        Attributes:
            issue_type_id (str): The ID of the issue type.
            new_status_id (str): The ID of the new status.
            status_id (str): The ID of the status.
     """

    issue_type_id: str
    new_status_id: str
    status_id: str





    def to_dict(self) -> dict[str, Any]:
        issue_type_id = self.issue_type_id

        new_status_id = self.new_status_id

        status_id = self.status_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeId": issue_type_id,
            "newStatusId": new_status_id,
            "statusId": status_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_id = d.pop("issueTypeId")

        new_status_id = d.pop("newStatusId")

        status_id = d.pop("statusId")

        status_mapping = cls(
            issue_type_id=issue_type_id,
            new_status_id=new_status_id,
            status_id=status_id,
        )

        return status_mapping

