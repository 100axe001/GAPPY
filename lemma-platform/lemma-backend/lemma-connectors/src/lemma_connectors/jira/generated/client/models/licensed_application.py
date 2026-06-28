from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.licensed_application_plan import LicensedApplicationPlan






T = TypeVar("T", bound="LicensedApplication")



@_attrs_define
class LicensedApplication:
    """ Details about a licensed Jira application.

        Attributes:
            id (str): The ID of the application.
            plan (LicensedApplicationPlan): The licensing plan.
     """

    id: str
    plan: LicensedApplicationPlan





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        plan = self.plan.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "plan": plan,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        plan = LicensedApplicationPlan(d.pop("plan"))




        licensed_application = cls(
            id=id,
            plan=plan,
        )

        return licensed_application

