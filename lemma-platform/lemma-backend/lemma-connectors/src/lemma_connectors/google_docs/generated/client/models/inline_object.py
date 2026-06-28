from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.inline_object_properties import InlineObjectProperties
  from ..models.inline_object_suggested_inline_object_properties_changes import InlineObjectSuggestedInlineObjectPropertiesChanges





T = TypeVar("T", bound="InlineObject")



@_attrs_define
class InlineObject:
    """ An object that appears inline with text. An InlineObject contains an EmbeddedObject such as an image.

        Attributes:
            inline_object_properties (InlineObjectProperties | Unset): Properties of an InlineObject.
            object_id (str | Unset): The ID of this inline object. Can be used to update an object’s properties.
            suggested_deletion_ids (list[str] | Unset): The suggested deletion IDs. If empty, then there are no suggested
                deletions of this content.
            suggested_inline_object_properties_changes (InlineObjectSuggestedInlineObjectPropertiesChanges | Unset): The
                suggested changes to the inline object properties, keyed by suggestion ID.
            suggested_insertion_id (str | Unset): The suggested insertion ID. If empty, then this is not a suggested
                insertion.
     """

    inline_object_properties: InlineObjectProperties | Unset = UNSET
    object_id: str | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_inline_object_properties_changes: InlineObjectSuggestedInlineObjectPropertiesChanges | Unset = UNSET
    suggested_insertion_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.inline_object_properties import InlineObjectProperties
        from ..models.inline_object_suggested_inline_object_properties_changes import InlineObjectSuggestedInlineObjectPropertiesChanges
        inline_object_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inline_object_properties, Unset):
            inline_object_properties = self.inline_object_properties.to_dict()

        object_id = self.object_id

        suggested_deletion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_deletion_ids, Unset):
            suggested_deletion_ids = self.suggested_deletion_ids



        suggested_inline_object_properties_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_inline_object_properties_changes, Unset):
            suggested_inline_object_properties_changes = self.suggested_inline_object_properties_changes.to_dict()

        suggested_insertion_id = self.suggested_insertion_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if inline_object_properties is not UNSET:
            field_dict["inlineObjectProperties"] = inline_object_properties
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if suggested_deletion_ids is not UNSET:
            field_dict["suggestedDeletionIds"] = suggested_deletion_ids
        if suggested_inline_object_properties_changes is not UNSET:
            field_dict["suggestedInlineObjectPropertiesChanges"] = suggested_inline_object_properties_changes
        if suggested_insertion_id is not UNSET:
            field_dict["suggestedInsertionId"] = suggested_insertion_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inline_object_properties import InlineObjectProperties
        from ..models.inline_object_suggested_inline_object_properties_changes import InlineObjectSuggestedInlineObjectPropertiesChanges
        d = dict(src_dict)
        _inline_object_properties = d.pop("inlineObjectProperties", UNSET)
        inline_object_properties: InlineObjectProperties | Unset
        if isinstance(_inline_object_properties,  Unset):
            inline_object_properties = UNSET
        else:
            inline_object_properties = InlineObjectProperties.from_dict(_inline_object_properties)




        object_id = d.pop("objectId", UNSET)

        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        _suggested_inline_object_properties_changes = d.pop("suggestedInlineObjectPropertiesChanges", UNSET)
        suggested_inline_object_properties_changes: InlineObjectSuggestedInlineObjectPropertiesChanges | Unset
        if isinstance(_suggested_inline_object_properties_changes,  Unset):
            suggested_inline_object_properties_changes = UNSET
        else:
            suggested_inline_object_properties_changes = InlineObjectSuggestedInlineObjectPropertiesChanges.from_dict(_suggested_inline_object_properties_changes)




        suggested_insertion_id = d.pop("suggestedInsertionId", UNSET)

        inline_object = cls(
            inline_object_properties=inline_object_properties,
            object_id=object_id,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_inline_object_properties_changes=suggested_inline_object_properties_changes,
            suggested_insertion_id=suggested_insertion_id,
        )


        inline_object.additional_properties = d
        return inline_object

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
