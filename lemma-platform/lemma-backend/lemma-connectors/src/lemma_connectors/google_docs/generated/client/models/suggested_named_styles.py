from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.named_styles import NamedStyles
  from ..models.named_styles_suggestion_state import NamedStylesSuggestionState





T = TypeVar("T", bound="SuggestedNamedStyles")



@_attrs_define
class SuggestedNamedStyles:
    """ A suggested change to the NamedStyles.

        Attributes:
            named_styles (NamedStyles | Unset): The named styles. Paragraphs in the document can inherit their TextStyle and
                ParagraphStyle from these named styles.
            named_styles_suggestion_state (NamedStylesSuggestionState | Unset): The suggestion state of a NamedStyles
                message.
     """

    named_styles: NamedStyles | Unset = UNSET
    named_styles_suggestion_state: NamedStylesSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.named_styles import NamedStyles
        from ..models.named_styles_suggestion_state import NamedStylesSuggestionState
        named_styles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.named_styles, Unset):
            named_styles = self.named_styles.to_dict()

        named_styles_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.named_styles_suggestion_state, Unset):
            named_styles_suggestion_state = self.named_styles_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if named_styles is not UNSET:
            field_dict["namedStyles"] = named_styles
        if named_styles_suggestion_state is not UNSET:
            field_dict["namedStylesSuggestionState"] = named_styles_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.named_styles import NamedStyles
        from ..models.named_styles_suggestion_state import NamedStylesSuggestionState
        d = dict(src_dict)
        _named_styles = d.pop("namedStyles", UNSET)
        named_styles: NamedStyles | Unset
        if isinstance(_named_styles,  Unset):
            named_styles = UNSET
        else:
            named_styles = NamedStyles.from_dict(_named_styles)




        _named_styles_suggestion_state = d.pop("namedStylesSuggestionState", UNSET)
        named_styles_suggestion_state: NamedStylesSuggestionState | Unset
        if isinstance(_named_styles_suggestion_state,  Unset):
            named_styles_suggestion_state = UNSET
        else:
            named_styles_suggestion_state = NamedStylesSuggestionState.from_dict(_named_styles_suggestion_state)




        suggested_named_styles = cls(
            named_styles=named_styles,
            named_styles_suggestion_state=named_styles_suggestion_state,
        )


        suggested_named_styles.additional_properties = d
        return suggested_named_styles

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
