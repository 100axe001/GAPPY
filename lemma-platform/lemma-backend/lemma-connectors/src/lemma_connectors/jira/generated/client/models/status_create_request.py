from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.status_create import StatusCreate
  from ..models.status_scope import StatusScope





T = TypeVar("T", bound="StatusCreateRequest")



@_attrs_define
class StatusCreateRequest:
    """ Details of the statuses being created and their scope.

        Attributes:
            scope (StatusScope): The scope of the status.
            statuses (list[StatusCreate]): Details of the statuses being created.
     """

    scope: StatusScope
    statuses: list[StatusCreate]





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_create import StatusCreate
        from ..models.status_scope import StatusScope
        scope = self.scope.to_dict()

        statuses = []
        for statuses_item_data in self.statuses:
            statuses_item = statuses_item_data.to_dict()
            statuses.append(statuses_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "scope": scope,
            "statuses": statuses,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_create import StatusCreate
        from ..models.status_scope import StatusScope
        d = dict(src_dict)
        scope = StatusScope.from_dict(d.pop("scope"))




        statuses = []
        _statuses = d.pop("statuses")
        for statuses_item_data in (_statuses):
            statuses_item = StatusCreate.from_dict(statuses_item_data)



            statuses.append(statuses_item)


        status_create_request = cls(
            scope=scope,
            statuses=statuses,
        )

        return status_create_request

