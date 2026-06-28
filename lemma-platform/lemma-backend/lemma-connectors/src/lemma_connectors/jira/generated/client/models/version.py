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
  from ..models.simple_link import SimpleLink
  from ..models.version_issues_status import VersionIssuesStatus





T = TypeVar("T", bound="Version")



@_attrs_define
class Version:
    """ Details about a project version.

        Attributes:
            archived (bool | Unset): Indicates that the version is archived. Optional when creating or updating a version.
            description (str | Unset): The description of the version. Optional when creating or updating a version.
            expand (str | Unset): Use [expand](em>#expansion) to include additional information about version in the
                response. This parameter accepts a comma-separated list. Expand options include:

                 *  `operations` Returns the list of operations available for this version.
                 *  `issuesstatus` Returns the count of issues in this version for each of the status categories *to do*, *in
                progress*, *done*, and *unmapped*. The *unmapped* property contains a count of issues with a status other than
                *to do*, *in progress*, and *done*.

                Optional for create and update.
            id (str | Unset): The ID of the version.
            issues_status_for_fix_version (VersionIssuesStatus | Unset): Counts of the number of issues in various statuses.
            move_unfixed_issues_to (str | Unset): The URL of the self link to the version to which all unfixed issues are
                moved when a version is released. Not applicable when creating a version. Optional when updating a version.
            name (str | Unset): The unique name of the version. Required when creating a version. Optional when updating a
                version. The maximum length is 255 characters.
            operations (list[SimpleLink] | Unset): If the expand option `operations` is used, returns the list of operations
                available for this version.
            overdue (bool | Unset): Indicates that the version is overdue.
            project (str | Unset): Deprecated. Use `projectId`.
            project_id (int | Unset): The ID of the project to which this version is attached. Required when creating a
                version. Not applicable when updating a version.
            release_date (datetime.date | Unset): The release date of the version. Expressed in ISO 8601 format (yyyy-mm-
                dd). Optional when creating or updating a version.
            released (bool | Unset): Indicates that the version is released. If the version is released a request to release
                again is ignored. Not applicable when creating a version. Optional when updating a version.
            self_ (str | Unset): The URL of the version.
            start_date (datetime.date | Unset): The start date of the version. Expressed in ISO 8601 format (yyyy-mm-dd).
                Optional when creating or updating a version.
            user_release_date (str | Unset): The date on which work on this version is expected to finish, expressed in the
                instance's *Day/Month/Year Format* date format.
            user_start_date (str | Unset): The date on which work on this version is expected to start, expressed in the
                instance's *Day/Month/Year Format* date format.
     """

    archived: bool | Unset = UNSET
    description: str | Unset = UNSET
    expand: str | Unset = UNSET
    id: str | Unset = UNSET
    issues_status_for_fix_version: VersionIssuesStatus | Unset = UNSET
    move_unfixed_issues_to: str | Unset = UNSET
    name: str | Unset = UNSET
    operations: list[SimpleLink] | Unset = UNSET
    overdue: bool | Unset = UNSET
    project: str | Unset = UNSET
    project_id: int | Unset = UNSET
    release_date: datetime.date | Unset = UNSET
    released: bool | Unset = UNSET
    self_: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    user_release_date: str | Unset = UNSET
    user_start_date: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_link import SimpleLink
        from ..models.version_issues_status import VersionIssuesStatus
        archived = self.archived

        description = self.description

        expand = self.expand

        id = self.id

        issues_status_for_fix_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issues_status_for_fix_version, Unset):
            issues_status_for_fix_version = self.issues_status_for_fix_version.to_dict()

        move_unfixed_issues_to = self.move_unfixed_issues_to

        name = self.name

        operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.to_dict()
                operations.append(operations_item)



        overdue = self.overdue

        project = self.project

        project_id = self.project_id

        release_date: str | Unset = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        released = self.released

        self_ = self.self_

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        user_release_date = self.user_release_date

        user_start_date = self.user_start_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if archived is not UNSET:
            field_dict["archived"] = archived
        if description is not UNSET:
            field_dict["description"] = description
        if expand is not UNSET:
            field_dict["expand"] = expand
        if id is not UNSET:
            field_dict["id"] = id
        if issues_status_for_fix_version is not UNSET:
            field_dict["issuesStatusForFixVersion"] = issues_status_for_fix_version
        if move_unfixed_issues_to is not UNSET:
            field_dict["moveUnfixedIssuesTo"] = move_unfixed_issues_to
        if name is not UNSET:
            field_dict["name"] = name
        if operations is not UNSET:
            field_dict["operations"] = operations
        if overdue is not UNSET:
            field_dict["overdue"] = overdue
        if project is not UNSET:
            field_dict["project"] = project
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if released is not UNSET:
            field_dict["released"] = released
        if self_ is not UNSET:
            field_dict["self"] = self_
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if user_release_date is not UNSET:
            field_dict["userReleaseDate"] = user_release_date
        if user_start_date is not UNSET:
            field_dict["userStartDate"] = user_start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_link import SimpleLink
        from ..models.version_issues_status import VersionIssuesStatus
        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        description = d.pop("description", UNSET)

        expand = d.pop("expand", UNSET)

        id = d.pop("id", UNSET)

        _issues_status_for_fix_version = d.pop("issuesStatusForFixVersion", UNSET)
        issues_status_for_fix_version: VersionIssuesStatus | Unset
        if isinstance(_issues_status_for_fix_version,  Unset):
            issues_status_for_fix_version = UNSET
        else:
            issues_status_for_fix_version = VersionIssuesStatus.from_dict(_issues_status_for_fix_version)




        move_unfixed_issues_to = d.pop("moveUnfixedIssuesTo", UNSET)

        name = d.pop("name", UNSET)

        _operations = d.pop("operations", UNSET)
        operations: list[SimpleLink] | Unset = UNSET
        if _operations is not UNSET:
            operations = []
            for operations_item_data in _operations:
                operations_item = SimpleLink.from_dict(operations_item_data)



                operations.append(operations_item)


        overdue = d.pop("overdue", UNSET)

        project = d.pop("project", UNSET)

        project_id = d.pop("projectId", UNSET)

        _release_date = d.pop("releaseDate", UNSET)
        release_date: datetime.date | Unset
        if isinstance(_release_date,  Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()




        released = d.pop("released", UNSET)

        self_ = d.pop("self", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()




        user_release_date = d.pop("userReleaseDate", UNSET)

        user_start_date = d.pop("userStartDate", UNSET)

        version = cls(
            archived=archived,
            description=description,
            expand=expand,
            id=id,
            issues_status_for_fix_version=issues_status_for_fix_version,
            move_unfixed_issues_to=move_unfixed_issues_to,
            name=name,
            operations=operations,
            overdue=overdue,
            project=project,
            project_id=project_id,
            release_date=release_date,
            released=released,
            self_=self_,
            start_date=start_date,
            user_release_date=user_release_date,
            user_start_date=user_start_date,
        )

        return version

