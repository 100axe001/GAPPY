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





T = TypeVar("T", bound="AddConditionalFormatRuleRequest")



@_attrs_define
class AddConditionalFormatRuleRequest:
    """ Adds a new conditional format rule at the given index. All subsequent rules' indexes are incremented.

        Attributes:
            index (int | Unset): The zero-based index where the rule should be inserted.
            rule (ConditionalFormatRule | Unset): A rule describing a conditional format.
     """

    index: int | Unset = UNSET
    rule: ConditionalFormatRule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_format_rule import ConditionalFormatRule
        index = self.index

        rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_format_rule import ConditionalFormatRule
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _rule = d.pop("rule", UNSET)
        rule: ConditionalFormatRule | Unset
        if isinstance(_rule,  Unset):
            rule = UNSET
        else:
            rule = ConditionalFormatRule.from_dict(_rule)




        add_conditional_format_rule_request = cls(
            index=index,
            rule=rule,
        )


        add_conditional_format_rule_request.additional_properties = d
        return add_conditional_format_rule_request

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
