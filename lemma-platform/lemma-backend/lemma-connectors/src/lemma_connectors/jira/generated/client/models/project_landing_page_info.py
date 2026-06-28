from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_landing_page_info_attributes import ProjectLandingPageInfoAttributes





T = TypeVar("T", bound="ProjectLandingPageInfo")



@_attrs_define
class ProjectLandingPageInfo:
    """ 
        Attributes:
            attributes (ProjectLandingPageInfoAttributes | Unset):
            board_id (int | Unset):
            board_name (str | Unset):
            project_key (str | Unset):
            project_type (str | Unset):
            queue_category (str | Unset):
            queue_id (int | Unset):
            queue_name (str | Unset):
            simple_board (bool | Unset):
            simplified (bool | Unset):
            url (str | Unset):
     """

    attributes: ProjectLandingPageInfoAttributes | Unset = UNSET
    board_id: int | Unset = UNSET
    board_name: str | Unset = UNSET
    project_key: str | Unset = UNSET
    project_type: str | Unset = UNSET
    queue_category: str | Unset = UNSET
    queue_id: int | Unset = UNSET
    queue_name: str | Unset = UNSET
    simple_board: bool | Unset = UNSET
    simplified: bool | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_landing_page_info_attributes import ProjectLandingPageInfoAttributes
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        board_id = self.board_id

        board_name = self.board_name

        project_key = self.project_key

        project_type = self.project_type

        queue_category = self.queue_category

        queue_id = self.queue_id

        queue_name = self.queue_name

        simple_board = self.simple_board

        simplified = self.simplified

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if board_id is not UNSET:
            field_dict["boardId"] = board_id
        if board_name is not UNSET:
            field_dict["boardName"] = board_name
        if project_key is not UNSET:
            field_dict["projectKey"] = project_key
        if project_type is not UNSET:
            field_dict["projectType"] = project_type
        if queue_category is not UNSET:
            field_dict["queueCategory"] = queue_category
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if queue_name is not UNSET:
            field_dict["queueName"] = queue_name
        if simple_board is not UNSET:
            field_dict["simpleBoard"] = simple_board
        if simplified is not UNSET:
            field_dict["simplified"] = simplified
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_landing_page_info_attributes import ProjectLandingPageInfoAttributes
        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: ProjectLandingPageInfoAttributes | Unset
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = ProjectLandingPageInfoAttributes.from_dict(_attributes)




        board_id = d.pop("boardId", UNSET)

        board_name = d.pop("boardName", UNSET)

        project_key = d.pop("projectKey", UNSET)

        project_type = d.pop("projectType", UNSET)

        queue_category = d.pop("queueCategory", UNSET)

        queue_id = d.pop("queueId", UNSET)

        queue_name = d.pop("queueName", UNSET)

        simple_board = d.pop("simpleBoard", UNSET)

        simplified = d.pop("simplified", UNSET)

        url = d.pop("url", UNSET)

        project_landing_page_info = cls(
            attributes=attributes,
            board_id=board_id,
            board_name=board_name,
            project_key=project_key,
            project_type=project_type,
            queue_category=queue_category,
            queue_id=queue_id,
            queue_name=queue_name,
            simple_board=simple_board,
            simplified=simplified,
            url=url,
        )

        return project_landing_page_info

