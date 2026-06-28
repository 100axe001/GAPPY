from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.simplified_hierarchy_level import SimplifiedHierarchyLevel





T = TypeVar("T", bound="Hierarchy")



@_attrs_define
class Hierarchy:
    """ The project issue type hierarchy.

        Attributes:
            base_level_id (int | Unset): The ID of the base level. This property is deprecated, see [Change notice: Removing
                hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-
                removing-hierarchy-level-ids-from-next-gen-apis/).
            levels (list[SimplifiedHierarchyLevel] | Unset): Details about the hierarchy level.
     """

    base_level_id: int | Unset = UNSET
    levels: list[SimplifiedHierarchyLevel] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.simplified_hierarchy_level import SimplifiedHierarchyLevel
        base_level_id = self.base_level_id

        levels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.levels, Unset):
            levels = []
            for levels_item_data in self.levels:
                levels_item = levels_item_data.to_dict()
                levels.append(levels_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if base_level_id is not UNSET:
            field_dict["baseLevelId"] = base_level_id
        if levels is not UNSET:
            field_dict["levels"] = levels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simplified_hierarchy_level import SimplifiedHierarchyLevel
        d = dict(src_dict)
        base_level_id = d.pop("baseLevelId", UNSET)

        _levels = d.pop("levels", UNSET)
        levels: list[SimplifiedHierarchyLevel] | Unset = UNSET
        if _levels is not UNSET:
            levels = []
            for levels_item_data in _levels:
                levels_item = SimplifiedHierarchyLevel.from_dict(levels_item_data)



                levels.append(levels_item)


        hierarchy = cls(
            base_level_id=base_level_id,
            levels=levels,
        )

        return hierarchy

