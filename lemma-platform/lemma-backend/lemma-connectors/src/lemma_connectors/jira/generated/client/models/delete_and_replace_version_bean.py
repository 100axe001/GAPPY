from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_field_replacement import CustomFieldReplacement





T = TypeVar("T", bound="DeleteAndReplaceVersionBean")



@_attrs_define
class DeleteAndReplaceVersionBean:
    """ 
        Attributes:
            custom_field_replacement_list (list[CustomFieldReplacement] | Unset): An array of custom field IDs
                (`customFieldId`) and version IDs (`moveTo`) to update when the fields contain the deleted version.
            move_affected_issues_to (int | Unset): The ID of the version to update `affectedVersion` to when the field
                contains the deleted version.
            move_fix_issues_to (int | Unset): The ID of the version to update `fixVersion` to when the field contains the
                deleted version.
     """

    custom_field_replacement_list: list[CustomFieldReplacement] | Unset = UNSET
    move_affected_issues_to: int | Unset = UNSET
    move_fix_issues_to: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_field_replacement import CustomFieldReplacement
        custom_field_replacement_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_field_replacement_list, Unset):
            custom_field_replacement_list = []
            for custom_field_replacement_list_item_data in self.custom_field_replacement_list:
                custom_field_replacement_list_item = custom_field_replacement_list_item_data.to_dict()
                custom_field_replacement_list.append(custom_field_replacement_list_item)



        move_affected_issues_to = self.move_affected_issues_to

        move_fix_issues_to = self.move_fix_issues_to


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if custom_field_replacement_list is not UNSET:
            field_dict["customFieldReplacementList"] = custom_field_replacement_list
        if move_affected_issues_to is not UNSET:
            field_dict["moveAffectedIssuesTo"] = move_affected_issues_to
        if move_fix_issues_to is not UNSET:
            field_dict["moveFixIssuesTo"] = move_fix_issues_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_replacement import CustomFieldReplacement
        d = dict(src_dict)
        _custom_field_replacement_list = d.pop("customFieldReplacementList", UNSET)
        custom_field_replacement_list: list[CustomFieldReplacement] | Unset = UNSET
        if _custom_field_replacement_list is not UNSET:
            custom_field_replacement_list = []
            for custom_field_replacement_list_item_data in _custom_field_replacement_list:
                custom_field_replacement_list_item = CustomFieldReplacement.from_dict(custom_field_replacement_list_item_data)



                custom_field_replacement_list.append(custom_field_replacement_list_item)


        move_affected_issues_to = d.pop("moveAffectedIssuesTo", UNSET)

        move_fix_issues_to = d.pop("moveFixIssuesTo", UNSET)

        delete_and_replace_version_bean = cls(
            custom_field_replacement_list=custom_field_replacement_list,
            move_affected_issues_to=move_affected_issues_to,
            move_fix_issues_to=move_fix_issues_to,
        )

        return delete_and_replace_version_bean

