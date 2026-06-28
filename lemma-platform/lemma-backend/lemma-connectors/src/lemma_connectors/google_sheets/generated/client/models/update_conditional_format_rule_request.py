from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conditional_format_rule import ConditionalFormatRule





T = TypeVar("T", bound="UpdateConditionalFormatRuleRequest")



@_attrs_define
class UpdateConditionalFormatRuleRequest:
    """ Updates a conditional format rule at the given index, or moves a conditional format rule to another index.

        Attributes:
            index (int | Unset): The zero-based index of the rule that should be replaced or moved.
            new_index (int | Unset): The zero-based new index the rule should end up at.
            rule (ConditionalFormatRule | Unset): A rule describing a conditional format.
            sheet_id (int | Unset): The sheet of the rule to move. Required if new_index is set, unused otherwise.
     """

    index: int | Unset = UNSET
    new_index: int | Unset = UNSET
    rule: ConditionalFormatRule | Unset = UNSET
    sheet_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_format_rule import ConditionalFormatRule
        index = self.index

        new_index = self.new_index

        rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        sheet_id = self.sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if new_index is not UNSET:
            field_dict["newIndex"] = new_index
        if rule is not UNSET:
            field_dict["rule"] = rule
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_format_rule import ConditionalFormatRule
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        new_index = d.pop("newIndex", UNSET)

        _rule = d.pop("rule", UNSET)
        rule: ConditionalFormatRule | Unset
        if isinstance(_rule,  Unset):
            rule = UNSET
        else:
            rule = ConditionalFormatRule.from_dict(_rule)




        sheet_id = d.pop("sheetId", UNSET)

        update_conditional_format_rule_request = cls(
            index=index,
            new_index=new_index,
            rule=rule,
            sheet_id=sheet_id,
        )


        update_conditional_format_rule_request.additional_properties = d
        return update_conditional_format_rule_request

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
