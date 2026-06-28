from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.person_properties import PersonProperties
  from ..models.person_suggested_text_style_changes import PersonSuggestedTextStyleChanges
  from ..models.text_style import TextStyle





T = TypeVar("T", bound="Person")



@_attrs_define
class Person:
    """ A person or email address mentioned in a document. These mentions behave as a single, immutable element containing
    the person's name or email address.

        Attributes:
            person_id (str | Unset): Output only. The unique ID of this link.
            person_properties (PersonProperties | Unset): Properties specific to a linked Person.
            suggested_deletion_ids (list[str] | Unset): IDs for suggestions that remove this person link from the document.
                A Person might have multiple deletion IDs if, for example, multiple users suggest deleting it. If empty, then
                this person link isn't suggested for deletion.
            suggested_insertion_ids (list[str] | Unset): IDs for suggestions that insert this person link into the document.
                A Person might have multiple insertion IDs if it's a nested suggested change (a suggestion within a suggestion
                made by a different user, for example). If empty, then this person link isn't a suggested insertion.
            suggested_text_style_changes (PersonSuggestedTextStyleChanges | Unset): The suggested text style changes to this
                Person, keyed by suggestion ID.
            text_style (TextStyle | Unset): Represents the styling that can be applied to text. Inherited text styles are
                represented as unset fields in this message. A text style's parent depends on where the text style is defined: *
                The TextStyle of text in a Paragraph inherits from the paragraph's corresponding named style type. * The
                TextStyle on a named style inherits from the normal text named style. * The TextStyle of the normal text named
                style inherits from the default text style in the Docs editor. * The TextStyle on a Paragraph element that's
                contained in a table may inherit its text style from the table style. If the text style does not inherit from a
                parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.
     """

    person_id: str | Unset = UNSET
    person_properties: PersonProperties | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_insertion_ids: list[str] | Unset = UNSET
    suggested_text_style_changes: PersonSuggestedTextStyleChanges | Unset = UNSET
    text_style: TextStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.person_properties import PersonProperties
        from ..models.person_suggested_text_style_changes import PersonSuggestedTextStyleChanges
        from ..models.text_style import TextStyle
        person_id = self.person_id

        person_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person_properties, Unset):
            person_properties = self.person_properties.to_dict()

        suggested_deletion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_deletion_ids, Unset):
            suggested_deletion_ids = self.suggested_deletion_ids



        suggested_insertion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_insertion_ids, Unset):
            suggested_insertion_ids = self.suggested_insertion_ids



        suggested_text_style_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_text_style_changes, Unset):
            suggested_text_style_changes = self.suggested_text_style_changes.to_dict()

        text_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style, Unset):
            text_style = self.text_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person_properties is not UNSET:
            field_dict["personProperties"] = person_properties
        if suggested_deletion_ids is not UNSET:
            field_dict["suggestedDeletionIds"] = suggested_deletion_ids
        if suggested_insertion_ids is not UNSET:
            field_dict["suggestedInsertionIds"] = suggested_insertion_ids
        if suggested_text_style_changes is not UNSET:
            field_dict["suggestedTextStyleChanges"] = suggested_text_style_changes
        if text_style is not UNSET:
            field_dict["textStyle"] = text_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_properties import PersonProperties
        from ..models.person_suggested_text_style_changes import PersonSuggestedTextStyleChanges
        from ..models.text_style import TextStyle
        d = dict(src_dict)
        person_id = d.pop("personId", UNSET)

        _person_properties = d.pop("personProperties", UNSET)
        person_properties: PersonProperties | Unset
        if isinstance(_person_properties,  Unset):
            person_properties = UNSET
        else:
            person_properties = PersonProperties.from_dict(_person_properties)




        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        suggested_insertion_ids = cast(list[str], d.pop("suggestedInsertionIds", UNSET))


        _suggested_text_style_changes = d.pop("suggestedTextStyleChanges", UNSET)
        suggested_text_style_changes: PersonSuggestedTextStyleChanges | Unset
        if isinstance(_suggested_text_style_changes,  Unset):
            suggested_text_style_changes = UNSET
        else:
            suggested_text_style_changes = PersonSuggestedTextStyleChanges.from_dict(_suggested_text_style_changes)




        _text_style = d.pop("textStyle", UNSET)
        text_style: TextStyle | Unset
        if isinstance(_text_style,  Unset):
            text_style = UNSET
        else:
            text_style = TextStyle.from_dict(_text_style)




        person = cls(
            person_id=person_id,
            person_properties=person_properties,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_insertion_ids=suggested_insertion_ids,
            suggested_text_style_changes=suggested_text_style_changes,
            text_style=text_style,
        )


        person.additional_properties = d
        return person

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
