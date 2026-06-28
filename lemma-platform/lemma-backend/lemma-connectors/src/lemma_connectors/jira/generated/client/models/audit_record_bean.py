from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.associated_item_bean import AssociatedItemBean
  from ..models.changed_value_bean import ChangedValueBean





T = TypeVar("T", bound="AuditRecordBean")



@_attrs_define
class AuditRecordBean:
    """ An audit record.

        Attributes:
            associated_items (list[AssociatedItemBean] | Unset): The list of items associated with the changed record.
            author_key (str | Unset): Deprecated, use `authorAccountId` instead. The key of the user who created the audit
                record.
            category (str | Unset): The category of the audit record. For a list of these categories, see the help article
                [Auditing in Jira applications](https://confluence.atlassian.com/x/noXKM).
            changed_values (list[ChangedValueBean] | Unset): The list of values changed in the record event.
            created (datetime.datetime | Unset): The date and time on which the audit record was created.
            description (str | Unset): The description of the audit record.
            event_source (str | Unset): The event the audit record originated from.
            id (int | Unset): The ID of the audit record.
            object_item (AssociatedItemBean | Unset): Details of an item associated with the changed record.
            remote_address (str | Unset): The URL of the computer where the creation of the audit record was initiated.
            summary (str | Unset): The summary of the audit record.
     """

    associated_items: list[AssociatedItemBean] | Unset = UNSET
    author_key: str | Unset = UNSET
    category: str | Unset = UNSET
    changed_values: list[ChangedValueBean] | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    event_source: str | Unset = UNSET
    id: int | Unset = UNSET
    object_item: AssociatedItemBean | Unset = UNSET
    remote_address: str | Unset = UNSET
    summary: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.associated_item_bean import AssociatedItemBean
        from ..models.changed_value_bean import ChangedValueBean
        associated_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.associated_items, Unset):
            associated_items = []
            for associated_items_item_data in self.associated_items:
                associated_items_item = associated_items_item_data.to_dict()
                associated_items.append(associated_items_item)



        author_key = self.author_key

        category = self.category

        changed_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changed_values, Unset):
            changed_values = []
            for changed_values_item_data in self.changed_values:
                changed_values_item = changed_values_item_data.to_dict()
                changed_values.append(changed_values_item)



        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        description = self.description

        event_source = self.event_source

        id = self.id

        object_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_item, Unset):
            object_item = self.object_item.to_dict()

        remote_address = self.remote_address

        summary = self.summary


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if associated_items is not UNSET:
            field_dict["associatedItems"] = associated_items
        if author_key is not UNSET:
            field_dict["authorKey"] = author_key
        if category is not UNSET:
            field_dict["category"] = category
        if changed_values is not UNSET:
            field_dict["changedValues"] = changed_values
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if event_source is not UNSET:
            field_dict["eventSource"] = event_source
        if id is not UNSET:
            field_dict["id"] = id
        if object_item is not UNSET:
            field_dict["objectItem"] = object_item
        if remote_address is not UNSET:
            field_dict["remoteAddress"] = remote_address
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.associated_item_bean import AssociatedItemBean
        from ..models.changed_value_bean import ChangedValueBean
        d = dict(src_dict)
        _associated_items = d.pop("associatedItems", UNSET)
        associated_items: list[AssociatedItemBean] | Unset = UNSET
        if _associated_items is not UNSET:
            associated_items = []
            for associated_items_item_data in _associated_items:
                associated_items_item = AssociatedItemBean.from_dict(associated_items_item_data)



                associated_items.append(associated_items_item)


        author_key = d.pop("authorKey", UNSET)

        category = d.pop("category", UNSET)

        _changed_values = d.pop("changedValues", UNSET)
        changed_values: list[ChangedValueBean] | Unset = UNSET
        if _changed_values is not UNSET:
            changed_values = []
            for changed_values_item_data in _changed_values:
                changed_values_item = ChangedValueBean.from_dict(changed_values_item_data)



                changed_values.append(changed_values_item)


        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        description = d.pop("description", UNSET)

        event_source = d.pop("eventSource", UNSET)

        id = d.pop("id", UNSET)

        _object_item = d.pop("objectItem", UNSET)
        object_item: AssociatedItemBean | Unset
        if isinstance(_object_item,  Unset):
            object_item = UNSET
        else:
            object_item = AssociatedItemBean.from_dict(_object_item)




        remote_address = d.pop("remoteAddress", UNSET)

        summary = d.pop("summary", UNSET)

        audit_record_bean = cls(
            associated_items=associated_items,
            author_key=author_key,
            category=category,
            changed_values=changed_values,
            created=created,
            description=description,
            event_source=event_source,
            id=id,
            object_item=object_item,
            remote_address=remote_address,
            summary=summary,
        )

        return audit_record_bean

