from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.document_style import DocumentStyle
  from ..models.document_style_suggestion_state import DocumentStyleSuggestionState





T = TypeVar("T", bound="SuggestedDocumentStyle")



@_attrs_define
class SuggestedDocumentStyle:
    """ A suggested change to the DocumentStyle.

        Attributes:
            document_style (DocumentStyle | Unset): The style of the document.
            document_style_suggestion_state (DocumentStyleSuggestionState | Unset): A mask that indicates which of the
                fields on the base DocumentStyle have been changed in this suggestion. For any field set to true, there's a new
                suggested value.
     """

    document_style: DocumentStyle | Unset = UNSET
    document_style_suggestion_state: DocumentStyleSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.document_style import DocumentStyle
        from ..models.document_style_suggestion_state import DocumentStyleSuggestionState
        document_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_style, Unset):
            document_style = self.document_style.to_dict()

        document_style_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_style_suggestion_state, Unset):
            document_style_suggestion_state = self.document_style_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if document_style is not UNSET:
            field_dict["documentStyle"] = document_style
        if document_style_suggestion_state is not UNSET:
            field_dict["documentStyleSuggestionState"] = document_style_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_style import DocumentStyle
        from ..models.document_style_suggestion_state import DocumentStyleSuggestionState
        d = dict(src_dict)
        _document_style = d.pop("documentStyle", UNSET)
        document_style: DocumentStyle | Unset
        if isinstance(_document_style,  Unset):
            document_style = UNSET
        else:
            document_style = DocumentStyle.from_dict(_document_style)




        _document_style_suggestion_state = d.pop("documentStyleSuggestionState", UNSET)
        document_style_suggestion_state: DocumentStyleSuggestionState | Unset
        if isinstance(_document_style_suggestion_state,  Unset):
            document_style_suggestion_state = UNSET
        else:
            document_style_suggestion_state = DocumentStyleSuggestionState.from_dict(_document_style_suggestion_state)




        suggested_document_style = cls(
            document_style=document_style,
            document_style_suggestion_state=document_style_suggestion_state,
        )


        suggested_document_style.additional_properties = d
        return suggested_document_style

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
