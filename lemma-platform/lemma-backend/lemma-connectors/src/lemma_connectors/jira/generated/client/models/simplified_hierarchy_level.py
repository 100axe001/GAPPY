from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="SimplifiedHierarchyLevel")



@_attrs_define
class SimplifiedHierarchyLevel:
    """ 
        Attributes:
            above_level_id (int | Unset): The ID of the level above this one in the hierarchy. This property is deprecated,
                see [Change notice: Removing hierarchy level IDs from next-gen
                APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-
                gen-apis/).
            below_level_id (int | Unset): The ID of the level below this one in the hierarchy. This property is deprecated,
                see [Change notice: Removing hierarchy level IDs from next-gen
                APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-
                gen-apis/).
            external_uuid (UUID | Unset): The external UUID of the hierarchy level. This property is deprecated, see [Change
                notice: Removing hierarchy level IDs from next-gen
                APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-
                gen-apis/).
            hierarchy_level_number (int | Unset):
            id (int | Unset): The ID of the hierarchy level. This property is deprecated, see [Change notice: Removing
                hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-
                removing-hierarchy-level-ids-from-next-gen-apis/).
            issue_type_ids (list[int] | Unset): The issue types available in this hierarchy level.
            level (int | Unset): The level of this item in the hierarchy.
            name (str | Unset): The name of this hierarchy level.
            project_configuration_id (int | Unset): The ID of the project configuration. This property is deprecated, see
                [Change oticen: Removing hierarchy level IDs from next-gen
                APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-
                gen-apis/).
     """

    above_level_id: int | Unset = UNSET
    below_level_id: int | Unset = UNSET
    external_uuid: UUID | Unset = UNSET
    hierarchy_level_number: int | Unset = UNSET
    id: int | Unset = UNSET
    issue_type_ids: list[int] | Unset = UNSET
    level: int | Unset = UNSET
    name: str | Unset = UNSET
    project_configuration_id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        above_level_id = self.above_level_id

        below_level_id = self.below_level_id

        external_uuid: str | Unset = UNSET
        if not isinstance(self.external_uuid, Unset):
            external_uuid = str(self.external_uuid)

        hierarchy_level_number = self.hierarchy_level_number

        id = self.id

        issue_type_ids: list[int] | Unset = UNSET
        if not isinstance(self.issue_type_ids, Unset):
            issue_type_ids = self.issue_type_ids



        level = self.level

        name = self.name

        project_configuration_id = self.project_configuration_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if above_level_id is not UNSET:
            field_dict["aboveLevelId"] = above_level_id
        if below_level_id is not UNSET:
            field_dict["belowLevelId"] = below_level_id
        if external_uuid is not UNSET:
            field_dict["externalUuid"] = external_uuid
        if hierarchy_level_number is not UNSET:
            field_dict["hierarchyLevelNumber"] = hierarchy_level_number
        if id is not UNSET:
            field_dict["id"] = id
        if issue_type_ids is not UNSET:
            field_dict["issueTypeIds"] = issue_type_ids
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if project_configuration_id is not UNSET:
            field_dict["projectConfigurationId"] = project_configuration_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        above_level_id = d.pop("aboveLevelId", UNSET)

        below_level_id = d.pop("belowLevelId", UNSET)

        _external_uuid = d.pop("externalUuid", UNSET)
        external_uuid: UUID | Unset
        if isinstance(_external_uuid,  Unset):
            external_uuid = UNSET
        else:
            external_uuid = UUID(_external_uuid)




        hierarchy_level_number = d.pop("hierarchyLevelNumber", UNSET)

        id = d.pop("id", UNSET)

        issue_type_ids = cast(list[int], d.pop("issueTypeIds", UNSET))


        level = d.pop("level", UNSET)

        name = d.pop("name", UNSET)

        project_configuration_id = d.pop("projectConfigurationId", UNSET)

        simplified_hierarchy_level = cls(
            above_level_id=above_level_id,
            below_level_id=below_level_id,
            external_uuid=external_uuid,
            hierarchy_level_number=hierarchy_level_number,
            id=id,
            issue_type_ids=issue_type_ids,
            level=level,
            name=name,
            project_configuration_id=project_configuration_id,
        )

        return simplified_hierarchy_level

