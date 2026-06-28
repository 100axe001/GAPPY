from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.filter_criteria_size_comparison import FilterCriteriaSizeComparison
from ..types import UNSET, Unset






T = TypeVar("T", bound="FilterCriteria")



@_attrs_define
class FilterCriteria:
    """ Message matching criteria.

        Attributes:
            exclude_chats (bool | Unset): Whether the response should exclude chats.
            from_ (str | Unset): The sender's display name or email address.
            has_attachment (bool | Unset): Whether the message has any attachment.
            negated_query (str | Unset): Only return messages not matching the specified query. Supports the same query
                format as the Gmail search box. For example, `"from:someuser@example.com rfc822msgid: is:unread"`.
            query (str | Unset): Only return messages matching the specified query. Supports the same query format as the
                Gmail search box. For example, `"from:someuser@example.com rfc822msgid: is:unread"`.
            size (int | Unset): The size of the entire RFC822 message in bytes, including all headers and attachments.
            size_comparison (FilterCriteriaSizeComparison | Unset): How the message size in bytes should be in relation to
                the size field.
            subject (str | Unset): Case-insensitive phrase found in the message's subject. Trailing and leading whitespace
                are be trimmed and adjacent spaces are collapsed.
            to (str | Unset): The recipient's display name or email address. Includes recipients in the "to", "cc", and
                "bcc" header fields. You can use simply the local part of the email address. For example, "example" and
                "example@" both match "example@gmail.com". This field is case-insensitive.
     """

    exclude_chats: bool | Unset = UNSET
    from_: str | Unset = UNSET
    has_attachment: bool | Unset = UNSET
    negated_query: str | Unset = UNSET
    query: str | Unset = UNSET
    size: int | Unset = UNSET
    size_comparison: FilterCriteriaSizeComparison | Unset = UNSET
    subject: str | Unset = UNSET
    to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        exclude_chats = self.exclude_chats

        from_ = self.from_

        has_attachment = self.has_attachment

        negated_query = self.negated_query

        query = self.query

        size = self.size

        size_comparison: str | Unset = UNSET
        if not isinstance(self.size_comparison, Unset):
            size_comparison = self.size_comparison.value


        subject = self.subject

        to = self.to


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if exclude_chats is not UNSET:
            field_dict["excludeChats"] = exclude_chats
        if from_ is not UNSET:
            field_dict["from"] = from_
        if has_attachment is not UNSET:
            field_dict["hasAttachment"] = has_attachment
        if negated_query is not UNSET:
            field_dict["negatedQuery"] = negated_query
        if query is not UNSET:
            field_dict["query"] = query
        if size is not UNSET:
            field_dict["size"] = size
        if size_comparison is not UNSET:
            field_dict["sizeComparison"] = size_comparison
        if subject is not UNSET:
            field_dict["subject"] = subject
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exclude_chats = d.pop("excludeChats", UNSET)

        from_ = d.pop("from", UNSET)

        has_attachment = d.pop("hasAttachment", UNSET)

        negated_query = d.pop("negatedQuery", UNSET)

        query = d.pop("query", UNSET)

        size = d.pop("size", UNSET)

        _size_comparison = d.pop("sizeComparison", UNSET)
        size_comparison: FilterCriteriaSizeComparison | Unset
        if isinstance(_size_comparison,  Unset):
            size_comparison = UNSET
        else:
            size_comparison = FilterCriteriaSizeComparison(_size_comparison)




        subject = d.pop("subject", UNSET)

        to = d.pop("to", UNSET)

        filter_criteria = cls(
            exclude_chats=exclude_chats,
            from_=from_,
            has_attachment=has_attachment,
            negated_query=negated_query,
            query=query,
            size=size,
            size_comparison=size_comparison,
            subject=subject,
            to=to,
        )


        filter_criteria.additional_properties = d
        return filter_criteria

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
