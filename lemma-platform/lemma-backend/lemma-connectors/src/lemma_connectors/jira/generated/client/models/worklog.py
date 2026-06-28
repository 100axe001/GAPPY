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
  from ..models.entity_property import EntityProperty
  from ..models.user_details import UserDetails
  from ..models.visibility import Visibility





T = TypeVar("T", bound="Worklog")



@_attrs_define
class Worklog:
    r""" Details of a worklog.

        Attributes:
            author (UserDetails | Unset): User details permitted by the user's Atlassian Account privacy settings. However,
                be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            comment (Any | Unset): A comment about the worklog in [Atlassian Document
                Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/). Optional when creating or
                updating a worklog.
            created (datetime.datetime | Unset): The datetime on which the worklog was created.
            id (str | Unset): The ID of the worklog record.
            issue_id (str | Unset): The ID of the issue this worklog is for.
            properties (list[EntityProperty] | Unset): Details of properties for the worklog. Optional when creating or
                updating a worklog.
            self_ (str | Unset): The URL of the worklog item.
            started (datetime.datetime | Unset): The datetime on which the worklog effort was started. Required when
                creating a worklog. Optional when updating a worklog.
            time_spent (str | Unset): The time spent working on the issue as days (\#d), hours (\#h), or minutes (\#m or
                \#). Required when creating a worklog if `timeSpentSeconds` isn't provided. Optional when updating a worklog.
                Cannot be provided if `timeSpentSecond` is provided.
            time_spent_seconds (int | Unset): The time in seconds spent working on the issue. Required when creating a
                worklog if `timeSpent` isn't provided. Optional when updating a worklog. Cannot be provided if `timeSpent` is
                provided.
            update_author (UserDetails | Unset): User details permitted by the user's Atlassian Account privacy settings.
                However, be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            updated (datetime.datetime | Unset): The datetime on which the worklog was last updated.
            visibility (Visibility | Unset): The group or role to which this item is visible.
     """

    author: UserDetails | Unset = UNSET
    comment: Any | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    issue_id: str | Unset = UNSET
    properties: list[EntityProperty] | Unset = UNSET
    self_: str | Unset = UNSET
    started: datetime.datetime | Unset = UNSET
    time_spent: str | Unset = UNSET
    time_spent_seconds: int | Unset = UNSET
    update_author: UserDetails | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    visibility: Visibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_property import EntityProperty
        from ..models.user_details import UserDetails
        from ..models.visibility import Visibility
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        comment = self.comment

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id

        issue_id = self.issue_id

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)



        self_ = self.self_

        started: str | Unset = UNSET
        if not isinstance(self.started, Unset):
            started = self.started.isoformat()

        time_spent = self.time_spent

        time_spent_seconds = self.time_spent_seconds

        update_author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_author, Unset):
            update_author = self.update_author.to_dict()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if author is not UNSET:
            field_dict["author"] = author
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if issue_id is not UNSET:
            field_dict["issueId"] = issue_id
        if properties is not UNSET:
            field_dict["properties"] = properties
        if self_ is not UNSET:
            field_dict["self"] = self_
        if started is not UNSET:
            field_dict["started"] = started
        if time_spent is not UNSET:
            field_dict["timeSpent"] = time_spent
        if time_spent_seconds is not UNSET:
            field_dict["timeSpentSeconds"] = time_spent_seconds
        if update_author is not UNSET:
            field_dict["updateAuthor"] = update_author
        if updated is not UNSET:
            field_dict["updated"] = updated
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_property import EntityProperty
        from ..models.user_details import UserDetails
        from ..models.visibility import Visibility
        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: UserDetails | Unset
        if isinstance(_author,  Unset):
            author = UNSET
        else:
            author = UserDetails.from_dict(_author)




        comment = d.pop("comment", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        id = d.pop("id", UNSET)

        issue_id = d.pop("issueId", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[EntityProperty] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = EntityProperty.from_dict(properties_item_data)



                properties.append(properties_item)


        self_ = d.pop("self", UNSET)

        _started = d.pop("started", UNSET)
        started: datetime.datetime | Unset
        if isinstance(_started,  Unset):
            started = UNSET
        else:
            started = isoparse(_started)




        time_spent = d.pop("timeSpent", UNSET)

        time_spent_seconds = d.pop("timeSpentSeconds", UNSET)

        _update_author = d.pop("updateAuthor", UNSET)
        update_author: UserDetails | Unset
        if isinstance(_update_author,  Unset):
            update_author = UNSET
        else:
            update_author = UserDetails.from_dict(_update_author)




        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated,  Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)




        _visibility = d.pop("visibility", UNSET)
        visibility: Visibility | Unset
        if isinstance(_visibility,  Unset):
            visibility = UNSET
        else:
            visibility = Visibility.from_dict(_visibility)




        worklog = cls(
            author=author,
            comment=comment,
            created=created,
            id=id,
            issue_id=issue_id,
            properties=properties,
            self_=self_,
            started=started,
            time_spent=time_spent,
            time_spent_seconds=time_spent_seconds,
            update_author=update_author,
            updated=updated,
            visibility=visibility,
        )


        worklog.additional_properties = d
        return worklog

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
