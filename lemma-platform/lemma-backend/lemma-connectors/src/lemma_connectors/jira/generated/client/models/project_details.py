from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.project_details_project_type_key import ProjectDetailsProjectTypeKey
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.avatar_urls_bean import AvatarUrlsBean
  from ..models.updated_project_category import UpdatedProjectCategory





T = TypeVar("T", bound="ProjectDetails")



@_attrs_define
class ProjectDetails:
    """ Details about a project.

        Attributes:
            avatar_urls (AvatarUrlsBean | Unset):
            id (str | Unset): The ID of the project.
            key (str | Unset): The key of the project.
            name (str | Unset): The name of the project.
            project_category (UpdatedProjectCategory | Unset): A project category.
            project_type_key (ProjectDetailsProjectTypeKey | Unset): The [project
                type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes) of the
                project.
            self_ (str | Unset): The URL of the project details.
            simplified (bool | Unset): Whether or not the project is simplified.
     """

    avatar_urls: AvatarUrlsBean | Unset = UNSET
    id: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    project_category: UpdatedProjectCategory | Unset = UNSET
    project_type_key: ProjectDetailsProjectTypeKey | Unset = UNSET
    self_: str | Unset = UNSET
    simplified: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.avatar_urls_bean import AvatarUrlsBean
        from ..models.updated_project_category import UpdatedProjectCategory
        avatar_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar_urls, Unset):
            avatar_urls = self.avatar_urls.to_dict()

        id = self.id

        key = self.key

        name = self.name

        project_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_category, Unset):
            project_category = self.project_category.to_dict()

        project_type_key: str | Unset = UNSET
        if not isinstance(self.project_type_key, Unset):
            project_type_key = self.project_type_key.value


        self_ = self.self_

        simplified = self.simplified


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_urls is not UNSET:
            field_dict["avatarUrls"] = avatar_urls
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if project_category is not UNSET:
            field_dict["projectCategory"] = project_category
        if project_type_key is not UNSET:
            field_dict["projectTypeKey"] = project_type_key
        if self_ is not UNSET:
            field_dict["self"] = self_
        if simplified is not UNSET:
            field_dict["simplified"] = simplified

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar_urls_bean import AvatarUrlsBean
        from ..models.updated_project_category import UpdatedProjectCategory
        d = dict(src_dict)
        _avatar_urls = d.pop("avatarUrls", UNSET)
        avatar_urls: AvatarUrlsBean | Unset
        if isinstance(_avatar_urls,  Unset):
            avatar_urls = UNSET
        else:
            avatar_urls = AvatarUrlsBean.from_dict(_avatar_urls)




        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        _project_category = d.pop("projectCategory", UNSET)
        project_category: UpdatedProjectCategory | Unset
        if isinstance(_project_category,  Unset):
            project_category = UNSET
        else:
            project_category = UpdatedProjectCategory.from_dict(_project_category)




        _project_type_key = d.pop("projectTypeKey", UNSET)
        project_type_key: ProjectDetailsProjectTypeKey | Unset
        if isinstance(_project_type_key,  Unset):
            project_type_key = UNSET
        else:
            project_type_key = ProjectDetailsProjectTypeKey(_project_type_key)




        self_ = d.pop("self", UNSET)

        simplified = d.pop("simplified", UNSET)

        project_details = cls(
            avatar_urls=avatar_urls,
            id=id,
            key=key,
            name=name,
            project_category=project_category,
            project_type_key=project_type_key,
            self_=self_,
            simplified=simplified,
        )

        return project_details

