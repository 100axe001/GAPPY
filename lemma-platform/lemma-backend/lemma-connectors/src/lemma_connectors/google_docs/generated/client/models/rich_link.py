from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rich_link_properties import RichLinkProperties
  from ..models.rich_link_suggested_text_style_changes import RichLinkSuggestedTextStyleChanges
  from ..models.text_style import TextStyle





T = TypeVar("T", bound="RichLink")



@_attrs_define
class RichLink:
    """ A link to a Google resource (such as a file in Drive, a YouTube video, or a Calendar event).

        Attributes:
            rich_link_id (str | Unset): Output only. The ID of this link.
            rich_link_properties (RichLinkProperties | Unset): Properties specific to a RichLink.
            suggested_deletion_ids (list[str] | Unset): IDs for suggestions that remove this link from the document. A
                RichLink might have multiple deletion IDs if, for example, multiple users suggest deleting it. If empty, then
                this person link isn't suggested for deletion.
            suggested_insertion_ids (list[str] | Unset): IDs for suggestions that insert this link into the document. A
                RichLink might have multiple insertion IDs if it's a nested suggested change (a suggestion within a suggestion
                made by a different user, for example). If empty, then this person link isn't a suggested insertion.
            suggested_text_style_changes (RichLinkSuggestedTextStyleChanges | Unset): The suggested text style changes to
                this RichLink, keyed by suggestion ID.
            text_style (TextStyle | Unset): Represents the styling that can be applied to text. Inherited text styles are
                represented as unset fields in this message. A text style's parent depends on where the text style is defined: *
                The TextStyle of text in a Paragraph inherits from the paragraph's corresponding named style type. * The
                TextStyle on a named style inherits from the normal text named style. * The TextStyle of the normal text named
                style inherits from the default text style in the Docs editor. * The TextStyle on a Paragraph element that's
                contained in a table may inherit its text style from the table style. If the text style does not inherit from a
                parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.
     """

    rich_link_id: str | Unset = UNSET
    rich_link_properties: RichLinkProperties | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_insertion_ids: list[str] | Unset = UNSET
    suggested_text_style_changes: RichLinkSuggestedTextStyleChanges | Unset = UNSET
    text_style: TextStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rich_link_properties import RichLinkProperties
        from ..models.rich_link_suggested_text_style_changes import RichLinkSuggestedTextStyleChanges
        from ..models.text_style import TextStyle
        rich_link_id = self.rich_link_id

        rich_link_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rich_link_properties, Unset):
            rich_link_properties = self.rich_link_properties.to_dict()

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
        if rich_link_id is not UNSET:
            field_dict["richLinkId"] = rich_link_id
        if rich_link_properties is not UNSET:
            field_dict["richLinkProperties"] = rich_link_properties
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
        from ..models.rich_link_properties import RichLinkProperties
        from ..models.rich_link_suggested_text_style_changes import RichLinkSuggestedTextStyleChanges
        from ..models.text_style import TextStyle
        d = dict(src_dict)
        rich_link_id = d.pop("richLinkId", UNSET)

        _rich_link_properties = d.pop("richLinkProperties", UNSET)
        rich_link_properties: RichLinkProperties | Unset
        if isinstance(_rich_link_properties,  Unset):
            rich_link_properties = UNSET
        else:
            rich_link_properties = RichLinkProperties.from_dict(_rich_link_properties)




        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        suggested_insertion_ids = cast(list[str], d.pop("suggestedInsertionIds", UNSET))


        _suggested_text_style_changes = d.pop("suggestedTextStyleChanges", UNSET)
        suggested_text_style_changes: RichLinkSuggestedTextStyleChanges | Unset
        if isinstance(_suggested_text_style_changes,  Unset):
            suggested_text_style_changes = UNSET
        else:
            suggested_text_style_changes = RichLinkSuggestedTextStyleChanges.from_dict(_suggested_text_style_changes)




        _text_style = d.pop("textStyle", UNSET)
        text_style: TextStyle | Unset
        if isinstance(_text_style,  Unset):
            text_style = UNSET
        else:
            text_style = TextStyle.from_dict(_text_style)




        rich_link = cls(
            rich_link_id=rich_link_id,
            rich_link_properties=rich_link_properties,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_insertion_ids=suggested_insertion_ids,
            suggested_text_style_changes=suggested_text_style_changes,
            text_style=text_style,
        )


        rich_link.additional_properties = d
        return rich_link

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
