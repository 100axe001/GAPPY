from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.health_check_result import HealthCheckResult





T = TypeVar("T", bound="ServerInformation")



@_attrs_define
class ServerInformation:
    """ Details about the Jira instance.

        Attributes:
            base_url (str | Unset): The base URL of the Jira instance.
            build_date (datetime.datetime | Unset): The timestamp when the Jira version was built.
            build_number (int | Unset): The build number of the Jira version.
            deployment_type (str | Unset): The type of server deployment. This is always returned as *Cloud*.
            health_checks (list[HealthCheckResult] | Unset): Jira instance health check results. Deprecated and no longer
                returned.
            scm_info (str | Unset): The unique identifier of the Jira version.
            server_time (datetime.datetime | Unset): The time in Jira when this request was responded to.
            server_title (str | Unset): The name of the Jira instance.
            version (str | Unset): The version of Jira.
            version_numbers (list[int] | Unset): The major, minor, and revision version numbers of the Jira version.
     """

    base_url: str | Unset = UNSET
    build_date: datetime.datetime | Unset = UNSET
    build_number: int | Unset = UNSET
    deployment_type: str | Unset = UNSET
    health_checks: list[HealthCheckResult] | Unset = UNSET
    scm_info: str | Unset = UNSET
    server_time: datetime.datetime | Unset = UNSET
    server_title: str | Unset = UNSET
    version: str | Unset = UNSET
    version_numbers: list[int] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.health_check_result import HealthCheckResult
        base_url = self.base_url

        build_date: str | Unset = UNSET
        if not isinstance(self.build_date, Unset):
            build_date = self.build_date.isoformat()

        build_number = self.build_number

        deployment_type = self.deployment_type

        health_checks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.health_checks, Unset):
            health_checks = []
            for health_checks_item_data in self.health_checks:
                health_checks_item = health_checks_item_data.to_dict()
                health_checks.append(health_checks_item)



        scm_info = self.scm_info

        server_time: str | Unset = UNSET
        if not isinstance(self.server_time, Unset):
            server_time = self.server_time.isoformat()

        server_title = self.server_title

        version = self.version

        version_numbers: list[int] | Unset = UNSET
        if not isinstance(self.version_numbers, Unset):
            version_numbers = self.version_numbers




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if build_date is not UNSET:
            field_dict["buildDate"] = build_date
        if build_number is not UNSET:
            field_dict["buildNumber"] = build_number
        if deployment_type is not UNSET:
            field_dict["deploymentType"] = deployment_type
        if health_checks is not UNSET:
            field_dict["healthChecks"] = health_checks
        if scm_info is not UNSET:
            field_dict["scmInfo"] = scm_info
        if server_time is not UNSET:
            field_dict["serverTime"] = server_time
        if server_title is not UNSET:
            field_dict["serverTitle"] = server_title
        if version is not UNSET:
            field_dict["version"] = version
        if version_numbers is not UNSET:
            field_dict["versionNumbers"] = version_numbers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health_check_result import HealthCheckResult
        d = dict(src_dict)
        base_url = d.pop("baseUrl", UNSET)

        _build_date = d.pop("buildDate", UNSET)
        build_date: datetime.datetime | Unset
        if isinstance(_build_date,  Unset):
            build_date = UNSET
        else:
            build_date = isoparse(_build_date)




        build_number = d.pop("buildNumber", UNSET)

        deployment_type = d.pop("deploymentType", UNSET)

        _health_checks = d.pop("healthChecks", UNSET)
        health_checks: list[HealthCheckResult] | Unset = UNSET
        if _health_checks is not UNSET:
            health_checks = []
            for health_checks_item_data in _health_checks:
                health_checks_item = HealthCheckResult.from_dict(health_checks_item_data)



                health_checks.append(health_checks_item)


        scm_info = d.pop("scmInfo", UNSET)

        _server_time = d.pop("serverTime", UNSET)
        server_time: datetime.datetime | Unset
        if isinstance(_server_time,  Unset):
            server_time = UNSET
        else:
            server_time = isoparse(_server_time)




        server_title = d.pop("serverTitle", UNSET)

        version = d.pop("version", UNSET)

        version_numbers = cast(list[int], d.pop("versionNumbers", UNSET))


        server_information = cls(
            base_url=base_url,
            build_date=build_date,
            build_number=build_number,
            deployment_type=deployment_type,
            health_checks=health_checks,
            scm_info=scm_info,
            server_time=server_time,
            server_title=server_title,
            version=version,
            version_numbers=version_numbers,
        )

        return server_information

