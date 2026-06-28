from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.status_update import StatusUpdate





T = TypeVar("T", bound="StatusUpdateRequest")



@_attrs_define
class StatusUpdateRequest:
    """ The list of statuses that will be updated.

        Attributes:
            statuses (list[StatusUpdate] | Unset): The list of statuses that will be updated.
     """

    statuses: list[StatusUpdate] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_update import StatusUpdate
        statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()
                statuses.append(statuses_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if statuses is not UNSET:
            field_dict["statuses"] = statuses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_update import StatusUpdate
        d = dict(src_dict)
        _statuses = d.pop("statuses", UNSET)
        statuses: list[StatusUpdate] | Unset = UNSET
        if _statuses is not UNSET:
            statuses = []
            for statuses_item_data in _statuses:
                statuses_item = StatusUpdate.from_dict(statuses_item_data)



                statuses.append(statuses_item)


        status_update_request = cls(
            statuses=statuses,
        )

        return status_update_request

