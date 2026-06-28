from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.auto_complete_suggestion import AutoCompleteSuggestion





T = TypeVar("T", bound="AutoCompleteSuggestions")



@_attrs_define
class AutoCompleteSuggestions:
    """ The results from a JQL query.

        Attributes:
            results (list[AutoCompleteSuggestion] | Unset): The list of suggested item.
     """

    results: list[AutoCompleteSuggestion] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.auto_complete_suggestion import AutoCompleteSuggestion
        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_complete_suggestion import AutoCompleteSuggestion
        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[AutoCompleteSuggestion] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = AutoCompleteSuggestion.from_dict(results_item_data)



                results.append(results_item)


        auto_complete_suggestions = cls(
            results=results,
        )

        return auto_complete_suggestions

