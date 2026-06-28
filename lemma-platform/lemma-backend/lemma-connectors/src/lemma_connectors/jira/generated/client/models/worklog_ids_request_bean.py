from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="WorklogIdsRequestBean")



@_attrs_define
class WorklogIdsRequestBean:
    """ 
        Attributes:
            ids (list[int]): A list of worklog IDs.
     """

    ids: list[int]





    def to_dict(self) -> dict[str, Any]:
        ids = self.ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ids": ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[int], d.pop("ids"))


        worklog_ids_request_bean = cls(
            ids=ids,
        )

        return worklog_ids_request_bean

