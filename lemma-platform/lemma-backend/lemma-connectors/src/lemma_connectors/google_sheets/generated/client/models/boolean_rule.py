from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.boolean_condition import BooleanCondition
  from ..models.cell_format import CellFormat





T = TypeVar("T", bound="BooleanRule")



@_attrs_define
class BooleanRule:
    """ A rule that may or may not match, depending on the condition.

        Attributes:
            condition (BooleanCondition | Unset): A condition that can evaluate to true or false. BooleanConditions are used
                by conditional formatting, data validation, and the criteria in filters.
            format_ (CellFormat | Unset): The format of a cell.
     """

    condition: BooleanCondition | Unset = UNSET
    format_: CellFormat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_condition import BooleanCondition
        from ..models.cell_format import CellFormat
        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        format_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if condition is not UNSET:
            field_dict["condition"] = condition
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_condition import BooleanCondition
        from ..models.cell_format import CellFormat
        d = dict(src_dict)
        _condition = d.pop("condition", UNSET)
        condition: BooleanCondition | Unset
        if isinstance(_condition,  Unset):
            condition = UNSET
        else:
            condition = BooleanCondition.from_dict(_condition)




        _format_ = d.pop("format", UNSET)
        format_: CellFormat | Unset
        if isinstance(_format_,  Unset):
            format_ = UNSET
        else:
            format_ = CellFormat.from_dict(_format_)




        boolean_rule = cls(
            condition=condition,
            format_=format_,
        )


        boolean_rule.additional_properties = d
        return boolean_rule

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
