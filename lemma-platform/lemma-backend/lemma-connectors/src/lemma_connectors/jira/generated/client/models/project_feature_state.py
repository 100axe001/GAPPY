from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.project_feature_state_state import ProjectFeatureStateState
from ..types import UNSET, Unset






T = TypeVar("T", bound="ProjectFeatureState")



@_attrs_define
class ProjectFeatureState:
    """ Details of the feature state.

        Attributes:
            state (ProjectFeatureStateState | Unset): The feature state.
     """

    state: ProjectFeatureStateState | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: ProjectFeatureStateState | Unset
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = ProjectFeatureStateState(_state)




        project_feature_state = cls(
            state=state,
        )

        return project_feature_state

