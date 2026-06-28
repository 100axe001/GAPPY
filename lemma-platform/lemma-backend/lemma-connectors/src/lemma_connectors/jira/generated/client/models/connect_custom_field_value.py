from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connect_custom_field_value_type import ConnectCustomFieldValueType
from ..types import UNSET, Unset






T = TypeVar("T", bound="ConnectCustomFieldValue")



@_attrs_define
class ConnectCustomFieldValue:
    """ A list of custom field details.

        Attributes:
            field_type_ (ConnectCustomFieldValueType): The type of custom field.
            field_id (int): The custom field ID.
            issue_id (int): The issue ID.
            number (float | Unset): The value of number type custom field when `_type` is `NumberIssueField`.
            option_id (str | Unset): The value of single select and multiselect custom field type when `_type` is
                `SingleSelectIssueField` or `MultiSelectIssueField`.
            rich_text (str | Unset): The value of richText type custom field when `_type` is `RichTextIssueField`.
            string (str | Unset): The value of string type custom field when `_type` is `StringIssueField`.
            text (str | Unset): The value of of text custom field type when `_type` is `TextIssueField`.
     """

    field_type_: ConnectCustomFieldValueType
    field_id: int
    issue_id: int
    number: float | Unset = UNSET
    option_id: str | Unset = UNSET
    rich_text: str | Unset = UNSET
    string: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field_type_ = self.field_type_.value

        field_id = self.field_id

        issue_id = self.issue_id

        number = self.number

        option_id = self.option_id

        rich_text = self.rich_text

        string = self.string

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "_type": field_type_,
            "fieldID": field_id,
            "issueID": issue_id,
        })
        if number is not UNSET:
            field_dict["number"] = number
        if option_id is not UNSET:
            field_dict["optionID"] = option_id
        if rich_text is not UNSET:
            field_dict["richText"] = rich_text
        if string is not UNSET:
            field_dict["string"] = string
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_type_ = ConnectCustomFieldValueType(d.pop("_type"))




        field_id = d.pop("fieldID")

        issue_id = d.pop("issueID")

        number = d.pop("number", UNSET)

        option_id = d.pop("optionID", UNSET)

        rich_text = d.pop("richText", UNSET)

        string = d.pop("string", UNSET)

        text = d.pop("text", UNSET)

        connect_custom_field_value = cls(
            field_type_=field_type_,
            field_id=field_id,
            issue_id=issue_id,
            number=number,
            option_id=option_id,
            rich_text=rich_text,
            string=string,
            text=text,
        )


        connect_custom_field_value.additional_properties = d
        return connect_custom_field_value

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
