from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IterativeCalculationSettings")



@_attrs_define
class IterativeCalculationSettings:
    """ Settings to control how circular dependencies are resolved with iterative calculation.

        Attributes:
            convergence_threshold (float | Unset): When iterative calculation is enabled and successive results differ by
                less than this threshold value, the calculation rounds stop.
            max_iterations (int | Unset): When iterative calculation is enabled, the maximum number of calculation rounds to
                perform.
     """

    convergence_threshold: float | Unset = UNSET
    max_iterations: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        convergence_threshold = self.convergence_threshold

        max_iterations = self.max_iterations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if convergence_threshold is not UNSET:
            field_dict["convergenceThreshold"] = convergence_threshold
        if max_iterations is not UNSET:
            field_dict["maxIterations"] = max_iterations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        convergence_threshold = d.pop("convergenceThreshold", UNSET)

        max_iterations = d.pop("maxIterations", UNSET)

        iterative_calculation_settings = cls(
            convergence_threshold=convergence_threshold,
            max_iterations=max_iterations,
        )


        iterative_calculation_settings.additional_properties = d
        return iterative_calculation_settings

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
