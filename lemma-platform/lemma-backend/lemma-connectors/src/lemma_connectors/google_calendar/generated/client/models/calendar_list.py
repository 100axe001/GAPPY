from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.calendar_list_entry import CalendarListEntry





T = TypeVar("T", bound="CalendarList")



@_attrs_define
class CalendarList:
    """ 
        Attributes:
            etag (str | Unset): ETag of the collection.
            items (list[CalendarListEntry] | Unset): Calendars that are present on the user's calendar list.
            kind (str | Unset): Type of the collection ("calendar#calendarList"). Default: 'calendar#calendarList'.
            next_page_token (str | Unset): Token used to access the next page of this result. Omitted if no further results
                are available, in which case nextSyncToken is provided.
            next_sync_token (str | Unset): Token used at a later point in time to retrieve only the entries that have
                changed since this result was returned. Omitted if further results are available, in which case nextPageToken is
                provided.
     """

    etag: str | Unset = UNSET
    items: list[CalendarListEntry] | Unset = UNSET
    kind: str | Unset = 'calendar#calendarList'
    next_page_token: str | Unset = UNSET
    next_sync_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.calendar_list_entry import CalendarListEntry
        etag = self.etag

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        kind = self.kind

        next_page_token = self.next_page_token

        next_sync_token = self.next_sync_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if etag is not UNSET:
            field_dict["etag"] = etag
        if items is not UNSET:
            field_dict["items"] = items
        if kind is not UNSET:
            field_dict["kind"] = kind
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if next_sync_token is not UNSET:
            field_dict["nextSyncToken"] = next_sync_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_list_entry import CalendarListEntry
        d = dict(src_dict)
        etag = d.pop("etag", UNSET)

        _items = d.pop("items", UNSET)
        items: list[CalendarListEntry] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CalendarListEntry.from_dict(items_item_data)



                items.append(items_item)


        kind = d.pop("kind", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        next_sync_token = d.pop("nextSyncToken", UNSET)

        calendar_list = cls(
            etag=etag,
            items=items,
            kind=kind,
            next_page_token=next_page_token,
            next_sync_token=next_sync_token,
        )


        calendar_list.additional_properties = d
        return calendar_list

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
