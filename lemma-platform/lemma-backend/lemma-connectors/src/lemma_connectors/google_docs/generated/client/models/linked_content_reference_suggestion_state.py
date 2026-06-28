from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.sheets_chart_reference_suggestion_state import SheetsChartReferenceSuggestionState





T = TypeVar("T", bound="LinkedContentReferenceSuggestionState")



@_attrs_define
class LinkedContentReferenceSuggestionState:
    """ A mask that indicates which of the fields on the base LinkedContentReference have been changed in this suggestion.
    For any field set to true, there's a new suggested value.

        Attributes:
            sheets_chart_reference_suggestion_state (SheetsChartReferenceSuggestionState | Unset): A mask that indicates
                which of the fields on the base SheetsChartReference have been changed in this suggestion. For any field set to
                true, there's a new suggested value.
     """

    sheets_chart_reference_suggestion_state: SheetsChartReferenceSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sheets_chart_reference_suggestion_state import SheetsChartReferenceSuggestionState
        sheets_chart_reference_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sheets_chart_reference_suggestion_state, Unset):
            sheets_chart_reference_suggestion_state = self.sheets_chart_reference_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sheets_chart_reference_suggestion_state is not UNSET:
            field_dict["sheetsChartReferenceSuggestionState"] = sheets_chart_reference_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sheets_chart_reference_suggestion_state import SheetsChartReferenceSuggestionState
        d = dict(src_dict)
        _sheets_chart_reference_suggestion_state = d.pop("sheetsChartReferenceSuggestionState", UNSET)
        sheets_chart_reference_suggestion_state: SheetsChartReferenceSuggestionState | Unset
        if isinstance(_sheets_chart_reference_suggestion_state,  Unset):
            sheets_chart_reference_suggestion_state = UNSET
        else:
            sheets_chart_reference_suggestion_state = SheetsChartReferenceSuggestionState.from_dict(_sheets_chart_reference_suggestion_state)




        linked_content_reference_suggestion_state = cls(
            sheets_chart_reference_suggestion_state=sheets_chart_reference_suggestion_state,
        )


        linked_content_reference_suggestion_state.additional_properties = d
        return linked_content_reference_suggestion_state

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
