from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_type_details import IssueTypeDetails
  from ..models.priority import Priority
  from ..models.status_details import StatusDetails
  from ..models.time_tracking_details import TimeTrackingDetails
  from ..models.user_details import UserDetails





T = TypeVar("T", bound="Fields")



@_attrs_define
class Fields:
    """ Key fields from the linked issue.

        Attributes:
            assignee (UserDetails | Unset): User details permitted by the user's Atlassian Account privacy settings.
                However, be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            issue_type (IssueTypeDetails | Unset): Details about an issue type.
            issuetype (IssueTypeDetails | Unset): Details about an issue type.
            priority (Priority | Unset): An issue priority.
            status (StatusDetails | Unset): A status.
            summary (str | Unset): The summary description of the linked issue.
            timetracking (TimeTrackingDetails | Unset): Time tracking details.
     """

    assignee: UserDetails | Unset = UNSET
    issue_type: IssueTypeDetails | Unset = UNSET
    issuetype: IssueTypeDetails | Unset = UNSET
    priority: Priority | Unset = UNSET
    status: StatusDetails | Unset = UNSET
    summary: str | Unset = UNSET
    timetracking: TimeTrackingDetails | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_type_details import IssueTypeDetails
        from ..models.priority import Priority
        from ..models.status_details import StatusDetails
        from ..models.time_tracking_details import TimeTrackingDetails
        from ..models.user_details import UserDetails
        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        issue_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_type, Unset):
            issue_type = self.issue_type.to_dict()

        issuetype: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issuetype, Unset):
            issuetype = self.issuetype.to_dict()

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        summary = self.summary

        timetracking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timetracking, Unset):
            timetracking = self.timetracking.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if issue_type is not UNSET:
            field_dict["issueType"] = issue_type
        if issuetype is not UNSET:
            field_dict["issuetype"] = issuetype
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if timetracking is not UNSET:
            field_dict["timetracking"] = timetracking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_type_details import IssueTypeDetails
        from ..models.priority import Priority
        from ..models.status_details import StatusDetails
        from ..models.time_tracking_details import TimeTrackingDetails
        from ..models.user_details import UserDetails
        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: UserDetails | Unset
        if isinstance(_assignee,  Unset):
            assignee = UNSET
        else:
            assignee = UserDetails.from_dict(_assignee)




        _issue_type = d.pop("issueType", UNSET)
        issue_type: IssueTypeDetails | Unset
        if isinstance(_issue_type,  Unset):
            issue_type = UNSET
        else:
            issue_type = IssueTypeDetails.from_dict(_issue_type)




        _issuetype = d.pop("issuetype", UNSET)
        issuetype: IssueTypeDetails | Unset
        if isinstance(_issuetype,  Unset):
            issuetype = UNSET
        else:
            issuetype = IssueTypeDetails.from_dict(_issuetype)




        _priority = d.pop("priority", UNSET)
        priority: Priority | Unset
        if isinstance(_priority,  Unset):
            priority = UNSET
        else:
            priority = Priority.from_dict(_priority)




        _status = d.pop("status", UNSET)
        status: StatusDetails | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = StatusDetails.from_dict(_status)




        summary = d.pop("summary", UNSET)

        _timetracking = d.pop("timetracking", UNSET)
        timetracking: TimeTrackingDetails | Unset
        if isinstance(_timetracking,  Unset):
            timetracking = UNSET
        else:
            timetracking = TimeTrackingDetails.from_dict(_timetracking)




        fields = cls(
            assignee=assignee,
            issue_type=issue_type,
            issuetype=issuetype,
            priority=priority,
            status=status,
            summary=summary,
            timetracking=timetracking,
        )

        return fields

