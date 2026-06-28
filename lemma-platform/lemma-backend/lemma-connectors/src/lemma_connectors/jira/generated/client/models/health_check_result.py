from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="HealthCheckResult")



@_attrs_define
class HealthCheckResult:
    """ Jira instance health check results. Deprecated and no longer returned.

        Attributes:
            description (str | Unset): The description of the Jira health check item.
            name (str | Unset): The name of the Jira health check item.
            passed (bool | Unset): Whether the Jira health check item passed or failed.
     """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    passed: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        passed = self.passed


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if passed is not UNSET:
            field_dict["passed"] = passed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        passed = d.pop("passed", UNSET)

        health_check_result = cls(
            description=description,
            name=name,
            passed=passed,
        )

        return health_check_result

