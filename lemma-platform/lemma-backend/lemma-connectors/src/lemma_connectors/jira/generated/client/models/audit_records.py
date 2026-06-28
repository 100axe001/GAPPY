from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.audit_record_bean import AuditRecordBean





T = TypeVar("T", bound="AuditRecords")



@_attrs_define
class AuditRecords:
    """ Container for a list of audit records.

        Attributes:
            limit (int | Unset): The requested or default limit on the number of audit items to be returned.
            offset (int | Unset): The number of audit items skipped before the first item in this list.
            records (list[AuditRecordBean] | Unset): The list of audit items.
            total (int | Unset): The total number of audit items returned.
     """

    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    records: list[AuditRecordBean] | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_record_bean import AuditRecordBean
        limit = self.limit

        offset = self.offset

        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)



        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if records is not UNSET:
            field_dict["records"] = records
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_record_bean import AuditRecordBean
        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        _records = d.pop("records", UNSET)
        records: list[AuditRecordBean] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:
                records_item = AuditRecordBean.from_dict(records_item_data)



                records.append(records_item)


        total = d.pop("total", UNSET)

        audit_records = cls(
            limit=limit,
            offset=offset,
            records=records,
            total=total,
        )

        return audit_records

