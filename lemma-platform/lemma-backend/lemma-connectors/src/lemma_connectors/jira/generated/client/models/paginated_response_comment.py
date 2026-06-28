from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.comment import Comment





T = TypeVar("T", bound="PaginatedResponseComment")



@_attrs_define
class PaginatedResponseComment:
    """ 
        Attributes:
            max_results (int | Unset):
            results (list[Comment] | Unset):
            start_at (int | Unset):
            total (int | Unset):
     """

    max_results: int | Unset = UNSET
    results: list[Comment] | Unset = UNSET
    start_at: int | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.comment import Comment
        max_results = self.max_results

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)



        start_at = self.start_at

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if results is not UNSET:
            field_dict["results"] = results
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment import Comment
        d = dict(src_dict)
        max_results = d.pop("maxResults", UNSET)

        _results = d.pop("results", UNSET)
        results: list[Comment] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = Comment.from_dict(results_item_data)



                results.append(results_item)


        start_at = d.pop("startAt", UNSET)

        total = d.pop("total", UNSET)

        paginated_response_comment = cls(
            max_results=max_results,
            results=results,
            start_at=start_at,
            total=total,
        )

        return paginated_response_comment

