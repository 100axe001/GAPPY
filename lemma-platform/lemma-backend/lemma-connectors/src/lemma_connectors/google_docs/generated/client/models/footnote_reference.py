from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.footnote_reference_suggested_text_style_changes import FootnoteReferenceSuggestedTextStyleChanges
  from ..models.text_style import TextStyle





T = TypeVar("T", bound="FootnoteReference")



@_attrs_define
class FootnoteReference:
    """ A ParagraphElement representing a footnote reference. A footnote reference is the inline content rendered with a
    number and is used to identify the footnote.

        Attributes:
            footnote_id (str | Unset): The ID of the footnote that contains the content of this footnote reference.
            footnote_number (str | Unset): The rendered number of this footnote.
            suggested_deletion_ids (list[str] | Unset): The suggested deletion IDs. If empty, then there are no suggested
                deletions of this content.
            suggested_insertion_ids (list[str] | Unset): The suggested insertion IDs. A FootnoteReference may have multiple
                insertion IDs if it's a nested suggested change. If empty, then this is not a suggested insertion.
            suggested_text_style_changes (FootnoteReferenceSuggestedTextStyleChanges | Unset): The suggested text style
                changes to this FootnoteReference, keyed by suggestion ID.
            text_style (TextStyle | Unset): Represents the styling that can be applied to text. Inherited text styles are
                represented as unset fields in this message. A text style's parent depends on where the text style is defined: *
                The TextStyle of text in a Paragraph inherits from the paragraph's corresponding named style type. * The
                TextStyle on a named style inherits from the normal text named style. * The TextStyle of the normal text named
                style inherits from the default text style in the Docs editor. * The TextStyle on a Paragraph element that's
                contained in a table may inherit its text style from the table style. If the text style does not inherit from a
                parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.
     """

    footnote_id: str | Unset = UNSET
    footnote_number: str | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_insertion_ids: list[str] | Unset = UNSET
    suggested_text_style_changes: FootnoteReferenceSuggestedTextStyleChanges | Unset = UNSET
    text_style: TextStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.footnote_reference_suggested_text_style_changes import FootnoteReferenceSuggestedTextStyleChanges
        from ..models.text_style import TextStyle
        footnote_id = self.footnote_id

        footnote_number = self.footnote_number

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
        if footnote_id is not UNSET:
            field_dict["footnoteId"] = footnote_id
        if footnote_number is not UNSET:
            field_dict["footnoteNumber"] = footnote_number
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
        from ..models.footnote_reference_suggested_text_style_changes import FootnoteReferenceSuggestedTextStyleChanges
        from ..models.text_style import TextStyle
        d = dict(src_dict)
        footnote_id = d.pop("footnoteId", UNSET)

        footnote_number = d.pop("footnoteNumber", UNSET)

        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        suggested_insertion_ids = cast(list[str], d.pop("suggestedInsertionIds", UNSET))


        _suggested_text_style_changes = d.pop("suggestedTextStyleChanges", UNSET)
        suggested_text_style_changes: FootnoteReferenceSuggestedTextStyleChanges | Unset
        if isinstance(_suggested_text_style_changes,  Unset):
            suggested_text_style_changes = UNSET
        else:
            suggested_text_style_changes = FootnoteReferenceSuggestedTextStyleChanges.from_dict(_suggested_text_style_changes)




        _text_style = d.pop("textStyle", UNSET)
        text_style: TextStyle | Unset
        if isinstance(_text_style,  Unset):
            text_style = UNSET
        else:
            text_style = TextStyle.from_dict(_text_style)




        footnote_reference = cls(
            footnote_id=footnote_id,
            footnote_number=footnote_number,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_insertion_ids=suggested_insertion_ids,
            suggested_text_style_changes=suggested_text_style_changes,
            text_style=text_style,
        )


        footnote_reference.additional_properties = d
        return footnote_reference

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
