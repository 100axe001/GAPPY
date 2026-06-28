from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_properties import ListProperties
  from ..models.list_suggested_list_properties_changes import ListSuggestedListPropertiesChanges





T = TypeVar("T", bound="List")



@_attrs_define
class List:
    """ A List represents the list attributes for a group of paragraphs that all belong to the same list. A paragraph that's
    part of a list has a reference to the list's ID in its bullet.

        Attributes:
            list_properties (ListProperties | Unset): The properties of a list that describe the look and feel of bullets
                belonging to paragraphs associated with a list.
            suggested_deletion_ids (list[str] | Unset): The suggested deletion IDs. If empty, then there are no suggested
                deletions of this list.
            suggested_insertion_id (str | Unset): The suggested insertion ID. If empty, then this is not a suggested
                insertion.
            suggested_list_properties_changes (ListSuggestedListPropertiesChanges | Unset): The suggested changes to the
                list properties, keyed by suggestion ID.
     """

    list_properties: ListProperties | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_insertion_id: str | Unset = UNSET
    suggested_list_properties_changes: ListSuggestedListPropertiesChanges | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_properties import ListProperties
        from ..models.list_suggested_list_properties_changes import ListSuggestedListPropertiesChanges
        list_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.list_properties, Unset):
            list_properties = self.list_properties.to_dict()

        suggested_deletion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_deletion_ids, Unset):
            suggested_deletion_ids = self.suggested_deletion_ids



        suggested_insertion_id = self.suggested_insertion_id

        suggested_list_properties_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_list_properties_changes, Unset):
            suggested_list_properties_changes = self.suggested_list_properties_changes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if list_properties is not UNSET:
            field_dict["listProperties"] = list_properties
        if suggested_deletion_ids is not UNSET:
            field_dict["suggestedDeletionIds"] = suggested_deletion_ids
        if suggested_insertion_id is not UNSET:
            field_dict["suggestedInsertionId"] = suggested_insertion_id
        if suggested_list_properties_changes is not UNSET:
            field_dict["suggestedListPropertiesChanges"] = suggested_list_properties_changes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_properties import ListProperties
        from ..models.list_suggested_list_properties_changes import ListSuggestedListPropertiesChanges
        d = dict(src_dict)
        _list_properties = d.pop("listProperties", UNSET)
        list_properties: ListProperties | Unset
        if isinstance(_list_properties,  Unset):
            list_properties = UNSET
        else:
            list_properties = ListProperties.from_dict(_list_properties)




        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        suggested_insertion_id = d.pop("suggestedInsertionId", UNSET)

        _suggested_list_properties_changes = d.pop("suggestedListPropertiesChanges", UNSET)
        suggested_list_properties_changes: ListSuggestedListPropertiesChanges | Unset
        if isinstance(_suggested_list_properties_changes,  Unset):
            suggested_list_properties_changes = UNSET
        else:
            suggested_list_properties_changes = ListSuggestedListPropertiesChanges.from_dict(_suggested_list_properties_changes)




        list_ = cls(
            list_properties=list_properties,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_insertion_id=suggested_insertion_id,
            suggested_list_properties_changes=suggested_list_properties_changes,
        )


        list_.additional_properties = d
        return list_

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
