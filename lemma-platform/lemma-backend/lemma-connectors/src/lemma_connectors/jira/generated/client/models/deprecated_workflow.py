from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scope import Scope





T = TypeVar("T", bound="DeprecatedWorkflow")



@_attrs_define
class DeprecatedWorkflow:
    """ Details about a workflow.

        Attributes:
            default (bool | Unset):
            description (str | Unset): The description of the workflow.
            last_modified_date (str | Unset): The datetime the workflow was last modified.
            last_modified_user (str | Unset): This property is no longer available and will be removed from the
                documentation soon. See the [deprecation
                notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-
                guide/) for details.
            last_modified_user_account_id (str | Unset): The account ID of the user that last modified the workflow.
            name (str | Unset): The name of the workflow.
            scope (Scope | Unset): The projects the item is associated with. Indicated for items associated with [next-gen
                projects](https://confluence.atlassian.com/x/loMyO).
            steps (int | Unset): The number of steps included in the workflow.
     """

    default: bool | Unset = UNSET
    description: str | Unset = UNSET
    last_modified_date: str | Unset = UNSET
    last_modified_user: str | Unset = UNSET
    last_modified_user_account_id: str | Unset = UNSET
    name: str | Unset = UNSET
    scope: Scope | Unset = UNSET
    steps: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.scope import Scope
        default = self.default

        description = self.description

        last_modified_date = self.last_modified_date

        last_modified_user = self.last_modified_user

        last_modified_user_account_id = self.last_modified_user_account_id

        name = self.name

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        steps = self.steps


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if last_modified_date is not UNSET:
            field_dict["lastModifiedDate"] = last_modified_date
        if last_modified_user is not UNSET:
            field_dict["lastModifiedUser"] = last_modified_user
        if last_modified_user_account_id is not UNSET:
            field_dict["lastModifiedUserAccountId"] = last_modified_user_account_id
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scope import Scope
        d = dict(src_dict)
        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        last_modified_date = d.pop("lastModifiedDate", UNSET)

        last_modified_user = d.pop("lastModifiedUser", UNSET)

        last_modified_user_account_id = d.pop("lastModifiedUserAccountId", UNSET)

        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = Scope.from_dict(_scope)




        steps = d.pop("steps", UNSET)

        deprecated_workflow = cls(
            default=default,
            description=description,
            last_modified_date=last_modified_date,
            last_modified_user=last_modified_user,
            last_modified_user_account_id=last_modified_user_account_id,
            name=name,
            scope=scope,
            steps=steps,
        )

        return deprecated_workflow

