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





T = TypeVar("T", bound="Comment")



@_attrs_define
class Comment:
    """ A comment.

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
            body (Any | Unset): The comment text in [Atlassian Document
                Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/).
            created (datetime.datetime | Unset): The date and time at which the comment was created.
            id (str | Unset): The ID of the comment.
            jsd_author_can_see_request (bool | Unset): Whether the comment was added from an email sent by a person who is
                not part of the issue. See [Allow external emails to be added as comments on
                issues](https://support.atlassian.com/jira-service-management-cloud/docs/allow-external-emails-to-be-added-as-
                comments-on-issues/)for information on setting up this feature.
            jsd_public (bool | Unset): Whether the comment is visible in Jira Service Desk. Defaults to true when comments
                are created in the Jira Cloud Platform. This includes when the site doesn't use Jira Service Desk or the project
                isn't a Jira Service Desk project and, therefore, there is no Jira Service Desk for the issue to be visible on.
                To create a comment with its visibility in Jira Service Desk set to false, use the Jira Service Desk REST API
                [Create request comment](https://developer.atlassian.com/cloud/jira/service-desk/rest/#api-rest-servicedeskapi-
                request-issueIdOrKey-comment-post) operation.
            properties (list[EntityProperty] | Unset): A list of comment properties. Optional on create and update.
            rendered_body (str | Unset): The rendered version of the comment.
            self_ (str | Unset): The URL of the comment.
            update_author (UserDetails | Unset): User details permitted by the user's Atlassian Account privacy settings.
                However, be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            updated (datetime.datetime | Unset): The date and time at which the comment was updated last.
            visibility (Visibility | Unset): The group or role to which this item is visible.
     """

    author: UserDetails | Unset = UNSET
    body: Any | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    jsd_author_can_see_request: bool | Unset = UNSET
    jsd_public: bool | Unset = UNSET
    properties: list[EntityProperty] | Unset = UNSET
    rendered_body: str | Unset = UNSET
    self_: str | Unset = UNSET
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

        body = self.body

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id

        jsd_author_can_see_request = self.jsd_author_can_see_request

        jsd_public = self.jsd_public

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)



        rendered_body = self.rendered_body

        self_ = self.self_

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
        if body is not UNSET:
            field_dict["body"] = body
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if jsd_author_can_see_request is not UNSET:
            field_dict["jsdAuthorCanSeeRequest"] = jsd_author_can_see_request
        if jsd_public is not UNSET:
            field_dict["jsdPublic"] = jsd_public
        if properties is not UNSET:
            field_dict["properties"] = properties
        if rendered_body is not UNSET:
            field_dict["renderedBody"] = rendered_body
        if self_ is not UNSET:
            field_dict["self"] = self_
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




        body = d.pop("body", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        id = d.pop("id", UNSET)

        jsd_author_can_see_request = d.pop("jsdAuthorCanSeeRequest", UNSET)

        jsd_public = d.pop("jsdPublic", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[EntityProperty] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = EntityProperty.from_dict(properties_item_data)



                properties.append(properties_item)


        rendered_body = d.pop("renderedBody", UNSET)

        self_ = d.pop("self", UNSET)

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




        comment = cls(
            author=author,
            body=body,
            created=created,
            id=id,
            jsd_author_can_see_request=jsd_author_can_see_request,
            jsd_public=jsd_public,
            properties=properties,
            rendered_body=rendered_body,
            self_=self_,
            update_author=update_author,
            updated=updated,
            visibility=visibility,
        )


        comment.additional_properties = d
        return comment

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
