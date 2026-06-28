from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.document_suggestions_view_mode import DocumentSuggestionsViewMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.body import Body
  from ..models.document_footers import DocumentFooters
  from ..models.document_footnotes import DocumentFootnotes
  from ..models.document_headers import DocumentHeaders
  from ..models.document_inline_objects import DocumentInlineObjects
  from ..models.document_lists import DocumentLists
  from ..models.document_named_ranges import DocumentNamedRanges
  from ..models.document_positioned_objects import DocumentPositionedObjects
  from ..models.document_style import DocumentStyle
  from ..models.document_suggested_document_style_changes import DocumentSuggestedDocumentStyleChanges
  from ..models.document_suggested_named_styles_changes import DocumentSuggestedNamedStylesChanges
  from ..models.named_styles import NamedStyles





T = TypeVar("T", bound="Document")



@_attrs_define
class Document:
    """ A Google Docs document.

        Attributes:
            body (Body | Unset): The document body. The body typically contains the full document contents except for
                headers, footers, and footnotes.
            document_id (str | Unset): Output only. The ID of the document.
            document_style (DocumentStyle | Unset): The style of the document.
            footers (DocumentFooters | Unset): Output only. The footers in the document, keyed by footer ID.
            footnotes (DocumentFootnotes | Unset): Output only. The footnotes in the document, keyed by footnote ID.
            headers (DocumentHeaders | Unset): Output only. The headers in the document, keyed by header ID.
            inline_objects (DocumentInlineObjects | Unset): Output only. The inline objects in the document, keyed by object
                ID.
            lists (DocumentLists | Unset): Output only. The lists in the document, keyed by list ID.
            named_ranges (DocumentNamedRanges | Unset): Output only. The named ranges in the document, keyed by name.
            named_styles (NamedStyles | Unset): The named styles. Paragraphs in the document can inherit their TextStyle and
                ParagraphStyle from these named styles.
            positioned_objects (DocumentPositionedObjects | Unset): Output only. The positioned objects in the document,
                keyed by object ID.
            revision_id (str | Unset): Output only. The revision ID of the document. Can be used in update requests to
                specify which revision of a document to apply updates to and how the request should behave if the document has
                been edited since that revision. Only populated if the user has edit access to the document. The revision ID is
                not a sequential number but an opaque string. The format of the revision ID might change over time. A returned
                revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across
                users. If the revision ID is unchanged between calls, then the document has not changed. Conversely, a changed
                ID (for the same document and user) usually means the document has been updated. However, a changed ID can also
                be due to internal factors such as ID format changes.
            suggested_document_style_changes (DocumentSuggestedDocumentStyleChanges | Unset): Output only. The suggested
                changes to the style of the document, keyed by suggestion ID.
            suggested_named_styles_changes (DocumentSuggestedNamedStylesChanges | Unset): Output only. The suggested changes
                to the named styles of the document, keyed by suggestion ID.
            suggestions_view_mode (DocumentSuggestionsViewMode | Unset): Output only. The suggestions view mode applied to
                the document. Note: When editing a document, changes must be based on a document with SUGGESTIONS_INLINE.
            title (str | Unset): The title of the document.
     """

    body: Body | Unset = UNSET
    document_id: str | Unset = UNSET
    document_style: DocumentStyle | Unset = UNSET
    footers: DocumentFooters | Unset = UNSET
    footnotes: DocumentFootnotes | Unset = UNSET
    headers: DocumentHeaders | Unset = UNSET
    inline_objects: DocumentInlineObjects | Unset = UNSET
    lists: DocumentLists | Unset = UNSET
    named_ranges: DocumentNamedRanges | Unset = UNSET
    named_styles: NamedStyles | Unset = UNSET
    positioned_objects: DocumentPositionedObjects | Unset = UNSET
    revision_id: str | Unset = UNSET
    suggested_document_style_changes: DocumentSuggestedDocumentStyleChanges | Unset = UNSET
    suggested_named_styles_changes: DocumentSuggestedNamedStylesChanges | Unset = UNSET
    suggestions_view_mode: DocumentSuggestionsViewMode | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.body import Body
        from ..models.document_footers import DocumentFooters
        from ..models.document_footnotes import DocumentFootnotes
        from ..models.document_headers import DocumentHeaders
        from ..models.document_inline_objects import DocumentInlineObjects
        from ..models.document_lists import DocumentLists
        from ..models.document_named_ranges import DocumentNamedRanges
        from ..models.document_positioned_objects import DocumentPositionedObjects
        from ..models.document_style import DocumentStyle
        from ..models.document_suggested_document_style_changes import DocumentSuggestedDocumentStyleChanges
        from ..models.document_suggested_named_styles_changes import DocumentSuggestedNamedStylesChanges
        from ..models.named_styles import NamedStyles
        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        document_id = self.document_id

        document_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_style, Unset):
            document_style = self.document_style.to_dict()

        footers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.footers, Unset):
            footers = self.footers.to_dict()

        footnotes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.footnotes, Unset):
            footnotes = self.footnotes.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        inline_objects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inline_objects, Unset):
            inline_objects = self.inline_objects.to_dict()

        lists: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lists, Unset):
            lists = self.lists.to_dict()

        named_ranges: dict[str, Any] | Unset = UNSET
        if not isinstance(self.named_ranges, Unset):
            named_ranges = self.named_ranges.to_dict()

        named_styles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.named_styles, Unset):
            named_styles = self.named_styles.to_dict()

        positioned_objects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positioned_objects, Unset):
            positioned_objects = self.positioned_objects.to_dict()

        revision_id = self.revision_id

        suggested_document_style_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_document_style_changes, Unset):
            suggested_document_style_changes = self.suggested_document_style_changes.to_dict()

        suggested_named_styles_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_named_styles_changes, Unset):
            suggested_named_styles_changes = self.suggested_named_styles_changes.to_dict()

        suggestions_view_mode: str | Unset = UNSET
        if not isinstance(self.suggestions_view_mode, Unset):
            suggestions_view_mode = self.suggestions_view_mode.value


        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if body is not UNSET:
            field_dict["body"] = body
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_style is not UNSET:
            field_dict["documentStyle"] = document_style
        if footers is not UNSET:
            field_dict["footers"] = footers
        if footnotes is not UNSET:
            field_dict["footnotes"] = footnotes
        if headers is not UNSET:
            field_dict["headers"] = headers
        if inline_objects is not UNSET:
            field_dict["inlineObjects"] = inline_objects
        if lists is not UNSET:
            field_dict["lists"] = lists
        if named_ranges is not UNSET:
            field_dict["namedRanges"] = named_ranges
        if named_styles is not UNSET:
            field_dict["namedStyles"] = named_styles
        if positioned_objects is not UNSET:
            field_dict["positionedObjects"] = positioned_objects
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if suggested_document_style_changes is not UNSET:
            field_dict["suggestedDocumentStyleChanges"] = suggested_document_style_changes
        if suggested_named_styles_changes is not UNSET:
            field_dict["suggestedNamedStylesChanges"] = suggested_named_styles_changes
        if suggestions_view_mode is not UNSET:
            field_dict["suggestionsViewMode"] = suggestions_view_mode
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body import Body
        from ..models.document_footers import DocumentFooters
        from ..models.document_footnotes import DocumentFootnotes
        from ..models.document_headers import DocumentHeaders
        from ..models.document_inline_objects import DocumentInlineObjects
        from ..models.document_lists import DocumentLists
        from ..models.document_named_ranges import DocumentNamedRanges
        from ..models.document_positioned_objects import DocumentPositionedObjects
        from ..models.document_style import DocumentStyle
        from ..models.document_suggested_document_style_changes import DocumentSuggestedDocumentStyleChanges
        from ..models.document_suggested_named_styles_changes import DocumentSuggestedNamedStylesChanges
        from ..models.named_styles import NamedStyles
        d = dict(src_dict)
        _body = d.pop("body", UNSET)
        body: Body | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = Body.from_dict(_body)




        document_id = d.pop("documentId", UNSET)

        _document_style = d.pop("documentStyle", UNSET)
        document_style: DocumentStyle | Unset
        if isinstance(_document_style,  Unset):
            document_style = UNSET
        else:
            document_style = DocumentStyle.from_dict(_document_style)




        _footers = d.pop("footers", UNSET)
        footers: DocumentFooters | Unset
        if isinstance(_footers,  Unset):
            footers = UNSET
        else:
            footers = DocumentFooters.from_dict(_footers)




        _footnotes = d.pop("footnotes", UNSET)
        footnotes: DocumentFootnotes | Unset
        if isinstance(_footnotes,  Unset):
            footnotes = UNSET
        else:
            footnotes = DocumentFootnotes.from_dict(_footnotes)




        _headers = d.pop("headers", UNSET)
        headers: DocumentHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = DocumentHeaders.from_dict(_headers)




        _inline_objects = d.pop("inlineObjects", UNSET)
        inline_objects: DocumentInlineObjects | Unset
        if isinstance(_inline_objects,  Unset):
            inline_objects = UNSET
        else:
            inline_objects = DocumentInlineObjects.from_dict(_inline_objects)




        _lists = d.pop("lists", UNSET)
        lists: DocumentLists | Unset
        if isinstance(_lists,  Unset):
            lists = UNSET
        else:
            lists = DocumentLists.from_dict(_lists)




        _named_ranges = d.pop("namedRanges", UNSET)
        named_ranges: DocumentNamedRanges | Unset
        if isinstance(_named_ranges,  Unset):
            named_ranges = UNSET
        else:
            named_ranges = DocumentNamedRanges.from_dict(_named_ranges)




        _named_styles = d.pop("namedStyles", UNSET)
        named_styles: NamedStyles | Unset
        if isinstance(_named_styles,  Unset):
            named_styles = UNSET
        else:
            named_styles = NamedStyles.from_dict(_named_styles)




        _positioned_objects = d.pop("positionedObjects", UNSET)
        positioned_objects: DocumentPositionedObjects | Unset
        if isinstance(_positioned_objects,  Unset):
            positioned_objects = UNSET
        else:
            positioned_objects = DocumentPositionedObjects.from_dict(_positioned_objects)




        revision_id = d.pop("revisionId", UNSET)

        _suggested_document_style_changes = d.pop("suggestedDocumentStyleChanges", UNSET)
        suggested_document_style_changes: DocumentSuggestedDocumentStyleChanges | Unset
        if isinstance(_suggested_document_style_changes,  Unset):
            suggested_document_style_changes = UNSET
        else:
            suggested_document_style_changes = DocumentSuggestedDocumentStyleChanges.from_dict(_suggested_document_style_changes)




        _suggested_named_styles_changes = d.pop("suggestedNamedStylesChanges", UNSET)
        suggested_named_styles_changes: DocumentSuggestedNamedStylesChanges | Unset
        if isinstance(_suggested_named_styles_changes,  Unset):
            suggested_named_styles_changes = UNSET
        else:
            suggested_named_styles_changes = DocumentSuggestedNamedStylesChanges.from_dict(_suggested_named_styles_changes)




        _suggestions_view_mode = d.pop("suggestionsViewMode", UNSET)
        suggestions_view_mode: DocumentSuggestionsViewMode | Unset
        if isinstance(_suggestions_view_mode,  Unset):
            suggestions_view_mode = UNSET
        else:
            suggestions_view_mode = DocumentSuggestionsViewMode(_suggestions_view_mode)




        title = d.pop("title", UNSET)

        document = cls(
            body=body,
            document_id=document_id,
            document_style=document_style,
            footers=footers,
            footnotes=footnotes,
            headers=headers,
            inline_objects=inline_objects,
            lists=lists,
            named_ranges=named_ranges,
            named_styles=named_styles,
            positioned_objects=positioned_objects,
            revision_id=revision_id,
            suggested_document_style_changes=suggested_document_style_changes,
            suggested_named_styles_changes=suggested_named_styles_changes,
            suggestions_view_mode=suggestions_view_mode,
            title=title,
        )


        document.additional_properties = d
        return document

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
