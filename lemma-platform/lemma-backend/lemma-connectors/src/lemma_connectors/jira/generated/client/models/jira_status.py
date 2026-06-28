from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.jira_status_status_category import JiraStatusStatusCategory
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_issue_types import ProjectIssueTypes
  from ..models.status_scope import StatusScope





T = TypeVar("T", bound="JiraStatus")



@_attrs_define
class JiraStatus:
    """ Details of a status.

        Attributes:
            description (str | Unset): The description of the status.
            id (str | Unset): The ID of the status.
            name (str | Unset): The name of the status.
            scope (StatusScope | Unset): The scope of the status.
            status_category (JiraStatusStatusCategory | Unset): The category of the status.
            usages (list[ProjectIssueTypes] | Unset): Projects and issue types where the status is used. Only available if
                the `usages` expand is requested.
     """

    description: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    scope: StatusScope | Unset = UNSET
    status_category: JiraStatusStatusCategory | Unset = UNSET
    usages: list[ProjectIssueTypes] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_issue_types import ProjectIssueTypes
        from ..models.status_scope import StatusScope
        description = self.description

        id = self.id

        name = self.name

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        status_category: str | Unset = UNSET
        if not isinstance(self.status_category, Unset):
            status_category = self.status_category.value


        usages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usages, Unset):
            usages = []
            for usages_item_data in self.usages:
                usages_item = usages_item_data.to_dict()
                usages.append(usages_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if usages is not UNSET:
            field_dict["usages"] = usages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_issue_types import ProjectIssueTypes
        from ..models.status_scope import StatusScope
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: StatusScope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = StatusScope.from_dict(_scope)




        _status_category = d.pop("statusCategory", UNSET)
        status_category: JiraStatusStatusCategory | Unset
        if isinstance(_status_category,  Unset):
            status_category = UNSET
        else:
            status_category = JiraStatusStatusCategory(_status_category)




        _usages = d.pop("usages", UNSET)
        usages: list[ProjectIssueTypes] | Unset = UNSET
        if _usages is not UNSET:
            usages = []
            for usages_item_data in _usages:
                usages_item = ProjectIssueTypes.from_dict(usages_item_data)



                usages.append(usages_item)


        jira_status = cls(
            description=description,
            id=id,
            name=name,
            scope=scope,
            status_category=status_category,
            usages=usages,
        )

        return jira_status

