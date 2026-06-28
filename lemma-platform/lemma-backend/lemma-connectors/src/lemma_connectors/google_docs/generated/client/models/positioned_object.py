from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.positioned_object_properties import PositionedObjectProperties
  from ..models.positioned_object_suggested_positioned_object_properties_changes import PositionedObjectSuggestedPositionedObjectPropertiesChanges





T = TypeVar("T", bound="PositionedObject")



@_attrs_define
class PositionedObject:
    """ An object that's tethered to a Paragraph and positioned relative to the beginning of the paragraph. A
    PositionedObject contains an EmbeddedObject such as an image.

        Attributes:
            object_id (str | Unset): The ID of this positioned object.
            positioned_object_properties (PositionedObjectProperties | Unset): Properties of a PositionedObject.
            suggested_deletion_ids (list[str] | Unset): The suggested deletion IDs. If empty, then there are no suggested
                deletions of this content.
            suggested_insertion_id (str | Unset): The suggested insertion ID. If empty, then this is not a suggested
                insertion.
            suggested_positioned_object_properties_changes (PositionedObjectSuggestedPositionedObjectPropertiesChanges |
                Unset): The suggested changes to the positioned object properties, keyed by suggestion ID.
     """

    object_id: str | Unset = UNSET
    positioned_object_properties: PositionedObjectProperties | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_insertion_id: str | Unset = UNSET
    suggested_positioned_object_properties_changes: PositionedObjectSuggestedPositionedObjectPropertiesChanges | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.positioned_object_properties import PositionedObjectProperties
        from ..models.positioned_object_suggested_positioned_object_properties_changes import PositionedObjectSuggestedPositionedObjectPropertiesChanges
        object_id = self.object_id

        positioned_object_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positioned_object_properties, Unset):
            positioned_object_properties = self.positioned_object_properties.to_dict()

        suggested_deletion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_deletion_ids, Unset):
            suggested_deletion_ids = self.suggested_deletion_ids



        suggested_insertion_id = self.suggested_insertion_id

        suggested_positioned_object_properties_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_positioned_object_properties_changes, Unset):
            suggested_positioned_object_properties_changes = self.suggested_positioned_object_properties_changes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if positioned_object_properties is not UNSET:
            field_dict["positionedObjectProperties"] = positioned_object_properties
        if suggested_deletion_ids is not UNSET:
            field_dict["suggestedDeletionIds"] = suggested_deletion_ids
        if suggested_insertion_id is not UNSET:
            field_dict["suggestedInsertionId"] = suggested_insertion_id
        if suggested_positioned_object_properties_changes is not UNSET:
            field_dict["suggestedPositionedObjectPropertiesChanges"] = suggested_positioned_object_properties_changes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.positioned_object_properties import PositionedObjectProperties
        from ..models.positioned_object_suggested_positioned_object_properties_changes import PositionedObjectSuggestedPositionedObjectPropertiesChanges
        d = dict(src_dict)
        object_id = d.pop("objectId", UNSET)

        _positioned_object_properties = d.pop("positionedObjectProperties", UNSET)
        positioned_object_properties: PositionedObjectProperties | Unset
        if isinstance(_positioned_object_properties,  Unset):
            positioned_object_properties = UNSET
        else:
            positioned_object_properties = PositionedObjectProperties.from_dict(_positioned_object_properties)




        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        suggested_insertion_id = d.pop("suggestedInsertionId", UNSET)

        _suggested_positioned_object_properties_changes = d.pop("suggestedPositionedObjectPropertiesChanges", UNSET)
        suggested_positioned_object_properties_changes: PositionedObjectSuggestedPositionedObjectPropertiesChanges | Unset
        if isinstance(_suggested_positioned_object_properties_changes,  Unset):
            suggested_positioned_object_properties_changes = UNSET
        else:
            suggested_positioned_object_properties_changes = PositionedObjectSuggestedPositionedObjectPropertiesChanges.from_dict(_suggested_positioned_object_properties_changes)




        positioned_object = cls(
            object_id=object_id,
            positioned_object_properties=positioned_object_properties,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_insertion_id=suggested_insertion_id,
            suggested_positioned_object_properties_changes=suggested_positioned_object_properties_changes,
        )


        positioned_object.additional_properties = d
        return positioned_object

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
