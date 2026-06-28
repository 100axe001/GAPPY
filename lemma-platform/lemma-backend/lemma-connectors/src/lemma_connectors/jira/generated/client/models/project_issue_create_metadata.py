from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.avatar_urls_bean import AvatarUrlsBean
  from ..models.issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata





T = TypeVar("T", bound="ProjectIssueCreateMetadata")



@_attrs_define
class ProjectIssueCreateMetadata:
    """ Details of the issue creation metadata for a project.

        Attributes:
            avatar_urls (AvatarUrlsBean | Unset):
            expand (str | Unset): Expand options that include additional project issue create metadata details in the
                response.
            id (str | Unset): The ID of the project.
            issuetypes (list[IssueTypeIssueCreateMetadata] | Unset): List of the issue types supported by the project.
            key (str | Unset): The key of the project.
            name (str | Unset): The name of the project.
            self_ (str | Unset): The URL of the project.
     """

    avatar_urls: AvatarUrlsBean | Unset = UNSET
    expand: str | Unset = UNSET
    id: str | Unset = UNSET
    issuetypes: list[IssueTypeIssueCreateMetadata] | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.avatar_urls_bean import AvatarUrlsBean
        from ..models.issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata
        avatar_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar_urls, Unset):
            avatar_urls = self.avatar_urls.to_dict()

        expand = self.expand

        id = self.id

        issuetypes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issuetypes, Unset):
            issuetypes = []
            for issuetypes_item_data in self.issuetypes:
                issuetypes_item = issuetypes_item_data.to_dict()
                issuetypes.append(issuetypes_item)



        key = self.key

        name = self.name

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_urls is not UNSET:
            field_dict["avatarUrls"] = avatar_urls
        if expand is not UNSET:
            field_dict["expand"] = expand
        if id is not UNSET:
            field_dict["id"] = id
        if issuetypes is not UNSET:
            field_dict["issuetypes"] = issuetypes
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar_urls_bean import AvatarUrlsBean
        from ..models.issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata
        d = dict(src_dict)
        _avatar_urls = d.pop("avatarUrls", UNSET)
        avatar_urls: AvatarUrlsBean | Unset
        if isinstance(_avatar_urls,  Unset):
            avatar_urls = UNSET
        else:
            avatar_urls = AvatarUrlsBean.from_dict(_avatar_urls)




        expand = d.pop("expand", UNSET)

        id = d.pop("id", UNSET)

        _issuetypes = d.pop("issuetypes", UNSET)
        issuetypes: list[IssueTypeIssueCreateMetadata] | Unset = UNSET
        if _issuetypes is not UNSET:
            issuetypes = []
            for issuetypes_item_data in _issuetypes:
                issuetypes_item = IssueTypeIssueCreateMetadata.from_dict(issuetypes_item_data)



                issuetypes.append(issuetypes_item)


        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        project_issue_create_metadata = cls(
            avatar_urls=avatar_urls,
            expand=expand,
            id=id,
            issuetypes=issuetypes,
            key=key,
            name=name,
            self_=self_,
        )

        return project_issue_create_metadata

