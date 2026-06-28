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





T = TypeVar("T", bound="UpdateConditionalFormatRuleResponse")



@_attrs_define
class UpdateConditionalFormatRuleResponse:
    """ The result of updating a conditional format rule.

        Attributes:
            new_index (int | Unset): The index of the new rule.
            new_rule (ConditionalFormatRule | Unset): A rule describing a conditional format.
            old_index (int | Unset): The old index of the rule. Not set if a rule was replaced (because it is the same as
                new_index).
            old_rule (ConditionalFormatRule | Unset): A rule describing a conditional format.
     """

    new_index: int | Unset = UNSET
    new_rule: ConditionalFormatRule | Unset = UNSET
    old_index: int | Unset = UNSET
    old_rule: ConditionalFormatRule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_format_rule import ConditionalFormatRule
        new_index = self.new_index

        new_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_rule, Unset):
            new_rule = self.new_rule.to_dict()

        old_index = self.old_index

        old_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.old_rule, Unset):
            old_rule = self.old_rule.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if new_index is not UNSET:
            field_dict["newIndex"] = new_index
        if new_rule is not UNSET:
            field_dict["newRule"] = new_rule
        if old_index is not UNSET:
            field_dict["oldIndex"] = old_index
        if old_rule is not UNSET:
            field_dict["oldRule"] = old_rule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_format_rule import ConditionalFormatRule
        d = dict(src_dict)
        new_index = d.pop("newIndex", UNSET)

        _new_rule = d.pop("newRule", UNSET)
        new_rule: ConditionalFormatRule | Unset
        if isinstance(_new_rule,  Unset):
            new_rule = UNSET
        else:
            new_rule = ConditionalFormatRule.from_dict(_new_rule)




        old_index = d.pop("oldIndex", UNSET)

        _old_rule = d.pop("oldRule", UNSET)
        old_rule: ConditionalFormatRule | Unset
        if isinstance(_old_rule,  Unset):
            old_rule = UNSET
        else:
            old_rule = ConditionalFormatRule.from_dict(_old_rule)




        update_conditional_format_rule_response = cls(
            new_index=new_index,
            new_rule=new_rule,
            old_index=old_index,
            old_rule=old_rule,
        )


        update_conditional_format_rule_response.additional_properties = d
        return update_conditional_format_rule_response

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
