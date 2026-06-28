from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.issue_type_issue_create_metadata_fields import IssueTypeIssueCreateMetadataFields
  from ..models.scope import Scope





T = TypeVar("T", bound="IssueTypeIssueCreateMetadata")



@_attrs_define
class IssueTypeIssueCreateMetadata:
    """ Details of the issue creation metadata for an issue type.

        Attributes:
            avatar_id (int | Unset): The ID of the issue type's avatar.
            description (str | Unset): The description of the issue type.
            entity_id (UUID | Unset): Unique ID for next-gen projects.
            expand (str | Unset): Expand options that include additional issue type metadata details in the response.
            fields (IssueTypeIssueCreateMetadataFields | Unset): List of the fields available when creating an issue for the
                issue type.
            hierarchy_level (int | Unset): Hierarchy level of the issue type.
            icon_url (str | Unset): The URL of the issue type's avatar.
            id (str | Unset): The ID of the issue type.
            name (str | Unset): The name of the issue type.
            scope (Scope | Unset): The projects the item is associated with. Indicated for items associated with [next-gen
                projects](https://confluence.atlassian.com/x/loMyO).
            self_ (str | Unset): The URL of these issue type details.
            subtask (bool | Unset): Whether this issue type is used to create subtasks.
     """

    avatar_id: int | Unset = UNSET
    description: str | Unset = UNSET
    entity_id: UUID | Unset = UNSET
    expand: str | Unset = UNSET
    fields: IssueTypeIssueCreateMetadataFields | Unset = UNSET
    hierarchy_level: int | Unset = UNSET
    icon_url: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    scope: Scope | Unset = UNSET
    self_: str | Unset = UNSET
    subtask: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_type_issue_create_metadata_fields import IssueTypeIssueCreateMetadataFields
        from ..models.scope import Scope
        avatar_id = self.avatar_id

        description = self.description

        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        expand = self.expand

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        hierarchy_level = self.hierarchy_level

        icon_url = self.icon_url

        id = self.id

        name = self.name

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        self_ = self.self_

        subtask = self.subtask


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_id is not UNSET:
            field_dict["avatarId"] = avatar_id
        if description is not UNSET:
            field_dict["description"] = description
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if expand is not UNSET:
            field_dict["expand"] = expand
        if fields is not UNSET:
            field_dict["fields"] = fields
        if hierarchy_level is not UNSET:
            field_dict["hierarchyLevel"] = hierarchy_level
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if self_ is not UNSET:
            field_dict["self"] = self_
        if subtask is not UNSET:
            field_dict["subtask"] = subtask

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_type_issue_create_metadata_fields import IssueTypeIssueCreateMetadataFields
        from ..models.scope import Scope
        d = dict(src_dict)
        avatar_id = d.pop("avatarId", UNSET)

        description = d.pop("description", UNSET)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id,  Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)




        expand = d.pop("expand", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: IssueTypeIssueCreateMetadataFields | Unset
        if isinstance(_fields,  Unset):
            fields = UNSET
        else:
            fields = IssueTypeIssueCreateMetadataFields.from_dict(_fields)




        hierarchy_level = d.pop("hierarchyLevel", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = Scope.from_dict(_scope)




        self_ = d.pop("self", UNSET)

        subtask = d.pop("subtask", UNSET)

        issue_type_issue_create_metadata = cls(
            avatar_id=avatar_id,
            description=description,
            entity_id=entity_id,
            expand=expand,
            fields=fields,
            hierarchy_level=hierarchy_level,
            icon_url=icon_url,
            id=id,
            name=name,
            scope=scope,
            self_=self_,
            subtask=subtask,
        )

        return issue_type_issue_create_metadata

