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
  from ..models.change_details import ChangeDetails
  from ..models.history_metadata import HistoryMetadata
  from ..models.user_details import UserDetails





T = TypeVar("T", bound="Changelog")



@_attrs_define
class Changelog:
    """ A changelog.

        Attributes:
            author (UserDetails | Unset): User details permitted by the user's Atlassian Account privacy settings. However,
                be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            created (datetime.datetime | Unset): The date on which the change took place.
            history_metadata (HistoryMetadata | Unset): Details of issue history metadata.
            id (str | Unset): The ID of the changelog.
            items (list[ChangeDetails] | Unset): The list of items changed.
     """

    author: UserDetails | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    history_metadata: HistoryMetadata | Unset = UNSET
    id: str | Unset = UNSET
    items: list[ChangeDetails] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.change_details import ChangeDetails
        from ..models.history_metadata import HistoryMetadata
        from ..models.user_details import UserDetails
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        history_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.history_metadata, Unset):
            history_metadata = self.history_metadata.to_dict()

        id = self.id

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if author is not UNSET:
            field_dict["author"] = author
        if created is not UNSET:
            field_dict["created"] = created
        if history_metadata is not UNSET:
            field_dict["historyMetadata"] = history_metadata
        if id is not UNSET:
            field_dict["id"] = id
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_details import ChangeDetails
        from ..models.history_metadata import HistoryMetadata
        from ..models.user_details import UserDetails
        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: UserDetails | Unset
        if isinstance(_author,  Unset):
            author = UNSET
        else:
            author = UserDetails.from_dict(_author)




        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        _history_metadata = d.pop("historyMetadata", UNSET)
        history_metadata: HistoryMetadata | Unset
        if isinstance(_history_metadata,  Unset):
            history_metadata = UNSET
        else:
            history_metadata = HistoryMetadata.from_dict(_history_metadata)




        id = d.pop("id", UNSET)

        _items = d.pop("items", UNSET)
        items: list[ChangeDetails] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ChangeDetails.from_dict(items_item_data)



                items.append(items_item)


        changelog = cls(
            author=author,
            created=created,
            history_metadata=history_metadata,
            id=id,
            items=items,
        )

        return changelog

