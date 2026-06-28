from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.time_tracking_configuration import TimeTrackingConfiguration





T = TypeVar("T", bound="Configuration")



@_attrs_define
class Configuration:
    """ Details about the configuration of Jira.

        Attributes:
            attachments_enabled (bool | Unset): Whether the ability to add attachments to issues is enabled.
            issue_linking_enabled (bool | Unset): Whether the ability to link issues is enabled.
            sub_tasks_enabled (bool | Unset): Whether the ability to create subtasks for issues is enabled.
            time_tracking_configuration (TimeTrackingConfiguration | Unset): Details of the time tracking configuration.
            time_tracking_enabled (bool | Unset): Whether the ability to track time is enabled. This property is deprecated.
            unassigned_issues_allowed (bool | Unset): Whether the ability to create unassigned issues is enabled. See
                [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.
            voting_enabled (bool | Unset): Whether the ability for users to vote on issues is enabled. See [Configuring Jira
                application options](https://confluence.atlassian.com/x/uYXKM) for details.
            watching_enabled (bool | Unset): Whether the ability for users to watch issues is enabled. See [Configuring Jira
                application options](https://confluence.atlassian.com/x/uYXKM) for details.
     """

    attachments_enabled: bool | Unset = UNSET
    issue_linking_enabled: bool | Unset = UNSET
    sub_tasks_enabled: bool | Unset = UNSET
    time_tracking_configuration: TimeTrackingConfiguration | Unset = UNSET
    time_tracking_enabled: bool | Unset = UNSET
    unassigned_issues_allowed: bool | Unset = UNSET
    voting_enabled: bool | Unset = UNSET
    watching_enabled: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.time_tracking_configuration import TimeTrackingConfiguration
        attachments_enabled = self.attachments_enabled

        issue_linking_enabled = self.issue_linking_enabled

        sub_tasks_enabled = self.sub_tasks_enabled

        time_tracking_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_tracking_configuration, Unset):
            time_tracking_configuration = self.time_tracking_configuration.to_dict()

        time_tracking_enabled = self.time_tracking_enabled

        unassigned_issues_allowed = self.unassigned_issues_allowed

        voting_enabled = self.voting_enabled

        watching_enabled = self.watching_enabled


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attachments_enabled is not UNSET:
            field_dict["attachmentsEnabled"] = attachments_enabled
        if issue_linking_enabled is not UNSET:
            field_dict["issueLinkingEnabled"] = issue_linking_enabled
        if sub_tasks_enabled is not UNSET:
            field_dict["subTasksEnabled"] = sub_tasks_enabled
        if time_tracking_configuration is not UNSET:
            field_dict["timeTrackingConfiguration"] = time_tracking_configuration
        if time_tracking_enabled is not UNSET:
            field_dict["timeTrackingEnabled"] = time_tracking_enabled
        if unassigned_issues_allowed is not UNSET:
            field_dict["unassignedIssuesAllowed"] = unassigned_issues_allowed
        if voting_enabled is not UNSET:
            field_dict["votingEnabled"] = voting_enabled
        if watching_enabled is not UNSET:
            field_dict["watchingEnabled"] = watching_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_tracking_configuration import TimeTrackingConfiguration
        d = dict(src_dict)
        attachments_enabled = d.pop("attachmentsEnabled", UNSET)

        issue_linking_enabled = d.pop("issueLinkingEnabled", UNSET)

        sub_tasks_enabled = d.pop("subTasksEnabled", UNSET)

        _time_tracking_configuration = d.pop("timeTrackingConfiguration", UNSET)
        time_tracking_configuration: TimeTrackingConfiguration | Unset
        if isinstance(_time_tracking_configuration,  Unset):
            time_tracking_configuration = UNSET
        else:
            time_tracking_configuration = TimeTrackingConfiguration.from_dict(_time_tracking_configuration)




        time_tracking_enabled = d.pop("timeTrackingEnabled", UNSET)

        unassigned_issues_allowed = d.pop("unassignedIssuesAllowed", UNSET)

        voting_enabled = d.pop("votingEnabled", UNSET)

        watching_enabled = d.pop("watchingEnabled", UNSET)

        configuration = cls(
            attachments_enabled=attachments_enabled,
            issue_linking_enabled=issue_linking_enabled,
            sub_tasks_enabled=sub_tasks_enabled,
            time_tracking_configuration=time_tracking_configuration,
            time_tracking_enabled=time_tracking_enabled,
            unassigned_issues_allowed=unassigned_issues_allowed,
            voting_enabled=voting_enabled,
            watching_enabled=watching_enabled,
        )

        return configuration

