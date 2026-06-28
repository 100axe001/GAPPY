from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.licensed_application import LicensedApplication





T = TypeVar("T", bound="License")



@_attrs_define
class License:
    """ Details about a license for the Jira instance.

        Attributes:
            applications (list[LicensedApplication]): The applications under this license.
     """

    applications: list[LicensedApplication]





    def to_dict(self) -> dict[str, Any]:
        from ..models.licensed_application import LicensedApplication
        applications = []
        for applications_item_data in self.applications:
            applications_item = applications_item_data.to_dict()
            applications.append(applications_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "applications": applications,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.licensed_application import LicensedApplication
        d = dict(src_dict)
        applications = []
        _applications = d.pop("applications")
        for applications_item_data in (_applications):
            applications_item = LicensedApplication.from_dict(applications_item_data)



            applications.append(applications_item)


        license_ = cls(
            applications=applications,
        )

        return license_

