from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.refresh_data_source_object_execution_status import RefreshDataSourceObjectExecutionStatus





T = TypeVar("T", bound="RefreshDataSourceResponse")



@_attrs_define
class RefreshDataSourceResponse:
    """ The response from refreshing one or multiple data source objects.

        Attributes:
            statuses (list[RefreshDataSourceObjectExecutionStatus] | Unset): All the refresh status for the data source
                object references specified in the request. If is_all is specified, the field contains only those in failure
                status.
     """

    statuses: list[RefreshDataSourceObjectExecutionStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.refresh_data_source_object_execution_status import RefreshDataSourceObjectExecutionStatus
        statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()
                statuses.append(statuses_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if statuses is not UNSET:
            field_dict["statuses"] = statuses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refresh_data_source_object_execution_status import RefreshDataSourceObjectExecutionStatus
        d = dict(src_dict)
        _statuses = d.pop("statuses", UNSET)
        statuses: list[RefreshDataSourceObjectExecutionStatus] | Unset = UNSET
        if _statuses is not UNSET:
            statuses = []
            for statuses_item_data in _statuses:
                statuses_item = RefreshDataSourceObjectExecutionStatus.from_dict(statuses_item_data)



                statuses.append(statuses_item)


        refresh_data_source_response = cls(
            statuses=statuses,
        )


        refresh_data_source_response.additional_properties = d
        return refresh_data_source_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
