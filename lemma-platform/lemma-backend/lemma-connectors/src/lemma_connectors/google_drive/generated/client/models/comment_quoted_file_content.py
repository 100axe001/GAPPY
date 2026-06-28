from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CommentQuotedFileContent")



@_attrs_define
class CommentQuotedFileContent:
    """ The file content to which the comment refers, typically within the anchor region. For a text file, for example, this
    would be the text at the location of the comment.

        Attributes:
            mime_type (str | Unset): The MIME type of the quoted content.
            value (str | Unset): The quoted content itself. This is interpreted as plain text if set through the API.
     """

    mime_type: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        mime_type = self.mime_type

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mime_type = d.pop("mimeType", UNSET)

        value = d.pop("value", UNSET)

        comment_quoted_file_content = cls(
            mime_type=mime_type,
            value=value,
        )


        comment_quoted_file_content.additional_properties = d
        return comment_quoted_file_content

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
