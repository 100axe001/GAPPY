from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.change import Change





T = TypeVar("T", bound="ChangeList")



@_attrs_define
class ChangeList:
    """ A list of changes for a user.

        Attributes:
            changes (list[Change] | Unset): The list of changes. If nextPageToken is populated, then this list may be
                incomplete and an additional page of results should be fetched.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#changeList".
                Default: 'drive#changeList'.
            new_start_page_token (str | Unset): The starting page token for future changes. This will be present only if the
                end of the current changes list has been reached.
            next_page_token (str | Unset): The page token for the next page of changes. This will be absent if the end of
                the changes list has been reached. If the token is rejected for any reason, it should be discarded, and
                pagination should be restarted from the first page of results.
     """

    changes: list[Change] | Unset = UNSET
    kind: str | Unset = 'drive#changeList'
    new_start_page_token: str | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.change import Change
        changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()
                changes.append(changes_item)



        kind = self.kind

        new_start_page_token = self.new_start_page_token

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if changes is not UNSET:
            field_dict["changes"] = changes
        if kind is not UNSET:
            field_dict["kind"] = kind
        if new_start_page_token is not UNSET:
            field_dict["newStartPageToken"] = new_start_page_token
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change import Change
        d = dict(src_dict)
        _changes = d.pop("changes", UNSET)
        changes: list[Change] | Unset = UNSET
        if _changes is not UNSET:
            changes = []
            for changes_item_data in _changes:
                changes_item = Change.from_dict(changes_item_data)



                changes.append(changes_item)


        kind = d.pop("kind", UNSET)

        new_start_page_token = d.pop("newStartPageToken", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        change_list = cls(
            changes=changes,
            kind=kind,
            new_start_page_token=new_start_page_token,
            next_page_token=next_page_token,
        )


        change_list.additional_properties = d
        return change_list

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
